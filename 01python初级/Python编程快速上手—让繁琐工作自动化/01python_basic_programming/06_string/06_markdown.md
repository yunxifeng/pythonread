# 笔记
1. upper()、 lower()
2.isX 字符串方法
除了 islower()和 isupper()， 还有几个字符串方法，它们的名字以 is 开始。这些
方法返回一个布尔值， 描述了字符串的特点。下面是一些常用的 isX 字符串方法：
 isalpha()返回 True， 如果字符串只包含字母， 并且非空；
 isalnum()返回 True，如果字符串只包含字母和数字，并且非空；
 isdecimal()返回 True，如果字符串只包含数字字符，并且非空；
 isspace()返回 True，如果字符串只包含空格、制表符和换行，并且非空；
 istitle()返回 True，如果字符串仅包含以大写字母开头、后面都是小写字母的单词。
3. startswith()和 endswith()
    - startswith()和 endswith()方法返回 True， 如果它们所调用的字符串以该方法传入
      的字符串开始或结束。否则， 方法返回 False。
4. join()和 split()
    - 如果有一个字符串列表，需要将它们连接起来，成为一个单独的字符串， join()方法就很有用。 
        - >>>', '.join(['cats', 'rats', 'bats'])
          'cats, rats, bats' 
    - split()针对一个字符串调用， 返回一个字符串列表。
        - 参数: 自定义分隔符,默认是空格
        - >>> 'My name is Simon'.split()
          ['My', 'name', 'is', 'Simon']
        - 一个常见的 split()用法， 是按照换行符分割多行字符串。
5.rjust()、ljust()和center()方法对齐文本
    - rjust()和 ljust()字符串方法返回调用它们的字符串的填充版本， 通过插入空格来对齐文本。
    - center():  让文本居中
        - 两个参数:
            - 一个整数长度， 用于对齐字符串。
            - 第二个可选参数将指定一个填充字符， 取代空格字符。
            - 参看案例
6.用 strip()、 rstrip()和 lstrip()删除空白字符
    - 有一个可选的字符串参数,指定出现的哪些字符应该被删除,字符的顺序并不重要
7.用pyperclip模块(第三方模块)拷贝粘贴字符串
    - 函数copy(), 复制内容到剪贴板,返回None
    - 函数parse(), 从剪贴板接受内容,返回接受内容
        - 如果你的程序之外的某个程序改变了剪贴板的内容， paste()函数就会返回它。
    - 可以向计算机的剪贴板发送文本， 或从它接收文本。
8.项目一---->口令保管箱
    - 关于sys.argv[]
        - [http://www.cnblogs.com/aland-1415/p/6613449.html]
        - sys.argv[]说白了就是一个从程序外部获取参数的桥梁，这个“外部”很关键，所以那些试图从代码来说明它作用的解释一直没看明白。
          因为我们从外部取得的参数可以是多个，所以获得的是一个列表（list)，也就是说sys.argv其实可以看作是一个列表，所以才能用[]提取其中的元素。
          其第一个元素是程序本身，随后才依次是外部给予的参数。
        - 案例: test.py
# 习题
1.转义字符表示字符串中的一些字符，这些字符用别的方式很难在代码中打出来。
!!!2.\n换行符,\t制表符
3.\\
4.双引号来标识字符串的开始和结束。
!!!5.多行字符串让你在字符串中使用换行符，而不必用\n 转义字符。
6.e,Hello,Hello,lo world!
7.HELLO,True,hello
8.• ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
  • 'There-can-be-only-one.'
9.rjust(), ljust(), center()
10.lstrip(), rstrip()
