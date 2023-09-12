# -*- coding: utf-8 -*-
import subprocess
import time
from datetime import datetime
import psutil
import os

import subprocess




def main():

    command_str = ["dstat -a"] 
    proc = subprocess.Popen(command_str, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    proc.stdout.readline()
    proc.stdout.readline()
    while True:
        date       = datetime.now().strftime("%Y/%m/%d %H:%M:%S")          # 現在時刻
        temp       = run_shell_command("vcgencmd measure_temp")      # CPU温度
        clock      = run_shell_command("vcgencmd measure_clock arm") # CPU周波数
        clock      = str(int(clock)/1000000000)
        volts      = run_shell_command("vcgencmd measure_volts")     # CPU電圧
        memory_cpu = run_shell_command("vcgencmd get_mem arm")       # CPUのメモリ使用量
        memory_gpu = run_shell_command("vcgencmd get_mem gpu")       # GPUのメモリ使用量
        cpu = psutil.cpu_percent(percpu=True)                        # CPU使用率
        memory_percent = psutil.virtual_memory().percent             # メモリ使用率

        buf = proc.stdout.readline().replace('|', ' ').split()
        print(buf)
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

        print("{}, temp:{}, cpu:{}, clock:{}, volts:{},mem_p:{},net:{}".format(date, temp, cpu,clock, volts,memory_percent,dstat_json["net"]["send"]))


        time.sleep(0.8) # 1秒待つ
        
        
        fname = datetime.now().strftime('%Y%m%d')+".csv"
        if(os.path.isfile(fname)):
            fp = open(fname, 'a',encoding='Shift-JIS')
            
        else:
            fp = open(fname, 'w',encoding='Shift-JIS')
            fp.write("time,temp,cpu1,cpu2,cpu3,cpu4,clock,volts,mem_p,net_recv,net_send\n")

        # 結果表示
        fp.write("{},{},{},{},{},{},{},{},{},{},{}\n".format(datetime.now().strftime('%H:%M:%S'), temp, cpu[0],cpu[1],cpu[2],cpu[3],clock, volts, memory_percent, dstat_json["net"]["recv"], dstat_json["net"]["send"]))
        fp.close()

# シェルコマンドを実行する関数
def run_shell_command(command_str):
    proc = subprocess.run(command_str, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    result = proc.stdout.split("=")
    return result[1].replace('\n', '')


if __name__ == '__main__':
    main()
