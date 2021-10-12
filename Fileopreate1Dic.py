import ast


def transtodic(a):  # 打开一个.tdesktop-theme文件 返回一个字典
    binl = []
    with open(a, "rb") as fb:
        m = fb.readlines()
        for x in m:
            try:
                bins = list(x).index(59)

                binl = binl + list(x)[:bins] + [59, 10]
                # print(list(x))
            except ValueError:
                pass
        s = ""
        for i in binl:
            s = s + chr(i)

        help = "{\"" + s.replace(": ", "\": \"").replace(";\n", "\",\n\"").rstrip("\"") + "}"
        filr = ast.literal_eval(help)
    for x, y in filr.items():
        if list(y)[0] != '#':
            filr[x] = parloops(filr, y)  # 整合

    return filr


def parloops(dic, x):  # 递归

    if list(dic[x])[0] != "#":
        asi = dic[x]
        return parloops(dic, asi)
    else:
        return dic[x]


def parese(a,b=0): #传一个#号开头的值

    if len(a)<=7:
        return [a,"0"]
    else:
        oran="".join(list(a)[:-2])
        m="".join(list(a)[-2:])
        if b:
            sub="{:.2f}".format(int(m, 16) / 255)
            final=float(sub)
            return [oran,str(final-b)]
        else:
            return [oran,"{:.2f}".format(int(m,16)/255)]

transtodic("Cup/colors.tdesktop-theme")