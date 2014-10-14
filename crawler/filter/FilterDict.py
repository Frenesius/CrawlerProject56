__author__ = 'j'
import re as regex

class FilterDict():
    pass


    def __init__(self):
        pass

    def getDict(self, dictionary):
        newDict = {}
        y = 0

        for x in dictionary:
            key =  dictionary.keys()[y]
            value =  dictionary.values()[y]
            y +=1
            if key or value != "":
                newDict.update({str(key): str(value)})

        return newDict

    def printDict(self, dict):

        print "Printing dict"
        y = 0
        for x in dict:
            key =  dict.keys()[y]
            value =  dict.values()[y]
            print key, value
            y +=1
