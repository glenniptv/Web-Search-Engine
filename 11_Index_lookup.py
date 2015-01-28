#Aim is to define lookup function for index
#We would like index as [ [key1, [url1, url2, url3 ...] ],
#			  [key2, [url1, url2, url3 ...] ],
#

#Find Keyword in Index
def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []
