# 笔记
1.不使用regex-->07--p01.py
2.使用regex-->07--p02.py
    - 向 re.compile()传入一个字符串值，表示正则表达式，它将返回一个 Regex 模式对象（或者就简称为 Regex 对象）。
    - Regex 对象的 search()方法查找传入的字符串， 寻找该正则表达式的所有匹配。
    - 没有找到该正则表达式模式， search()方法将返回 None。如果找到了该模式，
      search()方法将返回第一个 Match 对象。 Match 对象有一个 group()方法，它返回被查找字
      符串中实际匹配的文本
3.常用字符分类的缩写代码
\d      0 到 9 的任何数字
\D      除 0 到 9 的数字以外的任何字符

\w      任何字母、数字或下划线字符（可以认为是匹配“单词”字符）
\W      除字母、数字和下划线以外的任何字符

\s      空格、制表符或换行符（可以认为是匹配“空白”字符）
\S      除空格、制表符和换行符以外的任何字符
4.总结:
     ?                   匹配零次或一次前面的分组。
     *                   匹配零次或多次前面的分组。
     +                   匹配一次或多次前面的分组。
     {n}                 匹配 n 次前面的分组。
     {n,}                匹配 n 次或更多前面的分组。
     {,m}                匹配零次到 m 次前面的分组。
     {n,m}               匹配至少 n 次、至多 m 次前面的分组。
     {n,m}?或*?或+?      对前面的分组进行非贪心匹配。
     ^spam               意味着字符串必须以 spam 开始。
     spam$               意味着字符串必须以 spam 结束。
     .                   匹配所有字符，换行符除外。
     \d、 \w 和\s        分别匹配数字、单词和空格。
     \D、 \W 和\S        分别匹配出数字、单词和空格外的所有字符。
     [abc]               匹配方括号内的任意字符（诸如 a、 b 或 c）。
     [^abc]              匹配不在方括号内的任意字符。
5.re.compile()的第二个参数:
    - re.DOTALL-->允许匹配换行符
    - re.I或re.IGNORECASE-->忽略大小写
    - re.VERBOSE-->忽略正则表达式中的空白符和注释
6.regex对象的方法:
    - search()
        - 传入要匹配的文本
    - findall()
        - 传入要匹配的文本
    - sub()
        - 两个参数:
            - 字符串,用于取代发现的匹配
            - 要匹配的文本