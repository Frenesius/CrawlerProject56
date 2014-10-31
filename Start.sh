#!/bin/bash
echo "starting"
echo "Crawling GPU"
sleep 1
	sudo scrapy crawl GPUcrawl
echo "DONE CRAWLING GPU"
sleep 1
echo "Crawling CPU"
sleep 1
	sudo scrapy crawl PROCESSORcrawl
echo "DONE CRAWLING CPU"
sleep 1

echo "Crawling RAM"
sleep 1
	sudo scrapy crawl MEMORYcrawl
echo "DONE CRAWLING RAM"
sleep 1

echo "Crawling PSU"
sleep 1
	sudo scrapy crawl PSUcrawl
echo "DONE CRAWLING RAM"
sleep 1

echo "Crawling Motherboard"
sleep 1
	sudo scrapy crawl MOTHERBOARDcrawl
echo "DONE CRAWLING RAM"
sleep 1

echo "Crawling Case"
sleep 1
	sudo scrapy crawl CASEcrawl
echo "DONE CRAWLING Case"
sleep 1

echo "Crawling Soundcard"
sleep 1
	sudo scrapy crawl SOUNDCARDcrawl
echo "DONE CRAWLING SOUNDCARD"
sleep 1

echo "Crawling SSD"
sleep 1
	sudo scrapy crawl SSDcrawl
echo "DONE CRAWLING SSD"
sleep 1

echo "Crawling HDD"
sleep 1
	sudo scrapy crawl HDDcrawl
echo "DONE CRAWLING HDD"
sleep 1

echo "Crawling Optical Drive"
sleep 1
	sudo scrapy crawl OPTICALDRIVEcrawl
echo "DONE CRAWLING OPTICALDRIVE"
sleep 1








echo "FINISHED"
sleep 3
