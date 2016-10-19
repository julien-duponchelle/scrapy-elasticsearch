# Copyright 2014 Michael Malocha <michael@knockrentals.com>
#
# Expanded from the work by Julien Duponchelle <julien@duponchelle.info>.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Elastic Search Pipeline for scrappy expanded with support for multiple items"""

from datetime import datetime
from elasticsearch import Elasticsearch, helpers
from six import string_types
from .transportNTLM import TransportNTLM

import logging
import hashlib
import types


class InvalidSettingsException(Exception):
    pass


class ElasticSearchPipeline(object):
    settings = None
    es = None
    items_buffer = []

    @classmethod
    def validate_settings(cls, settings):
        def validate_setting(setting_key):
            if settings[setting_key] is None:
                raise InvalidSettingsException('%s is not defined in settings.py' % setting_key)

        required_settings = {'ELASTICSEARCH_SERVERS', 'ELASTICSEARCH_INDEX', 'ELASTICSEARCH_TYPE'}

        for required_setting in required_settings:
            validate_setting(required_setting)

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        ext.settings = crawler.settings

        cls.validate_settings(ext.settings)

        es_servers = ext.settings['ELASTICSEARCH_SERVERS']
        es_servers = es_servers if isinstance(es_servers, list) else [es_servers]

        authType = ext.settings['ELASTICSEARCH_AUTH']
        if authType == 'NTLM':
            ext.es = Elasticsearch(hosts=es_servers,
                                   transport_class=TransportNTLM,
                                   ntlm_user= ext.settings['ELASTICSEARCH_USERNAME'],
                                   ntlm_pass= ext.settings['ELASTICSEARCH_PASSWORD'],
                                   timeout=ext.settings.get('ELASTICSEARCH_TIMEOUT',60))
        else :
            ext.es = Elasticsearch(hosts=es_servers, timeout=ext.settings.get('ELASTICSEARCH_TIMEOUT', 60))
        return ext

    def get_unique_key(self, unique_key):
        if isinstance(unique_key, list):
            unique_key = unique_key[0].encode('utf-8')
        elif not isinstance(unique_key, string_types):
            raise Exception('unique key must be str or unicode')

        return unique_key

    def index_item(self, item):

        index_name = self.settings['ELASTICSEARCH_INDEX']
        index_suffix_format = self.settings.get('ELASTICSEARCH_INDEX_DATE_FORMAT', None)

        if index_suffix_format:
            index_name += "-" + datetime.strftime(datetime.now(),index_suffix_format)

        index_action = {
            '_index': index_name,
            '_type': self.settings['ELASTICSEARCH_TYPE'],
            '_source': dict(item)
        }

        if self.settings['ELASTICSEARCH_UNIQ_KEY'] is not None:
            item_unique_key = item[self.settings['ELASTICSEARCH_UNIQ_KEY']]
            unique_key = self.get_unique_key(item_unique_key)
            item_id = hashlib.sha1(unique_key).hexdigest()
            index_action['_id'] = item_id
            logging.debug('Generated unique key %s' % item_id)

        self.items_buffer.append(index_action)

        if len(self.items_buffer) >= self.settings.get('ELASTICSEARCH_BUFFER_LENGTH', 500):
            self.send_items()
            self.items_buffer = []

    def send_items(self):
        helpers.bulk(self.es, self.items_buffer)

    def process_item(self, item, spider):
        if isinstance(item, types.GeneratorType) or isinstance(item, list):
            for each in item:
                self.process_item(each, spider)
        else:
            self.index_item(item)
            logging.debug('Item sent to Elastic Search %s' % self.settings['ELASTICSEARCH_INDEX'])
            return item

    def close_spider(self, spider):
        if len(self.items_buffer):
            self.send_items()

