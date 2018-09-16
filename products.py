# products
products = []
while True:
    name = input('請輸入產品名稱 ,（ 如輸入 q 就結束 ）')
    if name == 'q':
        break
    price = input('請輸入產品價格 ')
    products.append([name, price])

  
print(products)
for p in products:
    print(p[0] ,'的價格是 ', p[1])

with open('products.csv' , 'w' , encoding ='utf-8') as f:
     f.write('商品,價格 \n')
     for p in products:
         f.write(p[0] +' ,' + p[1] + '\n' )

