# IOCTF Usage Document

ioctf is a io package writen by pure python3 in ctf competation.

## Install

```shell
pip install ioctf
```

## Usage

### io_base

`info()` return the info about target.

`recv(count)` return the content received from target,the count is how many you want bytes you want to received.

`recvuntil(data)` receive bytes until meet the data, return all bytes include data.

`recvline(data)` receive bytes until meet a '\n', return all bytes include data.

`send(data)` send the data bytes to target, return the number of bytes sended successfully.

`sendline(data)` just send data with a line in the end.

`close()` close target.

`interactive()` interactive with the target.

### remote

`remote(io_base)` is a class for connecting with remote server.The differnce between socket lib in python3 and remote here is that remote supply more feathers for io with remote server.

```python
from ioctf import *
con = remote("123.123.123.123",8080)
con.sendline(b"Hello Alice!")
assert con.recvuntil(b"Bob!")==b"Hello Bob!"
con.interactive()
```

### process

`process(io_base)` is same as remote class but for local process.

```python
from ioctf import *
con = process("./keyCrack")
con.recvuntil("Plz input the password:")
con.sendline(b"zhimakaimen!")
con.interactive()
```
