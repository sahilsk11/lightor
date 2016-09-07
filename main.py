import conversion
#import control
import informationhandle
import datetime


def reset_override():
    if (db.file["override"]["override_on"] == False):
        return False
    now = datetime.datetime.now()
    off = db.file["override"]["off"]
    if (now >= off):
        db.change_override(False)
        return False
    return True

def switch_lights(change_state, override):
    if (override == True):
        #controller.ports_on()
        return 0

def run_program(db, zip):
    override = db.file["override"]["override_on"]
    (lat, lon) = conversion.convert_zip(zip)
    (sunrise, sunset) = conversion.format_date(lat, lon)
    db.add_readable_times(sunset, sunrise)
    change_state = conversion.on_now(lat, lon)
    db.transfer_ports()
    reset_override()
    print db.file["frontend"]

ports = [3, 5, 8]
zip = 95138

db = informationhandle.informationhandler(ports)
db.set_ports("ON")

#controller = control.relay_control(ports)

run_program(db, zip)