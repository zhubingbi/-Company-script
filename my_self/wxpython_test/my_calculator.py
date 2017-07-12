#!/usr/bin/python
# coding=utf-8
import wx

app = wx.App()
# 创建一个主APP
frame = wx.Frame(None, title='z-sir计算器', size = (420, 350))
panel = wx.Panel(frame)
# 画布创建panel

btn1 = wx.Button(panel, label='CE')
btn2 = wx.Button(panel, label='C')
btn3 = wx.Button(panel, label='backspace')
btn4 = wx.Button(panel, label='%')
btn5 = wx.Button(panel, label='7')
btn6 = wx.Button(panel, label='8')
btn7 = wx.Button(panel, label='9')
btn8 = wx.Button(panel, label='X')
btn9 = wx.Button(panel, label='4')
btn10 = wx.Button(panel, label='5')
btn11 = wx.Button(panel, label='6')
btn12 = wx.Button(panel, label='—')
btn13 = wx.Button(panel, label='1')
btn14 = wx.Button(panel, label='2')
btn15 = wx.Button(panel, label='3')
btn16 = wx.Button(panel, label='+')
btn17 = wx.Button(panel, label='')
btn18 = wx.Button(panel, label='0')
btn19 = wx.Button(panel, label='.')
btn20 = wx.Button(panel, label='=')
# 创建计算器所有按钮，很麻烦的感觉

result = wx.TextCtrl(panel)
# 创建结果展示框

sBox = wx.BoxSizer()
sBox1 = wx.BoxSizer()
sBox2 = wx.BoxSizer()
sBox3 = wx.BoxSizer()
sBox4 = wx.BoxSizer()
# 5行水平尺寸器

vBox = wx.BoxSizer(wx.VERTICAL)
# 垂直的尺寸器

sBox.Add(btn1, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox.Add(btn2, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox.Add(btn3, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox.Add(btn4, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
# 添加第一行水平尺寸器，proportion=1 是在这一行占用的比例，border=1代表间距, 中间是填充
sBox1.Add(btn5, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox1.Add(btn6, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox1.Add(btn7, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox1.Add(btn8, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)

sBox2.Add(btn9, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox2.Add(btn10, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox2.Add(btn11, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox2.Add(btn12, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)

sBox3.Add(btn13, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox3.Add(btn14, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox3.Add(btn15, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox3.Add(btn16, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)

sBox4.Add(btn17, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox4.Add(btn18, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox4.Add(btn19, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
sBox4.Add(btn20, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)

vBox.Add(result, proportion=2, flag=wx.EXPAND|wx.ALL, border=1)
vBox.Add(sBox, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
vBox.Add(sBox1, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
vBox.Add(sBox2, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
vBox.Add(sBox3, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
vBox.Add(sBox4, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)


panel.SetSizer(vBox)
# 声明主尺寸器

frame.Show()
app.MainLoop()