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

componentList = {"CPUcrawl":cpu_urls, "CPUpath": cpu_path, "GPUpath":gpu_path, "GPUcrawl":gpu_urls}
databaseConfig = {"db_path":db_path}








