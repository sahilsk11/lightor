import json
import urllib
import passwords
import datetime
import calendar
import time

def convert_zip(zip_code):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(zip_code) + "&key=" + str(passwords.map_api())
    fh = urllib.urlopen(url)
    read = fh.read()
    load = json.loads(read)
    return load["results"][0]["geometry"]["location"]["lat"], load["results"][0]["geometry"]["location"]["lng"]

def get_sunset_dark(lat, lon):
    url = "http://api.sunrise-sunset.org/json?formatted=0&lat=%s&lng=%s" % (lat, lon)
    fh = urllib.urlopen(url)
    read = fh.read()
    load = json.loads(read)
    return load["results"]["sunset"], load["results"]["civil_twilight_end"]

def utc_2_local(utc):
        print "utc_2_local: before convert:", utc
        timestamp =  calendar.timegm((datetime.datetime.strptime( utc, TIME_FORMAT)).timetuple())
        local = datetime.datetime.fromtimestamp(timestamp).strftime(TIME_FORMAT)
        print "utc_2_local: after convert:", local

(lat, lon) = convert_zip(95138)
(utc_sunset, utc_dark) = get_sunset_dark(lat, lon)
print utc_2_local(utc_sunset)
