import os # operating system
products = []

if os.path.isfile('products.csv'): # 檢察檔案
    print('yeah ! 找到檔案了')
    # 讀取檔案 
    with open ('products.csv', 'r',encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name,price])
    print(products) 

else:
    print('找不到檔案')


# 輸入產品資料
while True:
    name = input('請輸入產品名稱 ,（ 如輸入 q 就結束 ）')
    if name == 'q':
        break
    price = input('請輸入產品價格 ')
    products.append([name, price]) 
print(products)

# 印出產品資料
for p in products:
    print(p[0] ,'的價格是 ', p[1])

# 寫入檔案
with open('products.csv' , 'w' , encoding = 'utf-8') as f:
     f.write('商品,價格 \n')
     for p in products:
         f.write(p[0] +' ,' + p[1] + '\n' )

