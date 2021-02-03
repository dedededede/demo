# -*- encoding: utf8 -*-

step = 5
forward = 1  # 顺时针， -1 表示逆时针
total = 6


class Node(object):
    def __init__(self, value):
        self.next = None
        self.pre = None
        self.value = value


class LinkList(object):
    def __init__(self):
        self.link_list = None

    def create_link(self, element):
        for i in range(1, element + 1):
            node = Node(i)

            if self.link_list is None:
                self.link_list = node
                continue

            cur = self.link_list
            while cur:
                if cur.next:
                    cur = cur.next
                else:
                    break
            cur.next = node
            node.pre = cur

        node.next = self.link_list
        self.link_list.pre = node

    def get_last_survival(self, step, forward):
        cur = self.link_list
        count = 1
        delete_element = []
        if forward == 1:  # 顺时针，按着next遍历
            while cur:
                if total - len(delete_element) == 1:
                    print delete_element
                    print cur.next.value
                    return cur.next.value
                cur = cur.next
                count += 1
                if count == step:
                    delete_element.append(cur.value)
                    cur.next.pre = cur.pre
                    cur.pre.next = cur.next
                    count = 1

        else:  # 逆时针，按着pre进行遍历
            pass


obj = LinkList()
obj.create_link(total)
obj.get_last_survival(step, forward)