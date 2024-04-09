class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return Node, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False
    def append(self, obj):

        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def show_tree(self, node):
        if node is not None:
            self.show_tree(node.left)
            print(node.data)
            self.show_tree(node.right)

    def show_wide_tree(self, node):
        if node is None:
            return

        result = ""
        v = [node]
        while v:
            vn = []
            for x in v:
                result += str(x.data)
                if x.left:
                    vn.append(x.left)
                if x.right:
                    vn.append(x.right)
                if x != v[-1]:
                    result += " "
            result += "\n"
            v = vn


        print(result)


    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.right = s.left

        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left



    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent


    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

def search_node(node, value):
    if node is None or node.data == value:
        return node

    if value < node.data:
        return search_node(node.left, value)
    else:
        return search_node(node.right, value)

def insert_node(node, value):
    if node is None:
        return Node(value)

    if value < node.data:
        node.left = insert_node(node.left, value)
    else:
        node.right = insert_node(node.right, value)

    return node



v = [10, 5, 7, 16, 13, 2, 20, 56, 78]
t = Tree()
for x in v:
    t.append(Node(x))
t.show_wide_tree(t.root)
t.del_node(2)
t.show_wide_tree(t.root)



v = [10, 5, 7, 16, 13, 2, 20, 56, 78]
t = Tree()
for x in v:
    t.append(Node(x))

key = 2
result = search_node(t.root, key)
if result:
    print(f"Узел с ключом {key} найден.")
else:
    print(f"Узел с ключом {key} не найден.")

v = [10, 5, 7, 16, 13, 2, 20, 56, 78]
t = Tree()
for x in v:
    t.root = insert_node(t.root, x)


t.show_wide_tree(t.root)
key = 25
t.root = insert_node(t.root, key)

t.show_wide_tree(t.root)
