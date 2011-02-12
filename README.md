Description
===========
It's a pipeline which allow you to store scrapy items in elastic search engine.

Install
=======
   pip install "ScrapyElasticSearch"

Configure your settings.py:
----------------------------
    ITEM_PIPELINES = [
      'scrapyelasticsearch.ElasticSearchPipeline',
    ]

    ELASTICSEARCH_SERVER = 'localhost'
    ELASTICSEARCH_PORT = 9200
    ELASTICSEARCH_INDEX = 'scrapy'
    ELASTICSEARCH_TYPE = 'items'
    ELASTICSEARCH_UNIQ_KEY = 'url'

Changelog
=========
0.1: First Version


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