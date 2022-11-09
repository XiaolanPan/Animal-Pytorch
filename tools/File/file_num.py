'''
    获取文件夹内文件的数量个数

'''

import os
path1 = ""                           # 输入一级文件夹地址
files1 = os.listdir(path1)           # 读入一级文件夹
num1 = len(files1)                   # 统计一级文件夹中的二级文件夹个数
num2 = []                            # 建立空列表
for i in range(num1):                # 遍历所有二级文件夹
    path2 = path1 +'//' +files1[i]   # 某二级文件夹的路径
    files2 = os.listdir(path2)       # 读入二级文件夹
    num2.append(len(files2))         # 二级文件夹中的文件个数
    
print("所有二级文件夹名:")
print(files1)                        # 打印二级文件夹名称
print("所有二级文件夹中的文件个数:")
print(num2)                          # 打印二级文件夹中的文件个数

print("对应输出:")
xinhua = dict(zip(files1,num2))      # 将二级文件夹名称和所含文件个数组合成字典
sum = 0
for key,value in xinhua.items():     # 将二级文件夹名称和所含文件个数对应输出
    print('{key}:{value}'.format(key = key, value = value))
    sum += value
print(sum)   