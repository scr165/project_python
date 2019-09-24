from sys import argv
from os.path import exists

script,from_file,to_file=argv
#script,from_file=argv
#infile=open(from_file,'a')
indata=infile.read()

#indata=infile.write("\n How are you?")

print(f"Is outfile exists? {exists(outfile)}")
if exists(to_file) == True:
    outfile=open(to_file,'w')
    outfile.write(indata)
    infile.close()
    outfile.close()
    print("The file is successfully copied")
else:
    print("you r out of your mind")
