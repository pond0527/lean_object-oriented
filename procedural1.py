#!/usr/local/bin/python
# encoding: utf-8

import sys


def main(args):
    coin, item_name = (int(args[0]), args[1])
    print(f'入力= お金: {coin} 買う商品: {item_name}')

    if item_name == 'tea':
        tea_price = 100
        if tea_price > coin:
            show_result('入力エラー：お金が足りません')
            return 1

        # おつり計算
        change = coin - tea_price

        show_result(
            '商品情報：',
            '    商品名：tea  価格：100',
            f'おつり：{change}'
        )
        return 0
    else:
        show_result('入力エラー：存在しない商品です')
        return 1

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
