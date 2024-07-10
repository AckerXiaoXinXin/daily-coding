import pyttsx3
import time

# 初始化文字转语音引擎
engine = pyttsx3.init()


# 读取文件
def read_and_speak(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for line in lines:
            # 去除每行的换行符并读取
            cleaned_line = line.strip()
            if cleaned_line:  # 确保不是空行
                print(f'Reading aloud: {cleaned_line}')
                engine.say(cleaned_line)
                engine.runAndWait()  # 开始语音输出
                time.sleep(6)  # 每个单词或短语间暂停6秒
    except Exception as e:
        print(f"An error occurred: {e}")


# 文件路径
filename = 'path_to_your_file.txt'  # 修改为你的文本文件的路径
read_and_speak(filename)
