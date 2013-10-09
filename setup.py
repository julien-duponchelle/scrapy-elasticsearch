from distutils.core import setup
setup(name='ScrapyElasticSearch',
      version='0.2',
      license='Apache License, Version 2.0',
      description='A pipeline which allows Scrapy objects to be sent directly to ElasticSearch.',
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
