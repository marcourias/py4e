#  7.1 Write a program that prompts for a file name, then opens that file and reads through the file, 
# and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

filename = input("Ingrese el nombre del archivo: ")

try:
    fhandle = open(filename)
except:
    print("No se pudo leer el archivo.")
    quit()

for line in fhandle:
    line = line.rstrip()
    cap_line = line.upper()
    print(cap_line)