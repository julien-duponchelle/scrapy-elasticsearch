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

"""Elastic Search Pipeline for scrappy expanded  with support for multiple items"""

from elasticsearch import Elasticsearch
import logging
import hashlib
import types

class ElasticSearchPipeline(object):
    settings = None
    es = None

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        ext.settings = crawler.settings

        es_servers = ext.settings['ELASTICSEARCH_SERVER']
        es_servers = es_servers if isinstance(es_servers, list) else [es_servers]

        es_port = ext.settings['ELASTICSEARCH_PORT']

        ext.es = Elasticsearch(hosts=es_servers)
        return ext

    def index_item(self, item):
        if self.settings.get('ELASTICSEARCH_UNIQ_KEY'):
            uniq_key = self.settings.get('ELASTICSEARCH_UNIQ_KEY')
            if isinstance(item[uniq_key], str):
                unique_key = unique_key
            elif isinstance(item[uniq_key], list) and len(item[uniq_key]) == 1:
                unique_key = item[uniq_key][0]
            else:
                raise Exception('unique key must be str or list')

            local_id = hashlib.sha1(unique_key).hexdigest()
            logging.debug("Generated unique key %s" % local_id)
        else:
            local_id = item['id']

        self.es.index(index=self.settings.get('ELASTICSEARCH_INDEX'),
                      doc_type=self.settings.get('ELASTICSEARCH_TYPE'),
                      id=local_id,
                      body=dict(item))

    def process_item(self, item, spider):
        if isinstance(item, types.GeneratorType) or isinstance(item, types.ListType):
            for each in item:
                self.process_item(each, spider)
        else:
            self.index_item(item)
            logging.debug("Item sent to Elastic Search %s" % self.settings.get('ELASTICSEARCH_INDEX'))
            return item
