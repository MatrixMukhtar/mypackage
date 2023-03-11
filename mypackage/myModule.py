def top_n (items,n):
    '''Return the top n items in descending order

    Args:
    items(array):list or array-like object
    n: num of items to return
    '''
    for i in range(n):
        for j in range(len(items)-1):
            if items[j]<items[j+1]: # if successor higher than number
                items[j],items[j+1]= items[j+1],items[j]
    return items[:n]