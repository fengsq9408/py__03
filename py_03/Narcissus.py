"""
所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。

例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

利用for循环控制100-999个数，每个数分解出个位，十位，百位。

"""

for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            m = a*100+b*10+c
#           n = a ^ 3+b ^ 3+c ^ 3
#           n = a*a*a+b*b*b+c*c*c
            n = a**3+b**3+c**3
            if m == n:
                print(m)
