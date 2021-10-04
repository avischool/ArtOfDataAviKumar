def count(biglist):
    finaldict = {}
    for element in biglist:
        if element not in finaldict:
            finaldict[i] = 1
        else:
            finaldict[i] += 1
    return finaldict


print(count(["hello","hello","world","world","hello"]))


        
