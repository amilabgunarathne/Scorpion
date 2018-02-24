import hashlib
import base64
import uuid

text = input()

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
    print (hashed_password)
else:
    print ('error')
