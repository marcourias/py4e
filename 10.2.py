# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for 
# each of the messages. You can pull the hour out from the 'From ' line by finding the time and 
# then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fhandle = open('mbox-short.txt')

hours = dict()
times = []


for line in fhandle:
    words = line.split()

    if len(words) > 0 and words[0] == 'From':
        counter = 0
        for hour in words[5].split(':'):
            if counter == 0:
                times.append(hour)
                counter += 1


for hour in times:
    hours[hour] = hours.get(hour,0) + 1

lista = list()

for k,v in sorted(hours.items()):
    print(k,v)
           
    
#print(times)
#print(hours)


