#read_python = open("read_from_python.txt", "r") #read
#read_python = open("read_from_python.txt", "w") write
#read_python = open("read_from_python.txt", "r+") read and write
read_python = open("read_from_python.txt", "a") #to append
read_python.write("toby _ human resourses")
read_python.write("\nkelly _ human resourses")
#print(read_python.read())
# we can read each line, and completely.
#print(read_python.read())
#print(read_python.readline())
#print(read_python.readline())
#print(read_python.readlines())
#print(read_python.readlines()[1])
#for employee in read_python.readlines():
 #   print(employee)

read_python.close()