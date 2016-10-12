# Store Temperature and Humidity data

## Intro
Store temperature and humidity data from a DHT_22 sensor connected to a Raspberry PI board to a sqlite3 database. 

## How To
1. Connect the sensor to the port 17 on the Raspberry Pi board
2. Clone current repository
4. Clone and install Adafruit_DHT repository (https://github.com/adafruit/Adafruit_Python_DHT) follow steps
3. Update the DB variable with the path to the weather-data.db file
4. Create a crontab job that runs readdata.py every hour or so (depending on your needs). Or just make a script and add the script to the crontab (https://help.ubuntu.com/community/CronHowto). 
