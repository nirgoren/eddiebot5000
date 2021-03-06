from time import perf_counter
import os
from ctypes import *

# for python 3.8 and up:
# os.add_dll_directory(os.getcwd())

_vcontroller = cdll.LoadLibrary('vcontroller.dll')

eps = 0.001


class Clock:
    def __init__(self, fps):
        self.frame_length = 1 / fps
        self.next = perf_counter() + self.frame_length

    def sleep(self):
        while perf_counter() < self.next:
            _vcontroller.wait()
            pass
        # if perf_counter() < self.next:
        #     _vcontroller.nanosleep(int(((self.next-perf_counter()) * 10000)))
        self.next += self.frame_length + int(perf_counter()-self.next)*self.frame_length
        # self.next = perf_counter() + self.frame_length

    def reset(self):
        self.next = perf_counter() + self.frame_length
