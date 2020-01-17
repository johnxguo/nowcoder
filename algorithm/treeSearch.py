def search(tree):
    if not tree:
        return 
    search(tree.left)
    search(tree.right)
    print(tree.value)


def search(tree):
    node = tree.root
    stack = []
    while node:
        if not node.left && not node.right:
            if stack.count == 0:
                break
            node = stack.pop()
            continue
        stack.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if stack.count == 0:
            break
        node = stack.pop()
        print(node.value)

