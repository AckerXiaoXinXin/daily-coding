import random
import time
import pyttsx3


def generate_random_number():
    """生成一个五位以下的随机数"""
    return random.randint(0, 99999)


def speak_number(number):
    """使用英语朗读数字"""
    engine = pyttsx3.init()
    engine.say(str(number))
    engine.runAndWait()
    time.sleep(6)  # 等待6秒


def main():
    for _ in range(10):
        number = generate_random_number()
        print(f"Generated number: {number}")
        speak_number(number)


if __name__ == "__main__":
    main()