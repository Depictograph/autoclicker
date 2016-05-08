
# coding: utf-8

# In[ ]:

from pymouse import PyMouse
from pymouse import PyMouseEvent
import time
import random


# In[ ]:

class Recorder(PyMouseEvent):
    def __init__(self):
        self.reset()
    def click(self, x, y, button, press):
        if button == 3:
            self.end()
        if not self.stopped()
        self.timer.start()
        if self.timer.started():
            waittime = self.timer.stop()
            wait = Wait(waittime)
            self.moves.append(wait)
        click = Click(self.m, x, y, button, press)
        self.moves.append(click)

    def end(self):
        print "Stopping"
        self.stopped = True
        self.stop()
    def move(self, x, y):
        if self.timer.started():
            waittime = self.timer.stop()
            wait = Wait(waittime)
            self.moves.append(wait)
        move = Move(self.m, x, y)
        self.moves.append(move)
        self.timer.start()
    def reset(self):
        PyMouseEvent.__init__(self, capture=False, capture_move=False)
        self.m = PyMouse()
        self.timer = Timer()
        self.moves = []
        self.stopped = False
    def replay(self, times):
        if not self.stopped:
            print 'Must stop recording first'
            return
        print 'Replaying...'
        while times > 0:
            print 'Times left ' + str(times)
            for e in self.moves:
                e.run()
            times -= 1
        print "Done"

class Timer():
    def __init__(self):
        self.t = -1
    def start(self):
        self.t = time.time()
    def stop(self, delay=1.2):
        st = time.time()
        elapsed = (st - self.t) * delay
        self.t = -1
        return elapsed
    def started(self):
        return self.t != -1
class Event():
    def __init__(self, m, x, y, button, press):
        self.m = m
        self.x = x
        self.y = y
        self.button = button
        self.press = press
class Click(Event):
    def __init__(self, m, x, y, button, press):
        Event.__init__(self, m, x, y, button, press)
    def run(self):
        self.m.click(self.x, self.y, self.button)
        
class Move(Event):
    def __init__(self, m, x, y):
        Event.__init__(self, m, x, y, None, None)
    def run(self):
        self.m.move(self.x, self.y)
class Wait():
    def __init__(self, t):
        self.time = t
    def run(self):
        time.sleep(self.time)
        
    
        
        
        
    


# In[ ]:

r = Recorder()
r.start()

