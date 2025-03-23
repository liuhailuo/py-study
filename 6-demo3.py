import pprint
from functools import reduce
## 购物车功能分析

products = [{"goodsNo":1000,"goodsName":"iphone","price":12000,"stock":10},
            {"goodsNo":1001,"goodsName":"ipad","price":11000,"stock":11},
            {"goodsNo":1002,"goodsName":"macBook","price":13000,"stock":12},
            {"goodsNo":1003,"goodsName":"xiaomi","price":14000,"stock":13}]

carts ={1000:5,1002:1,1006:9}


def add_product(goodsNo:int,goodsName:str,price:float,stock:int):
      # 创建一个新的商品字典
    products.append({
        "goodsNo": goodsNo,
        "goodsName": goodsName,
        "price": price,
        "stock": stock
    })
    # print(pprint.pprint(products))

def get_product_by_id(goodsNo:int):
    for item in products:
        if item["goodsNo"] == goodsNo:
            return item
    return None    

def calc_cart_cost(carts:dict):
   total = 0
   for key,val in carts.items():
      product = get_product_by_id(key)
      if product is not None:
        total += product["price"]*val
      else:
         print(f"商品{key},商品数量{val},不存在")
         continue 
   print(f"共消费{total}元")
   return total

add_product(1004,"xiaopeng",12500,10)

get_product_by_id(1004)


calc_cart_cost(carts)
# ​**double(x)**：定义了一个函数，功能是返回 x + x。
# ​**map(double, range(5))**：将 double 函数应用到 range(5) 生成的序列 [0, 1, 2, 3, 4] 上。
# ​**list(result)**：将 map 对象转换为列表并打印。
print(list(map(lambda x:x+x,range(5))))

print(range(5))


print(list(map(lambda x:x+x,range(5))))    

# 定义函数
def double(x):
    return x + x

# 使用 map 函数
result = map(double, range(5))

# 转换为列表并输出
print(list(result))

result = dict(map(lambda product: (product["goodsNo"], product["stock"]), products))

print(dict(map(lambda product: (product["goodsNo"],product["stock"]),products)))



print(dict([(1000, 10), (1001, 11), (1002, 12), (1003, 13)]))

total_stock = reduce(lambda acc, product: acc + product["stock"], products, 0)

print(total_stock)

