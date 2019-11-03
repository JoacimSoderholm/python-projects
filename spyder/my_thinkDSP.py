# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:22:14 2019

@author: smoeg
"""

import thinkdsp as dsp
import sys
import matplotlib.pyplot as plt
import numpy as np
Pi = 3.14
winamp = '\"C:\\Program Files (x86)\\Winamp\\winamp.exe\"'


def playfile(filename):
    '''stores wave to filename and plays it using winamp, then returns a dsp wav file'''
    dsp.play_wave(filename, winamp)
    return dsp.read_wave(filename)


def writefile(wave, filename):
    wave.write(filename)

class Fib:
    '''A fibonacci sequence'''
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


class Think:
    '''Experimentation functions exploring thinkdsp'''
    def makingwaves(self):
        '''trying to make waves'''
        cos_sig = dsp.CosSignal(freq=440, amp=1.0, offset=0)
        sin_sig = dsp.SinSignal(freq=880, amp=0.5, offset=dsp.PI2)
        sig = dsp.SinSignal(660, 1.0, 0)

        mix = sin_sig + cos_sig + sig
        # mix.plot()
        # list = print(range(10))
        # print(list[4])
        # print(list)
        # plt.plot(range(mix.evaluate(3)), 'x')
        wave = mix.make_wave(duration=0.005, start=0, framerate=11025)
        plt.plot(wave.ys, 'x')
        # plt.plot
        # plt.plot(wave.ys, 'o')
        
        for n in range(5):
            print(wave.ys[n])

        
        #wave.play()
        # spectrum=wave.make_spectrum()
        # spectrum.plot()
        # violin_wave = dsp.read_wave('input.wav')
        # plt.plot()
        # plt.plot(range(10), 'x')

    def wa(self, wave, filename):
        '''stores wave to filename and plays it using winamp, then returns a dsp wav file'''
        wave.write(filename)
        dsp.read_wave(filename)
        dsp.play_wave(filename, winamp)
        # file.plot()
        return

    def Exercise1(self):
        file = wa('mario.wav')
        spectrum = file.make_spectrum()
        # spectrum.plot()
        spectrum.high_pass(1000, 0.01)
        file = spectrum.make_wave()
        file.write('mario2.wav')
        self.wa('mario2.wav')
        cos_sig = dsp.CosSignal(freq=440, amp=1.0, offset=0)
        sin_sig = dsp.SinSignal(freq=880, amp=0.5, offset=0)
        sig = dsp.SinSignal(660, 1.0, 0)
        mix = sin_sig + cos_sig + sig
        # mix.plot()
        w = mix.make_wave(3, 0, 11025)
        wa(w, 'mix.wav')

    def Exercise2(self):
        pass


class Sawtooth(dsp.Signal):

    'This is a docstring for Sawtooth?'

    def __init__(self, freq=440, amp=1.0, offset=0, func=np.sin):
        print('Creating Sawstring')
        dsp.Signal.__init__(self)
        self.freq = freq
        self.amp = amp
        self.offset = offset
        self.func = np.sin

    def evaluate(self, ts):
        """Evaluates the signal at the given times.
        ts: float array of times
        returns: float wave array
        """
        # cycles = self.freq * ts + self.offset / dsp.PI2
        # frac, _ = np.modf(cycles)
        # ys = self.amp * np.sign(dsp.unbias(frac))
        ts = np.asarray(ts)
        cycles = self.freq * ts + self.offset / dsp.PI2
        frac, _ = np.modf(cycles)
        # ys = np.abs(frac - 0.5)
        ys = dsp.normalize(dsp.unbias(frac), self.amp)
        return ys


def __main__():
    pass


if __name__ == '__main__':
    fib = Fib(1000)
    for n in Fib(1000):
        print(n, end=' ')
    t = Think()
    triangle = dsp.TriangleSignal(20)
    #triangle.plot()
    saw = Sawtooth(20)
    # saw.plot()
    wave = saw.make_wave()
    s = wave.make_spectrum()
    #s.plot()
    
    #square = dsp.SquareSignal(1000)
    sig = dsp.SquareSignal(1100, 1, 0)
    wv = sig.make_wave(framerate=10000)
    # writefile(wv, 'square.wav')
    # playfile('square.wav')
    sp = wv.make_spectrum()
    fs = sp.fs
    
    sig = dsp.TriangleSignal(440)
    wv = sig.make_wave(1, 0, 11025)
    sp = wv.make_spectrum()

    writefile(wv, 'tri.wav')
    playfile('tri.wav')
    
    print(sp.hs[0])
    sp.plot()
    
    sp.hs[0] = 100
    wv = sp.make_wave()

    writefile(wv, 'new.wav')
    playfile('new.wav')    
    sp.plot()
    # exit    
    # t.Exercise1()
    #t.Exercise2()
    #t.makingwaves()
    
