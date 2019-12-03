#! /usr/bin/python3
# coding: utf-8
# mail:zhuowangy2k@outlook.com
# test file for simple ioctf package

from ioctf import *

io = remote("188.131.177.11",9191)
io.sendline(b"Hello Alice!")
assert b"Hello Bob!" == io.recv(10)
io.close()
