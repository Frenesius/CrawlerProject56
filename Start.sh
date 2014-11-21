echo "=== Starting the crawler ==="
echo "\tChmod +x to the executables"
sudo chmod +x Refresh-Crawl-Links.sh
sudo chmod +x Crawl-Specs.sh
sudo chmod +x Update-Prices.sh
echo "\tDone chmod"
echo "\tStaring the crawls"
./Refresh-Crawl-Links.sh
echo "1/3 Done"
sleep 10
./Crawl-Specs.sh
echo "2/3 Done"
sleep 10
./Update-Prices.sh
echo "3/3 Done"
sleep 10
echo "=== Done ==="
