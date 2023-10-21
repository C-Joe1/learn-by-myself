prog = "Program: "                                                      # 常用变量定义
err = "Error: "


class BMIClac:                                                          # 外部可调用主类
    def __init__(self, user_weight, user_height):                           # 构造方法
        self.user_weight = user_weight
        self.user_height = user_height

    @staticmethod
    def get_weight():                                                       # 读取键盘输入体重的方法
        user_weight = input(prog + "请输入您的体重（单位：kg）: ")                  # 读取输入后传给变量 weight
        return float(user_weight)                                               # 取浮点数后返回变量 weight

    @staticmethod
    def get_height():                                                       # 读取键盘输入身高的方法
        user_height = input(prog + "请输入您的身高（单位：m）: ")                   # 将读取输入传给变量 height
        return float(user_height)                                               # 取浮点数后返回变量 height

    @staticmethod
    def bmi_clac(weight, height):                                           # 传入体重身高，计算 BMI 指数的方法
        user_bmi = weight / height ** 2                                         # BMI 计算公式，计算结果传给变量 user_bmi
        return user_bmi                                                         # 返回变量 user_bmi

    def main(self):                                                         # 主运行方法
        try:                                                                    # 逻辑代码
            weight = self.get_weight()                                              # 调用 get 方法，返回值传给变量 weight
            height = self.get_height()                                              # 调用 get 方法，返回值传给变量 height
            bmi = self.bmi_clac(weight, height)                                     # 调用 bmi_clac 方法，计算 BMI 数值
        except ValueError:                                                      # 检测数值错误
            print(err + "您输入了不合规范的字符（输入为空、输入非数字字符），请重新运行程序，并输入正确的数字。")
        except ZeroDivisionError:                                               # 检测除数为零错误
            print(err + "身高不能为零，请重新运行程序，并输入正确的数字。")
        except:                                                                 # 其他错误
            print(err + "发生未知错误，请重新运行程序。")
        else:                                                                   # try/except 检测无错误后进入 else 判断
            if bmi == 0:                                                            # 检测体重为零错误，并判断 BMI 量级
                print(err + "体重不能为零，请重新运行程序，并输入正确的数字。")
            elif 0.01 <= bmi < 18.5:
                print(prog + "您的BMI值为：" + format(bmi, '.2f') + "（取后两位小数），低于正常体重。")
            elif 18.5 <= bmi < 25:
                print(prog + "您的BMI值为：" + format(bmi, '.2f') + "（取后两位小数），属于正常体重。")
            elif 25 <= bmi < 30:
                print(prog + "您的BMI值为：" + format(bmi, '.2f') + "（取后两位小数），属于超重。")
            elif 30 <= bmi < 35:
                print(prog + "您的BMI值为：" + format(bmi, '.2f') + "（取后两位小数），属于一类肥胖。")
            elif 35 <= bmi < 40:
                print(prog + "您的BMI值为：" + format(bmi, '.2f') + "（取后两位小数），属于二类肥胖。")
            elif bmi >= 40:
                print(prog + "您的BMI值为：" + format(bmi, '.2f') + "（取后两位小数），属于三类肥胖。")
        finally:                                                                # 程序结束输出
            print(prog + "程序运行结束。")


bmi_clac = BMIClac(BMIClac.get_weight, BMIClac.get_height)              # 实例化 BMIClac 类，传入类中方法
bmi_clac.main()                                                         # 调用 BMIClac 类的主运行方法
