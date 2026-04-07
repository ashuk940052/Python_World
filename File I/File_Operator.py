# Notice the 'r' before the string. This creates a "raw string" so Python doesn't get confused by the backslashes.
f = open(r"C:\Users\hp\Desktop\Intelliji Java codes\Python_World\Python_World\File I\demo.txt", "r+")

data = f.read()

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

f.write("I am adding another lin eby sune the write function in read and write mode")
print(data)
print(type(data))


f.close()