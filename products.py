# products
products = []
while True:
    name = input('請輸入產品名稱 ,（ 如輸入 q 就結束 ）')
    if name == 'q':
        break
    price = input('請輸入產品價格 ')
    products.append([name, price])

    #products.append(price)
  

print(products)
#
#