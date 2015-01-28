#Aim is to define basic structure of Index
#We would like index as [ [key1, [url1, url2, url3 ...] ],
#			  [key2, [url1, url2, url3 ...] ],
#			  ....                              ] 

index = []

#Adds an entry to index
add_to_Index(index, keyword, url):
	for entry in index:
		if keyword == entry[0]:
			entry[1].append(url)
			return
	index.append([keyword, [url]])
	
