'''
Contains all the configs to crawl
    -   Paths
    -   links
    -   Dict



'''

#Db config path
db_path = "configs/db_config.conf"

#CPU
cpu_urls = ["http://tweakers.net/pricewatch/394885/intel-core-i7-4790k-boxed/specificaties/"]
cpu_path = "crawler/configs/CPU.conf"

#GPU
gpu_urls = ["http://tweakers.net/pricewatch/416125/msi-geforce-gtx-970-gaming-4g/specificaties/",
            "http://tweakers.net/pricewatch/416125/msi-geforce-gtx-970-gaming-4g/specificaties/",
            "http://tweakers.net/pricewatch/416129/asus-strix-gtx970-dc2oc-4gd5/specificaties/",
            "http://tweakers.net/pricewatch/416136/evga-geforce-gtx-970-superclocked-acx-20-4gb/specificaties/",
            "http://tweakers.net/pricewatch/416180/gigabyte-gv-n970g1-gaming-4gd/specificaties/",
            "http://tweakers.net/pricewatch/362247/sapphire-r9-290-4gb-gddr5-oc-tri-x/specificaties/"]
gpu_path = "crawler/configs/GPU.conf"

#MOBO
mobo_urls = ["http://tweakers.net/pricewatch/335948/msi-z87-g45-gaming/specificaties/"]
mobo_path = "crawler/configs/MOTHERBOARD.conf"

#MEMORY
mem_urls = ["http://tweakers.net/pricewatch/323351/crucial-ballistix-tactical-blt2c4g3d1608et3lx0ceu/specificaties/"]
mem_path = "crawler/configs/MEMORY.conf"

#PSU
psu_urls = ["http://tweakers.net/pricewatch/256222/seasonic-s12ii-bronze-520w/specificaties/"]
psu_path = "crawler/configs/PSU.conf"

#CASE
case_urls = ["http://tweakers.net/pricewatch/331061/cooler-master-n300-(kkn1-closed)/specificaties/"]
case_path = "crawler/configs/CASE.conf"


#HDD
hdd_urls = ["http://tweakers.net/pricewatch/385624/wd-red-sata-6-gb-s-wd60efrx-6tb/specificaties/"]
hdd_path = "crawler/configs/HDD.conf"

#SOUNDCARD
soundcard_urls = ["http://tweakers.net/pricewatch/229176/asus-xonar-essence-stx/specificaties/"]
soundcard_path = "crawler/configs/SOUNDCARD.conf"

#OPTICALDRIVE
opticaldrive_urls = ["http://tweakers.net/pricewatch/336304/samsung-sh-224db-zwart/specificaties/"]
opticaldrive_path = "crawler/configs/OPTICALDRIVE.conf"

#SSD
ssd_urls = ["http://tweakers.net/pricewatch/391575/crucial-mx100-256gb/specificaties/"]
ssd_path = "crawler/configs/SSD.conf"





componentList = {"PROCESSORcrawl":cpu_urls, "PROCESSORpath": cpu_path,                          #CPU
                 "GPUpath":gpu_path, "GPUcrawl":gpu_urls,                                       #GPU
                 "MEMORYcrawl":mem_urls, "MEMORYpath":mem_path,                                 #MEMORY
                 "PSUcrawl":psu_urls ,"PSUpath":psu_path,                                       #PSU
                 "MOTHERBOARDcrawl":mobo_urls,"MOTHERBOARDpath":mobo_path,                      #MOTHERBOARD
                 "CASEcrawl":case_urls,"CASEpath":case_path,                                    #CASE
                 "HDDcrawl":hdd_urls, "HDDpath":hdd_path,                                       #HDD
                 "SOUNDCARDcrawl":soundcard_urls,"SOUNDCARDpath":soundcard_path,                #SOUNDCARD
                 "OPTICALDRIVEcrawl":opticaldrive_urls, "OPTICALDRIVEpath":opticaldrive_path,   #OPTICALDRIVE
                 "SSDcrawl":ssd_urls, "SSDpath":ssd_path                                        #SSD
                 }

databaseConfig = {"db_path":db_path}








