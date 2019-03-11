# 技巧一
# l = ["python", "C", "C++", "PHP", "C#"]
# # for i in range(len(l)):
# #     print("index " + str(i) + " in l is: " + l[i])

# 技巧二
# cat = ["fat", "bleak", "loud"]
# size, color, disposition = cat
# print(size)

# 关于list
# l = ["python", "C", "C++", "PHP", "C#"]
# print(l.index("C"))
# print(l.insert(2, "JAVA"))
# del l[0]
# l.remove("C++")
# print(l)
# # 逆序
# l.sort(reverse=True)

# 缩进规则中的例外01--list
spam = ['apples',
'oranges',

                            'bananas',
'cats']

print(spam)

# 缩进规则中的例外02--续行字符\
print('Four score and seven ' + \
'years ago...')

# string
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(newName)

# Tuple
t = ("hello")
print(type(t))
t = ("hello",)
print(type(t))

print(list("he'l'lo"))


# 关于copy和deepcopy
import copy
l = [[1], [1,2], [1,2,3]]
ll = copy.copy(l)
ll[0][0] = 0
print(l, ll)

s = [[1], [1,2], [1,2,3]]
ss = copy.deepcopy(l)
ss[0][0] = 0
print(s, ss)
