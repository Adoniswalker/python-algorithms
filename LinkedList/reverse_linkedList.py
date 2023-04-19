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


def reverse(head):
  pre = None
  cur = head
  while cur:
    next = cur.next
    cur.next = pre
    pre = cur
    cur = next
  return pre


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()

if __name__ == '__main__':
    main()

# class TestSolution(unittest.TestCase):
#     def test_solution(self):
#         self.assertEqual(solution([4, 5, 6, 7]), [7, 6, 5, 4])


# 4 -> 5 -> 6 -> 7 -> null
# pre = null
# cur = head
# loop
#   prev = cur
#   cur.next = pre
#   cur = head = prev
#   4->