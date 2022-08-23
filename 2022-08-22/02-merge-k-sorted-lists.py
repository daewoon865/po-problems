class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next
def mergeKLists(self, lists: list):
  bucket = dict()
  for i in range (-1 * (pow(-10,4)), (pow(10,4)+1)):
    bucket[i] = 0

  for j in lists:
    while j:
      bucket[j.val] = bucket[j.val] + 1
      j = j.next

  builder = ListNode()
  points = builder

  for k,v in bucket.items():
    for i in range (1, v+1):
      tmp = ListNode()
      tmp.val = k
      builder.next = tmp
      builder = builder.next            

  return points.next
