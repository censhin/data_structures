#!/usr/bin/env python

class Node():

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, node):
        self.next_node = node

class LinkedList():

    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head == None

    def get_count(self):
        return self.count

    def insert(self, value):
        new_node = Node(value)
        new_node.set_next(self.head)
        self.head = new_node
        self.count+=1

    def delete(self, value):
        current = self.head
        previous = None
        found = False
        while found is False:
            if current.get_value() == value:
                found = True
                previous.set_next(current.get_next())
                current.set_next(None)
                self.count-=1
            else:
                previous = current
                current = current.get_next()

    def search(self, value):
        current = self.head
        found = False
        while found is False:
            if current.get_value() == None:
                return "Could not find the given value."
            elif current.get_value() == value:
                found = True
            else:
                current = current.get_next()
        return current

if __name__ == '__main__':
    ll = LinkedList()

    print "Node is empty: {}".format(ll.is_empty())
    for n in xrange(5):
        ll.insert(n)
    print "Node is empty: {}".format(ll.is_empty())

    for n in xrange(5):
        x = ll.search(n)
        print "Node at {} with a value of {}".format(x, x.get_value())

    print "List has {} nodes".format(ll.get_count())
    ll.delete(2)
    print "List has {} nodes".format(ll.get_count())
    ll.delete(3)
    print "List has {} nodes".format(ll.get_count())
