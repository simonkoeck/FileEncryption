# FileEncryption

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


License
----
MIT License
Copyright (c) 2018 Simon Koeck
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
