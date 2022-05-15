
# 链表定义
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


def print_list(data):
    head = data
    my_list = []
    while head:
        my_list.append(head.value)
        head = head.next
    print(my_list)
    return my_list[::-1]


if __name__ == '__main__':
    print('start')
    c = ListNode(7)
    b = ListNode(6, c)
    a = ListNode(5, b)
    c = print_list(a)
    print(c)
