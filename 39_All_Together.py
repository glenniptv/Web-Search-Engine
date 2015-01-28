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

#------Indexing is done with Dictionary-------

def Index_read_me():
	print """
		We have now chnaged Index function to look like:
		{ k1 : { url_list :
			 	{ 	u1 :	{
			 				total : count,		//Keyword score
			 				score : score,
			 				ctotal : count,		//Click Score
			 				cscore : score,
			 				tscore : score		//Total score
			 			}
			 			
			 		u2 : 	{
			 				total : count,
			 				score : score,
			 				ctotal : count,
			 				cscore : score,
			 				...
			 			}
			 	},
			 total :	count,
			 links_clicked: count
			 
		       }
		   k2: {.....
		   	}
		}
	     """

#Adds an entry to index
def add_to_index(index, keyword, page):
	if keyword in index:
		index[keyword]["total"] += 1
		
		if page not in index[keyword]["url"]:
			index[keyword]["url"][page] = {"total" : 0, "score" : float(0.0), "ctotal" : 0,
			 "cscore" : 0.0, "tscore" : 0.0} 
		index[keyword]["url"][page]["total"] += 1
		change_score(index, keyword)
		
	else:
		index[keyword] = { 
					"url" : 
						{ page : 
							{"total" : 1, 
							"score" : float(1.0), 
							"ctotal" : 0, 
							"cscore" : 0.0, 
							"tscore" : 1.0
							} 
						}, 
					"total" : 1,
					"ctotal" : 0
				}   
	
#Gets the content of page, and split them to get the entry
def add_page_to_index(index, url):
	for word in get_page(url).split():
		if not word.isalpha():
			import re
			word = re.sub('[,()<>/.//]', '', word)
		add_to_index(index, word.lower(), url)
		
#Find Keyword in Index
def lookup(index,keyword):
    if keyword in index:
    	return index[keyword]
    return None
		
#-------END OF INDEXING FUNCTIONS------

#------Ranking Functions--------

def link_graph_read_me():
	print """
		Link graph describes inlinks and outlinks as followsL
		{	url1:	[u2, u3, u4.... ],
			url2:   [u1, u3, u4....],
		}
		"""
#Adds link to page.
def add_to_graph(graph, page, link):
	if page in graph:
		graph[page].append(link)
	else:
		graph[page] = [link]
	
#Changes the Keyword score!	
def change_score(index, keyword):
	for url in index[keyword]["url"]:
		old_score = index[keyword]["url"][url]["score"]
		new_score = index[keyword]["url"][url]["total"]/float(index[keyword]["total"])
		index[keyword]["url"][url]["score"] = new_score
		index[keyword]["url"][url]["tscore"] = index[keyword]["url"][url]["tscore"] - old_score + new_score
		
		
#Using Page rank Formula.
def compute_ranks(graph):
	d = 0.8 # damping factor
	numloops = 10

	ranks = {}
	npages = len(graph)
	
	for page in graph:
		ranks[page] = 1.0 / npages
#	print ranks

	for i in range(0, numloops):
	
		newranks = {}
		
		for page in graph:
		    newrank = (1 - d) / npages
		   
		    for node in graph:
			if page in graph[node]:
			    newrank = newrank + ( (d * ranks[node]) / len(graph[node]) )
		    
		    newranks[page] = newrank
		    
		ranks = newranks
#		print ranks
		
	return ranks

#I am Feeling Lucky, based on PageRank Algorithm + Total Score of keyword

def lucky_search(index, ranks, keyword):
    keyword  = keyword.lower()
    if keyword not in index:
        return None
    url_list = index[keyword]["url"]
#    print url_list
    best_score = 0
    best_url = ""
    for url in url_list:
        score = ranks[url] + index[keyword]["url"][url]["tscore"]
#        print url, score
        if score > best_score:
            best_score = score
            best_url = url
    return best_url, best_score
    
#------END OF RANKING FUNCTIONS-----------

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
	index = {}
	graph = {}
	
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
		
		    graph[page] = links
			
		    add_page_to_index(index, page)
		    #print final
		    union(tocrawl, final)
		    #print tocrawl
		    crawled.append(page)
		    
	return index, graph
			
#------ END OF CRAWLER -----------------------------

#Main Definition
seed = "http://udacity.com/cs101x/urank/index.html"
			
index, graph =  crawl_web(seed, 10)
ranks = compute_ranks(graph)

#print graph
#print ranks
result = lucky_search(index, ranks, 'Hummus')



