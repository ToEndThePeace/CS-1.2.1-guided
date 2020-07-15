import time
from singly_linked_lists import LinkedList

n = 100000

ll = LinkedList()
l = []

start_time = time.time()
for i in range(n):
    ll.append(i)
end_time = time.time()
print(f"Linked list implementation took {end_time - start_time}")

start_time = time.time()
for i in range(n):
    l.append(i)
end_time = time.time()
print(f"Array list implementation took {end_time - start_time}")

start_time = time.time()
for i in range(n):
    ll.remove_head()
end_time = time.time()
print(f"Linked list implementation took {end_time - start_time}")

start_time = time.time()
for i in range(n):
    l.pop(0)
end_time = time.time()
print(f"Array list implementation took {end_time - start_time}")
