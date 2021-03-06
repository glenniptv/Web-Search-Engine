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
	
#Crawl the Whole Web
#Use two lists : tocrawl and Crawled
#tocrawl: All web-pages still to be visited
#Crawled: All web-pages visited
#breadth-first Approach
def crawl_web(seed, max_depth = 2):

	tocrawl = [[seed, 0]]		#This time, we keep track of depth of loop
	crawled = []
	
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

		    #print final
		    union(tocrawl, final)
		    #print tocrawl
		    crawled.append(page)
		    
	return crawled
			
#------ END OF CRAWLER -----------------------------

#Main Definition
seed = "https://www.google.co.in/"
			
c_list =  crawl_web(seed, 1)
for i in c_list:
	print i

