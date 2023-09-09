import os
import shutil
from datetime import datetime


def close_window():
    if os.name == "nt":
        # Windows系统
        os.system("taskkill /f /im python.exe")
    else:
        # 其他系统
        os.system("kill -9 {}".format(os.getpid()))


# Copy File Area
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
    grade_list = ["初一", "初二", "初三", "高一", "高二", "高三"]
    grade_num = input(f"请选择年级（输入数字 1-{len(grade_list)}）：\n{grade_list}\n")

    try:
        grade_num = int(grade_num)
        if grade_num < 1 or grade_num > len(grade_list):
            raise ValueError
    except ValueError:
        print("输入不合法，请重新输入")
        return 0

    grade_name = grade_list[int(grade_num) - 1]
    class_name = input("请输入班级：")
    class_name = f"({class_name})班"
    folder_path = create_folder(week_num, grade_name, class_name)
    template_dir = "模板"

    if not os.path.exists(template_dir):
        os.mkdir(template_dir)
    copy_template_files(template_dir, folder_path)

    return 7


def FileCopy_Start():
    FileCopy()
    if FileCopy() == "None":
        FileCopy()

# Distribute Area

def Main():
    program_list = ["新周复制", "统计某日数据整合", "还是不知道是啥程序"]

    while True:
        print("请选择要执行的程序：")
        for i, program in enumerate(program_list):
            print(f"{i + 1}. {program}")
        print("0. 退出程序")

        choice = input("请输入程序编号：")
        if choice == "0":
            break

        try:
            choice = int(choice)
            if choice < 1 or choice > len(program_list):
                raise ValueError
        except ValueError:
            print("输入不合法，请重新输入")
            continue

        program_name = program_list[choice - 1]
        print(f"正在打开 {program_name} ...")
        # 在这里执行对应的程序
        if program_name == "新周复制":
            FileCopy_Start()
            print("程序已完成")
        elif program_name == "统计某日数据整合":
            print("程序已完成")

    print("程序已退出")


if __name__ == "__main__":
    Main()
