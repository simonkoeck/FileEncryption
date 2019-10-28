from distutils.core import setup
setup(
  name = 'PythonFileEncryption',
  packages = ['PythonFileEncryption'],
  version = '0.1.1',
  license='MIT',
  description = 'Encrypt you .py or .pyw files to unreadable code', 
  author = 'Simon Köck',
  author_email = 'simply.studios.business@gmail.com',
  url = 'https://github.com/simonkoeck/PythonFileEncryption',
  download_url = 'https://github.com/simonkoeck/PythonFileEncryption/archive/v_01.tar.gz',
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