#!/usr/local/bin/python
# encoding: utf-8

import sys


# 例外:入力不正
class InvalidInputException(Exception):
    pass


# 自動販売機クラス
class VendingMachine:
    def __init__(self, *items):
        self.items = items

    def process(self, coin, item_name):
        select_item = self._find_item(item_name)
        if select_item is None:
            raise InvalidInputException('存在しない商品です')

        if select_item.price > coin:
            raise InvalidInputException('お金が足りません')


        change = coin - select_item.price

        return change, select_item

    def _find_item(self, item_name):
        for item in self.items:
            if item_name == item.name:
                return item

        return None


# 商品クラス
class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


def main(args):
    vending_machine = VendingMachine(
            Item('tea', 100)
    )

    coin, item_name = (int(args[0]), args[1])
    print(f'入力：お金={coin} 買う商品={item_name}')

    try:
        change, select_item = vending_machine.process(coin, item_name)
        show_result(
            '商品情報:',
            f'    商品名：{select_item.name} 価格：{select_item.price}',
            f'おつり：{change}'
        )
    except InvalidInputException as e:
        show_result("入力エラー：{}".format(e))


def show_result(*messages):
    print('*'*30)
    for msg in messages:
        print(msg)
    print('*'*30)
    print('')


#
#    利用者
#    # お金、商品名を入力

#        # 商品存在チェック
#        # IF 商品が存在しない
#        # THEN 入力エラー
#        # 商品価格と入力された金額を比較
#        # IF 商品価格 > 入力金額
#        # ELSE 入力エラーを伝える
#        # おつりの計算
#        # 商品情報を表示
#
#    # 買った商品を使う
#
if __name__ == '__main__':
    exit_code = main(sys.argv[1:])
    sys.exit(exit_code)
