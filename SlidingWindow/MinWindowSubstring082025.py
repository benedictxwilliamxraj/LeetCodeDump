def minWindow(self, s: str, t: str) -> str:
    # edge case 
    if t == "":
        return ""
    # make window untill i find all t
    # note len 
    # Q: how to track elements ? -> hashmaps 
    dt = defaultdict(int)
    window = defaultdict(int)
    
    res, resLen = [-1,-1], float("infinity")
    
    for i in t:
        dt[i] += 1
    have, need = 0 , len(dt)
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c]+=1
        #print(c)
        if c in dt and window[c] == dt[c]:
            have+=1
        #print(have)
        while have == need:
            # update result
            if (r-l+1) < resLen:
                res = [l,r]
                resLen = r-l+1
            window[s[l]]-=1
            if s[l] in dt and window[s[l]] < dt[s[l]]:
                have-=1
            l+=1
    print(l,r)
    l, r = res
    print(l,r)
    return s[l:r+1] if resLen!=float("infinity") else ""
    