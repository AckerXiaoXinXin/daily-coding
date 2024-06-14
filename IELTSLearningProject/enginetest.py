import pyttsx3

def init_engine():
    try:
        # 尝试初始化语音引擎
        engine = pyttsx3.init()
        print("语音引擎初始化成功！")
        return engine
    except ImportError:
        # 如果在 MacOS 上出现问题，尝试指定 nsss (NSSpeechSynthesizer) 引擎
        print("标准初始化失败，尝试使用 NSSpeechSynthesizer...")
        engine = pyttsx3.init('nsss')
        return engine
    except Exception as e:
        print(f"初始化语音引擎失败: {str(e)}")
        return None

def main():
    engine = init_engine()
    if engine:
        engine.say("Hello, welcome to your MacBook's text-to-speech service.")
        engine.runAndWait()

if __name__ == '__main__':
    main()
