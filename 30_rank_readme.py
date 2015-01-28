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
	     
def link_graph_read_me():
	print """
		Link graph describes inlinks and outlinks as followsL
		{	url1:	[u2, u3, u4.... ],
			url2:   [u1, u3, u4....],
		}
		"""
