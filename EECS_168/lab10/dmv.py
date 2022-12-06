# dmv.py

from driversLicense import License

class DMV:
    def __init__(self, fileName):
        """This function helps assign initial values to all of my variables"""
        self.file = fileName
    def buildLicenseList(self):
        """This function retrieves the file and builds a list of all the licenses within it"""
        licenseList = []
        for each in open(self.file, 'r'):
            line = each.split()
            license = License(line[0], line[1], line[2], line[3], line[4])
            licenseList.append(license)
        return licenseList
    def interface(self):
        """This function runs the program and calls all the other functions for the user"""
        while True:
            print("Select an option:")
            print("1) Print all Drivers Info, sorted by drivers license numbers")
            print("2) Print drivers by last initial")
            print("3) Print all young, unregistered voters")
            print("4) Print drivers of a specific age")
            print("5) Quit")
            response = int(input("Enter your choice: "))
            if response == 1:
                self.sortNum()
            if response == 2:
                self.sortInit()
            if response == 3:
                self.youngBums()
            if response == 4:
                ageIn = input("What age you would like to sort for?: ")
                self.singleAge(ageIn)
            if response == 5:
                print("Goodbye!!")
                break
    def sortNum(self):
        """This function sorts all the licenses within a DMV by license number"""
        tempList = self.buildLicenseList()
        idList = []
        for each in tempList:
            idList.append(each._lnumber)
            idList.sort()
        for eachid in idList:
            for eachlicense in tempList:
                if eachid == eachlicense._lnumber:
                    print(eachlicense)

    def sortInit(self):
        """This function sorts all of the licenses within in a DMV by last initial"""
        tempList = self.buildLicenseList()
        lnameList = []
        for each in tempList:
            lnameList.append(each._lname)
            lnameList.sort()
        for eachlname in lnameList:
            for eachlicense in tempList:
                if eachlname == eachlicense._lname:
                    print(eachlicense)

    def youngBums(self):
        """This function filters out all the licenses in a DMV between the ages of 18 and 24 if they are not a registered voter"""
        tempList = self.buildLicenseList()
        for each in tempList:
            if 18 < int(each._age) < 24 and each._voter == "N":
                print(each)


    def singleAge(self, ageIn):
        """This funciton sorts out all the licenses within a DMV that are of a particular inputted age"""
        tempList = self.buildLicenseList()
        for each in tempList:
            if each._age == ageIn:
                print(each)