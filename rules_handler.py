#!/usr/bin/python3.3


# Load csv file in a list
def load_rules(rules, filename="rules.csv"):

    try:
        f = open(filename, "r")
        
    except FileNotFoundError:
        print("Unable to open : " + filename)
        return -1
    
    lines = f.readlines()
    
    for l in lines:
        l = l[:-1]
        rules.append(l.split(","))
        
    f.close()

# Write list to csv file
def write_rules(rules, filename="rules.csv"):
    f = open(filename, "w")
    
    for i in rules:
        f.write(i[0] + "," + i[1]+"\n")
    
    f.close()
