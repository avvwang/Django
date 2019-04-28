from django.test import TestCase

# Create your tests here.


i=open(r'c:\Users\heliang\Desktop\1.txt',mode='r')
txt=i.read()
print(txt)
x=open(r'c:\Users\heliang\Desktop\2.txt',mode='a')
x.write(txt)
