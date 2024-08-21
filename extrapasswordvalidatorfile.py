import bcrypt

password = b"this is my password"
hashed = bcrypt.hashpw(password,bcrypt.gensalt())
print(hashed)

entered_password = input("Enter Password To login: ")
entered_password = bytes(entered_password, encoding='utf-8')

if bcrypt.checkpw(entered_password, hashed):
    print('Login Successful')
else:
    print('Invalid PassWord')