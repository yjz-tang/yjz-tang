# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt#
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)
plt.title(r'$f(x)=sin(x)$') 
plt.plot(x, y)
#plt.show()

x1 = [t*0.375*np.pi for t in x]
y1 = np.sin(x1)
plt.subplot(1,2,2)
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') 
plt.plot(x1, y1)
plt.show()# -*- coding: UTF-8 -*-
#coding=utf-8

import matplotlib.pyplot as plt#导入2D绘图库文件，并将其引用的名字改成plt
import numpy as np#导入数值计算扩展，将其引用名字改为np
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
x = np.linspace(0, 3 * np.pi, 100)#范围从0~100，每隔3pi取一个点
y = np.sin(x)#y为以x为自变量的sin函数

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#表示所画图形是一行，2列，中的第一个图形
plt.title(r'$f(x)=sin(x)$')#设置图像标题
plt.plot(x, y)#第一个图像以x为x轴数据, y为y轴数据
#plt.show()#显示在图片内

x1 = [t*0.375*np.pi for t in x]#x1为以0.375*pi*t为横坐标
y1 = np.sin(x1)#y1为以x1为自变量的sin函数
plt.subplot(1,2,2)#示所画图形是一行，2列，中的第二个图形
# plt.title(u"测试2") #注意：在前面加一个u
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') 
plt.plot(x1, y1)#第二个图像以x为x轴数据, y1为y轴数据，x1改为x后就有了相同的横坐标，可以直观的比较两个图像了
plt.show()#显示在图片内