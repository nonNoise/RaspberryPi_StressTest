import subprocess

command_str = ["dstat -a"] 
proc = subprocess.Popen(command_str, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
proc.stdout.readline()
proc.stdout.readline()

while True:
    buf = proc.stdout.readline().replace('|', '').split()
    dstat_json = {}
    dstat_json["cpu_usage"]  = {}
    dstat_json["cpu_usage"]["usr"]  = buf[0]
    dstat_json["cpu_usage"]["sys"]  = buf[1]
    dstat_json["cpu_usage"]["idl"]  = buf[2]
    dstat_json["cpu_usage"]["wai"]  = buf[3]
    dstat_json["cpu_usage"]["stl"]  = buf[4]
    dstat_json["dsk"]  = {}
    dstat_json["dsk"]["read"]       = buf[5]
    dstat_json["dsk"]["writ"]       = buf[6]
    dstat_json["net"]  = {}
    dstat_json["net"]["recv"]       = buf[7]
    dstat_json["net"]["send"]       = buf[8]
    dstat_json["paging"] = {} 
    dstat_json["paging"]["in"]      = buf[9]
    dstat_json["paging"]["out"]     = buf[10]
    dstat_json["system"] = {} 
    dstat_json["system"]["int"]     = buf[11]
    dstat_json["system"]["csw"]     = buf[12]
    print(dstat_json["net"])
       
    