# 商品名と価格の辞書
products = {
    "玉ねぎ": 100,
    "人参": 150,
    "キャベツ": 200,
    "マヨネーズ": 250,
    "マンゴー": 300
}

product2 = {
    "玉ねぎ": 150,
    "人参": 100,
    "キャベツ": 150,
    "マヨネーズ": 200,
    "マンゴー": 300
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
