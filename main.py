import psutil


if __name__ == "__main__":
    list_of_programs = []
    psutil.process_iter(attrs=None, ad_value=None)
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            process_data = proc.cwd
            process_location = psutil.Process(processID).exe()
            # print(processName , "\t\t\t", processID, "\t\t\t", process_location)            
            # list_of_programs.append(processName)
            if "Microsoft.SkypeApp_14.54.85.0_x64__kzf8qxf38zg5c" in process_location:
                print("The good skype has been detected!")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        


    # print(list_of_programs)
    # how_many_instances = 0
    # how_many_instances += list_of_programs.count("Skype.exe")
    # print(how_many_instances)