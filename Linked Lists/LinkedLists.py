class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    if value == None and self.head_node == None:
      self.head_node = None
    else:
      self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = "<head> "
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + " "
      current_node = current_node.get_next_node()
    return string_list + '<Tail>'
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

""" 
Complexity of the nth_last_node():

Time = O(n) since we must iterate through the entire list once.
Space = O(1) since we always use three variables no matter what the size of the list is. (Two pointers and one counter)


"""

def nth_last_node(linked_list, n):
  nth_last_pointer = None
  tail_pointer = linked_list.head_node
  count = 1

  while tail_pointer is not None:
    tail_pointer = tail_pointer.get_next_node()
    count += 1

    if count >= n + 1:
      if nth_last_pointer == None:
        nth_last_pointer = linked_list.head_node
      else:
        nth_last_pointer = nth_last_pointer.get_next_node()
  return nth_last_pointer

def generate_test_linked_list(start):
  linked_list = LinkedList()
  for i in range(start, 0, -1):
    linked_list.insert_beginning(i)
  return linked_list

# Use this to test your nth_last_node function:
# test_list = generate_test_linked_list(50)
# print(test_list.stringify_list())
# nth_last = nth_last_node(test_list, 4)
# print(nth_last.value)

"""
Complexity of the swap_nodes() function

Time: O(n) since each while loop has a O(n) runtime and constans are dropped.
Space: O(1) since we always use 4 variables regardless of the input.

"""

def swap_nodes(input_list, val1, val2):
  print(f'Swapping {val1} with {val2}')

  node1_prev = None
  node2_prev = None
  node1 = input_list.head_node
  node2 = input_list.head_node

  if val1 == val2:
    print("Elements are the same - no swap needed")
    return

  while node1 is not None:
    if node1.get_value() == val1:
      break
    node1_prev = node1
    node1 = node1.get_next_node()

  while node2 is not None:
    if node2.get_value() == val2:
      break
    node2_prev = node2
    node2 = node2.get_next_node()

  if (node1 is None or node2 is None):
    print("Swap not possible - one or more element is not in the list")
    return

  if node1_prev is None:
    input_list.head_node = node2
  else:
    node1_prev.set_next_node(node2)

  if node2_prev is None:
    input_list.head_node = node1
  else:
    node2_prev.set_next_node(node1)

  temp = node1.get_next_node()
  node1.set_next_node(node2.get_next_node())
  node2.set_next_node(temp)


# Use this to test your swap_nodes function:

# ll = generate_test_linked_list(10)
# print(ll.stringify_list())
# swap_nodes(ll, 9, 1)
# print(ll.stringify_list())

"""
Complexity of the swap_nodes() function

Time: O(n) since again we have to iterate through the whole list once.
Space: O(1) since we always use 2 variables no matter what.

"""

def find_middle(linked_list):
  fast_pointer = linked_list.head_node
  slow_pointer = linked_list.head_node
  while fast_pointer:
    fast_pointer = fast_pointer.next_node
    if fast_pointer is not None:
      fast_pointer = fast_pointer.next_node
      slow_pointer = slow_pointer.next_node
  return(slow_pointer)

# Use this to test your code:
test_list = generate_test_linked_list(7)
print(test_list.stringify_list())
middle_node = find_middle(test_list)
print(middle_node.value)