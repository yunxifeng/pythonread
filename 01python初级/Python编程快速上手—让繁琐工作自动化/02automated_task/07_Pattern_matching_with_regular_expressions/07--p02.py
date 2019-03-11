import re

# phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')#regex对象
# m = phoneNumRegex.search("My phoneNumber is 456-789-6789 and 789-456-5676")#match对象
# print(m.group())

# 利用括号分组
# \( 和 \) 是转义,表示()
num = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
m = num.search("My phoneNumber is (456) 789-6789 and 789-456-5676")
# 向 group()
# 匹配对象方法传入整数 1 或 2， 就可以取得匹配文本的不同部分。 向 group()方法传
# 入 0 或不传入参数， 将返回整个匹配的文本。
print(m.group())
print(m.group(1))
print(m.group(2))
# 如果想要一次就获取所有的分组，请使用 groups()方法， 注意函数名的复数形式。
print(m.groups())


# |
# 如果需要匹配真正的管道字符，就用倒斜杠转义，即\|。
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# ?
# 第一个作用: 表示可选的分组
# 有时候，想匹配的模式是可选的。就是说，不论这段文本在不在，正则表达式
# 都会认为匹配。字符?表明它前面的分组在这个模式中是可选的。
# 如果需要匹配真正的问号字符，就使用转义字符\?。
b = re.compile(r'Bat(wo)?man')
m1 = b.search("T adventures of Batman")
print(m1.group())
m2 = b.search('The adventures of Batwoman')
print(m2.group())

# *
# *（称为星号）意味着“匹配零次或多次”，即星号之前的分组，可以在文本中出现任意次。
# 如果需要匹配真正的星号字符，就在正则表达式的星号字符前加上倒斜杠，即\*。
b = re.compile(r'Bat(wo)*man')
m3 = b.search("T adventures of Batman")
print(m3.group())
m4 = b.search('The adventures of Batwowowoman')
print(m4.group())

# +
# +（加号） 意味着“匹配一次或多次”。
#如果需要匹配真正的加号字符，在加号前面加上倒斜杠实现转义： \+。
b = re.compile(r'Bat(wo)+man')
try:
    m5 = b.search("T adventures of Batman")
    print(m5.group())
except Exception:
    print("None")
m6 = b.search('The adventures of Batwowowoman')
print(m6.group())

# {n}, {m,n}, {m,}, {,n}
# 前面内容重复特定次数
# 贪婪匹配: 在有二义的情况下，它们会尽可能匹配最长的字符串。
# 注: 别加空格...
haRegex = re.compile(r'(Ha){1,4}')
mo1 = haRegex.search('HaHaHaHakjsadhlash')
print(mo1.group())

# ?
# 第二个作用: 声明非贪婪匹配
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()


# search()方法-->返回Match对象
# findall()方法-->如果没有分组,返回字符串列表;如果有分组,返回元组的列表
num1 = re.compile(r'(\(\d{3}\)) (\d{3}-\d{4})')
num2 = re.compile(r'\(\d{3}\) \d{3}-\d{4}')
m1 = num1.findall("My phoneNumber is (456) 789-6789 and (789) 456-5676")
m2 = num2.findall("My phoneNumber is (456) 789-6789 and (789) 456-5676")
print(m1)
print(m2)

# 建立自己的字符分类-->[]
# 在方括号内，普通的正则表达式符号不会被解释。这意味着，你不需
# 要前面加上倒斜杠转义
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# [^ asd]-->表示匹配所有非'a', 's', 'd'的字符
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))


# ^ 和 $
# 在正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文本开始处。
# 正则表达式的末尾加上美元符号（$），表示该字符串必须以这个正则表达式的模式结束。
beginsWithHello = re.compile(r'^Hello')
m1 = beginsWithHello.search('Hello world!')
print(m1.group())

endsWithNumber = re.compile(r'\d$')
m2 = endsWithNumber.search('Your number is 42')
print(m2.group())

wholeStringIsNum = re.compile(r'^\d+$')
t1 = wholeStringIsNum.search('1234567890')
t2 = wholeStringIsNum.search('12345xyz67890')# None
t3 = wholeStringIsNum.search('12 34567890')# None
print(t1.group())


# .(通配符)
# 匹配除了换行(\n)之外的所有字符(注:句点字符只匹配一个字符)
# 要匹配真正的句点， 就是用倒斜杠转义： \
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

# .* -->匹配任意文本
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group())
# 非贪婪
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
# 贪婪
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())


# 匹配换行符\n
# 向re.compile()传入第二个参数-->re.DOTALL-->让句点字符匹配所有字符， 包括换行字符。
noNewlineRegex = re.compile('.*')
n1 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.'
                      'Uphold the law.')
print(n1.group())

noNewlineRegex = re.compile('.*', re.DOTALL)
n2 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.'
                      'Uphold the law.')
print(n2.group())

# 不区分大小写匹配
# 传入第二个参数-->re.I或者 re.IGNORECASE
robocop = re.compile(r'robocop', re.I)
z = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(z)



# sub()
# 用sub()方法替换字符串
agentNamesRegex = re.compile(r'Agent (\w)\w*')
# \1****表示使用第一分组(\w)和****替换匹配到的所有字符
s = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(s)


# re.VERBOSE参数--忽略正则表达式中的空白符和注释
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    \d{3}                           # first 3 digits
    (\s|-|\.)                       # separator
    \d{4}                           # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
    )''', re.VERBOSE)


# 组合使用 re.IGNOREC ASE、 re.DOTALL 和 re.VERBOSE
# re.compile()只接受一个值作为第二参数
# 可使用管道字符"|"将他们组合起来,"|"在这里称为"按位或"操作符
# 下面的语法过时了,参考[ http://nostarch.com/automatestuff/]
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

