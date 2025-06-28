age = ['10','20','30','40','50','60','70','80','90']
results = []
for a in age:
    year = int(a)
    if  year <= 18 :
        results.append('小灯滚啊')
    elif 18 <= year < 30:
        results.append('中登')
    elif 30 <= year < 40:
        results.append('老中登')
    else:
        results.append('超级老登')
for a, r in zip(age, results):
    print(f"{a}岁: {r}")
