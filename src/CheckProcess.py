import wmi

WMI_OBJ = wmi.WMI()

process_list = WMI_OBJ.Win32_process()

for process in process_list:
    print(process)
    break
