import Adafruit_DHT as dht_sensor
import sqlite3 as sqlite3
import datetime as datetime

SENSORTYPE = dht_sensor.DHT22
GPIO_PIN = 17
DB = '/path/to/file'


def get_readings():
    try:
        humidity, temperature = dht_sensor.read_retry(sensor=SENSORTYPE, pin=GPIO_PIN)
        connection = sqlite3.connect(DB)
        cursor = connection.cursor()

        if (humidity is not None) and (temperature is not None):
            cursor.execute("INSERT INTO temperature_humidity VALUES ( NULL, ?, ?, ?)", (round(humidity, 2), round(temperature, 2), str(datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S"))))
            connection.commit()            
        else:
            print("Exception humidity is None or temperature is None")        

    except sqlite3.Error as e:
        print("SQL Error: {0}".format(e.args[0]))

    except Exception as e:
        print("Error: {0}".format(e.args[0]))

    finally:
        connection.close()
        print("Done")

if __name__ == "__main__":
    get_readings()

