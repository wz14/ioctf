#! /usr/bin/python3
# coding: utf-8
# mail:zhuowangy2k@outlook.com
# a simple io package for ctf use python3

import threading, sys, os, socket, subprocess

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

    def interactive(self):
        print('[+] interative with',self.info())
        def recv_thread():
            while True:
                try:
                    cur = self.recv(1)
                    sys.stdout.write(cur)
                    sys.stdout.flush()
                except EOFError:
                    print('Got EOF while reading in interactive')
                    break
        t = threading.Thread(target = recv_thread,daemon=True)
        t.start()
        while True:
            print('$', end='')
            data = ''
            while True:
                d = sys.stdin.read(1)
                data += d
                if d == b'\n':
                    break
            self.send(data)

class remote(io_base):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip,port))
    
    def info(self):
        return self.ip+":"+str(self.port)

    def send(self,data:bytes):
        return self.sock.send(data)
     
    def recv(self, count):
        return self.sock.recv(count)

    def close(self):
        self.sock.close()
        
    
class process:
    def __init__(self, cmd):
        self.pipe = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE)

    def send(self, data):
        return self.pipe.stdin.write(data)

    def recv(self, count):
        return self.pipe.stdout.read(count)

    def close(self):
        try:
            self.pipe.kill()
        except OSError:
            pass
