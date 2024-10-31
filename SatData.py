# Author: Jovane Cano
# GitHub Username: jovanecano
# Date: 10/30/2024
# Description:
""" program contains a class named SatData that reads a json file
 and writes the data to a text file in a csv format"""

#importing the json module
import json

class SatData:
    def __init__(self):
        with open('sat.json', 'r') as file:
            self._data = json.load(file)

    #method to create headers (hardcoding), prepares the outfile, and saves as csv
    def save_as_csv(self,dbns):
        #creating the headers
        headers = ["DBN", "School Name", "Number of test takers", "Critical Reading Mean", "Math Mean", "Writing Mean"]

