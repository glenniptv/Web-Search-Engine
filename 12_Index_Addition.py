#Aim is to define basic structure of Index
#We would like index as [ [key1, [url1, url2, url3 ...] ],
#			  [key2, [url1, url2, url3 ...] ],
#			  ....                              ] 

index = []

#Adds an entry to index
def add_to_Index(index, keyword, url):
	for entry in index:
		if keyword == entry[0]:
			entry[1].append(url)
			return
	index.append([keyword, [url]])
	
#Gets the content of page, and split them to get the entry
def add_page_to_Index(index, url,  content = get_page(url)):
	words = content.split()
	
	for word in words:
		add_to_Index(index, word.lower(), url)
