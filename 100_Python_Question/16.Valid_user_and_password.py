#Take input username,password
username = input("Enter your username : ")
password = input("Enter your password : ")

if(username == "admin" and password == "admin123"):
    print("Login successful")
else: 
    print("Invalid username  or password")

# output
# Enter your username : admin
# Enter your password : admin123
# Login successful