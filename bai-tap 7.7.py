# Nhập số tiền cần đổi
money = int(input("Nhập số tiền cần đổi: "))

# Liệt kê các mệnh giá tiền
denominations = [500000, 200000, 100000, 50000]

# Đếm số lượng tờ cần thiết cho mỗi mệnh giá
notes = collection.Counter(denomination for denomination in denominations if money >= denomination)

# In kết quả
print("Số tiền muốn đổi:", money)
for denomination, number in notes.items():
    print("Số tờ mệnh giá", denomination, ":", number)