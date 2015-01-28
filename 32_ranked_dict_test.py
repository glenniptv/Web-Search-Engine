def Index_read_me():
	print """
		We have now chnaged Index function to look like:
		{ k1 : { url_list :
			 	{ 	u1 :	{
			 				total : count,		//Keyword score
			 				score : score,
			 				ctotal : count,		//Click Score
			 				cscore : score,
			 				lscore : score,		//Link Score
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
			 "cscore" : 0.0, "lscore" : 0.0, "tscore" : 0.0} 
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
							"lscore" : 0.0, 
							"tscore" : 0.0
							} 
						}, 
					"total" : 1,
					"ctotal" : 0
				}   

def change_score(index, keyword):
	for url in index[keyword]["url"]:
		index[keyword]["url"][url]["score"] = index[keyword]["url"][url]["total"]/float(index[keyword]["total"])
		

#----Testing Procedure
index = {}
for x in range(1, 2):
	for y in range(1, 4):
		add_to_index(index, x, (x+y)/2)

print index
	

