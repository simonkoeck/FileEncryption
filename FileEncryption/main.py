import base64
from cryptography.fernet import Fernet
import string
import random

class Encryptor:

    def randomstring(self, stringLength):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))

    def encrypt(self, path, ouput_path, include_imports=False, key_length=10):
        if(not path.endswith(".py") and not path.endswith(".pyw")):
            raise Exception("{} is no .py or .pyw File!".format(path))
        imports = ""
        data = ""
        key = Fernet.generate_key()
        try:
            f = open(path, "r+")
            lines = f.readlines()
            f.close()
        except Exception as e:
            raise Exception(e)

        for line in lines:
            if (line.startswith("import") or line.startswith("from")) and not include_imports:
               imports += line
            else:
                if not line.startswith("#") and not line.startswith("\n"):
                    data += line

        randomname = self.randomstring(key_length)
        randomname1 = self.randomstring(key_length)
        randomname2 = self.randomstring(key_length)
        randomname3 = self.randomstring(key_length)

        imports += "# FileEncryptor 0.1.2 \n"
        imports += "# https://pypi.org/project/PythonFileEncryption/"
        imports += "\n"
        imports += "from base64 import b64decode as {}\n".format(randomname)
        imports += "from cryptography.fernet import Fernet as {}\n".format(randomname1)
        imports += "{} = {}\n".format(randomname3, key)
        imports += "{} = {}({})\n".format(randomname2, randomname1, randomname3)
        filedata = imports

        f = Fernet(key)

        filedata += 'exec({}.decrypt({}({})))'.format(randomname2, randomname, base64.b64encode(f.encrypt(data.encode())))

        f = open(ouput_path, "w")
        f.write(filedata)
        f.close()
