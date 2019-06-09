def find_more(find_this, in_this):
    find_length = len(find_this)
    in_length = len(in_this)
    for i in range(in_length-find_length+1):
        if in_this[i:i+find_length] == find_this:
            return i
    return -1
