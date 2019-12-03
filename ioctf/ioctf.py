#! /usr/bin/python3
# coding: utf-8
# mail:zhuowangy2k@outlook.com
# a simple io package for ctf use python3

import threading, sys, os, socket, subprocess

MAX_RECV=10000 # define the max recv once in interactive mode.

class io_base():

    def __init__(self):
        pass
    
    def info(self):
        pass

    def send(self,data:bytes)->int:
        pass

    def recv(self,count:int)->bytes:
        pass
    
    def close(self):
        pass
    
    def sendline(self, data:bytes)->int:
        return self.send(data + b'\n')

    def recvuntil(self, data:bytes)->bytes:
        buf = b''
        while True:
            buf += self.recv(1)
            if len(buf)<len(data):
                continue
            if buf[-len(data):]==data:
                return buf
            return buf

    def recvline(self)->bytes:
        return self.recvuntil(b"\n")

    def isdebug(self)->bool:
        pass

    def interactive(self):
        print('[+] interative with',self.info())
        def recv_thread():
            while True:
                try:
                    cur = self.recv(MAX_RECV)
                    if self.isdebug():
                        print("[recv]:",str(cur))
                    sys.stdout.write(cur.decode()) # TODO:utf-8 is not enough.
                    sys.stdout.flush()
                except EOFError:
                    print('Got EOF while reading in interactive')
                    break
        t = threading.Thread(target = recv_thread,daemon=True)
        t.start()
        while True:
            data = ''
            while True:
                d = sys.stdin.read(1)
                if self.isdebug():
                    print("[send]:",d)
                data += d
                if d == '\n':
                    break
            self.send(data.encode())

class remote(io_base):

    def __init__(self, ip, port,debug=False):
        self.ip = ip
        self.port = port
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip,port))
        self.debug = debug
    
    def info(self):
        return self.ip+":"+str(self.port)

    def send(self,data:bytes):
        return self.sock.send(data)
     
    def recv(self, count):
        return self.sock.recv(count)

    def close(self):
        self.sock.close()
        
    
class process:
    def __init__(self, cmd,debug=False):
        self.pipe = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        self.debug = debug

    def send(self, data):
        return self.pipe.stdin.write(data)

    def recv(self, count):
        return self.pipe.stdout.read(count)

    def close(self):
        try:
            self.pipe.kill()
        except OSError:
            pass
