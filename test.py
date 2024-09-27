# arithmetic
# +, -, *, /, %, **

a = 10
b = 3
c = a + b

print ("total: ", c)
print (a, "+",b,"=",c)
print ("modulus of", a, "%", b, "=", a%b)

# then try others..

# boolean
# and, or, not

# simple NOT
a = False
b = not a
print ("b is not a =", b)

# AND
a = 1
b = 0

print ("a AND b =", a and b)
print ("a AND b =", bool(a and b)) # the boolean of '0' is mean False

# Real Example for Boolean

realpassword = "abc123"
mypassword = input("type password")

print(type(realpassword)) #check data type
print(type(mypassword)) #check data type

result = realpassword == mypassword

print("the username and password is = ", result)

if mypassword == realpassword:
    print("logged in")
else:
    print("wrong password")