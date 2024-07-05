from multiprocessing import Process


def test1():
    print("process 1")


def test2():
    print("process 2")


process1 = Process(target=test1())
process2 = Process(target=test2())

process2.start()
process1.start()

process1.join()
process2.join()

