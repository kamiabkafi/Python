import random
import string
password_len=8
charVal= string.ascii_letters + string.digits + string.punctuation

password=""
for i in range(password_len):
    password+=random.choice(charVal)
print(password)

# res="".join([random.choice(charVal) for i in range(password_len)])
# print(res)