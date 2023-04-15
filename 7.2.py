#  7.2 Write a program that prompts for a file name, then opens that file and reads through the file, 
# looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values from each of the lines and
# compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.

# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.


while True:
    fname = input("Ingrese el nombre del archivo: ")
    try:
        fhandle = open(fname)
    except:
        print("No se encontró el archivo.")
        continue

    text = 'X-DSPAM-Confidence:'
    count = 0
    total = 0

    for line in fhandle:
        if text in line:
            count += 1
            lineConf = line[19:].rstrip()
            lineNum = float(lineConf)
            total += lineNum


    avg = total/count
    print(f'Average spam confidence: {avg}')
    break