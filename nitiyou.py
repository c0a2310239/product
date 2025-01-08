import json

# JSONファイルの読み込み
with open("nitiyou.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# JSONファイルの内容をすべて表示
for item, stores in data.items():
    print(f"{item}:")
    for store in stores:
        print(f"  - {store}")
