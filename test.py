
# import json

# # JSONファイルの読み込み
# with open("stores_data.json", "r", encoding="utf-8") as file:
#     data = json.load(file)

# product_store = data["product_store"]
# miscellaneous_store = data["miscellaneous_store"]
# daily_goods_store = data["daily_goods_store"]
# distance = data["distance"]

# # 商品ごとの距離順でソートして表示
# def display_sorted_products(product_dict):
#     for product_name, stores in product_dict.items():
#         sorted_stores = sorted(stores, key=lambda store: distance[store])
#         print(f"{product_name}:")
#         for store in sorted_stores:
#             print(f"  - {store}: {distance[store]} km")

# print("商品と店舗の距離一覧:\n")

# # 各カテゴリの商品を表示
# display_sorted_products(product_store)
# display_sorted_products(miscellaneous_store)
# display_sorted_products(daily_goods_store)


# import json

# # JSONファイルの読み込み
# with open("kakaku_data.json", "r", encoding="utf-8") as file:
#     data = json.load(file)

# product_store = data["product_store"]
# miscellaneous_store = data["miscellaneous_store"]
# daily_goods_store = data["daily_goods_store"]
# distance = data["distance"]

# # 店舗を価格順にソートする関数
# def sort_stores_by_price(stores, price_data):
#     return sorted(stores, key=lambda store: int(price_data[store].replace("円", "")))

# # 各カテゴリの商品を店舗を価格順にソートして表示
# def display_sorted_products(category, category_name):
#     print(f"\n{category_name}:")
#     for product, stores in category.items():
#         sorted_stores = sort_stores_by_price(stores, distance)
#         print(f"\n商品名: {product}")
#         for store in sorted_stores:
#             print(f"  {store}: {distance[store]}")

# # 商品カテゴリごとのソート結果を表示
# display_sorted_products(product_store, "食品")
# display_sorted_products(miscellaneous_store, "雑貨")
# display_sorted_products(daily_goods_store, "日用品")


import json

# 距離データの読み込み
with open("stores_data.json", "r", encoding="utf-8") as file:
    distance_data = json.load(file)

# 価格データの読み込み
with open("kakaku_data.json", "r", encoding="utf-8") as file:
    price_data = json.load(file)

# カテゴリごとのデータ
product_store = distance_data["product_store"]
miscellaneous_store = distance_data["miscellaneous_store"]
daily_goods_store = distance_data["daily_goods_store"]

# 距離情報と価格情報
distance = distance_data["distance"]
prices = price_data["distance"]

# 店舗を価格順にソートする関数
def sort_stores_by_price(stores, price_data):
    return sorted(stores, key=lambda store: int(price_data[store].replace("円", "")))

# 店舗を距離順にソートする関数
def sort_stores_by_distance(stores, distance_data):
    def parse_distance(value):
        # 距離データが文字列なら数値に変換
        if isinstance(value, str):
            return float(value.replace(" km", ""))
        return value  # すでに数値型の場合はそのまま返す

    return sorted(stores, key=lambda store: parse_distance(distance_data[store]))

# 各カテゴリの商品を店舗ごとに価格順・距離順でソートして表示
def display_sorted_products(category, category_name):
    print(f"\n{category_name}:")
    for product, stores in category.items():
        print(f"\n商品名: {product} (価格順)")
        sorted_stores_by_price = sort_stores_by_price(stores, prices)
        for store in sorted_stores_by_price:
            print(f"  - {store}: {prices[store]}")

        print(f"\n商品名: {product} (距離順)")
        sorted_stores_by_distance = sort_stores_by_distance(stores, distance)
        for store in sorted_stores_by_distance:
            print(f"  - {store}: {distance[store]}")

# 各カテゴリごとの結果を表示
display_sorted_products(product_store, "食品")
display_sorted_products(miscellaneous_store, "雑貨")
display_sorted_products(daily_goods_store, "日用品")


