import pandas as pd
import json

# 读取 Excel 文件
file_path = '~/Downloads/example_json_data_2.xlsx'  # 请替换为您的文件路径
df = pd.read_excel(file_path, header=None)  # 没有标题行，所以使用 header=None

# 解析 JSON 数据并转换为 DataFrame
parsed_data = df[0].apply(json.loads)  # 解析每行的 JSON 数据

# 将解析后的数据转换为 DataFrame
parsed_df = pd.json_normalize(parsed_data)

# 保存结果到新的 Excel 文件
output_file_path = 'parsed_data_2.xlsx'
parsed_df.to_excel(output_file_path, index=False)

print("数据解析完成并保存到", output_file_path)
