from collections import Counter

def processFile(inputFile, outputFile):
    #Read the input file
    leftColumn = []
    rightColumn = []

    with open(inputFile, 'r') as file:
        for line in file:
            left, right = line.strip().split('   ') #split the columns into left and right
            
            #Append column values into lists
            leftColumn.append(float(left))
            rightColumn.append(float(right))

    #Sort both column arrays
    leftColumn.sort()
    rightColumn.sort()

    #Calculate distances
    distances = [abs(left - right) for left, right in zip(leftColumn, rightColumn)]

    #Write distances to output file
    with open(outputFile, 'w') as file:
        for distance in distances:
            file.write(f"{distance}\n")
    
    #Print the sum of the distances
    totalDistance = sum(distances)
    print(f"Total Distance Between Lists: {totalDistance}")

def calculateSimilarity(inputFile):
    #Read the input file
    leftColumn = []
    rightColumn = []

    with open(inputFile, 'r') as file:
        for line in file:
            left, right = line.strip().split('   ') #split the columns into left and right
            
            #Append column values into lists
            leftColumn.append(float(left))
            rightColumn.append(float(right))

    #Sort both column arrays
    leftColumn.sort()
    rightColumn.sort()

    #Count occurrences of each number in the right column
    rightCount = Counter(rightColumn)

    #Initialize Similarity Score
    similarity = 0

    #Calculate similarity score
    for number in leftColumn:
        similarity += number * rightCount[number]

    return similarity

#Specify input and output
inputFile = 'input.txt'
outputFile = 'distances.txt'

#Solve the problem
processFile(inputFile, outputFile)
print(f"Similarity Score: {calculateSimilarity(inputFile)}")