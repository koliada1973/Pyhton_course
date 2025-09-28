import multiprocessing

# def test(name):
#     print(f'here {name}')
#
# if __name__ == '__main__':
#     processes = []
#     for i in range(5):
#         t = multiprocessing.Process(target=test, args=(i,))
#         processes.append(t)
#         t.start()
#
#     for process in processes:
#         process.join()



import os

# def test(name):
#     print(f'here {name}, process: {os.getpid()}, parent process: {os.getppid()}')
#
# if __name__ == '__main__':
#     processes = []
#     for i in range(5):
#         t = multiprocessing.Process(target=test, args=(i,))
#         processes.append(t)
#         t.start()
#
#     for process in processes:
#         process.join()


# result = []
#
# def square_list(mylist):
#     global result
#     for num in mylist:
#         result.append(num * num)
#     print("Result(in process p1): {}".format(result))
#
# if __name__ == '__main__':
#     temp = [1, 2, 3, 4]
#
#     p1 = multiprocessing.Process(target=square_list, args=(temp,))
#     p1.start()
#     p1.join()
#
#     print(result)

# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]
#
# if __name__ == '__main__':
#     num = multiprocessing.Value('d', 0.0)
#     arr = multiprocessing.Array('i', range(10))
#
#     print(num.value)
#     print(arr)
#
#     p = multiprocessing.Process(target=f, args=(num, arr))
#     p.start()
#     p.join()
#
#     print(num.value)
#     print(arr[:])


# def square_list(mylist, res):
#     global result
#     for ind, num in enumerate(mylist):
#         res[ind]= num * num
#     print("Result(in process p1): {}".format(result[:]))
#
# if __name__ == "__main__":
#     temp = [1, 2, 3, 4]
#     result = multiprocessing.Array('i', 4)
#
#     p1 = multiprocessing.Process(target=square_list, args=(temp, result))
#     p1.start()
#     p1.join()
#
#     print(result[:])


import time
# Не завжди працює...
# def square_list(mylist, q):
#     for num in mylist:
#         q.put(num * num)
#
# def read_from_queue(q):
#     time.sleep(0.1)     # Рішення!!
#     while not q.empty():
#         print(q.get())
#
# if __name__ == '__main__':
#     temp = [1, 2, 3, 4]
#     q = multiprocessing.Queue()
#     p1 = multiprocessing.Process(target=square_list, args=(temp, q))
#     p2 = multiprocessing.Process(target=read_from_queue, args=(q,))
#
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

# def sender(conn, msgs):
#     for msg in msgs:
#         conn.send(msg)
#         print(f"Sent the message: {msg} from process {os.getpid()}")
#     conn.close()
#
#
# def receiver(conn):
#     while True:
#         msg = conn.recv()
#         if msg == "END":
#             break
#         print(f"Received the message: {msg} in process {os.getpid()}")
#
# if __name__ == '__main__':
#     msgs = ["hello", "hey", "hru?", "END"]
#
#     # creating a pipe
#     parent_conn, child_conn = multiprocessing.Pipe()
#
#     # creating new processes
#     p1 = multiprocessing.Process(target=sender, args=(parent_conn, msgs))
#     p2 = multiprocessing.Process(target=receiver, args=(child_conn,))
#
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()

def f(x):
    return x * x

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        result = pool.apply_async(f, (10,))  # evaluate "f(10)" asynchronously in a single process
        print(result.get(timeout=1))  # prints "100" unless your computer is *very* slow

        print(pool.map(f, range(10)))  # prints "[0, 1, 4,..., 81]"

        it = pool.imap(f, range(10))
        print(next(it))  # prints "0"
        print(next(it))  # prints "1"
        print(it.next(timeout=1))  # prints "4" unless your computer is *very* slow

        # result = pool.apply_async(time.sleep, (10,))
        # print(result.get(timeout=1))  # raises multiprocessing.TimeoutError