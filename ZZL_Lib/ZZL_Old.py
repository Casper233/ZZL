import os
import shutil
from datetime import datetime

# 让用户输入周数和班级
week_num = input("请输入周数：")
class_name = input("请输入班级名称：")

# 创建文件夹
folder_name = "第" + week_num + "周 " + class_name
os.mkdir(folder_name)

# 写入log
with open(folder_name + "/log.txt", "w") as f:
    f.write(str(datetime.now()) + " 主程序已启动\n")

with open(folder_name + "/log.txt", "a") as f:
    f.write(str(datetime.now()) + " 周数为 " + week_num + "\n")

with open(folder_name + "/log.txt", "a") as f:
    f.write(str(datetime.now()) + " 班级为 " + class_name + "\n")

with open(folder_name + "/log.txt", "a") as f:
    f.write(str(datetime.now()) + " 创建文件夹成功\n")

# 检测是否有/模板 文件夹，如果没有，则新建/模板
if not os.path.exists("模板"):
    os.mkdir("模板")

# 复制/模板 的所有文件
for file_name in os.listdir("模板"):
    shutil.copy("模板/" + file_name, folder_name)

# 写入log
with open(folder_name + "/log.txt", "a") as f:
    f.write(str(datetime.now()) + " 复制文件成功\n")
