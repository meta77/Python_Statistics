import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 設定
np.random.seed(0)  # 再現性確保
n_samples = 10000  # 実験回数
sample_size = 5    # 1回の実験で使うサイコロの数

# 実験：サイコロをn_sample回振り、平均値を記録
means = []
for _ in range(n_samples):
    dice_rolls = np.random.randint(1, 7, sample_size)  # サイコロを5個振る
    means.append(np.mean(dice_rolls))  # 平均値を記録

# 可視化
plt.figure(figsize=(10,6))
sns.histplot(means, kde=True, color='skyblue')
plt.title(f'サイコロ{sample_size}個の平均値分布（実験回数:{n_samples}回）')
plt.xlabel('平均値')
plt.ylabel('頻度')
plt.axvline(np.mean(means), color='red', linestyle='--', label=f'平均: {np.mean(means):.2f}')
plt.legend()
plt.show()