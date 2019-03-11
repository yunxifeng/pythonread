import requests
from operator import itemgetter

# 执行API调用并存储响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print("Status Code: ", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对于每篇文章,都执行一个API调用
    url = ("https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json")
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        "title": response_dict["title"],
        "link": "https://news.ycombinator.com/item?id=" + str(submission_id),
        # 不确定某个键是否包含在字典中时， 可使用方法dict.get() ， 它在指定的键存在时返回与之相关联的值， 并在指定的键不存在时返回你指定
        # 的值（这里是0） 。
        "comments": response_dict.get("descendants", 0)
    }
    submission_dicts.append(submission_dict)

#  使用了模块operator 中的函数itemgetter() （见❼） 。 我们向这个函数传递了键'comments' ， 因此它将从这个列表的每个
# 字典中提取与键'comments' 相关联的值。 这样， 函数sorted() 将根据这种值对列表进行排序。 我们将列表按降序排列
submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict["title"])
    print("Discussion link:", submission_dict["link"])
    print("Comments:", submission_dict["comments"])