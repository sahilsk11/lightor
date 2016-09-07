import json
import urllib
import passwords
import datetime
import datetime
from dateutil import tz

def convert_zip(zip_code):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(zip_code) + "&key=" + str(passwords.map_api())
    fh = urllib.urlopen(url)
    read = fh.read()
    load = json.loads(read)
    return load["results"][0]["geometry"]["location"]["lat"], load["results"][0]["geometry"]["location"]["lng"]

def get_dark_time(lat, lon):
    now = str(datetime.datetime.now())
    url = "http://api.sunrise-sunset.org/json?formatted=0&lat=%s&lng=%s&date=%s" % (lat, lon, now)
    fh = urllib.urlopen(url)
    read = fh.read()
    load = json.loads(read)
    return load["results"]["civil_twilight_end"]

def get_sunrise(lat, lon):
    dt_now = datetime.datetime.now()
    dt_next = dt_now + datetime.timedelta(days=1)
    dt_next = str(dt_next)
    url = "http://api.sunrise-sunset.org/json?formatted=0&lat=%s&lng=%s&date=%s" % (lat, lon, dt_next)
    fh = urllib.urlopen(url)
    read = fh.read()
    load = json.loads(read)
    return load["results"]["astronomical_twilight_begin"]

def from_utc(utc):
    utc = datetime.datetime.strptime(utc, "%Y-%m-%dT%H:%M:%S+00:00")
    UTC_OFFSET_TIMEDELTA = datetime.datetime.utcnow() - datetime.datetime.now()
    local = utc - UTC_OFFSET_TIMEDELTA
    return local

def on_now(lat, lon):
    current_time = str(datetime.datetime.now())
    sunset_time = get_dark_time(lat, lon)
    sunrise_time = get_sunrise(lat, lon)
    sunset_time = from_utc(sunset_time)
    sunrise_time = from_utc(sunrise_time)
    current_time = current_time[:19]
    current_time = datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')
    return (sunrise_time > current_time > sunset_time)

def format_date(lat, lon):
    sunrise_time = from_utc(get_sunrise(lat, lon))
    sunset_time = from_utc(get_dark_time(lat, lon))
    readable_sunrise_time = datetime.datetime.strftime(sunrise_time, '%I:%M %p')
    readable_sunset_time = datetime.datetime.strftime(sunset_time, '%I:%M %p')
    return (readable_sunset_time, readable_sunrise_time)
