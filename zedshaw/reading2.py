from sys import argv
from os.path import exists

#prompting user for filename via Cla(command line argument)
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#opening first file and using read function to it
in_file = open(from_file)
indata = in_file.read()
#the above two lines of code can be written in one line as below
#in_file = open(from_file);indata = in_file.read()

#len(indata) calculate the length of text written in bytes
print(f"The input file is {len(indata)} bytes long")

#prompting user, if they want to copy the file or not
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

#opening second file and using read function to it
out_file = open(to_file, "w")
out_file.write(indata)

#done copying
print("Alright, all done.")

#closing both files
out_file.close()
in_file.close()