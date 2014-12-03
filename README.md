Description
===========
Scrapy pipeline which allow you to store scrapy items in Elastic Search.

Install
=======
   pip install ScrapyElasticSearch

Configure settings.py:
----------------------
    from scrapy import log

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
    ELASTICSEARCH_LOG_LEVEL= log.DEBUG

Changelog
=========

* 0.6: Bug fix
* 0.5: Abilit to persist object; Option to specify logging level
* 0.4: Remove debug
* 0.3: Auth support
* 0.2: Scrapy 0.18 support
* 0.1: Initial release

Issues
=============
If you find any bugs or have any questions, please report them to "issues" (https://github.com/knockrentals/scrapy-elasticsearch/issues)

Contributors
=============
* Michael Malocha (https://github.com/mjm159)
* Ignacio Vazquez (https://github.com/ignaciovazquez)
* Julien Duponchelle (https://github.com/noplay)
* Jay Stewart (https://github.com/solidground)

Licence
=======
Copyright 2014 Michael Malocha

Expanded on the work by Julien Duponchelle

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
