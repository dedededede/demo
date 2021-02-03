class FreqStack(object):
    def __init__(self):
        self.stack = []
        self.stack_element = {}
        self.stack_index = {}
        self.max_element_count = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if x not in self.stack_element:
            self.stack_element[x] = 0
        self.stack_element[x] += 1

        count = self.stack_element[x]
        if count not in self.stack_index:
            self.stack_index[count] = []

        self.stack_index[count].append(x)

        if count > self.max_element_count:
            self.max_element_count = count

    def pop(self):
        """
        :rtype: int
        """
        x = self.stack_index[self.max_element_count].pop()
        self.stack_element[x] -= 1
        if not self.stack_index[self.max_element_count]:
            self.max_element_count -= 1
        return x





obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)


print obj.pop()
print obj.pop()


print obj.pop()
print obj.pop()
print obj.pop()
print obj.pop()
