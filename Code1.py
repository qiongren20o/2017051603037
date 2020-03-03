#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
while True:
    print('本程序用来计算ax^2+bx+c=0的两个根')
    print('使用请输入continue，退出请输入exit')
    XZ = input()
    if XZ == 'continue':
        def PFG(a,b,c):
            #math.sqrt() 计算平方根
            x1 = (-b+(math.sqrt((b**2)-4*a*c)))/(2*a)
            x2 = (-b-(math.sqrt((b**2)-4*a*c)))/(2*a)
            return x1,x2
        print("请输入a，按回车结束输入")
        x = input()
        print("请输入b，按回车结束输入")
        y = input()
        print("请输入c，按回车结束输入")
        z = input()
        p = PFG(int(x),int(y),int(z))
        print('第一个根是',p[0])
        print('第二个根是',p[1])
    elif XZ == 'exit':
        print('谢谢使用，回车结束')
        a = input()
        exit()
    else:
        print('输入错误，请重新输入')
