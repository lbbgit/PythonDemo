import sys

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")


class e1(Exception):
    pass

class e2(e1):
    pass

class e3(Exception):
    pass

for cls in [B, C, D,e1,e2,e3]:#,'x','yy','y'
    try:
        raise cls()
    except (D,C):
        print("D or C")
    except C:
        print("C")
    except B:
        print("B")
    # except e1:
    #     print("e1 oru")
    except e2:
        print("e2 oru-------",e2.args)#e2.args
        # x,y = e2.args
        # print('x =', x)
        # print('y =', y)
    except e3:
        print("e3 [did't catch will eroor]")
    # except ('x', 'yy'):
    #     print("x or yy")
    # except ('y'):
    #     print("y")
    except:
        print("Unexpected error:", sys.exc_info()[0])
else:
    print ("成");

