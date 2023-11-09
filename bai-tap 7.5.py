"""
Binary of x 0b1111 , Binary of y 0b1100
x & y =  0b1100
x | y =  0b1111
x ^ y =  0b11
~x =  -0b10000
x << 2 =  0b111100
y >> 2 =  0b11"""
x = 15
y = 12

print('Binary of x', bin(x), ', Binary of y', bin(y))
# Output:
# Binary of x 1111, Binary of y 1100

print('x & y = ', bin(x & y))
# Output:
# x & y = 1100

print('x | y = ', bin(x | y))
# Output:
# x | y = 1111

print('x ^ y = ', bin(x ^ y))
# Output:
# x ^ y = 0011

print('~x = ', bin(~x))
# Output:
# ~x = 0000

print('x << 2 = ', bin(x << 2))
# Output:
# x << 2 = 11100

print('y >> 2 = ', bin(y >> 2))
# Output:
# y >> 2 = 0011
"""
x and y: False
x or y: True
not x: False
x is y: False
x is not y: True
"""
x = True
y = False

print('x and y :',x and y)
# Output: False

print('x or y :',x or y)
# Output: True

print('not x :', not x)
# Output: False

print('x is y:', x is y)
# Output: False

print('x is not y:', x is not y)
# Output: True
# Nhập số tiền cần đổi
money = int(input("Nhập số tiền cần đổi: "))

# Liệt kê các mệnh giá tiền
denominations = [500000, 200000, 100000, 50000]

# Đếm số lượng tờ cần thiết cho mỗi mệnh giá
notes = collections.Counter(denomination for denomination in denominations if money >= denomination)

# In kết quả
print("Số tiền muốn đổi:", money)
for denomination, number in notes.items():
    print("Số tờ mệnh giá", denomination, ":", number)