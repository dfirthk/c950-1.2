import datetime
from datetime import timedelta

from csvReader import packageList
from hashTable import HashTable

#Creating Package Class along with it's associated functions
class Package:
    def __init__(self, packageID, address, city, state, zip, deadline, weight, notes, status="At the Hub", departTime = None, delTime = None):
        self.id = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.status = status
        self.departTime = departTime
        self.delTime = delTime
        self.truck = None
    #def __repr__(self):
        #return (f"{self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight}, {self.notes}, {self.status}, {self.departTime}, {self.delTime}")

    #Formatted return string of the object.
    def __str__(self):
        return f" {self.id} || {self.address} || {self.city} || {self.state} || {self.zip} || Deadline: {self.deadline} || {self.weight} ||  {self.notes} || {self.status} || Departure Time: {self.departTime} || Delivery Time: {self.delTime} || Truck Number: {self.truck}"

    #Function updating package status based on the time, as special notes change package instructions during the day
    def packageStatus(self, currentTime):
        tempDelTime = ''
        if self.delTime == None:
            tempStatus = "At the Hub"
        elif currentTime < self.departTime:
            tempStatus = "At the Hub"
        elif currentTime < self.delTime:
            tempStatus = "En Route"
        else:
            tempStatus = "Delivered"
            tempDelTime = self.delTime

        tempAddress = self.address
        tempZip = self.zip
        if self.id == 9:
            if currentTime < datetime.timedelta(hours=10, minutes=20):
                tempAddress = "300 State St"
                tempZip = "84103"
        return tempStatus, f" {self.id} || {tempAddress} || {self.city} || {self.state} || {tempZip} || Deadline: {self.deadline} ||  {self.weight} || {self.notes} || {tempStatus} ||  Departure Time: {self.departTime} || Delivery Time: {tempDelTime} || Truck Number: {self.truck}"

#Function that will insert packageList from csvReader.py into a packageHash object to later be inserted into the HashTable
def insertPackages(packageHash):
    for package in packageList:
        p = Package(
            packageID=int(package[0]),
            address=package[1],
            city=package[2],
            state=package[3],
            zip=package[4],
            deadline=package[5],
            weight=float(package[6]),
            notes=package[7]
        )
        packageHash.insert(p.id, p)

#Linking the packageHash list to the HashTable and inserting the data from the list to the HashTable
packageHash = HashTable()