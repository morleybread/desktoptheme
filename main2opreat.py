from Fileopreate1Dic import *
from getPicbyterbase64 import *
from main3opreate import *
import xml.etree.ElementTree as etree


tree = etree.parse("template/new.svg")
root = tree.getroot()
root.set("xmlns:xlink", "http://www.w3.org/1999/xlink")


def main1s(pat, pa):
    for x in root.iter():
        if 'class' in x.attrib:
            arr = ["titleButtonBg", "sideBarBg", "sideBarIconFg", "sideBarTextFg", "sideBarBgActive",
                   "sideBarIconFgActive", "sideBarTextFgActive", "filterInputActiveBg", "dialogsOnlineBadgeFgActive",
                   "titleButtonCloseBg"]
            cla = x.attrib["class"]
            if cla in arr:
                if cla == arr[1]:
                    x.set("fill", "#293a4c")
                if cla == arr[2]:
                    x.set("fill", "#8393a3")
                if cla == arr[3]:
                    x.set("fill", "#8897a6")
                if cla == arr[5]:
                    x.set("fill", "#5eb5f7")
                if cla == arr[4]:
                    x.set("fill", "#17212b")
                if cla == arr[6]:
                    x.set("fill", "#17212b")
                if cla == arr[7]:
                    x.set("fill", transtodic(pat)["windowBg"])
                if cla == arr[8]:
                    x.set("fill", transtodic(pat)["windowFgActive"])
                if cla == arr[0]:
                    x.set("fill", transtodic(pat)["menuIconFg"])
                if cla == arr[9]:
                    x.set("fill", transtodic(pat)["menuIconFg"])

            if x.attrib["class"] == "IMG":
                x.set("xlink:href", "data:image/jpeg;base64," + getpicbas(pa))

            elif x.attrib["class"] == "PreviewBack" or x.attrib["class"] == "PreviewShadow":

                x.set("fill", parese(transtodic(pat)["msgInBg"])[0])
                x.set("stop-opacity", parese(transtodic(pat)["msgInBg"])[1])

            elif "stop-color" in x.attrib:
                try:
                    x.set("stop-color", parese(transtodic(pat)[x.attrib["class"]])[0])
                    x.set("stop-opacity", parese(transtodic(pat)[x.attrib["class"]])[1])
                except KeyError:
                    try:
                        tem = "".join(list(x.attrib["class"])[:-6])
                        x.set("stop-color", parese(transtodic(pat)[tem])[0])
                        x.set("stop-opacity", parese(transtodic(pat, b=0.2)[tem])[1])
                    except:
                        pass
            else:
                try:
                    x.set("fill", parese(transtodic(pat)[x.attrib["class"]])[0])
                    # x.set("fill-opacity",parese(transtodic("Cup/colors.tdesktop-theme")[x.attrib["class"]])[1])
                except:
                    pass

    tree.write("image" + ".svg")
    # main2s(pat)
