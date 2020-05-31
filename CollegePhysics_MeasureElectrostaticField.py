#coding = gbk

import os

while True:
	print("模拟法测静电场实验的计算器\nAuthor@地球虫子\n")

	#数据
	total = 0.0
	value = [0,0,0,0,0,0]#存储输入的值
	sumAll = 0#计算σ求和

	try:
		n = int(input("请输入数据组数："))
		if n <= 1:
			print("憨批，这里输大于一的整数！程序已结束。")
			os._exit(0)
	except ValueError:
		print("憨批，这里输大于零整数！程序已结束。")
		os._exit(0)

	try:
		rTheo = float(input("请输入r理论值："))
	except ValueError:
		print("憨批，这里输浮点数！程序已结束。")
		os._exit(0)

	for i in range(n):
		try:
			value[i] = float(input("请输入测量值" + str(i + 1) + "："))
		except ValueError:
			print("憨批，这里输浮点数！程序已结束。")
			os._exit(0)
		total = total + value[i]
		sumAll += (value[i] - rTheo) ** 2

	avr = total / n
	print("平均值：" + str(avr))

	print("Δ：" + str(avr - rTheo))

	sigma = pow(sumAll / (n * (n - 1)), 1 / 2)
	print("σ：" + str(sigma))

	print("E：" + str(sigma / rTheo))

	flag = input("\n要继续吗？输入N退出：")
	print()

	if ((flag == "N") & (flag == "n")):
		os._exit(0)