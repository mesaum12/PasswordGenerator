import string
import random

def passGen():
    string1=string.ascii_uppercase
    string2=string.ascii_lowercase
    string3=string.digits
    string4=string.punctuation
    
    passlen=int(input("Enter the length of the password to be set\n"))

    s=[]
    s.extend(list(string1))
    s.extend(list(string2))
    s.extend(list(string3))
    s.extend(list(string4))
    random.shuffle(s)
    print(''.join(s[0:passlen]))
    print('This is my code sample for the feature branch');
passGen()