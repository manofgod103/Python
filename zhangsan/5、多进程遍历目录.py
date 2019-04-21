import os
import time
from multiprocessing import Process, Pool


def run(path):
    # 判断到这个路径指向的是文件夹，再次获取里面的内容
    list_files = os.listdir(path)
    for file_name in list_files:
        print(file_name)


if __name__ == "__main__":
    # 创建进程池
    pool = Pool(2)

    path = r"D:\File\HZ1901\Day16"

    t1 = time.time()
    # 获取path下所有的文件
    list_file = os.listdir(path)

    # 遍历这些文件
    for file in list_file:
        # 拼接绝对路径
        abs_path = os.path.join(path, file)
        # 把任务放入进程池
        pool.apply_async(run, args=(abs_path,))
    # 关闭进程池
    pool.close()
    # 开启进程
    pool.join()

    t2 = time.time()
    print(t2 - t1)

"""
上面的代码执行的结果和上一个文件中的结果相同，时间相对较慢
因为进程的创建和销毁都会消耗时间

运算量大的任务不宜使用多进程执行

io量大的任务适合使用多进程

进程数量不能开太多
"""
