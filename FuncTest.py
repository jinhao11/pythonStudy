#关键字参数，能够指定要传递的参数，不用按照顺序


def func(a,b,c):
    print('a=%s' %a)
    print('b=%s' %b)
    print('c=%s' %c)



func(1,2,3)

func(1,c=3,b=2)


#可变长参数的函数设计
def func2(a,*b,c):
    print('a=%s' % a)

    print('c=%s' % c)

func2(2,c=1)
