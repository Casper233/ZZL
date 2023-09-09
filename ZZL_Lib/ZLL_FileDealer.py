import os
import docx
import argparse
import logging
import datetime

def start_dealer():
    if not os.path.exists('dealer_temp'):
        os.makedirs('dealer_temp')
    if not os.path.exists('logs'):
        os.makedirs('logs')
    # 初始化日志模块
    now = datetime.datetime.now()

    # 创建logger对象
    logger = logging.getLogger(__name__)

    # 设置日志级别为INFO
    logger.setLevel(logging.INFO)

    # 创建文件处理器
    filename = now.strftime("%Y-%m-%d_%H-%M-%S") + "dealer-log.txt"
    file_handler = logging.FileHandler(os.path.join('logs', filename))


    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # 添加处理器到logger
    logger.addHandler(file_handler)

    main()
    logger.info("正在启动Dealer")

# 列出指定目录中的所有文件和文件夹

def list_files(path, show_files=True):
    logging.info(f"列出目录 {os.path.abspath(path)} 中的文件和文件夹")
    try:
        files = os.listdir(path)
    except Exception as e:
        logging.error(f"无法列出 {path} 目录中的文件和文件夹！")
        raise e
    if show_files:
        for i, f in enumerate(files):
            if os.path.isdir(os.path.join(path, f)):
                files[i] = f + '/'
            logging.info(f" {i+1}. {files[i]}")
            print(f" {i+1}. {files[i]}")
    else:
        files = []
    return files




# 选择一个文件或文件夹
def choose_file_or_folder(files, path, show_files=True):
    # 选择一个文件或文件夹
    while True:
        choice = input("请选择一个文件或文件夹（输入数字）或输入'..'(返回上一级目录)：")
        if choice == '..':
            path = os.path.dirname(os.path.abspath(path))  # 返回上一级目录
            files = list_files(path, show_files=True)  # 列出上一级目录的文件和文件夹
        elif choice.isdigit() and int(choice) >= 1 and int(choice) <= len(files):
            filename = files[int(choice)-1]
            if filename.endswith('/'):
                filename = filename[:-1]  # 去掉文件夹名称末尾的 '/'
                path = os.path.join(path, filename)  # 进入选择的文件夹
                files = list_files(path, show_files=True)  # 列出该文件夹中的文件和文件夹
            else:
                path = os.path.join(path, filename)  # 选择的是文件，更新路径
            return path, files




# 处理单个Word文件
def deal_with_docx(filename):
    try:
        doc = docx.Document(filename)
    except Exception as e:
        logging.error(f"文件 {filename} 不是有效的 Word 文件或者无法打开")
        print(f"文件 {filename} 不是有效的 Word 文件或者无法打开")
        choice = input("是否重新选择文件？（y/n）")
        if choice.lower() == 'y':
            return
        else:
            raise e

    # 将文本信息存储到文件中
    with open('dealer_temp/deal.txt', 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            if para.text.strip():  # 只处理非空段落
                f.write(para.text + '\n')
    logging.info(f"文件 {filename} 中的文本信息已经存储到 dealer_temp/deal.txt 文件中")
    print(f"文件 {filename} 中的文本信息已经存储到 dealer_temp/deal.txt 文件中")


# 处理一个文件夹中的所有Word文件
def deal_with_folder(foldername):
    # 处理一个文件夹中的所有Word文件
    while True:
        files = os.listdir(foldername)
        docx_files = [f for f in files if os.path.isfile(os.path.join(foldername, f)) and f.endswith('.docx')]
        if len(docx_files) == 0:
            logging.warning("文件夹中没有Word文件")
            print("文件夹中没有Word文件")
            foldername, files = choose_file_or_folder(files, foldername)
        else:
            break

    # 让用户选择要处理的 Word 文件
    if len(docx_files) > 1:
        logging.info(f"文件夹中有以下 {len(docx_files)} 个Word文件：")
        print(f"文件夹中有以下 {len(docx_files)} 个Word文件：")
        for i, f in enumerate(docx_files):
            logging.info(f"  {i+1}. {f}")
        while True:
            choice = input("请选择一个文件（输入数字）：")
            if choice.isdigit() and int(choice) >= 1 and int(choice) <= len(docx_files):
                filename = docx_files[int(choice)-1]
                filepath = os.path.join(foldername, filename)
                logging.info(f"处理文件 {filepath} 中的文本信息...")
                print(f"处理文件 {filepath} 中的文本信息...")
                deal_with_docx(filepath)
                break
    else:
        filename = docx_files[0]
        filepath = os.path.join(foldername, filename)
        logging.info(f"处理文件 {filepath} 中的文本信息...")
        print(f"处理文件 {filepath} 中的文本信息...")
        deal_with_docx(filepath)



# 主程序
def main():
    parser = argparse.ArgumentParser(description='处理Word文件中的文本信息')
    parser.add_argument('path', metavar='path', type=str, nargs='?', default=os.getcwd(),
                        help='指定要处理的文件或文件夹路径，默认为当前工作目录')
    args = parser.parse_args()
    # 判断要处理的路径是否存在
    if not os.path.exists(args.path):
        logging.error(f"路径 {args.path} 不存在")
        print(f"路径 {args.path} 不存在")
        return
    # 判断要处理的路径是文件还是文件夹
    if os.path.isfile(args.path) and args.path.endswith('.docx'):
        # 处理单个Word文件
        logging.info(f"处理文件 {args.path} 中的文本信息...")
        print(f"处理文件 {args.path} 中的文本信息...")
        deal_with_docx(args.path)
    elif os.path.isdir(args.path):
        # 处理一个文件夹中的所有Word文件
        os.chdir(args.path)  # 将当前工作目录更改为指定路径
        files = list_files(args.path)
        print("目录列表：")
        for i, f in enumerate(files):
            print(f" {i + 1}. {f}")
        deal_with_folder(args.path)
    else:
        logging.error(f"路径 {args.path} 不是一个有效的Word文件或文件夹！")
        print(f"路径 {args.path} 不是一个有效的Word文件或文件夹！")


if __name__ == '__main__':
    start_dealer()
