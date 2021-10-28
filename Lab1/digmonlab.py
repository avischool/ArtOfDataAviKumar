import csv


def largesthp():
    with open("digimon.csv", "r") as f:
        data = csv.DictReader(f)
        finaldict = {}
        for pokemon in data:
            species = pokemon['Digimon']
            hp = pokemon['HP']
            if species not in finaldict:
                finaldict[species] = 0
            finaldict[species] += float(hp)
        
        for i in range(3):
            max_key = max(finaldict,key=finaldict.get)
            print(max_key)
            print(finaldict[max_key])
            finaldict.pop(max_key)

# This function simply iterates through every row, adds each speed to the variable "total", 
# and divides "total" by the number of Digimon. This gives us the average speed of all the digimon.
def averagespeed():
    with open("digimon.csv", "r") as f:
        data = csv.DictReader(f)
        total = 0
        digimon_count = 0
        for pokemon in data:
            total += float(pokemon['Spd'])
            digimon_count+=1
    return total/digimon_count


# Our dictionary is set up as {trait:number of digimon with that trait}
# The first parement is the column name, and the second is the trait or characteristic we are trying to identify
# We go through each row and if a characteristic is not yet a key in our dictionary, we add it and find how many times that specific
# characteristic shows up. We then just print out what the number of digimon with the characteristic that the function is calling 
def getcount(column_name,specific_trait):
    with open("digimon.csv", "r") as f:
        data = csv.DictReader(f)
        finaldict = {}
        for pokemon in data:
            attribute = pokemon[column_name]
            if attribute not in finaldict:
                finaldict[attribute] = 0 
            finaldict[attribute] += 1
    return finaldict[specific_trait]


# We are running a triple nested for loop. This allows us to iterate through every possible combination of three digimon.
#"listofteams" originally printed triplets that had two of the same digimon, so to prevent this, the function checks whether there 
# is a duplicate in the list by converting it to a set, and seeing if the lengths are the same.
def bestteam():
    with open("digimon.csv", "r") as f:
        data = list(csv.DictReader(f))
        listofteams = []
        for a in range(0,len(data)):
            for b in range(a+1,len(data)):
                for c in range(b+1,len(data)):
                    totalatk = float(data[a]['Atk'])+float(data[b]['Atk'])+float(data[c]['Atk'])
                    totalmemory = float(data[a]['Memory'])+float(data[b]['Memory'])+float(data[c]['Memory'])
                    if totalatk >= 300 and  totalmemory<= 15:
                        specific_team = [data[a]['Digimon'],data[b]['Digimon'],data[c]['Digimon']]
                        listofteams.append(specific_team)
                        
    return listofteams
    
print(bestteam())
