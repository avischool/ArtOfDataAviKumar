import csv

def findinfo(characteristic):
    with open("penguins.csv", "r") as f:
        data = csv.DictReader(f)
        finaldict={}
        for penguin in data:
            species = penguin['species']
            bill_length = penguin[characteristic]
            if species not in finaldict:
                finaldict[species] = {}
                finaldict[species]["lengths"] = []
            listlengths = finaldict[species]["lengths"]
            listlengths = listlengths.append(bill_length)
    return finaldict


def getaverage(trait):
    finaldict = findinfo(trait)   
    
    listoflengths = []
    biggest = ""

    for key in finaldict:
        numoflengths = 0
        finallength=0
        
        for length in finaldict[key]['lengths']:
            finallength += float(length)
            numoflengths += 1
        listoflengths.append((finallength/numoflengths))
        if max(listoflengths) == finallength/numoflengths:
            biggest = key
    
    return listoflengths
        

print(getanswer('bill_length_mm'))