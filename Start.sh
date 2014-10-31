#!/bin/bash
echo "starting"
echo "Crawling GPU"
sleep 1
	sudo scrapy crawl GPUcrawl
echo "DONE CRAWLING GPU"
sleep 1
echo "Crawling CPU"
sleep 1
	sudo scrapy crawl CPUcrawl
echo "DONE CRAWLING CPU"
sleep 1

echo "Crawling RAM"
sleep 1
	sudo scrapy crawl MEMORYcrawl
echo "DONE CRAWLING RAM"
sleep 1

echo "FINISHED"
sleep 3
