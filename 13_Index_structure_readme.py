def Index_read_me():
	print """
		We have now chnaged Index function to look like:
		[ [k1, [						1st_entry : entry[0]
			[u1, count], 						    entry[1], link	
			[u2, count], 
			[u3, count] 
		       ]
		   ] ,
		  [k2, [
		  	[u1, count],
		  	[u2, count],
		  	[u3, count],
		       ]
		  ]
		]
	     """
index = []

def add_to_index(index, keyword, url):
	for entry in index:
		if keyword == entry[0]:
		#	print entry[1]
			for link in entry[1]:
			#	print link
				if url == link[0]:
					link[1] += 1
					return
			entry[1].append([[url, 0]])
			return
	index.append([keyword, [[url, 0]]])
	
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print index


