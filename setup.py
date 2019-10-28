from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = 'FileEncryption',
  packages = ['FileEncryption'],
  version = '0.1.6',
  license='MIT',
  description = 'Encrypt you .py or .pyw files to unreadable code', 
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Simon Köck',
  author_email = 'simply.studios.business@gmail.com',
  url = 'https://github.com/simonkoeck/FileEncryption',
  download_url = 'https://github.com/simonkoeck/FileEncryption/archive/v_01.tar.gz',
  keywords = ['File', 'Encryption', 'Unreadable'],
  install_requires=[
          'cryptography',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)