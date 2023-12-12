import os
import sys
import shutil


def tars_divide(data, output):  # 定义函数将不同的文件分类
    # data : path to the data
    # output: path to the output
    ext = os.path.splitext(data)[1]  # 获取文件的扩展名
    base = os.path.basename(data)  # 获取文件的基本名
    if ext == ".txt" and base == "mCG_file.txt":  # 将mCG的txt格式的文件进行分类整理
        mCG_dir = os.path.join(output, "mCG")  # 将mCG_dir的路径修改为path/to/output/mCG
        os.makedirs(mCG_dir, exist_ok=True)  # 创建path/to/output/mCG这个路径对应的文件夹
        shutil.move(data, mCG_dir)  # 将mCGdata文件移动到mCG_dir路径下
    elif ext == ".sam":  # 将bismark产生的sam文件分类
        sam_dir = os.path.join(output, "sam")
        os.makedirs(sam_dir, exist_ok=True)
        shutil.move(data, sam_dir)
    elif ext == ".txt":  # 将其他的txt文件分类整理
        parental_dir = os.path.join(output, "parental")
        os.makedirs(parental_dir, exist_ok=True)
        shutil.move(data, parental_dir)
    else:
        other_dir = os.path.join(output, "other")
        os.makedirs(other_dir, exist_ok=True)
        shutil.move(data, other_dir)
        print(f"File {base} does not match any criteria, moved to other folder.")


data_dir = sys.argv[1]  # 命令行第一个参数输入输入文件路径
output_dir = sys.argv[2]  # 命令行第二个参数输入输出文件路径
# 获取输入数据目录下的所有文件名
file_list = os.listdir(data_dir)
# 过滤掉格式不对的文件
data_list = [file for file in file_list if file.endswith(".txt") or file.endswith(".sam")]
# 整理文件从而保证后续分析按顺序进行
data_list = sorted(data_list)
for filename in data_list:
    data = os.path.join(data_dir, filename)  # 拼接文件的完整路径
    output = output_dir
    tars_divide(data, output)
