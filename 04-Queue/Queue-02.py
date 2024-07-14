w
inp = input("Enter people and time : ").split(" ")
a, b = inp
lst = list(a)

q = Queue(lst)
q1 = Queue()
q2 = Queue()
b = int(b)
for i in range(b):
    if not q1.is_empty() and not i%3:
        q1.pop()
    if not q2.is_empty() and  i%2:
        q2.pop()
    if q1.size() < 5 and not q.is_empty():
        out = q.pop()
        q1.enqueue(out)
    elif q2.size() < 5 and not q.is_empty():
        out = q.pop()
        q2.enqueue(out)
    print(f"{i+1} {q} {q1} {q2}")



    # print(f"\n+++{i} \n{q}\n{q1}\n{q2}+++\n")
