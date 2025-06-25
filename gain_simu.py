import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# パラメータの設定
# ----------------------------
initial_money = 10000            # 初期資金（円）
win_rate = 0.80               # 勝率
gain = 0.13               # 勝ったときの利益　（%）
loss = -0.15         # 負けたときの損失（%）
num_trials = 140   # 取引回数（シミュレーション回数）
two = 0
money100 = 0
money1000 = 0

# ----------------------------
# シミュレーションの準備
# ----------------------------
money = initial_money
money_history = [money]

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


print(money)
print(money100)
print(money_history)


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
