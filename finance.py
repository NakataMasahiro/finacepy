#[] coding: utf-8

import random
import math

def Calc_CompoundInterest(A, r, n):
    # Aは元金、rは年利、nは複利する年数（コメントの付け方はあとでもうちょっとちゃんとしたものにする）。
    # 返り値はn年後の総額。これは下記のしきで算出される。
    #  return = A * (1 + r) ** n
    # 関数のスコープをファイル内に限定したいけど、やり方がわからん涙
    return A*(1+r)**n



def Calc_CompoundInterest_List(a, r):
    # aはキャッシュフロー流列のリスト。rは年利、nは複利する年数（コメントの付け方はあとでもうちょっとちゃんとしたものにする）。
    # 返り値はn年後の総額。これは下記の式で算出される。
    sum = 0
    for i in range(len(a)):
        sum += Calc_CompoundInterest(a[i], r, len(a)-i)
    return sum

def Calc_PV(B, r, n):
    # Bはn年後のキャッシュフロー、rは年利。
    # 返り値はキャッシュフローの現在価値。
    # 関数のスコープをファイル内に限定したいけど、やり方がわからん涙
    return B/((1.0 + r)**n)


def Calc_PV_List(a, r):
    # aはキャッシュフロー流列のリスト。rは年利、nは複利する年数（コメントの付け方はあとでもうちょっとちゃんとしたものにする）。
    # 返り値は引数で指定したキャッシュフロー流列の現在価値
    sum = 0
    for i in range(len(a)):
        sum += Calc_PV(a[i], r, i)
    return sum

def randomwalk(steps, yini):
    # steps:ランダムウォークのステップ数。yini:初期位置 返り値はランダムウォークの履歴をリストで返す(ndarrayかなんかにした方がいいのかな汗)。
    # 注意:randomモジュールのimportが必要。これについてはなんか色々やり方あるやろうからまた修正する。
    position = yini
    walk = [position]
    for i in range(steps):
        step = 1 if random.randint(0,1) else -1
        position += step
        walk.append(position)
    return walk


def two_asset_portfolio(r1, r2, sigma1, sigma2, sigma12, w1, w2):
    # arg
    # r1: 資産1の収益率 r2:資産2の収益率
    # sigma1:資産1の分散 sigma2:資産2の分散 sigma12 資産1と2の共分散
    
    return math.sqrt(w1 * w1 * sigma1 ** 2 + 2 * w1 * w2 * sigma12 + w2 * w2 * sigma2 **2)
