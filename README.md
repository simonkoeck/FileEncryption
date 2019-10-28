# FileEncryption - Make Python Code unreadable!

## Usage

In the following paragraphs, I am going to describe how you can get and use FileEncryption for your own projects.

###  Getting it

To download FileEncryption, either fork this github repo or simply use Pypi via pip.
```sh
$ pip install FileEncryption
```

### Using

```Python
from FileEncryption import Encryptor

encryptor = Encryptor() # Create a new instace of the Encryptor-Class

encryptor.encrypt(path="../input_file.py", ouput_path="./output.py")

```
