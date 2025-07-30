import numpy as np
import matplotlib.pyplot as plt
import statistics
import math

# ----------------------------
# パラメータの設定
# ----------------------------
initial_money = 50000            # 初期資金（円）
win_rate = 0.82           # 勝率
gain = 0.08       # 勝ったときの利益　（%）
loss = -0.1  # 負けたときの損失（%）
num_trials = 100  # 取引回数（シミュレーション回数）
two = 0
money100 = 0
money1000 = 0
money2 = 0

money_list = []

# ----------------------------
# シミュレーションの準備
# ----------------------------
money = initial_money
money_history = [money]


for n in range(100):
# ----------------------------
# シミュレーション本体
# ----------------------------
    for i in range(num_trials):
        if np.random.rand() < win_rate: # 0以上1未満の乱数（float型の実数）を1個生成する
        # 勝った場合
            money *= (1 + gain)
        else:
        # 負けた場合
            money *= (1 + loss)
        money_history.append(money) # 取引の履歴

        if money >= 1000000:
            if money100 == 0:
                money100 = i

        if money >= 10000000:
            if money1000 == 0:
                money1000 = i

        if money >= initial_money * 2:
            if money2 == 0:
                money2 = i

    money_list.append(money)
    money = initial_money

# 結果の見た目をわかりやすくする
def convert_to_yen_unit_with_commas(n):
    # 小数点以下はすべて無視（切り捨て）
    if not isinstance(n, (int, float)):
        raise ValueError("数値（intまたはfloat）で入力してください")

    n = int(n)  # 小数点以下を切り捨て

    units = [
        (10**12, '兆'),
        (10**8, '億'),
        (10**4, '万'),
    ]

    result = ""
    for unit_value, unit_name in units:
        if n >= unit_value:
            quotient, n = divmod(n, unit_value)
            result += f"{format(quotient, ',')}{unit_name}"
    if n > 0 or result == "":
        result += format(n, ',')
    return result



print(money_list)
print('平均:',convert_to_yen_unit_with_commas(statistics.mean(money_list)))
print('標準偏差:',convert_to_yen_unit_with_commas(statistics.pstdev(money_list)))


'''
print('現在の価格：', money)
print('変換：', convert_to_yen_unit_with_commas(money))
print('2倍になるまでかかった回数：', money2)
print('100万を超えるまでにかかった回数：', money100)
print('1000万を超えるまでにかかった回数：', money1000)
# print('取引履歴：', money_history)


# ----------------------------
# 結果のプロット
# ----------------------------
plt.figure(figsize=(12, 6))
plt.plot(money_history, label="資金の推移", color='blue')
plt.axhline(y=initial_money, color='gray', linestyle='--', label="初期資金")
plt.title("資金推移のシミュレーション")
plt.xlabel("取引回数")
plt.ylabel("資金（円）")
plt.legend()
plt.grid(True)
plt.show()
'''