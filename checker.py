# -*- coding: utf-8 -*-
import subprocess
import time
from datetime import datetime
import psutil
import os

def main():
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
        print("{}, temp:{}, cpu:{}, clock:{}, volts:{}, cpu_m:{},cpu_p:{}, gpu_m:{}".format(date, temp, cpu,clock, volts, memory_cpu,memory_percent, memory_gpu))
        
        """    
        fname = datetime.now().strftime('%Y%m%d')+".csv"
        if(os.path.isfile(fname)):
            fp = open(fname, 'a',encoding='Shift-JIS')
            
        else:
            fp = open(fname, 'w',encoding='Shift-JIS')
            fp.write("time,temp,cpu1,cpu2,cpu3,cpu4,clock,volts,cpu_m,cpu_p,gpu_m\n")


        # 結果表示
        fp.write("{},{},{},{},{},{},{},{},{},{},{}\n".format(datetime.now().strftime('%H:%M:%S'), temp, cpu[0],cpu[1],cpu[2],cpu[3],clock, volts, memory_cpu,memory_percent, memory_gpu))
        fp.close()
        time.sleep(0.8) # 1秒待つ
        """

# シェルコマンドを実行する関数
def run_shell_command(command_str):
    proc = subprocess.run(command_str, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    result = proc.stdout.split("=")
    return result[1].replace('\n', '')

if __name__ == '__main__':
    main()
