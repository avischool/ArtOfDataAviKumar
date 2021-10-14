import csv

def oneaverage(specificspecies):
    with open("penguins.csv", "r") as f:
        data = csv.DictReader(f)
        table = {}
        thing = 0
        anotherthing = 0
        for penguin in data:
            if penguin['species'] == specificspecies:
                thing += float(penguin['bill_length_mm'])
                anotherthing += 1
        
        return thing/anotherthing

with open("penguins.csv", "r") as f:
    data = csv.DictReader(f)
    diction = {}
    for penguin in data:
        species = penguin['species']
        if species not in diction:
            diction[species] = {}
        if penguin['bill_length']
    
