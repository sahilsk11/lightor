import shelve
import conversion
import datetime

"""
Object contains:
1. On and off times
2. Current state
"""
class informationhandler:
    def __init__(self, ports=[]):
        self.file = shelve.open("data-storage.shelve", writeback=True)
        if (not self.file.has_key("ports")):
            self.file["ports"] = {}
            index = 0
            if (len(ports) <= 0):
                raise RuntimeError('Invalid Port')
            for index in range(0, len(ports)):
                self.file["ports"][index] = {}
                self.file["ports"][index]["name"] = "Unnamed Zone " + str(index+1)
                self.file["ports"][index]["port"] = ports[index]
                self.file["ports"][index]["state"] = "OFF"
                index+=1
            self.file["override"] = {}
            self.file["override"]["override_on"] = False
            self.file["frontend"] = {}

    def change_light_name(self, old_name, new_name):
        for index in self.file["ports"]:
            if (self.file["ports"][index]["name"] == old_name):
                self.file["ports"][index]["name"] = new_name
                return True
        return False
    
    def transfer_ports(self):
        temp = self.file["ports"]
        self.file["frontend"]["ports"] = temp
                
    def set_port(self, index, state):
        if ((not state == "ON") and (not state == "OFF")):
            return False
        else:
            self.file["ports"][index]["state"] = state
            return True
    
    def set_ports(self, state):
        if ((not state == "ON") and (not state == "OFF")):
            return False
        for index in self.file["ports"]:
            self.set_port(index, state)
        return True
    
    def add_readable_times(self, sunrise, sunset):
        self.file["frontend"]["readable_times"] = {}
        self.file["frontend"]["readable_times"]["sunrise"] = sunrise
        self.file["frontend"]["readable_times"]["sunset"] = sunset
        
    def change_override(self, override_on, override_state=False):
        self.file["override"]["override_on"] = override_on
        if (override_on == True):
            self.file["override"]["setting"] = override_state
            self.file["override"]["off"] = datetime.datetime.now() + datetime.timedelta(hours=1)

    def delete_shelve(self):
        self.file.clear()       