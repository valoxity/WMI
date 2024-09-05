# pyinstaller --onefile --uac-admin  WMI.py

import wmi

import time
# Initialize the WMI interface
c = wmi.WMI()
 
def get_windows_device_id():
    try:
        # Create a WMI object
        wmi_obj = wmi.WMI() 
        # Query the Win32_ComputerSystemProduct class to get the device ID
        for item in wmi_obj.Win32_ComputerSystemProduct():
            return item.UUID.strip()  # Strip any leading or trailing whitespaces
    except Exception as e:
        print("Error:", e)
        return None
     
# Retrieve CPU information
for cpu in c.Win32_Processor():
    print(f"CPU ID: {cpu.ProcessorId}")

# Retrieve motherboard information
for board in c.Win32_BaseBoard():
    print(f"Motherboard Serial Number: {board.SerialNumber}")

# Retrieve hard drive information
for disk in c.Win32_DiskDrive():
    print(f"Hard Drive Serial Number: {disk.SerialNumber}")

# Retrieve network adapter MAC address
for nic in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
    print(f"MAC Address: {nic.MACAddress}")

print(f"WMI: {get_windows_device_id()}" )