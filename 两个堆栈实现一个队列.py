#
# class MyStack:
#
#     def __init__(self):
#         self.stack = []
#         pass
#
#     def pop(self):
#         return self.stack[-1]
#
#     def push(self, value):
#         pass
#
#     def length(self):
#         return len(self.stack)
#
#
# class MyQueue:
#     def __init__(self):
#         self.stack1 = MyStack()
#         self.stack2 = MyStack()
#
#     def append_tail(self, value):
#         self.stack1.push(value)
#
#     def delete_head(self, value):
#         if not self.stack2:
#             for i in range(self.stack1.length()):
#                 v = self.stack1.pop()
#                 self.stack2.push(v)
#             self.stack2.pop()
#         else:
#             self.stack2.pop()

class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def pop(self):

        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_out:
                key = self.stack_in.pop()
                self.stack_out.append(key)
            return self.stack_out.pop()

    def push(self, value):
        self.stack_in.append(value)

    def empty(self):
        if not self.stack_in and not self.stack_out:
            return True
        else:
            return False
