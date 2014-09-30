from distutils.core import setup
from setuptools import find_packages

setup(name='ScrapyElasticSearch',
      version='0.5',
      license='Apache License, Version 2.0',
      description='Scrapy pipeline which allow you to store multiple scrapy items in Elastic Search.',
      author='Michael Malocha, Julien Duponchelle',
      author_email='michael@knockrentals.com, julien@duponchelle.info',
      url='https://github.com/knockrentals/scrapy-elasticsearch.git',
      download_url = 'https://github.com/knockrentals/scrapy-elasticsearch/tarball/master',
      keywords="scrapy elastic search",
      packages = find_packages(),
      platforms = ['Any'],
      install_requires = ['scrapy', 'pyes'],
      classifiers = [ 'Development Status :: 4 - Beta',
                      'Environment :: No Input/Output (Daemon)',
                      'License :: OSI Approved :: Apache Software License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
