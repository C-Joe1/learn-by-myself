def get_weight():                                               # 读取键盘输入体重
    user_weight = input("Program: 请输入您的体重（单位：kg）：")     # 读取输入后传给变量 weight
    return float(user_weight)                                   # 取浮点数后返回变量 weight


def get_height():                                               # 读取键盘输入身高
    user_height = input("Program: 请输入您的身高（单位：m）：")      # 将读取输入传给变量 height
    return float(user_height)                                   # 取浮点数后返回变量 height


def bmi_clac(weight, height):                                   # 传入体重身高，计算 BMI 指数
    user_bmi = weight / height ** 2                             # BMI 计算公式，计算结果传给变量 user_bmi
    return user_bmi                                             # 返回变量 user_bmi


def main():                                                     # 主体代码
    try:                                                        # 逻辑代码
        weight = get_weight()                                   # 调用 get 方法，返回值传给变量 weight
        height = get_height()                                   # 调用 get 方法，返回值传给变量 height
        bmi = bmi_clac(weight, height)                          # 调用 bmi_clac 方法，计算 BMI 数值
    except ValueError:                                          # 检测数值错误
        print("Error: 您输入了不合规范的字符（输入为空、输入非数字字符），请重新运行程序，并输入正确的数字。")
    except ZeroDivisionError:                                   # 检测除数为零错误
        print("Error: 身高不能为零，请重新运行程序，并输入正确的数字。")
    except:                                                     # 其他错误
        print("Error: 发生未知错误，请重新运行程序。")
    else:
        if bmi == 0:                                            # 体重为零错误
            print("Error: 体重不能为零，请重新运行程序，并输入正确的数字。")
        else:                                                   # 正常输出
            print("Program: 您的BMI值为：" + format(bmi, '.2f') + "（取后两位小数）")
    finally:                                                    # 程序结束输出
        print("Program: 程序运行结束。")


main()                                                          # 调用主体代码
