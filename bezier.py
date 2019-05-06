import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 参考: http://d.hatena.ne.jp/Ko-Ta/20091025/p1

def _bezier(p1, p2, vp1, vp2, t):
    """ベジェ曲線の座標を返す関数
    
    :param p1: 始点
    :type p1: float
    :param p2: 終点
    :type p2: float
    :param vp1: 第1制御点
    :type vp1: float
    :param vp2: 第2制御点
    :type vp2: float
    :param t: パラメーター
    :type t: float
    :return: 座標
    :rtype: float
    """
    p = (1-t)**3 * p1 + 3 * (1-t)**2 * t * vp1 + 3 * (1-t) * t**2 * vp2 + t**3 * p2
    return p


def _bezier_linearlen(x1, y1, x2, y2, vx1, vy1, vx2, vy2, t, n=16):
    """ベジェ曲線の距離均等変換
    
    :param x1: 始点x座標
    :type x1: float
    :param y1: 始点y座標
    :type y1: float
    :param x2: 終点x座標
    :type x2: float
    :param y2: 終点y座標
    :type y2: float
    :param vx1: 第1制御点x座標
    :type vx1: float
    :param vy1: 第1制御点y座標
    :type vy1: float
    :param vx2: 第2制御点x座標
    :type vx2: float
    :param vy2: 第2制御点y座標
    :type vy2: float
    :param t: パラメーター
    :type t: float
    :param n: 分割数, defaults to 50
    :type n: int, optional
    :return: 
    :rtype: float
    """
    ll = []
    x = y = 0.0
    px = py = 0
    tt = ni = 0
    i = 0

    # 最低分割数
    if (n<4):
        return t
    
    # 0.0～1.0外はそのまま返そう
    if (t<=0.0) or (t>=1.0):
        return t
    
    ni = 1.0/n
    tt = 0.0

    px = _bezier(x1,x2,vx1,vx2,0.0)
    py = _bezier(y1,y2,vy1,vy2,0.0)
    ll.insert(0,0.0)

    for i in range(1, n+1 ):
        tt = tt + ni
        x = _bezier(x1,x2,vx1,vx2,tt)
        y = _bezier(y1,y2,vy1,vy2,tt)
        ll.insert(i, ll[i-1] + np.sqrt((x-px)*(x-px) + (y-py)*(y-py)))
        px = x
        py = y
    
    x = 1.0/ll[n]

    for i in range(1, n+1 ):
        ll[i] = ll[i]*x

    for i in range(n):
        if (t>=ll[i])and(t<=ll[i+1]):
            break
        if (i>=n):
            return t

    x = (ll[i+1]-ll[i])
    if (x<0.0001):
        x = 0.0001        # 例外対策
    x = (t-ll[i]) / x                   # 区画内の比率を求めて
    return (i*(1.0-x) + (i+1)*x) * ni # 線形補間

x1 = 0
y1 = 0
x2 = 1
y2 = 1
vx1 = 0.55
vy1 = 0
vx2 = 1
vy2 = 1-0.55

n = 100

# グラフ描画用
fig = plt.figure(figsize=(5,5))

ims=[]
for i in range(n):
    tt = i/n
    tt = _bezier_linearlen(x1,y1,x2,y2, vx1,vy1,vx2,vy2,tt)
    dx = _bezier(x1,x2, vx1,vx2, tt)
    dy = _bezier(y1,y2, vy1,vy2, tt)
    im = plt.scatter(dx, dy)
    ims.append([im])

# アニメーション設定
ani = animation.ArtistAnimation(fig, ims, interval=0.1, repeat_delay=1000)
ani.save('test.gif', writer="imagemagick")
plt.show()
