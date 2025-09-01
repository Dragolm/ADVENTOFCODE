import inspect
import importlib


# This must be able to:
# take a path from the user ->
path = input("Enter the path to the folder:")  #2021/trial_question

# ask the user whether to run the demo input or input file -> 
demo_or_not = int(input("Enter 1 for demo input and 2 for true input:"))

# go to the folder specified in the path -> 
if(demo_or_not == 1):
    inp = open(path + "/demoinput.txt", "r")
    input_array = [inpu for inpu in inp]
elif(demo_or_not == 2):
    inp = open(path + "/input.txt", "r")
    input_array = [inpu for inpu in inp]

#Converting the '/' in the path to . for inportin the module
dottedpath = ""
for chr in path:
    if(chr == '/'):
        dottedpath += '.'
    else:
        dottedpath += chr
dottedpath += '.'

#import the method
func = importlib.import_module(dottedpath + "runnable", path)

#Run the program: 
result = func.doit(input_array)

# display the output
print(result)

#end credits:
inp.close()