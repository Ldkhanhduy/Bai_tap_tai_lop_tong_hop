import pandas as pd
import numpy as n
import matplotlib.pyplot as plt

ex = pd.read_csv("D:/Baitap/BT_EXCEL/honda_sell_data.csv", index_col=None)
#Tính lượt đánh giá nhiều nhất, ít nhất theo từng năm
a = ex.pivot_table(index="Year", values="Consumer_Review_#", aggfunc=max)
print(a[6:19]) #Đọc từ hàng 6 đến hàng 18
pd.DataFrame.to_excel(a, "D:/he.xlsx")
#Tính lượt đánh giá nhiều nhất, ít nhất theo mẫu xe
b = ex.pivot_table(index="Model", values="Price", aggfunc=min)
print(b.tail(10)) #Đọc 10 hàng dưới cùng
#tính giá trị trung bình xếp hạng xe theo từng năm
c = ex.pivot_table(index="Model", values="Consumer_Rating", aggfunc=n.mean)
print(c.head(10)) #Đọc 10 hàng đầu

print("Giá trị trung bình:",ex["Consumer_Rating"].mean())
d = ex["Consumer_Rating"].var()
print("Phương sai của giá trị trung bình là:",d)
# sắp xếp giá tiền theo thứ tự tăng dần
e = ex.sort_values("Price")
# Đọc file gồm 2 thuộc tính là mẫu xe đã được sắp xếp theo giá tiền
print(e["Price"])
# Hệ số tương quan
print(ex[["Consumer_Review_#", "Consumer_Rating"]])
#Tứ phân vị
e1 = ex["Consumer_Rating"].quantile(0.25)
e2 = ex["Consumer_Rating"].quantile(0.5)
e3 = ex["Consumer_Rating"].quantile(0.75)
print(e1, e2, e3)
# Bảng phân bổ
danh_gia = ["Kém", "Tạm", "Khá", "Tốt"]
dk = [0, e1, e2, e3, 5]
ex["Xếp loại"] = pd.cut(ex["Consumer_Rating"], bins=dk, labels=danh_gia)
# print(ex[100:120][["Consumer_Rating","Xếp loại"]])
ex.sort_values("Xếp loại")
ga = ex.pivot_table(index="Year",columns="Xếp loại",values="Consumer_Review_#", aggfunc=sum)
print(ga)
plt.plot(ex["Xếp loại"],ex["Consumer_Review_#"],".",color="blue")
plt.xlabel("Consumer_Rating")
plt.ylabel("Consumer_Review_#")
plt.title("Biểu đồ hiển thị mối tương quan giữa xếp hạng và lượt đánh giá")
plt.show()


