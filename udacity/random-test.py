#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 11/27/13 09:13:56 (CST)
# Modified Time: 11/27/13 09:31:28 (CST)
def random_test():
    N = 4
    add = 0
    remove = 0
    addFull = 0
    removeEmpty = 0
    q = Queue(N)
    q.checkRep()
    l = []
    for i in range(100000):
        if (random.random() <0.5):
            z = random.randint(0,1000000)
            res = q.enqueue(z)
            q.checkRep()
            if res:
                l.append(z)
                add += 1
            else:
                assert len(l) == N
                assert q.full()
                q.checkRep()
                addFull += 1
        else:
            dequeued = q.dequeue()
            q.checkRep()
            if dequeued is None:
                assert len(l) == 0
                assert q.empty()
                q.checkRep()
                removeEmpty +=1
            else:
                expected_value = l.pop(0)
                assert dequeued == expected_value
                remove += 1
    while True:
        res = q.dequeue()
        q.checkRep()
        if res is None:
            break
        z = l.pop(0)
        assert z == res
    assert len(l) == 0

    print "adds: " + str(add)
    print "adds to a full queue: " + str(addFull)
    print "removes: " + str(remove)
    print "removes from an empty queue: " + str(removeEmpty)
