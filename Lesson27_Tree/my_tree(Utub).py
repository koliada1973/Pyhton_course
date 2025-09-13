class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent_node, value):
        # Перевірка чи вузел node одразу має значення None
        if node is None:
            return None, parent_node, False
        # Якщо шукане значення знаходиться в поточному вузлі,
        # то додавати новий вузол не потрібно, щоб не мати дублікатів значень
        if value == node.data:
            # Повертаємо вузол, батьківський вузол
            # і True (флаг того, що шукане значення знайдене в цій віршині (вузлі))
            return node, parent_node, True
        # Якщо шукане значення меньше того, що знаходиться в поточному вузлі -
        # потрібно йти лівою стороною (якщо існує лівий потомок)
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        # Якщо шукане значення більшо того, що знаходиться в поточному вузлі -
        # потрібно йти правою стороною (якщо існує правий потомок)
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        # Повертаємо вузол (до якого будемо добавляти новий вузол), батьківський вузол
        # і False (флаг того, що вузла з шуканим значенням не знайдено)
        return node, parent_node, False

    def append(self, obj: Node):
        if self.root is None:
            self.root = obj
            return obj
        # Передаємо в метод __find:
        # - корінь дерева (бо пошук починається з корневого вузла),
        # - None (бо у корня немає предків),
        # - значення об'єкта, який потрібно додати до дерева (obj.data)
        # Отримуємо:
        # s - посилання на об'єкт (попередню вершину), до якого будемо добавляти нову вершину (вузол)
        # p - посилання
        # flag_find - флаг, чи знайдено шукане значення
        s, p, flag_find = self.__find(self.root, None, obj.data)

        # Якщо flag_find != True (тобто можна додавати нову вершину);
        # а також s != None (тобто є об'єкт (вузол), до якого ми будемо додавати новий об'єкт (вузол)
        if not flag_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
        return obj

    def show_tree(self, node):
        if node is None:
            return
        else:
            self.show_tree(node.left)
            print(node.data)
            self.show_tree(node.right)

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]  # Список для відображення вершин поточного рівня
        while v:
            vn = []
            for x in v:
                print(x.data, end = ' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_leaf (self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.right = s.left
        elif p.right == s:
            if s.right is None:
                p.right = s.left
            elif s.left is None:
                p.left = s.right

    def __find_min(self, node, parent_node):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent_node


    def del_node(self, key):
        s, p, flag_find = self.__find(self.root, None, key)

        # Якщо flag_find == False, то вершина (вузол) з шуканим значенням не була знайдена
        if not flag_find:
            return None

        # 1 ситуація -  вершина s листова:
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)   # p - батьківська вершина для видаляємої вершини s

        # 2 ситуація - видалення вершини з існуючим правим або лівим нащадком (тільки з одним нащадком):
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)

        # 3 ситуація - видалення вершини з обома нащадками.
        # При цьому замість видаляємого вузла має бути вставлений вузул з тих,
        # що мають БІЛЬШЕ значення, ніж у видаляємого вузла (тобто з правої гілки),
        # але з НАІМЕНЬШИМ значенням (тобто наіменьше з правої гілки):
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.del_one_child(sr, pr)



# l = [10,5,7,16,13,2,20]
l = [20,5,24,2,16,11,18]

tree1 = Tree()
for i in l:
    tree1.append(Node(i))


tree1.del_node(16)
# tree1.show_tree(tree1.root)
tree1.show_wide_tree(tree1.root)