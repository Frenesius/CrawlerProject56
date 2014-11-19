import crawler.filter.LinkManager as linkMan
'''
Contains all the configs to crawl
    -   Paths
    -   links
    -   Dict



'''
linkManager = linkMan.ParseLinks()
#Db config path
db_path = "configs/db_config.conf"

#CPU
cpu_urls = linkManager.getCrawlLinks("CPULink")
cpu_path = "crawler/configs/CPU.conf"

#GPU
gpu_urls = linkManager.getCrawlLinks("GPULink")
gpu_path = "crawler/configs/GPU.conf"

#MOBO
mobo_urls = linkManager.getCrawlLinks("MOTHERBOARDLink")
mobo_path = "crawler/configs/MOTHERBOARD.conf"

#MEMORY
mem_urls = linkManager.getCrawlLinks("MEMORYLink")
mem_path = "crawler/configs/MEMORY.conf"

#PSU
psu_urls = linkManager.getCrawlLinks("PSULink")
psu_path = "crawler/configs/PSU.conf"

#CASE
case_urls = linkManager.getCrawlLinks("CASELink")
case_path = "crawler/configs/CASE.conf"


#HDD
hdd_urls = linkManager.getCrawlLinks("HDDLink")
hdd_path = "crawler/configs/HDD.conf"

#SOUNDCARD
soundcard_urls = linkManager.getCrawlLinks("SOUNDCARDLink")
soundcard_path = "crawler/configs/SOUNDCARD.conf"

#OPTICALDRIVE
opticaldrive_urls = linkManager.getCrawlLinks("OPTICALDRIVELink")
opticaldrive_path = "crawler/configs/OPTICALDRIVE.conf"

#SSD
ssd_urls = linkManager.getCrawlLinks("SSDLink")
ssd_path = "crawler/configs/SSD.conf"

#TEST
test_urls = linkManager.getCrawlLinks("TESTLink")
test_path = "crawler/configs/TEST.conf"



componentList = {"PROCESSORcrawl":cpu_urls, "PROCESSORpath": cpu_path,                          #CPU
                 "GPUpath":gpu_path, "GPUcrawl":gpu_urls,                                       #GPU
                 "MEMORYcrawl":mem_urls, "MEMORYpath":mem_path,                                 #MEMORY
                 "PSUcrawl":psu_urls ,"PSUpath":psu_path,                                       #PSU
                 "MOTHERBOARDcrawl":mobo_urls,"MOTHERBOARDpath":mobo_path,                      #MOTHERBOARD
                 "CASEcrawl":case_urls,"CASEpath":case_path,                                    #CASE
                 "HDDcrawl":hdd_urls, "HDDpath":hdd_path,                                       #HDD
                 "SOUNDCARDcrawl":soundcard_urls,"SOUNDCARDpath":soundcard_path,                #SOUNDCARD
                 "OPTICALDRIVEcrawl":opticaldrive_urls, "OPTICALDRIVEpath":opticaldrive_path,   #OPTICALDRIVE
                 "SSDcrawl":ssd_urls, "SSDpath":ssd_path,                                       #SSD
                 "TESTcrawl":test_urls, "TESTpath":test_path                                    #TEST
                 }

databaseConfig = {"db_path":db_path}
#########################

#SOUNDCARD

soundcard_path_price = "crawler/configs/price/SOUNDCARD.conf"
soundcard_urls_price = linkManager.getPriceCrawlLinks("crawler/price-config/SOUNDCARD.json")
soundcard_EAN_price = linkManager.getEANList("crawler/price-config/SOUNDCARD.json")


price_configs = {"SOUNDCARDpath":soundcard_path_price, "SOUNDCARDprice":soundcard_urls_price, "SOUNDCARDEAN":soundcard_EAN_price,
}