CREATE TABLE IF NOT EXISTS 'temperature_humidity' (
  'id' integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  'humidity' real NOT NULL,
  'temperature' real NOT NULL,
  'datetime_stamp' datetime NOT NULL  
);

CREATE INDEX temperature_humidity_id ON temperature_humidity(id);