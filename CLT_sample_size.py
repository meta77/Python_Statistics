# 試行ごとのサンプルサイズが気になる。実験したい。

# 試行ごとのサンプル数を、10〜50の間でランダムにする。
# 試行回数を100回、1000回、10000回にする。


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 試行回数のリスト
num_experiments_list = [100, 1000, 10000]

# サンプル数をランダムにする範囲
sample_size_min = 10
sample_size_max = 50

# グラフを描画
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

for i, num_experiments in enumerate(num_experiments_list):
    averages = []  # 各試行の平均値を格納するリスト

    for _ in range(num_experiments):
        sample_size = np.random.randint(sample_size_min, sample_size_max + 1)  # サンプルサイズをランダムに選択
        samples = np.random.uniform(0, 1, sample_size)  # 0から1の一様分布の乱数を生成
        avg = np.mean(samples)  # サンプルの平均を計算
        averages.append(avg)

    # ヒストグラムを描画
    sns.histplot(averages, bins=30, kde=True, color='blue', alpha=0.7, ax=axes[i])
    axes[i].set_title(f"試行回数: {num_experiments}")
    axes[i].set_xlabel("サンプル平均")
    axes[i].set_ylabel("頻度")
    axes[i].grid(True)

plt.tight_layout()
plt.show()
