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

class ElasticSearchPipeline(object):
    def __init__(self):
        self.settings = get_project_settings()

        basic_auth = {'username': self.settings['ELASTICSEARCH_USERNAME'], 'password': self.settings['ELASTICSEARCH_PASSWORD']}

        if self.settings['ELASTICSEARCH_PORT']:
            uri = "%s:%d" % (self.settings['ELASTICSEARCH_SERVER'], self.settings['ELASTICSEARCH_PORT'])
        else:
            uri = "%s" % (self.settings['ELASTICSEARCH_SERVER'])

        self.es = ES([uri], basic_auth=basic_auth)

    def index_item(self, item):
        if self.settings['ELASTICSEARCH_UNIQ_KEY']:
            local_id = hashlib.sha1(item[uniq_key)]).hexdigest()
            log.msg("Generated unique key %s" % local_id, level=self.settings['ELASTICSEARCH_LOG_LEVEL'])
            op_type = 'none'
        else:
            op_type = 'create'
            local_id = item['id']
        self.es.index(dict(item),
                      self.settings['ELASTICSEARCH_INDEX'],
                      self.settings['ELASTICSEARCH_TYPE'],
                      id=local_id,
                      op_type=op_type)


    def process_item(self, item, spider):
        if isinstance(item, types.GeneratorType) or isinstance(item, types.ListType):
            for each in item:
                self.process_item(each, spider)
        else:
            self.index_item(item)
            log.msg("Item sent to Elastic Search %s" %
                    (self.settings['ELASTICSEARCH_INDEX']),
                    level=self.settings['ELASTICSEARCH_LOG_LEVEL'], spider=spider)
            return item
