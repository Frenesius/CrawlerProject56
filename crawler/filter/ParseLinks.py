class ParseLinks():

    def __init__(self):
        pass

    def parseLinks(self, linkString, amountInt):
        linkArray = []
        print linkString
        print amountInt
        for x in range(1,amountInt):
            parsedLink = linkString+ str(x)
            linkArray.append(parsedLink)
        return linkArray
