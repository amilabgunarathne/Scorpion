import hashlib
import base64
import uuid
import random
import string

def check_password(text):

    lis = ['~','!','@','#','$','%','^','&','*','_','-','+','=','`','|','(',')','{','}','[',']','.','?']

    def test( text ):
        if (any(i.islower() for i in text)):
             if (any(i.isupper() for i in text)):
                for i in text:
                    if i in lis:
                        return (True)

    if ((len(text)>5 and len(text)<9) and test(text)):
        salt     = base64.urlsafe_b64encode(uuid.uuid4().bytes)
        t_sha = hashlib.sha512()
        hashed_password =  base64.urlsafe_b64encode(t_sha.digest())
        return (hashed_password.decode("utf-8") )
    else:
        return ('error')

def random_password():
    lis = ['~','!','@','#','$','%','^','&','*','_','-','+','=','`','|','(',')','{','}','[',']','.','?']
    test = ""
    for i in range(4):
        test = test + str(random.randint(0,9))
    test = test + random.choice(string.ascii_letters).lower()
    test = test + random.choice(string.ascii_letters).upper()
    test = test + lis[random.randint(0,len(lis))]
    return test

