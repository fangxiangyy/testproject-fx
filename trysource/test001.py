
def logger(fn):
    def wrap(*args,**kwargs):
        print("args={},kwargs={}".format(args,kwargs))
        ret = fn(*args,**kwargs)
        return ret
    return wrap

@logger
def add(x,y):
    return  x+y

@logger
def add1(x,y,z):
    return x+y+z

# foo = logger(add)
# print(foo(4,6))
#
# add=logger(add)
# print(add(4,6))

print(add1(4,6,4))

