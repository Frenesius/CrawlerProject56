__author__ = 'j'
import re as regex

class FilterDict():
    timesFiltered = 0


    def __init__(self):
        pass

    def filterDictionary(self, dictionary):
        filteredDict = {}
        filteredDict = self.filterEmpty(dictionary)


        self.printDict(filteredDict)

    def filterEmpty(self, dictionary):
        newDict = {}
        y = 0

        for x in dictionary:
            key =  dictionary.keys()[y]
            value =  dictionary.values()[y]
            y +=1
            pattern = r"\[u'\\xa0'\]"
            pattern2 = r"(\[\])"
            pattern3 = r"(\[\s\])"
            if regex.search(pattern, key) or regex.search(pattern, value):
                print "filtered"
            elif regex.search(pattern2, key) or regex.search(pattern2, value):
                print "filtered"
            elif regex.search(pattern3, key) or regex.search(pattern3, value):
                print "filtered"
            else:
                newDict.update({str(key): str(value)})
        self.timesFiltered += 1
        return newDict

    def filterSpaces(self):
        pass


    def printDict(self, dict):
        print " ++++++++++++++++++++"
        print " PRINTING NEWEST DICT"
        print " Dict has been %s times filtered!" % self.timesFiltered
        print " Dict has %s lines!" % len(dict)
        print " ++++++++++++++++++++"

        y = 0
        for x in dict:
            key =  dict.keys()[y]
            value =  dict.values()[y]
            print key, value
            y +=1
