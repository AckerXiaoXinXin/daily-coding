"""
Project Name: LLM_LEARNING
Module Description: learn transfromer with huggingface
Author: lixin
Date: 2024-07-11
Version: 1.0.0
Email: 395095201@qq.com, zangaixiaoxinxin@gmail.com

Description:
    None.

Usage:
    None.

Examples:
    If applicable, include a simple usage example.

Todo:
    - Reimplement transfromer with torch.

@file: LLM_LEARNING/Transformer_Learning
@software: Visual Studio Code
"""

from transformers import pipeline


transcriber  = pipeline(task="automatic-speech-recognition")

print(transcriber("https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac"))

transcriber = pipeline(model="openai/whisper-large-v2")



