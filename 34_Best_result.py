#I am Feeling Lucky, based on PageRank Algorithm exclusively.

def lucky_search(index, ranks, keyword):
    if keyword not in index:
        return None
    url_list = index[keyword]
    best_score = 0
    best_url = url_list[0]
    for url in url_list:
        score = ranks[url]
        if score > best_score:
            best_score = score
            best_url = url
    return best_url
