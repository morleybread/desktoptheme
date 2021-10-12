#
# from Fileopreate1Dic import *
# import xml.etree.ElementTree as etree
#
#
# def main2s(a):
#     tree = etree.parse("image.svg")
#     root = tree.getroot()
#     root.set("xmlns:xlink", "http://www.w3.org/1999/xlink")
#
#     for x in root.iter():
#
#         if 'class' in x.attrib:
#             #     try:
#             #        if x.attrib["fill"]=='#ffd200':
#             #
#             #            x.set("fill", "#ff0000")
#             #
#             #     except:
#             #         pass
#
#             #
#             # titleButtonBg
#             # titleButtonBg
#             # sideBarBg
#             # sideBarIconFg
#             # sideBarTextFg
#
#             # sideBarTextFg
#             # sideBarBgActive
#             # sideBarBgActive
#             # sideBarBgActive
#
#             # sideBarIconFgActive
#             # sideBarTextFgActive
#             # sideBarIconFg
#             # sideBarTextFgActive
#             # filterInputActiveBg
#
#             # a=a+1
#             # # print(a)
#             # # print(x.attrib)
#             # b=transtodic("Cup/colors.tdesktop-theme")[x.attrib["class"]]
#             #
#
#             arr = ["titleButtonBg", "sideBarBg", "sideBarIconFg", "sideBarTextFg", "sideBarBgActive",
#                    "sideBarIconFgActive", "sideBarTextFgActive", "filterInputActiveBg", "dialogsOnlineBadgeFgActive",
#                    "titleButtonCloseBg"]
#             cla = x.attrib["class"]
#             if cla in arr:
#                 if cla == arr[1]:
#                     x.set("fill", "#293a4c")
#                 if cla == arr[2]:
#                     x.set("fill", "#8393a3")
#                 if cla == arr[3]:
#                     x.set("fill", "#8897a6")
#                 if cla == arr[5]:
#                     x.set("fill", "#5eb5f7")
#                 if cla == arr[4]:
#                     x.set("fill", "#17212b")
#                 if cla == arr[6]:
#                     x.set("fill", "#17212b")
#                 if cla == arr[7]:
#                     x.set("fill", transtodic(a)["windowBg"])
#                 if cla == arr[8]:
#                     x.set("fill", transtodic(a)["windowFgActive"])
#                 if cla == arr[0]:
#                     x.set("fill", transtodic(a)["menuIconFg"])
#                 if cla == arr[9]:
#                     x.set("fill", transtodic(a)["menuIconFg"])
#                 # windowFgActive
#
#
#     tree.write("image2" + ".svg")
