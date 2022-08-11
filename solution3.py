def __contains__(self, data):
    return self._contains(data, self.root)  # Start at the root

def _contains(self, data, node):
    if node.data != None:
        if node.data == data:
            return True
        elif node.data < data:
            if node.right == None:
                return False
            else:
                return self._contains(data, node.right)
        else:
            if node.left == None:
                return False
            else:
                return self._contains(data, node.left) 

print(3 in tree) # True
print(2 in tree) # False
print(7 in tree) # True
print(6 in tree) # True
print(9 in tree) # False
