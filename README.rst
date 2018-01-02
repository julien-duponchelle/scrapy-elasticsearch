Description
===========
Scrapy pipeline which allows you to store scrapy items in Elastic Search.

Install
=======
::

   pip install ScrapyElasticSearch

   If you need support for ntlm:
   pip install "ScrapyElasticSearch[extras]"

Usage (Configure settings.py:)
----------------------
::

   ITEM_PIPELINES = {
       'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 500
   }

   ELASTICSEARCH_SERVERS = ['localhost']
   ELASTICSEARCH_INDEX = 'scrapy'
   ELASTICSEARCH_INDEX_DATE_FORMAT = '%Y-%m'
   ELASTICSEARCH_TYPE = 'items'
   ELASTICSEARCH_UNIQ_KEY = 'url'  # Custom unique key

   # can also accept a list of fields if need a composite key
   ELASTICSEARCH_UNIQ_KEY = ['url', 'id']

ELASTICSEARCH_SERVERS - list of hosts or string (single host). Host format: protocl://username:password@host:port.
Examples:
    - ['http://username:password@elasticsearch.example.com:9200']
    - ['http://elasticsearch.example.com:9200']
    - 'https://elasticsearch.example.com:9200'

Available parameters (in settings.py:)
----------------------
::

   ELASTICSEARCH_INDEX - elastic search index
   ELASTICSEARCH_INDEX_DATE_FORMAT - the format for date suffix for the index, see python datetime.strftime for format. Default is no date suffix.
   ELASTICSEARCH_TYPE - elastic search type
   ELASTICSEARCH_UNIQ_KEY - optional field, unique key in string (must be a field or a list declared in model, see items.py)
   ELASTICSEARCH_BUFFER_LENGTH - optional field, number of items to be processed during each bulk insertion to Elasticsearch. Default size is 500.
   ELASTICSEARCH_AUTH  - optional field, set to 'NTLM' to use NTLM authentification
   ELASTICSEARCH_USERNAME - optional field, set to 'DOMAIN\username', only used with NLTM authentification
   ELASTICSEARCH_PASSWORD - optional field, set to your 'password', only used with NLTM authentification

   ELASTICSEARCH_CA - optional settings to if es servers require custom CA files.
   Example:
   ELASTICSEARCH_CA = {
        'CA_CERT': '/path/to/cacert.pem',
        'CLIENT_CERT': '/path/to/client_cert.pem',
        'CLIENT_KEY': '/path/to/client_key.pem'
  }


Here is an example app (dirbot https://github.com/jayzeng/dirbot) in case you are still confused.

Dependencies
=========
See requirements.txt

Changelog
=========
* 0.9: Accept custom CA cert to connect to es clusters
* 0.8: Added support for NTLM authentification
* 0.7.1: Added date format to the index name and a small bug fix
    - ELASTICSEARCH_BUFFER_LENGTH default was 9999, this has been changed to reflect documentation.

* 0.7: A number of backwards incompatibility changes are introduced:
    - Changed ELASTICSEARCH_SERVER to ELASTICSEARCH_SERVERS
    - ELASTICSEARCH_SERVERS accepts string or list
    - ELASTICSEARCH_PORT is removed, you can specify it in the url
    - ELASTICSEARCH_USERNAME and ELASTICSEARCH_PASSWORD are removed. You can use this format ELASTICSEARCH_SERVERS=['http://username:password@host:port']
    - Changed scrapy.log to logging as scrapy now uses the logging module

* 0.6.1: Able to pull configs from spiders (in addition to reading from config file)
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
* Jay Zeng (Maintainer) (https://github.com/jayzeng)
* Michael Malocha (https://github.com/mjm159)
* Ignacio Vazquez (https://github.com/ignaciovazquez)
* Julien Duponchelle (https://github.com/noplay)
* Jay Stewart (https://github.com/solidground)
* Alessio Cimarelli (https://github.com/jenkin)
* Doug Parker (https://github.com/dougiep16)
* Jean-Sebastien Gervais (https://github.com/jsgervais)


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
