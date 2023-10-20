# 打开文件，用 readlines & for loop 读取文件
with open("./data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line)

# # 打开文件，用 readline & while loop 读取文件
# with open("./data.txt", "r", encoding="utf-8") as f:
#     line = f.readline()
#     while line != "":
#         print(line)
#         line = f.readline()

# # 打开文件，用 read 读取文件
# with open("./data.txt", "r", encoding="utf-8") as f:
#     print(f.read())