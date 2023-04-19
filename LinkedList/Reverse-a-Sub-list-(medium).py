# Reverse a Sub-list (medium)
# https://www.educative.io/courses/grokking-the-coding-interview/qVANqMonoB2
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
  count = 0
  node = head
  while count < p-2:
    node = node.next
    count +=1
  pre, cur = None, node.next
  while cur and count < q-1:
    count += 1
    temp = cur.next
    cur.next = pre
    pre = cur
    cur = temp
  pre.print_list()
  cur.print_list()
  pre.next = temp
  head.next = pre
  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()
