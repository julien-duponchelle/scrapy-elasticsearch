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
from scrapy.conf import settings
from scrapy import log

class ElasticSearchPipeline(object):
    def __init__(self):
        uri = "%s:%d" % (settings['ELASTICSEARCH_SERVER'], settings['ELASTICSEARCH_PORT'])
        self.es = ES([uri])

    def process_item(self, item, spider):
        if self.__get_uniq_key() is None:
            self.es.index(dict(item), settings['ELASTICSEARCH_INDEX'], settings['ELASTICSEARCH_TYPE'])
        else:
            self.es.index(dict(item), settings['ELASTICSEARCH_INDEX'], settings['ELASTICSEARCH_TYPE'],
                          hashlib.sha1(item[self.__get_uniq_key()]).hexdigest())
        log.msg("Item send to Elastic Search %s" %
                    (settings['ELASTIC_SEARCH_INDEX']),
                    level=log.DEBUG, spider=spider)  
        return item

    def __get_uniq_key(self):
        if not settings['ELASTICSEARCH_UNIQ_KEY'] or settings['ELASTICSEARCH_UNIQ_KEY'] == "":
            return None
        return settings['ELASTICSEARCH_UNIQ_KEY']
   
