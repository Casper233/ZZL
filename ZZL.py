import ZZL_Lib.ZZL_CopyFile
import os


def close_window():
    if os.name == "nt":
        # Windows系统
        os.system("taskkill /f /im python.exe")
    else:
        # 其他系统
        os.system("kill -9 {}".format(os.getpid()))


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
            ZZL_Lib.ZZL_CopyFile.FileCopy()
            print("程序已完成")

    print("程序已退出")


if __name__ == "__main__":
    Main()
