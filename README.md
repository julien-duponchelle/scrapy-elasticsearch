Description
===========
Scrapy-ElasticSearch is a pipeline which allows Scrapy objects to be sent directly to ElasticSearch.

Install
=======
   pip install "ScrapyElasticSearch"

Configure settings.py:
----------------------
    ITEM_PIPELINES = [
      'scrapyelasticsearch.ElasticSearchPipeline',
    ]

    ELASTICSEARCH_SERVER = 'localhost' # If not 'localhost' prepend 'http://'
    ELASTICSEARCH_PORT = 9200 # If port 80 leave blank
    ELASTICSEARCH_USERNAME = ''
    ELASTICSEARCH_PASSWORD = ''
    ELASTICSEARCH_INDEX = 'scrapy'
    ELASTICSEARCH_TYPE = 'items'
    ELASTICSEARCH_UNIQ_KEY = 'url'

Changelog
=========

* 0.1: Initial release
* 0.2: Scrapy 0.18 support
* 0.3: Auth support
* 0.4: Remove debug

Contributors
=============
* Julien Duponchelle (http://github.com/noplay)
* Jay Stewart (https://github.com/solidground)

Licence
=======
Copyright 2011 Julien Duponchelle

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
