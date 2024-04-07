import os
import subprocess

# 执行系统命令函数
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

# 示例功能：查看系统信息
def get_system_info():
    output, _ = run_command('uname -a')
    print(output.decode('utf-8'))

if __name__ == "__main__":
    get_system_info()

