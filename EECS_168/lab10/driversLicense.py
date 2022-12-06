# driversLicense.py

class License:
    def __init__(self,lnumber = 0, fname = "", lname = "", age = 0, voter = ""):
        self._lnumber = lnumber
        self._fname = fname
        self._lname = lname
        self._age = age
        self._voter = voter
    def __lt__(self, other):
        return self._lnumber < other._lnumber
    def __gt__(self, other):
        return self._lnumber > other._lnumber
    def __le__(self, other):
        return self._lnumber <= other._lnumber
    def __ge__(self, other):
        return self._lnumber >= other._lnumber
    def __eq__(self, other):
        return self._lnumber == other._lnumber
    def __ne__(self, other):
        return self._lnumber != other._lnumber
    def __str__(self):
        output = f"Account Number: {self._lnumber}\n"
        output += f"Name: {self._lname}, {self._fname}\n"
        output += f"Age: {self._age}\n"
        output += f"Voter Status: {self._voter}\n"
        return output
    def __repr__(self):
        return f"License(lnumber = {self._lnumber}, fname = {self._fname}, lname = {self._lname}, age = {self._age}, voter = {self._voter}"