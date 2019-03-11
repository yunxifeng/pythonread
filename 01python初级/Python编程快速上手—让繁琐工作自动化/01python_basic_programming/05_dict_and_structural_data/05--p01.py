d = {"name": "yunxifeng", "age": "21", "sex": "man"}
s = d.get("address", "NotFound")
print(s)

t1 = d.setdefault("favorite_language", "python")
print(t1)
t2 = d.setdefault("favorite_language", "C")
print(t2)

# setdefault()使用技巧和漂亮打印pprint()
import pprint
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)
# 等价于
print(pprint.pformat(count))

# print(count)