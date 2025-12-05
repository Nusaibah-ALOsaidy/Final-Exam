# قائمة المنتجات (الاسم + السعر)
products = [
    ["ball", 10],
    ["pens", 20],
    ["doll", 35],
    ["watch", 50],
    ["shoes", 80]
]

# عرض المنتجات للمستخدم
print("Products List:")
for i, item in enumerate(products, start=1):
    print(f"{i}- {item[0]} (price: {item[1]} R.S)")

# طلب إدخال رقم المنتج
choice = input("Enter the number of product: ")

# التحقق من صحة الإدخال
if choice.isdigit():  # التأكد أن الإدخال رقم
    choice = int(choice)
    if 1 <= choice <= len(products):  # التأكد أنه ضمن نطاق المنتجات
        name = products[choice - 1][0]
        price = products[choice - 1][1]
        tax_price = price + (price * 0.15)  # حساب السعر شامل الضريبة

        print(f"Product: {name}")
        print(f"Price before tax: {price} R.S")
        print(f"Price with tax: {tax_price:.2f} R.S")
    else:
        print("❌ Number of product is not correct!")