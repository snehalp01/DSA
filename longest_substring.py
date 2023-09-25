# given a string s and an integer B find longest substring with maximum B dixtinct characters


def findsubstring(str,B):
    n = len(str)
    max_len = 1
    for i in range(n):
        print(i)
        e = i
        s = set()
        while(e<n):
            s.add(str[e])
            if len(s)>B:
                print(s)
                break
            e+=1
        max_len = max(max_len, e-i)
    return max_len
        
if __name__ == '__main__':
    s = "acbaab"
    B = 2
    max_len = findsubstring(s, B)
    print("max length: ", max_len)