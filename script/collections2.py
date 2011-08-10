from abc import ABCMeta, abstractmethod
 
 
class priority_queue(metaclass=ABCMeta):
 
    @abstractmethod
    def __len__(self): pass
 
    @abstractmethod
    def __contains__(self, item): pass
 
    @abstractmethod
    def add(self, item):
        "Add item to the queue."
 
    @abstractmethod
    def pop(self):
        "Remove and return the minimum item in the queue."
 
    @abstractmethod
    def peek(self):
        "Return the minimum item in the queue."
 
    @abstractmethod
    def decrease_key(self, old_item, new_item):
        "Replace old_item with new_item, where new_item < old_item."
 
 
class binary_heap(priority_queue):
 
#
# Original code by Kevin O'Connor,
# augmented by Tim Peters and Raymond Hettinger,
# modified by Chungmin Lee to add decrease_key() opereation.
#
# See the Python source code of heapq module in the standard library
# for the unmodified code.
#
 
    def __init__(self):
        self._items = []
        self._indexes_by_item = {}
 
    def __len__(self):
        return len(self._items)
 
    def __contains__(self, item):
        return item in self._indexes_by_item
 
    def add(self, item):
        if item in self._indexes_by_item:
            return
        items = self._items
        items.append(item)
        self._sift_up(0, len(items) - 1)
 
    def pop(self):
        items = self._items
        if not items:
            raise KeyError('pop from an empty heap')
        last_item = items.pop()
        if items:
            item = items[0]
            items[0] = last_item
            self._sift_down(0)
        else:
            item = last_item
        del self._indexes_by_item[item]
        return item
 
    def peek(self):
        items = self._items
        if not items:
            raise KeyError('peek from an empty heap')
        return items[0]
 
    def decrease_key(self, old_item, new_item):
        indexes_by_item = self._indexes_by_item
        if old_item not in indexes_by_item:
            raise KeyError('{0} not in a heap'.format(old_item))
        if new_item in indexes_by_item:
            raise KeyError('{0} in a heap'.format(new_item))
        if old_item <= new_item:
            raise ValueError('{0} <= {1}'.format(old_item, new_item))
        i = indexes_by_item.pop(old_item)
        self._items[i] = new_item
        self._sift_up(0, i)
 
    def _sift_up(self, start, i):
        items = self._items
        indexes_by_item = self._indexes_by_item
        item = items[i]
        while start < i:
            p = (i - 1) >> 1
            parent = items[p]
            if item < parent:
                items[i] = parent
                indexes_by_item[parent] = i
                i = p
            else:
                break
        items[i] = item
        indexes_by_item[item] = i
 
    def _sift_down(self, i):
        items = self._items
        indexes_by_item = self._indexes_by_item
        end = len(items)
        start = i
        item = items[i]
        c = 2 * i + 1
        while c < end:
            r = c + 1
            child = items[c]
            if r < end:
                right_child = items[r]
                if right_child < child:
                    c = r
                    child = right_child
            items[i] = child
            indexes_by_item[child] = i
            i = c
            c = 2 * i + 1
        items[i] = item
        indexes_by_item[item] = i
        self._sift_up(start, i)
 
 
class fibonacci_heap(priority_queue):
 
    def __init__(self):
        self._len = 0
        self._min = None
        self._trees_by_item = {}
 
    def __len__(self):
        return self._len
 
    def __contains__(self, item):
        return item in self._trees_by_item
 
    def add(self, item):
        trees_by_item = self._trees_by_item
        if item in trees_by_item:
            return
        t = fibonacci_heap._tree(item)
        self._add_tree(t)
        self._len += 1
        trees_by_item[item] = t
 
    def pop(self):
        min = self._min
        if min is None:
            raise KeyError('pop from an empty heap')
        item = min.item
        child = min.child
        min.child = None
        self._delete_tree(min)
        if child is not None:
            start = child
            while 1:
                next = child.right
                child.parent = None
                self._add_tree(child)
                if next is start:
                    break
                child = next
        if self._min is not None:
            self._consolidate_trees()
        self._len -= 1
        del self._trees_by_item[item]
        return item
 
    def peek(self):
        min = self._min
        if min is None:
            raise KeyError('peek from an empty heap')
        return min.item
 
    def decrease_key(self, old_item, new_item):
        trees_by_item = self._trees_by_item
        if old_item not in trees_by_item:
            raise KeyError('{0} not in a heap'.format(old_item))
        if new_item in trees_by_item:
            raise KeyError('{0} in a heap'.format(new_item))
        if old_item <= new_item:
            raise ValueError('{0} <= {1}'.format(old_item, new_item))
        current = trees_by_item.pop(old_item)
        current.item = new_item
        trees_by_item[new_item] = current
        parent = current.parent
        if parent is not None and new_item < parent.item:
            while parent is not None:
                child = parent.child
                if child.right is child:
                    parent.child = None
                else:
                    while child is not current:
                        child = child.right
                    child.right.left = child.left
                    child.left.right = child.right
                    if parent.child is child:
                        parent.child = child.right
                parent.degree -= 1
                current.parent = None
                current.marked = False
                self._add_tree(current)
                current = parent
                parent = parent.parent
                if not current.marked:
                    break
            if parent is not None:
                current.marked = True
        if parent is None and new_item < self._min.item:
            self._min = current
 
    def _add_tree(self, tree):
        min = self._min
        if min is None:
            tree.right = tree
            tree.left = tree
            self._min = tree
        else:
            tree.right = min
            tree.left = min.left
            min.left.right = tree
            min.left = tree
            if tree.item < min.item:
                self._min = tree
 
    def _delete_tree(self, tree):
        if tree.right is tree:
            self._min = None
        else:
            tree.right.left = tree.left
            tree.left.right = tree.right
            if self._min is tree:
                self._min = self._update_min(tree.right)
 
    def _update_min(self, start):
        min = start
        current = start.right
        while current is not start:
            if current.item < min.item:
                min = current
            current = current.right
        return min
 
    def _consolidate_trees(self):
        trees_by_degree = {}
        start = self._min
        end = start.left
        current = start
        while 1:
            d = current.degree
            next = current.right
            if d not in trees_by_degree:
                trees_by_degree[d] = current
            else:
                merged = current
                while d in trees_by_degree:
                    t1 = merged
                    t2 = trees_by_degree[d]
                    if t2.item < t1.item:
                        t1, t2 = t2, t1
                    self._delete_tree(t2)
                    child = t1.child
                    if child is None:
                        t1.child = t2
                        t2.right = t2
                        t2.left = t2
                    else:
                        t2.right = child
                        t2.left = child.left
                        child.left.right = t2
                        child.left = t2
                    t1.degree += 1
                    t2.parent = t1
                    merged = t1
                    del trees_by_degree[d]
                    d = merged.degree
                trees_by_degree[d] = merged
            if current is end:
                break
            current = next
 
    class _tree(object):
 
        def __init__(self, item):
            self.item = item
            self.parent = None
            self.right = None
            self.left = None
            self.child = None
            self.degree = 0
            self.marked = False