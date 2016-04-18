import ast
import re
from distutils.core import setup
from setuptools import find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('scrapyelasticsearch/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(name='ScrapyElasticSearch',
      version=version,
      license='Apache License, Version 2.0',
      description='Scrapy pipeline which allow you to store multiple scrapy items in Elastic Search.',
      long_description=open('README.rst').read(),
      author='Michael Malocha, Julien Duponchelle',
      author_email='michael@knockrentals.com, julien@duponchelle.info',
      url='https://github.com/knockrentals/scrapy-elasticsearch.git',
      download_url='https://github.com/knockrentals/scrapy-elasticsearch/tarball/master',
      keywords="scrapy elastic search",
      packages=find_packages(),
      platforms=['Any'],
      install_requires=['scrapy', 'elasticsearch'],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: No Input/Output (Daemon)',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python']
      )
