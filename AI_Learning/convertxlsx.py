import pandas as pd
import json

# 读取 Excel 文件
file_path = '~/Downloads/example_json_data.xlsx'
df = pd.read_excel(file_path)

# 假设每行只有一列，列名为 'json_data'
json_column = 'json_data'

# 解析 JSON 数据并转换为 DataFrame
parsed_data = df[json_column].apply(json.loads)

# 将解析后的数据转换为 DataFrame
parsed_df = pd.json_normalize(parsed_data)

# 保存结果到新的 Excel 文件
output_file_path = 'parsed_data.xlsx'
parsed_df.to_excel(output_file_path, index=False)

print("数据解析完成并保存到", output_file_path)
