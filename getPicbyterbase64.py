import base64



def getpicbas(a):

    with open(a,"rb")as hu:
        ss=hu.read()
        bas=base64.b64encode(ss)
        return bas.decode("utf-8")


