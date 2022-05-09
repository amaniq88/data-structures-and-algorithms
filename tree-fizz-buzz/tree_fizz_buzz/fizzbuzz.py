from queue import deque
class Node:
   def __init__(self, value, child = None) -> None:
      self.val = value
      self.children = []
      if child != None:
         for value in child:
            self.children.append(value)

def fizz_buzz_tree(root):
    if root.val == "None" :
      raise Exception("Null value ")
    if isinstance(root.val, int) == False:
       raise Exception("shoud be integer only ")
    head = Node(fizz_buzz(root.val))
    q = deque([(root, head)])
    while q:
      node, cloned = q.popleft()
      for chld in node.children:
         new_n = Node(fizz_buzz(chld.val))
         cloned.children.append(new_n)
         q.append((chld,new_n))
    return head

def treeprint(node, tree):
   if node == None:
      tree.append("None")
      return tree
   if tree == None:
      tree = []
   tree.append(node.val)
   for child in node.children:
      treeprint(child, tree)
   return tree


def fizz_buzz(node):
    if node % 3 == 0 and node % 5 == 0:
        return "FizzBuzz"
    elif node % 3 == 0 :
        return"Fizz"
    elif node % 5 == 0 :
        return"Buzz"
    else:
        return str(node)


# Driver program to test above functions
if __name__ == '__main__':

    node6 = Node(9)
    node5 = Node(56)
    node4 = Node(25, [node5, node6])
    node3 = Node(32)
    node2 = Node(27)
    node1 = Node(15, [node2, node3, node4])
    root = node1

    copynode = fizz_buzz_tree(root)
    print(treeprint(copynode, None))



