#Create Empty hash-Table with empty nbuckets.
#It is necessary to define empty bucket, since at time of lookup, we must have access to all buckets
def make_hashtable(nbuckets):
	return [ [] for x in range(nbuckets) ]
	
#Hash procedure
def hash_string(keyword,buckets):
	count = 0
	for char in keyword:
		count = (count + ord(char)) % buckets
	return count
    
#Get a Bucket from Hashtable
def get_bucket(hashtable, keyword):
	return hashtable[hash_string(keyword, len(hashtable))]

#Add an element in HashTable
def hashtable_add(htable, key, value):
	bucket = get_bucket(htable, key)
	
	for entry in bucket:
		if key == entry[0]:
			entry[1].append(value)
			return htable
	bucket.append([key, value])
	
	return htable

#Search Hashtable
def hash_lookup(htable, key):
	bucket = get_bucket(htable, key)
	
	for entry in bucket:
		if key == entry[0]:
			return entry[1]
	return None		
		
		
	
	
