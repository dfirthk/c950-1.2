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
        self.departTime = departTime if departTime is not None \
            else datetime.timedelta()
        self.delTime = delTime if delTime is not None \
            else datetime.timedelta()
    #def __repr__(self):
        #return (f"{self.address}, {self.city}, {self.state}, {self.zip}, {self.deadline}, {self.weight}, {self.notes}, {self.status}, {self.departTime}, {self.delTime}")

    def __str__(self):
        return f" {self.id} || {self.address} || {self.city} || {self.state} || {self.zip} || Deadline: {self.deadline} || {self.weight} ||  {self.notes} || {self.status} || Departure Time: {self.departTime} || Delivery Time: {self.delTime}"
    def packageStatus(self, currentTime):
        return f" {self.id} || , {self.address} || , {self.city} || , {self.state} || , {self.zip} || , Deadline: {self.deadline} ||, {self.weight} ||, {self.notes} ||, {self.status} || , Departure Time: {self.departTime} || , Delivery Time: {currentTime}"

    #Function updating package status based on the time, as special notes change package instructions during the day
    def updatePackage(self, currentTime):
        if self.delTime == None:
            self.status = "At the Hub"
        elif currentTime < self.departTime:
            self.status = "At the Hub"
        elif currentTime < self.delTime:
            self.status = "En Route"
        else:
            self.status = "Delivered"

        #Updating package 9's instruction based on what time it is.
        if self.id == 9 and currentTime > datetime.timedelta(hours=10, minutes=20):
            self.address = "410 S State St"
            self.zip = "84111"
        elif self.id == 9:
            self.address = "300 State St"
            self.zip = "84103"


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