import torch
from transformers import GPT2Tokenizer, BertTokenizer

# 加载GPT-2模型和Tokenizer
model_name = "gpt2"
model = GPT2AdapterModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# 配置并添加Prompt
prompt_config = PromptTuningConfig(
    prompt_length=20,  # 设置提示的长度
    prompt_projection="mlp",  # 投影方式，可以是"mlp"或"lstm"
)
model.add_prompt_tuning("task_prompt", prompt_config)

# 准备训练数据
texts = ["Hello, how are you?", "I am fine, thank you."]
labels = [0, 1]  # 假设是二分类任务

# 编码数据
inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True)
labels = torch.tensor(labels)

# 定义损失函数和优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

# 训练模型
model.train()
for epoch in range(3):  # 训练3个epoch
    optimizer.zero_grad()
    outputs = model(**inputs)
    logits = outputs.logits
    loss = criterion(logits, labels)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# 保存微调后的模型
model.save_pretrained("./task_prompt_model")