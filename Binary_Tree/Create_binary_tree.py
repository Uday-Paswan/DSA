class Node:
    def __init__(self,val=0):
        self.val=val
        self.left=None
        self.right=None
#Create Node Objects
drinks=Node("drinks")
hot=Node("hot")
cold=Node("cold")
tea=Node("tea")
coffee=Node("coffee")
cola=Node("cola")
fanta=Node("fanta")

#Connect Nodes
drinks.left=hot
drinks.right=cold

hot.left=tea
hot.right=coffee

cold.left=cola
cold.right=fanta

print(drinks.left.val)