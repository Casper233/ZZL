import os
import shutil
from datetime import datetime

def create_folder(week_num: str, grade_name: str, class_name: str) -> str:
    """创建文件夹，并返回文件夹路径"""
    folder_name = f"第{week_num}周 {grade_name}{class_name}"
    os.mkdir(folder_name)
    log_file = os.path.join(folder_name, "log.txt")
    with open(log_file, "w") as f:
        f.write(f"{datetime.now()} 主程序已启动\n")
        f.write(f"{datetime.now()} 周数为 {week_num}\n")
        f.write(f"{datetime.now()} 班级为 {grade_name}{class_name}\n")
        f.write(f"{datetime.now()} 创建文件夹成功\n")
    return folder_name

def copy_template_files(template_dir: str, dest_dir: str) -> None:
    try:
        for file_name in os.listdir(template_dir):
            src_file = os.path.join(template_dir, file_name)
            dest_file = os.path.join(dest_dir, file_name)
            shutil.copy(src_file, dest_file)
        with open(os.path.join(dest_dir, "log.txt"), "a") as f:
            f.write(f"{datetime.now()} 复制文件成功\n")
    except Exception as e:
        with open(os.path.join(dest_dir, "log.txt"), "a") as f:
            f.write(f"{datetime.now()} 复制文件失败：{e}\n")

def FileCopy():
    week_num = input("请输入周数：")
    grade_list = ["初一","初二","初三","高一","高二","高三"]
    grade_num = input(f"请选择年级（输入数字 1-{len(grade_list)}）：\n{grade_list}\n")

    try:
        grade_num = int(grade_num)
        if grade_num < 1 or grade_num > len(grade_list):
            raise ValueError
    except ValueError:
        print("输入不合法，请重新输入")
        return

    grade_name = grade_list[int(grade_num) - 1]
    class_name = input("请输入班级：")
    class_name = f"({class_name})班"
    folder_path = create_folder(week_num, grade_name, class_name)
    template_dir = "模板"

    if not os.path.exists(template_dir):
        os.mkdir(template_dir)
    copy_template_files(template_dir, folder_path)



if __name__ == "__main__":
    FileCopy()

