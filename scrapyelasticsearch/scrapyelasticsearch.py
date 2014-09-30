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

from pyes import ES
from scrapy import log
from scrapy.utils.project import get_project_settings
import hashlib
import types

class MalformSettingException(Exception):
    pass

class KeyNotFoundException(Exception):
    pass

class ElasticSearchPipeline(object):
    def __init__(self):
        self.settings = get_project_settings()

        self.enforce_settings()

        self.logging_level = self.settings['ELASTICSEARCH_LOG_LEVEL']

        basic_auth = {'username': self.settings['ELASTICSEARCH_USERNAME'], 'password': self.settings['ELASTICSEARCH_PASSWORD']}

        uri = "%s:%d" % (self.settings['ELASTICSEARCH_SERVER'], self.settings['ELASTICSEARCH_PORT'])

        self.es = ES([uri], basic_auth=basic_auth)

    def enforce_settings(self):
        # Enforce required Keys:
        if not 'ELASTICSEARCH_SERVER' in self.settings:
            raise KeyNotFoundException

        if self.settings['ELASTICSEARCH_SERVER'].startswith('http'):
            raise MalformSettingException('ELASTICSEARCH_SERVER must start with http')

        if not isinstance(self.settings['ELASTICSEARCH_PORT'], int):
            raise KeyNotFoundException

        if not 'ELASTICSEARCH_PORT' in self.settings:
            raise MalformSettingException('ELASTICSEARCH_PORT must be integer (e.g: 80, 9200)')

    def index_item(self, item, force_insert = False):
        """
            @param force_insert - flag to control whether to create or index
        """
        if self.settings['ELASTICSEARCH_UNIQ_KEY'] and self.settings['ELASTICSEARCH_UNIQ_KEY'] != '' and not force_insert:
            uniq_key = hashlib.sha1(item[uniq_key]).hexdigest()
            log.msg("Generated unique key %s" % uniq_key, level=self.logging_level)
            return self.es.index(dict(item),
                                 self.settings['ELASTICSEARCH_INDEX'],
                                 self.settings['ELASTICSEARCH_TYPE'],
                                 id=uniq_key)

        # Force to create a new index
        return self.es.index(dict(item),
                             self.settings['ELASTICSEARCH_INDEX'],
                             self.settings['ELASTICSEARCH_TYPE'],
                             id=item['id'],
                             force_insert=True)


    """
    Gets called by scrapy
    """
    def process_item(self, item, spider):
        # Recursively process items in list or generator
        if isinstance(item, types.GeneratorType) or isinstance(item, types.ListType):
            for each in item:
                self.process_item(each, spider)

        self.index_item(item)
        log.msg("Item sent to Elastic Search %s" %
                (self.settings['ELASTICSEARCH_INDEX']),
                level=self.logging_level, spider=spider)
        return item
