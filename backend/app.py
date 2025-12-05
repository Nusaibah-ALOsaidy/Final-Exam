# قائمة المنتجات (الاسم + السعر)
products = [
    ["product_1", 10],
    ["product_2", 20],
    ["product_3", 35],
    ["product_4", 50],
    ["product_5", 80]
]

# عرض المنتجات للمستخدم
print("Products List:")
for i, item in enumerate(products, start=1):
    print(f"{i}- {item[0]} (price: {item[1]} R.S)")
