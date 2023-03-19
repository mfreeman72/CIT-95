#1 TODO: an accumulator tallies up the amount of lines found to meet your criteria; count will count up amount of senders found, duplicates included

count = 0
#setting file to variable and opening file
# setting file to be opened, read and read all lines

f = open('mbox-short.txt', 'r')

sender_values = []
#2 TODO: my_line(used in for loop to iterate through file) and my_file_handle(locates text file and opens setting it to either r(read), w(write), or a(append))
for line in f:
    #3 TODO: includes first 5 characters through each line, used to locate sender portions of text
    if (line[0:5] == 'From '):
        #4 TODO: elements of a list are each indexes data
        sender_values.extend(word for word in line.split() if '@' in word)
        count = count + 1
# print(count, 'is amount of gathered contacts, dupes included')
#5 TODO: produces the prefix@domain after the 'From ' conditional
#6 TODO: splitting the prefix and domain @ the '@' into to separate list indexes
#7 TODO: from what I've read online ++/-- operators allow for error so clarification is needed in Python
senders = [*set(sender_values)]
# print(senders)
# *set() will find and remove duplicates in list and return as new list

# See about mapping to organize list into further detailed list
# find way to implement find method ex: locater = senders[1].find("@") or maybe just split
pref = []
dom = []
two_parts = []
for i in range(len(senders)):
    two_parts.extend(senders[i - 1].split('@'))

# print(two_parts)

dom = two_parts[1::2]
pref = two_parts[0::2]
dom = [*set(dom)]
# print(dom)
# print(pref)

pref_dict = {}
dom_dict = {}
#convert list to dictionary using zip method
def dict_maker(x, y, z = 0):
    for z in range(len(x)):
        z = z + 1
        # z not in use anymore but leaving for question
    it = iter(x)
    y = dict(zip(x, it))
    # print(y)
    return y

dom = dict_maker(dom, dom_dict)
pref = dict_maker(pref, pref_dict)
print(dom,'\n', pref)
#reminder to ask professor mohle how to better iterate so that each key increases by 1 instead of using key and val to be the same

# converted wrong part into dictionaries for assignment
