"""
Name: Avi Kumar
Assignment: Reading File Practice

"""

import csv

#This function creates a dictionary called finaldict. {speciesname: {characteristic: []}, speciesname: {characteristic[]}}
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


#This function provides an answer to question 1 and 2. It uses finaldict from our first fucntion, finds the average of
#each trait (that is made up of numbers), and spits out the largest average
def largestaverage(trait):
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
    
    return biggest


    
def getcount(penguin,trait,spectrait):
    finaldict = findinfo(trait)
    foo = finaldict[penguin]['lengths']
    return foo.count(spectrait)
            


print(largestaverage('bill_length_mm'))
print(largestaverage('body_mass_g'))
print(getcount('Chinstrap','island','Dream'))

