##3. Writing Our First Program

print('Hello World!')
print('What is your name?') #ask for their name
myName = input()
print('It si good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year.')


#change Data Type

print(str(26)) #Change to STRING
print(int('1234'))#Change to INTEGER
print(float('3.14'))#CHANGE TO FLOAT

#Type Programs into the file editor
#The execution starts at the top and moves down
# # Comments are ignored in Python
#Functions are mini programs in your progem
#print() DISPLAYS THE VALUE PASSED TO IT
#input() lets user type in a VALUE
#len() takes a string value and returns an INTEGER value of the string length
#int(), str(), and float() converts values data Type
