def count(biglist):
    finaldict = {}
    for i in biglist:
        if i not in finaldict:
            finaldict[i] = 1
        else:
            finaldict[i] += 1
    return finaldict


print(count(["hello","hello","world","world","hello"]))


        
