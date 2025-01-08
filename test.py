import json

# JSONファイルの読み込み
with open("stores_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

product_store = data["product_store"]
miscellaneous_store = data["miscellaneous_store"]
daily_goods_store = data["daily_goods_store"]
distance = data["distance"]

product_name = input("商品名を入力してください: ")

if product_name in product_store:
    stores_with_product = product_store[product_name]
elif product_name in miscellaneous_store:
    stores_with_product = miscellaneous_store[product_name]
elif product_name in daily_goods_store:
    stores_with_product = daily_goods_store[product_name]
else:
    stores_with_product = None

if stores_with_product:
    # 距離順に並べ替えて表示
    sorted_stores = sorted(stores_with_product, key=lambda store: distance[store])
    for store in sorted_stores:
        print(f"{product_name} {store}: {distance[store]} km")
else:
    print("その商品は見つかりませんでした。")

