# Trees

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branch must be a list'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        return tree(label(left) + label(right), [left, right])

def count_leaves(t):
    """Count the leaves of a tree."""
    if is_leaf(t):
        return 1
   # ans = 0
   # for branch in branches(t):
   #     ans += count_leaves(branch)
   # return ans
    branch_counts = [count_leaves(b) for b in branches(t)]
    return sum(branch_counts)

def leaves(tree):
    """Return a list containing the leaf labels of tree."""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)
    
def increment(t):
    """Return a tree like t with all labels incremented"""
    return tree(label(t) + 1, [increment(b) for b in branches(t)])

def print_tree(t, indent=0):
    """Print a tree with its constructor"""
    print('-' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
