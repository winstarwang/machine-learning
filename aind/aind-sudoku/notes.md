# 结题思路：

## naked_twins:

1. 找到每个unit的naked_twins(必须按每个unit找),保存含有naked_twins的unit index,box,value
2. 对于每个unit，根据naked_twins消除peers中的多余值
3. 经过1轮消除后，可能会产生新的naked_twins,所有需要循环执行step 1 and 2,直到整个数独的值不再更新为止

## 对角线数独：

1. 生成对角线数独的unit，然后将其加入unitlist即可解决

## search策略：迭代实现方式

1. 按value的长度从小到大生成搜索树的层级
2. 使用product函数生成所有搜索路径的组合（？生成的搜索空间太大，效率很低）
3. 按顺序选择一条搜索路径，一层层往下试探，尝试解题
4. 将试探不可行的搜索策略记下来，保存成经验，避免在下条搜索路径重走老路