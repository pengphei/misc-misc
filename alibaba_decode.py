#
#   阿里巴巴双十一密码破解答案
#   问题链接： 阿里云@微信公众号
#   编写： Phil Han
#

keys_str = "qwertyuiopasdfghjklzxcvbnm"

convert = [
    "Of zit kggd zitkt qkt ygxk ortfzoeqs wqlatzwqssl qfr zvg ortfzoeqs yggzwqssl. \n",
    "Fgv oy ngx vqfz zg hxz zitd of gft soft.piv dgfn lgsxzogfl qkt zitkt? \n",
    "Zohl:hstqlt eiqfut zit ygkd gy zit fxdwtk ngx utz.Zit Hkgukqddtkl! \n"
]

def convert_str_k(dstr):
    keys = ""
    for dd in dstr:
        str_id = keys_str.find(dd.lower())
        if(str_id >= 0):
            if(dd.islower()):
                real_str = chr(ord('a') + str_id)
                keys += real_str
            else:
                real_str = chr(ord('A') + str_id)
                keys += real_str                
        else:
            keys += dd
    return keys

#        
def convert_all(darray):
    strs = ""
    for dd in darray:
        strs += convert_str_k(dd)
    return strs

def combination(n, m):
    nn = 1
    mm = 1
    oo = 1
    for i in range(1, n):
        nn *= i
    for i in range(1, m):
        mm *= i
    for i in range(1, n-m):
        oo *= i

    return nn/(mm*oo)

def number_convert(num):
    bin_str = bin(num)
    out = bin_str + " ==>> " + "0b1000 \n" + "NOTE: 0b01 + 0b01 = 0b10\n"
    print(out)
    print("0x1000 ==>> 1024")

ans_0 = convert_all(convert)
ans_1 = combination(5,2)

print("## stage 0: \n")
print("keyboard \n")
print("## stage 1: \n")
print(convert_all(convert))
print("## stage 2: \n")
print(str(combination(5,2)) + "\n")
print("## stage 3: \n")
number_convert(ans_1)        



