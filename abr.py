def abr(h4str):
    
    x = h4str
    aug = "&lt;abbr title="
    uag = "&lt;/abbr&gt;"
    puag = "\"&gt;"
    i = 1

    abc = x.count(aug)

    while i <= abc:
        p1 = x.split(aug,1)[0]
        ppd = x.split(aug,1)[1]
        pp = ppd[2:len(ppd)]
        p2s = pp.split(uag,1)[0]
        p2e = p2s.find(puag) - 1
        p2 = p2s[0:p2e]
        p3 = pp.split(uag,1)[1]
        x = p1 + p2 + p3
        i+=1
        
    unabr = x
    return unabr





    




