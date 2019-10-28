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
```

### Initialize the Encryptor Class

```Python
encryptor = Encryptor() # Saving the instance in the encryptor variable
```
### Encrypt the Input File

```Python
encryptor.encrypt(path="input.py", ouput_path="output.py")
```

#### INPUT
```Python
import random

print(random.randint(10, 20))
```
#### OUTPUT
```Python
from base64 import b64decode as jbwptnorqx
from cryptography.fernet import Fernet as wuktjjutaj
eoqszeurnl = b'4lc8q5lMAKWlgswSwTHCircF2VWquMEGQP4B4aJHqbk='
bvpbxsamrw = wuktjjutaj(eoqszeurnl)
exec(bvpbxsamrw.decrypt(jbwptnorqx(b'Z0FBQUFBQmR0c2I1emNHMTZwTllnNnJHRjR3LW9CUVBXM2k3d2RsN2Q3czRqUEI4UGV5eFpVMWZRQUluVGo5OVZkVjRteHc1dGFqMFRxZDFxa0lNZ2tMa1ZVOUVrRmtrNHZMNWlGQjl0NGQyS3Y1VjNOWGllR2lkNVFRTFEtRC1lZGZ0RFJHOWcxbkY=')))
```
