from distutils.core import setup
setup(name='ScrapyElasticSearch',
      version='0.1',
      license='Apache License, Version 2.0',
      description='Scrapy pipeline which allow you to store scrapy items in Elastic Search.',
      author='Julien Duponchelle',
      author_email='julien@duponchelle.info',
      url='http://github.com/noplay/scrapy-elasticsearch',
      keywords="scrapy elastic search",
      py_modules=['scrapyelasticsearch'],
      platforms = ['Any'],
      install_requires = ['scrapy', 'pyes'],
      classifiers = [ 'Development Status :: 4 - Beta',
                      'Environment :: No Input/Output (Daemon)',
                      'License :: OSI Approved :: Apache Software License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
