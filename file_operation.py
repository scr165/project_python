from sys import argv
script,filename=argv
print("Opening the file")
file=open(filename,'w')
print("now truncting the file")
file.truncate()
print("now, we can enter three lines into the file")
line1=input(">")
line2=input(">")
line3=input(">")
file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)
file.write("\n")
print("**"*20)
file.close()
