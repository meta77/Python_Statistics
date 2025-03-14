import numpy as np

# データ
X = np.array([1, 2, 3])  # 勉強時間
y = np.array([50, 60, 70])  # テストの点数
n = len(X)

# 初期値
a, b = 0.0, 0.0

# ニュートン法の反復
for _ in range(100):
    # 予測値
    y_pred = a * X + b

    # 勾配（一次導関数）
    grad_a = -2 * np.sum(X * (y - y_pred))
    grad_b = -2 * np.sum(y - y_pred)

    # ヘッセ行列（二次導関数）
    hess_aa = 2 * np.sum(X**2)
    hess_bb = 2 * n
    hess_ab = 2 * np.sum(X)

    # ヘッセ行列の逆行列
    det = hess_aa * hess_bb - hess_ab**2
    inv_hess_aa = hess_bb / det
    inv_hess_bb = hess_aa / det
    inv_hess_ab = -hess_ab / det

    # パラメータ更新
    delta_a = -(inv_hess_aa * grad_a + inv_hess_ab * grad_b)
    delta_b = -(inv_hess_ab * grad_a + inv_hess_bb * grad_b)
    a += delta_a
    b += delta_b

print(f"最適な直線: y = {a:.1f}x + {b:.1f}")
# 出力: 最適な直線: y = 10.0x + 40.0


'''
勾配ベクトルの定義式
\[
\nabla E = \begin{bmatrix}
\frac{\partial E}{\partial a} \\
\frac{\partial E}{\partial b}
\end{bmatrix}
= \begin{bmatrix}
-2 \sum_{i=1}^n x_i (y_i - (a x_i + b)) \\
-2 \sum_{i=1}^n (y_i - (a x_i + b))
\end{bmatrix}
\]
'''


'''
更新式
\[
\begin{bmatrix}
a_{\text{new}} \\
b_{\text{new}}
\end{bmatrix}
= \begin{bmatrix}
a \\
b
\end{bmatrix}
- H^{-1} \nabla E
\]


'''