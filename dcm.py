# 商品名と価格の辞書
products = {
    "漂白剤": 100,
    "柔軟剤": 150,
    "ボディーソープ": 200,
    "シャンプー": 250,
    "リンス": 300
}

product2 = {
    "漂白剤": 150,
    "柔軟剤": 100,
    "ボディーソープ": 150,
    "シャンプー": 200,
    "リンス": 300
}

# 価格表示と価格比較の関数
def search_and_compare(product_name, product1, product2):
    if product_name in product1 and product_name in product2:
        price1 = product1[product_name]
        price2 = product2[product_name]
        print(f"{product_name}: 店舗1の価格は{price1}円, 店舗2の価格は{price2}円")
        if price1 < price2:
            print(f"{product_name}: 店舗1の方が{price2 - price1}円安いです")
        elif price1 > price2:
            print(f"{product_name}: 店舗2の方が{price1 - price2}円安いです")
        else:
            print(f"{product_name}: 両店舗の価格は同じです")
    elif product_name in product1:
        print(f"{product_name}: 店舗1の価格は{product1[product_name]}円, 店舗2の価格はありません")
    elif product_name in product2:
        print(f"{product_name}: 店舗1の価格はありません, 店舗2の価格は{product2[product_name]}円")
    else:
        print(f"{product_name}: 商品が見つかりません")

# 検索したい商品名を入力
search_product = input("検索したい商品名を入力してください: ")
search_and_compare(search_product, products, product2)
