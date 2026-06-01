import pandas as pd

scores = {
    "姓名": ["王小明", "陳小華", "林小美"],
    "成績": [85, 92, 78]
}

df = pd.DataFrame(scores)

print(df)
print("平均成績:", df["成績"].mean())
print("最高成績:", df["成績"].max())
print("最低成績:", df["成績"].min())
