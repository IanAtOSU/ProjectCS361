
def rem_list(l, key):
    found = False
    for i in l:
        for j in i:
            if j == key:
                found = True
                break
        if found == True:
            l.remove(i)
            break
    return l

