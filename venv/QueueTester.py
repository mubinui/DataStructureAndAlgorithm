import Queue as q

Queue_q = q.Queue() # Define class for creating an object
print(Queue_q.dequeue())
print(Queue_q.isEmpty())
Queue_q.enqueue(10)
Queue_q.enqueue(20)
Queue_q.enqueue(30)
Queue_q.enqueue(40)
Queue_q.enqueue(50)
Queue_q.enqueue(60)
print(Queue_q.isEmpty())

x = Queue_q.size()
print(x)
y = Queue_q.dequeue()
print(y)
z = Queue_q.size()
print(z)
a = Queue_q.peek()
print(a)
print(Queue_q.dequeue())
Queue_q.printList()