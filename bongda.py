import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
import time




def nhom_gia_tri():
    #Tính lượt đánh giá nhiều nhất, ít nhất theo từng năm
    a = ex.pivot_table(index="Year", values="Consumer_Review_#", aggfunc=max)
    print(a[6:19]) #Đọc từ hàng 6 đến hàng 18
    # pd.DataFrame.to_excel(a, "D:/he.xlsx")
    #Tính lượt đánh giá nhiều nhất, ít nhất theo mẫu xe
    b = ex.pivot_table(index="Model", values="Price", aggfunc=min)
    print(b.tail(10)) #Đọc 10 hàng dưới cùng
    #tính giá trị trung bình xếp hạng xe theo từng năm
    c = ex.pivot_table(index="Model", values="Consumer_Rating", aggfunc=n.mean)
    print(c.head(10)) #Đọc 10 hàng đầu
#
def thong_so():
    print("Giá trị trung bình:",ex["Consumer_Rating"].mean())
    d = ex["Consumer_Rating"].var()
    print("Phương sai của giá trị trung bình là:",d)
    # sắp xếp giá tiền theo thứ tự tăng dần
    e = ex.sort_values("Price")
    # Đọc file gồm 2 thuộc tính là mẫu xe đã được sắp xếp theo giá tiền
    print(e[["Model","Price"]])
    # Hệ số tương quan
    print(ex[["Consumer_Review_#", "Consumer_Rating"]])

# print(gA)
# print(ga)
def bieu_do_phantan():
    plt.plot(ex["Xếp loại"],ex["Consumer_Review_#"],".",color="blue")
    plt.xlabel("Consumer_Rating")
    plt.ylabel("Consumer_Review_#")
    plt.title("Biểu đồ hiển thị mối tương quan giữa xếp hạng và lượt đánh giá")
    plt.show()
# end = time.time()-start
# print(end)

def truy_van():
    truyvan = pd.crosstab(index=ex["Model"], columns=ex["Consumer_Rating"])
    truyvan_chuan = (truyvan-truyvan.min())/(truyvan.max()-truyvan.min())
    iloc = truyvan.iloc[1:10,0:2]
    print(iloc)
    print(truyvan_chuan[1:10][[3,4,5]])
def bieu_do_cot():
    ga_1 = ga[-5:-1]
    ga_1.plot.bar()
    plt.xlabel("Năm")
    plt.ylabel("Lượt đánh giá")
    plt.title("Biểu đồ lượt đánh giá qua các năm 2019-2022")
    plt.show()
# ga_2 = ga[-2:-1]/int(gA.values[-2][0])*100
# ga_3 0= ga[-3:-2]/int(gA.values[-3][0])*100
def bieu_do_tron():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)
    plt.title("Biểu đồ phần trăm về lượt đánh giá của năm 2021 và 2022")
    ax1.pie(gAA[2019], labels=danh_gia,autopct='%1.1f%%')
    ax1.legend()
    ax2.pie(gAA[2020], labels=danh_gia,autopct='%0.5f%%')
    ax2.legend()
    ax3.pie(gAA[2021], labels=danh_gia,autopct='%0.5f%%')
    ax3.legend()
    ax4.pie(gAA[2022], labels=danh_gia,autopct='%0.5f%%')
    ax4.legend()
    plt.show()

if __name__ == '__main__':
    a=input("Nhập file cần xử lí:")
    ex = pd.read_csv(a, index_col=None)
    # #Tứ phân vị
    e1 = ex["Consumer_Rating"].quantile(0.25)  # phân vị 1
    e2 = ex["Consumer_Rating"].quantile(0.5)  # phân vị 2
    e3 = ex["Consumer_Rating"].quantile(0.75)  # phân vị 3
    # # Bảng phân bổ
    danh_gia = ["Kém", "Trung bình", "Khá", "Tốt"]
    dk = [0, e1, e2, e3, 5]
    ex["Xếp loại"] = pd.cut(ex["Consumer_Rating"], bins=dk, labels=danh_gia)  # Tạo cột xếp hạng mới theo mức đánh giá
    # print(ex[100:120][["Consumer_Rating","Xếp loại"]])
    ex.sort_values("Xếp loại")
    ga = ex.pivot_table(index="Year", columns="Xếp loại", values="Consumer_Review_#", aggfunc=sum)
    gA = ex.pivot_table(index="Year", values="Consumer_Review_#", aggfunc=sum)
    gAA = ex.pivot_table(index="Xếp loại", columns="Year", values="Consumer_Review_#", aggfunc=sum)
    print(gAA)
    chon = input("Muốn làm gì:")
    if chon == "biểu đồ":
        chon1 = input("Biểu đồ chi:")
        if chon1 == "tròn":
            bieu_do_tron()
        elif chon1 == "cột":
            bieu_do_cot()
        elif chon1 == "phantan":
            bieu_do_phantan()
        else:
            print("không có dạng biểu đồ bạn chọn")
    else:
        nhom_gia_tri()
        truy_van()
        thong_so()
