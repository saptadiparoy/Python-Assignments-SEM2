#to write create file
file = open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\python\\SEM2\\UNIT 4\\finaltext.txt", "w")
file.write("hello")

#to append to file
file = open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\python\\SEM2\\UNIT 4\\finaltext.txt", "a")
file.write("\n1.next line")
file.write("\n2.nextnext line")

#to read to file
file = open("C:\\Users\\Lenovo\\OneDrive\\Desktop\\python\\SEM2\\UNIT 4\\finaltext.txt", "r")
content = file.read() 
print(content)

file.close()