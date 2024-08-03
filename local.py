import wmi

class Local:
    @staticmethod
    def get_graphics_driver_version():
        c = wmi.WMI()
        drivers = []
        for item in c.Win32_VideoController():
            drivers.append(f"{item.Name} - {item.DriverVersion}")
        return (drivers[-1][-6:]).replace('.','')
