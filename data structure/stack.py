class stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def delay(self):
        return self.items
#test
a = stack()
a.push(4)
a.push(5)
a.push(6)
a.pop()
print(a.delay())