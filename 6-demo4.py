import time
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper():
      start = time.time()
      func()
      stop = time.time()
      print(f"func 函数一共执行了{int(stop-start)}s")
    return wrapper    

@time_it

def work():
   print("func函数开始执行")
   time.sleep(1)
   print("func函数执行结束")

work()



def cache(func):
   cached_results = {}

   @wraps(func)
   def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        else:
            get_result = func(args)
            cached_results[args] =get_result
            return get_result
   return wrapper


@cache
def test(*args):
    print("来啦 老弟")
    if args == 1:
        return f"******今天是{args}*************"
    else:
        return f"*****明天是{args}****"
    
print(test(11))
print(test(11))
print(test(11))
print(test(11))