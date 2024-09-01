import wmi

class Local:
    @staticmethod
    def get_graphics_driver_version():
        c = wmi.WMI()
        drivers = []
        for item in c.Win32_VideoController():
            drivers.append(f"{item.Name} - {item.DriverVersion}")
        NVIDIADriver = [driver for driver in drivers if "NVIDIA" in driver]
        return (NVIDIADriver[0][-6:]).replace('.','')