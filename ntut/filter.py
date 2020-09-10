#載入pandas 模組
import pandas as pd
#建立Series
data = pd.Series([20,10,15])
#基本的Series操作
data =data ==20
print(data)

#建立DataFrame
data = pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000],
    "else":[1,2,3]
})
print(data)
print("-----------")
#取得特定欄位
print("取得特定欄位")
print(data["salary"])

print("-----------")
#取得特定列
print("取得特定列")
print(data.iloc[0])