def list_str(spam):
    for i in range(len(spam)):
        print(spam[i] + ", ", end="")
    print("and", spam[-1] + ".")


spam = ["apples", "bananas", "tofu", "cats"]
list_str(spam)

