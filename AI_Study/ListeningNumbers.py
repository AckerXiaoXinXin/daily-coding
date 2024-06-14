import pyttsx3
import time
import random

# 初始化语音引擎，尝试指定 nsss 驱动
engine = pyttsx3.init('nsss')

# 设置语速
engine.setProperty('rate', 150)

# 生成10个五位数以下的随机数字
random_numbers = [random.randint(1, 99999) for _ in range(10)]

# 用英语朗读这些数字，每个数字间隔6秒
def speak_numbers(numbers):
    for number in numbers:
        print("Now saying:", number)
        engine.say(str(number))
        engine.runAndWait()
        time.sleep(6)

# 调用函数
speak_numbers(random_numbers)
