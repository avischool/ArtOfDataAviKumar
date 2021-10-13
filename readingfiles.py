# # with open("favorite_colors.csv", "r") as f:  print(f) 
import csv
# with open("favorite_colors.csv", "r") as f:
#     data = csv.DictReader(f)
#     for row in data:
#         print(row)


def readingfiles(grade, favcolor):
    newdict = {9:[],10:[],11:[],12:[]}
    a = 0
    with open("favorite_colors.csv", "r") as f:
        data = csv.DictReader(f)
        for row in data:
            newdict[int(row['grade'])].append(row['favorite_color'])
    
    for (k,v) in newdict.items():
        if k == grade:
            for col in v:
                if col == favcolor:
                    a += 1
    print(a)







readingfiles(9,'yellow')