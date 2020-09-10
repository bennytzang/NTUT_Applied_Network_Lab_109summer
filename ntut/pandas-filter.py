import pandas as pd
# 篩選練習
# data = pd.Series([30, 15, 20,])
# condition= data>18
# print(condition)
# filteredData = data[condition]
# print(filteredData)

# data = pd.Series(["您好", "Python", "Pandas"])
# condition=data.str.contains("P")
# print(condition)
# filteredData=data[condition]
# print(filteredData)

#篩選練習 DataFrame
data=pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000, 50000, 40000]
})
print(data)
#condition=[False, True, True] 
condition=data["name"] == "Amy"
condition=data["salary"]>=40000
filteredData=data[condition]
print(filteredData)