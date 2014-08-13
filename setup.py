from distutils.core import setup
setup(name='ScrapyElasticSearch2',
      version='0.1',
      license='Apache License, Version 2.0',
      description='Scrapy pipeline which allow you to store multiple scrapy items in Elastic Search.',
      author='Michael Malocha',
      author_email='michael@knockrentals',
      url='https://github.com/knockrentals/scrapy-elasticsearch2.git',
      download_url = 'https://github.com/knockrentals/scrapy-elasticsearch2/tarball/0.1',
      keywords="scrapy elastic search",
      py_modules=['scrapyelasticsearch2'],
      platforms = ['Any'],
      install_requires = ['scrapy', 'pyes'],
      classifiers = [ 'Development Status :: 4 - Beta',
                      'Environment :: No Input/Output (Daemon)',
                      'License :: OSI Approved :: Apache Software License',
                      'Operating System :: OS Independent',
                      'Programming Language :: Python']
)
