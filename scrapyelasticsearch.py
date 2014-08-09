# Copyright 2011 Julien Duponchelle <julien@duponchelle.info>.
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

"""Elastic Search Pipeline for scrappy"""

from pyes import ES
import hashlib
from scrapy.utils.project import get_project_settings
from scrapy import log

class ElasticSearchPipeline(object):
    def __init__(self):

        self.settings = get_project_settings()

        basic_auth = {'username': self.settings['ELASTICSEARCH_USERNAME'], 'password': self.settings['ELASTICSEARCH_PASSWORD']}

        if self.settings['ELASTICSEARCH_PORT']:

            uri = "%s:%d" % (self.settings['ELASTICSEARCH_SERVER'], self.settings['ELASTICSEARCH_PORT'])
        else:
            uri = "%s" % (self.settings['ELASTICSEARCH_SERVER'])

        self.es = ES([uri], basic_auth=basic_auth)

    def process_item(self, item, spider):
        if self.__get_uniq_key() is None:
            log.msg("ELASTICSEARCH_UNIQ_KEY is NONE")
            self.es.index(dict(item), self.settings['ELASTICSEARCH_INDEX'], self.settings['ELASTICSEARCH_TYPE'],
                          id=item['id'], op_type='create',)
        else:
            log.msg("Generation SHA1")
            self.es.index(dict(item), self.settings['ELASTICSEARCH_INDEX'], self.settings['ELASTICSEARCH_TYPE'],
                          self._get_item_key(item))
        log.msg("Item send to Elastic Search %s" %
                    (self.settings['ELASTICSEARCH_INDEX']),
                    level=log.DEBUG, spider=spider)
        return item

    def _get_item_key(self, item):
        uniq = self.__get_uniq_key()

        if isinstance(uniq, list):
            values = [item[key] for key in uniq]
            value = ''.join(values)
        else:
            value = uniq

        return hashlib.sha1(value).hexdigest()

    def __get_uniq_key(self):
        if not self.settings['ELASTICSEARCH_UNIQ_KEY'] or self.settings['ELASTICSEARCH_UNIQ_KEY'] == "":
            return None
        return self.settings['ELASTICSEARCH_UNIQ_KEY']

