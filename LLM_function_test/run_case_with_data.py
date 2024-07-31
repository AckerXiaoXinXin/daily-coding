"""
Project Name: LLM_LEARNING
Module Description: run test on codeqwen
Author: lixin
Date: 2024-07-31
Version: 1.0.0
Email: 395095201@qq.com, zangaixiaoxinxin@gmail.com

Description:
    None.

Usage:
    None.

Examples:
    If applicable, include a simple usage example.

Todo:
    

@file: LLM_LEARNING/LLM_function_test
@software: Visual Studio Code
"""

import requests

url = "http://codeqwen1-5-7b-chat.jeeves-agi.klara.pek02.rack.zhihu.com/v1/completions"

input_text = "编写一个快速排序代码"

data = {
    "input" : input_text
}

response = requests.post(url, json=data)

if response.status_code == 200:
    answer =response.json().get("output")
    print(f"问题:{input_text}")
    print(f"回答:{answer}")
else:
    print(f"请求失败,状态码:{response.status_code}")








