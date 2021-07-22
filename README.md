# __感染症数理モデル__  
matplotlib.pyplotは、matplotlibパッケージの中のモジュールで、グラフを作るためのインターフェイスが集まっている。  
言語はpython3を使用する。
```
import matplotlib.pyplot as plt
```
・Sはsusceptible  
・Iはinfectious  
・Rはremoved/recovered  

3つのコンパートメントに分け，感染に係る状態
の時間的な変化をボトムアップ式にモデル化
```
S = N  # 未感染者
I = 1  # 感染者
R = 0  # 免疫感染者＋死亡者
```

```
N = 126000000  # 日本の人口 2021年3月1日現在
R0 = 2 #パラメータ
gamma = 0.2 # 回復/死亡率
beta = R0 * gamma / N # 感染率
```

凡例の調節して、グラフを描画する。
```
plt.title("SIR MODEL")
plt.plot(aS, "v-", label="S")
plt.plot(aI, "o-", label="I")
plt.plot(aR, "^-", label="R")
plt.legend()
plt.show()
```
![Figure_1](https://user-images.githubusercontent.com/65733429/126430827-9ea56b9e-7965-4573-b20f-0bf8b0ad800e.png)
# __感染症数理モデル、経営において__
感染症モデルはSNSユーザ数の変化に応用できる。SNSのユーザは感染者に相当し、SNSへの興味が薄れ利用しなくなることが回復に相当する。
