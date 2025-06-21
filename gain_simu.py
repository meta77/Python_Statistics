import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# パラメータの設定
# ----------------------------
initial_money = 50000            # 初期資金（円）
win_rate = 0.85                # 勝率
gain = 0.09                     # 勝ったときの利益　（%）
loss = -0.1                  # 負けたときの損失（%）
num_trials = 50          # 取引回数（シミュレーション回数）

# ----------------------------
# シミュレーションの準備
# ----------------------------
money = initial_money
money_history = [money]

# ----------------------------
# シミュレーション本体
# ----------------------------
for _ in range(num_trials):
    if np.random.rand() < win_rate:
        # 勝った場合
        money *= (1 + gain)
    else:
        # 負けた場合
        money *= (1 + loss)
    money_history.append(money)

print(money)
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
