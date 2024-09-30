import csv

#Creating function that allows me to pick the starting/ending rows/columns and then loop through the CSV's to pull the data I need and append to a list
def readData(filename, startRow, endRow, startCol, endCol):
    dataList = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
        for rowIndex in range(startRow, endRow):
            if rowIndex < len(data):
                row = data[rowIndex]
                selectedRow = []
                for colIndex in range(startCol, endCol):
                    if colIndex < len(row):
                        selectedRow.append(row[colIndex])
                dataList.append(selectedRow)
        return dataList

#Running readData on the Distances.csv and Packages.csv files to pull the needed data from the files and append it to their own lists
distanceList = readData("./csvs/Distances.csv", 8, 35, 2, 30)
packageList = readData("./csvs/Packages.csv", 8, 48, 0, 8)
addressList = readData("./csvs/Distances.csv", 5, 32, 0, 1)

#trimming addressList to be setup how I want

transformed_list = []

# Iterate through the addressList
for i, address in enumerate(addressList):
    # Convert address from list to string and split it at '\n'
    split_address = ''.join(address).split('\n')
    transformed_address = [i] + split_address
    transformed_list.append(transformed_address)

addressList = transformed_list

# Converting everything in the distanceList to floats
def convertToFloat(distanceList):
    floatList = []
    for sublist in distanceList:
        floatSublist = []
        for item in sublist:
            try:
                floatSublist.append(float(item))
            except ValueError:
                # Handle the case where conversion to float is not possible
                floatSublist.append(None)
        floatList.append(floatSublist)
    return floatList

#distanceList = convertToFloat(distanceList)

#Uncomment following commands to test if function is working
#print(distanceList)
#print(packageList)
#print(addressList)

for row in distanceList:
    print(row)
