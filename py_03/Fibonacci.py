"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·
斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，
斐波纳契数列以如下被以递推的方法定义：F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）在现代物理、准晶体结构、化学等领域，
斐波纳契数列都有直接的应用，为此，美国数学会从1963年起出版了以《斐波纳契数列季刊》为名的一份数学杂志，用于专门刊载这方面的研究成果。
"""


def fi(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fi(n-1) + fi(n-2)


a = fi(int(input("请输入:")))
print(a)
