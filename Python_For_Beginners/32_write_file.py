# 任务1：在一个新的名字为"poem.txt"的文件里，写入以下内容：
# 我欲乘风归去
# 文恐琼楼玉宇
# 高处不胜寒。

with open("./poem.txt", "w", encoding="utf-8") as f:
    f.write("我欲乘风归去\n又恐琼楼玉宇\n高处不胜寒。\n")

# 任务2：在上面的"poem.txt"文件结尾处，添加以下两句：
# 起舞弄清影，
# 何似在人间。

with open("./poem.txt", "a", encoding="utf-8") as f:
    f.write("起舞弄清影，\n何似在人间。\n")

# 个人追加任务，使用 a+ 模式在一次 open 中同时实现读写追加
# f.seek()是指针移动方法，此处如果不使用f.seek()，会导致指针处于文本最末端，无法读取文本内容

with open("./poem.txt", "a+", encoding="utf-8") as f:
    f.write("转朱阁，低绮户，照无眠。\n")
    f.seek(0)
    print(f.read())
