import matplotlib.pyplot as plt

N = 126000000  # 日本の人口 2021年3月1日現在
R0 = 2 #パラメータ
gamma = 0.2 # 回復/死亡率
beta = R0 * gamma / N # 感染率

S = N  # 未感染者
I = 1  # 感染者
R = 0  # 免疫感染者＋死亡者

aS = [S / N]
aI = [I / N]
aR = [R / N]
aRt = [R0]

for t in range(200):
    S, I, R = S - beta * S * I, I + beta * S * I - gamma * I, R + gamma * I
    Rt = beta * S / gamma
    aS.append(S / N)
    aI.append(I / N)
    aR.append(R / N)
    aRt.append(Rt)

plt.title("SIR MODEL")
plt.plot(aS, "v-", label="S")
plt.plot(aI, "o-", label="I")
plt.plot(aR, "^-", label="R")
plt.legend()
plt.show()