s = "hha".join("khk")
print(s)# khhahhhak
t = "h".join(["0", "0", "0"])
print(t)# 0h0h0

s = '''Dear Alice,
    How have you been? I am fine.
    There is a container in the fridge
    that is labeled "Milk Experiment".
    Please do not drink it.
    Sincerely,
    Bob'''
print(s.split("\n"))
print(s.startswith("Bob"))
print(s.endswith("D"))

s = "hello"
#' l.rjust(10)是说我们希望右对齐，将'Hello'放在一个长度为 10 的字符串中。
# 'Hello'有 5 个字符， 所以左边会加上 5 个空格， 得到一个 10 个字符的字符串， 实现
# 'Hello'右对齐。
print(s.rjust(10))
print(s.rjust(10, "*"))
print(s.center(11, "-"))


def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

t = "hello"
print(t.rstrip("hoe"))

# pyperclip
import pyperclip
# s = "yunxifeng"
# print(pyperclip.copy(s))
ss = pyperclip.paste()
print(ss)