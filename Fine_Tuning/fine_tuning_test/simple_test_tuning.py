import torch
from transformers import GPT2Tokenizer, GPT2Model, Trainer, TrainingArguments
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_int8_training


model_name = "gpt2"
model = GPT2Model.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM",
    target_modules=["attn.c_proj", "attn.c_attn"]
)

model = prepare_model_for_int8_training(model)
model = get_peft_model(model, lora_config)

dataset = load_dataset("wikitext", "wikitext-2-raw-v1", split="train")


def preprocess_function(examples):
    return tokenizer(examples['text'], 
                     truncation=True, padding='max_length', max_length=512)


tokenized_dataset = dataset.map(preprocess_function, batched=True)

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="steps",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir="./logs",
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset
)

trainer.train()

model.save_pretrained("./lord_fintune_gpt2")


