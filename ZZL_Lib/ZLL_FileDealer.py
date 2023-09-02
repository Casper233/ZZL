import os
import docx

# 列出当前文件夹所有目录
dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
print("当前文件夹包含的目录：")
for d in dirs:
    print(d)

# 让用户选择一个Word文件
print()
docx_files = [f for f in os.listdir('.') if f.endswith('.docx')]
if len(docx_files) == 0:
    print("当前文件夹中没有Word文件！")
else:
    print("当前文件夹中的Word文件：")
    for i, f in enumerate(docx_files):
        print(f"{i+1}. {f}")
    choice = int(input("请选择一个文件（输入数字）："))
    if choice < 1 or choice > len(docx_files):
        print("选择无效！")
    else:
        filename = docx_files[choice-1]
        print(f"你选择了文件 {filename}")
        # 读取Word文件中的信息
        doc = docx.Document(filename)
        print("文件中的段落数：", len(doc.paragraphs))
        print("文件中的表格数：", len(doc.tables))