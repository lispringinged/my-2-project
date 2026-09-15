score = int(input("请输入你的分数"))
if score >= 90:
    a = "优秀"
elif score >= 80:
    a = "良好"
elif score >= 70:
    a = "尚可"
elif score >= 60:
    a = "及格"
else:
    a = "不及格"
print(a)