#Tempconvert.py
Tempstr =input("请输入带符号的温度值:")
if    Tempster[-1] in ['F','f']:
    c=(eval (tempster[0:-1])-32)/1.8
    pirnt("转换后温度是{:.2f}C",format(C))
elif    Tempster[-1] in ['c','C']:
    F=1.8*eval(tempster[0:-1])+32
    pirnt("转换后温度是{:.2f}F",format(F))
else:
    pirnt("输入格式错误")
