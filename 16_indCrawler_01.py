#---- Helper Functions -----

#Union Operation of two lists, q is added to p
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

#Get Page Source code, if possible.
def get_page(page):
	import urllib2
	
	try:
		source = urllib2.urlopen(page)
	    	val =  source.read()
	    	source.close()
	    	return val
	except:
		return ""
		
#-------END OF HELPER FUNCTIONS -------

#------Index Functions-------

def Index_read_me():
	print """
		We have now chnaged Index function to look like:
		[ [k1, [ 
			[u1, count], 
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

#Adds an entry to index
def add_to_index(index, keyword, url):
	for entry in index:
		if keyword == entry[0]:
		#	print entry[1]
			for link in entry[1]:
			#	print link
				if url == link[0]:
					link[1] += 1
					return
			entry[1].append([[url, 1]])
			return
	index.append([keyword, [[url, 1]]])
	
#Gets the content of page, and split them to get the entry
def add_page_to_index(index, url):
	for word in get_page(url).split():
		if not word.isalpha():
			import re
			word = re.sub('[,()<>/.//]', '', word)
		add_to_index(index, word.lower(), url)
		
#Find Keyword in Index
def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []
		
#-------END OF INDEXING FUNCTIONS------

#------ Web Crawler --------------
	
#Get Next Link, return None if no More links on Page
#Works by searching for <a href = "....." 
def get_next_target(s) :
	start_link = s.find('<a href=')
	
	if start_link == -1:
		return None, 0
	
	start_quote = s.find('"', start_link)
	end_quote = s.find('"', start_quote + 1)
	url = s[start_quote+1:end_quote]
	return url, end_quote
	
#Using Get_next_target, get all links and return the list containing all URL's present in given page
def get_all_links(page):
	url_list = []
	while True:
		url, end_quote = get_next_target(page)
	
		if url:
			page = page[end_quote:]
			url_list.append(url)
		else:
			break
			
	return url_list
	
#Crawl the Whole Web, AND index it
#Use two lists : tocrawl and Crawled
#tocrawl: All web-pages still to be visited
#Crawled: All web-pages visited
#breadth-first Approach
def crawl_web(seed, max_depth = 2):

	tocrawl = [[seed, 0]]		#This time, we keep track of depth of loop
	crawled = []
	index = []
	
	while tocrawl:
		ele = tocrawl[0]
		page = ele[0]
		depth = ele[1]
		tocrawl = tocrawl[1:]
		
		if page not in crawled and depth <= max_depth:
		    links = get_all_links(get_page(page))
		    final = []
		    
		    for e in links:
			final.append([e, depth+1])
			
		    add_page_to_index(index, page)
		    #print final
		    union(tocrawl, final)
		    #print tocrawl
		    crawled.append(page)
		    
	return index
			
#------ END OF CRAWLER -----------------------------

#Main Definition
seed = "http://www.catb.org/jargon/"
			
index =  crawl_web(seed, 0)
for i in index:
	print i

