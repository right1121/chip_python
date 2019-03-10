# 通常の繰り返し
extension_1 = []
for i in range(10):
    extension_1.append(i**2)
extension_1

print(extension_1)

# リスト内表現構文
# [counter for counter in iterator]
comprehension_1= [i**2 for i in range(10)]

print(comprehension_1)
