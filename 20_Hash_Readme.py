def Hash_basic_read_me():
	print """
		We have now chnaged Index function to look like:
		[ 
		 [    --- first hash bucket
		  [k1, [u1, u2, u3....]], [k2, [u1, u2, u3]]
		 ],
		 [   ---- second hash bucket
		  [k3, [u1, u2, u3...]], [k4, [u1, u2, u3]]
		 ]
		] 
		
	     """
	     
def Hash_complicated_read_me():
	print """
		We have now chnaged Index function to look like:
		[ 
		 [    ---first hash bucket
		 	[k1, [ ---first keyword in first Hash bucket
				[u1, count], 
				[u2, count], 
				[u3, count] 
		       	     ]
		        ],
		  	[k2, [
		  		[u1, count],
		  		[u2, count],
		  		[u3, count],
		             ]
		  	]
		  ] -- end of first Hash bucket
		]
	     """
