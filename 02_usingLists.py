#---- Helper Functions -----

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
	
#------ END OF CRAWLER -----------------------------

#Main Definition
seed = "http://xkcd.com/"
	
print get_all_links(seed)

