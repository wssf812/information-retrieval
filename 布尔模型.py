import os
import jieba
# 分词
def jibafenci(text):
    str = jieba.cut(text, cut_all=False)
    cutstr = ' '.join(str)
    return cutstr
# 倒排索引
def daopaisuoyin():
    wordDict = {}
    for filename in os.listdir("C:\\Users\\Dell\\Desktop\\IR测试\\"):
        with open("C:\\Users\\Dell\\Desktop\\IR测试\\" + filename, 'r', encoding='utf-8'
                ,errors='ignore') as f:
            # 去除非法字符：encode('utf-8').decode('utf-8-sig')
            fencirel = jibafenci(f.readline().encode('utf-8').decode('utf-8-sig').strip("\n"))
            for word in fencirel.split(" "):
                if word in wordDict:
                    # 如果词是word中的键，那么就只将文件名添加进集合中来即可，
                    # add属性是集合的属性，dict没有add属性
                    wordDict[word].add(filename)
                else:
                    # 一个txt文件创建一个set，当word不再dict中时将文件名添加进set(又去重的功效),
                    #防止了文件名重复
                    wordSet = set()
                    wordSet.add(filename)
                    # 让dict中的键，词对应集合中的文件名，
                    wordDict[word] = wordSet
    return wordDict
# 进行查询（布尔--and查询）
def yucewendang(query,biaozhi):
   #  输入词分词
   quertyFenci = jibafenci(query).split(" ")
   # 第一个词
   one = quertyFenci[0]
   # 第二个词
   two = quertyFenci[-1]
   list=[]
   list2=[]
   for word,filename in daopaisuoyin().items():
         # 分别获取他们的倒排记录表
         if one in word:
            for name in filename:
                 list.append(name)
         if two in word:
             for name in filename:
                 list2.append(name)
   bool(list,list2,biaozhi)

def bool(list,list2,biaozhi):
  if  biaozhi =='and' :
   #   and布尔判断合并倒排记录表
     for rel in list:
         if rel in list2:
            print('您的查询结果是：',rel)
  if biaozhi == 'or':
   #   or布尔判断合并倒排记录表
      listset = set()
      for rel in list:
          list2.append(rel)
      for quchong in list2:
          listset.add(quchong)
      print('您的查询结果是：',listset)

# 输入一个查询(单一布尔查询)
query = input("请输入一个查询词：\n")

if 'or' in query:
    yucewendang(query, 'or')
else:
    yucewendang(query, 'and')





