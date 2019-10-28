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
import random

print(random.randint(10, 20))
```
