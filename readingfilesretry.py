import csv
with open("favorite_colors.csv", "r") as f:
    data = csv.DictReader(f)
    finaldict={}
    for student in data:
        grade = student['grade']
        color = student['favorite_color']
        if grade not in finaldict:
            finaldict[grade] = {}
        if color not in finaldict[grade]:
            finaldict[grade][color] = 0
        finaldict[grade][color] += 1
print(finaldict['12']['yellow'])