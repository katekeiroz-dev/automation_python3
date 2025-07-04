inputFile = open("inputFile.txt" , "r")
for line in inputFile :
    line_slit = line.split()
    if line_slit[2] == "F":
        print(line)
    
inputFile.close()