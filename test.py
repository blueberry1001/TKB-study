import json

with open('data_20241125_055027.json', 'r', encoding='utf-8') as file:
    # JSONデータを読み込む
    data = json.load(file)
import model_build
print(model_build.modelbuild(data))