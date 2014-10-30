import SpecsSpider

class ProcessorSpider(SpecsSpider.SpecsSpider):
    name = "CPUcrawl"
    pathName = "CPUpath"
    label = "PROCESSOR" #UITZOEKEN
    relation = "GRAPHICSCARD" #UITZOEKEN


