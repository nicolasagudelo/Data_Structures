from cgi import test
from os import remove


class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
    

class DoublyLinkedList:
    
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def stringify_list(self):
        string_list = "<head> "
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + " "
            current_node = current_node.get_next_node()
        return string_list + '<Tail>'
    
    def add_to_head(self, new_value):

        new_head = Node(new_value)
        current_head = self.head_node

        if current_head:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        self.head_node = new_head

        if self.tail_node is None:
            self.tail_node = new_head
    
    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node

        if current_tail:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        self.tail_node = new_tail

        if self.head_node is None:
            self.head_node = new_tail
    
    def remove_head(self):

        removed_head = self.head_node
        
        if removed_head == None:
            return None

        self.head_node = removed_head.get_next_node()
        
        if self.head_node != None:
            self.head_node.set_prev_node(None)

        if removed_head == self.tail_node:
            self.remove_tail()
        return removed_head.get_value()
        
    def remove_tail(self):
        
        removed_tail = self.tail_node
        
        if removed_tail == None:
            return None
        
        self.tail_node = removed_tail.get_prev_node()
        
        if self.tail_node != None:
            self.tail_node.set_next_node(None)

        if removed_tail == self.head_node:
            self.remove_head()
        return removed_tail.get_value()

    def remove_by_value(self, value):
        current_node = self.head_node
        while current_node:
            if current_node.value == value:
                if current_node == self.head_node:
                    self.remove_head()
                elif current_node == self.tail_node:
                    self.remove_tail()
                else:
                    current_node.get_prev_node().set_next_node(current_node.get_next_node())
                    current_node.get_next_node().set_prev_node(current_node.get_prev_node())
                    return current_node.get_value()
            current_node = current_node.get_next_node()
        return None


def generate_test_linked_list(start):
  linked_list = DoublyLinkedList()
  for i in range(start, 0, -1):
    linked_list.add_to_head(i)
  return linked_list

def generate_test_linked_list_tail(end):
  linked_list = DoublyLinkedList()
  for i in range(1, end + 1, 1):
    linked_list.add_to_tail(i)
  return linked_list

# Creating a Double Linked List from 1 to 10
test_list= generate_test_linked_list(10)
test_list2 = generate_test_linked_list_tail(10)
print(test_list.stringify_list())
print(test_list2.stringify_list())



# Testing remove_head method
test_list.remove_head()
print(test_list.stringify_list())

# Testing remove_tail method
test_list.remove_tail()
print(test_list.stringify_list())

# Testing removing by value
test_list.remove_by_value(5)
print(test_list.stringify_list())

del test_list, test_list2

# Using a double linked list to create a subway system.

subway = DoublyLinkedList()
subway.add_to_head('Times Square')
subway.add_to_head('Grand Central')
subway.add_to_head('Central Park')

print(subway.stringify_list())

subway.add_to_tail('Penn Station')
subway.add_to_tail('Wall Street')
subway.add_to_tail('Brooklyn Bridge')

print(subway.stringify_list())

subway.remove_head()
subway.remove_tail()

print(subway.stringify_list())

subway.remove_by_value('Times Square')

print(subway.stringify_list())