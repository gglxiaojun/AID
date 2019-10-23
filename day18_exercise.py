# 3. 每个灯泡都有"亮","灭"两种模式，
#     请打印出30个灯泡所有可能的模式
import itertools

# for item in itertools.product(["亮", "灭"], repeat=30):
#     print(item)

# 4. 年会节目有：
#     "舞蹈1","舞蹈2","舞蹈3","相声1","相声2","歌曲1","歌曲2","歌曲3","歌曲4"
#    请打印出节目所有排列的方案
#    要求：相同节目不能挨着.

list01 = ["舞蹈1", "舞蹈2", "舞蹈3", "相声1", "相声2", "歌曲1", "歌曲2", "歌曲3", "歌曲4"]
for item in itertools.permutations(list01, len(list01)):
    # ('歌曲4', '歌曲3', '歌曲2', '歌曲1', '舞蹈3', '舞蹈1', '相声2', '相声1', '舞蹈2')
    for i in range(len(item) - 1):
        if item[i][:2] == item[i + 1][:2]:
            break
    else:
        print(item)
