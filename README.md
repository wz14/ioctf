# IOCTF

A simple io package for ctf using python3.

## Motivation

Pwntools is a great tool for ctf competation.But sometimes it is not work for me using python3.What I just need is io communication with remote server easily.So I write this package using pure python3.You can install it using just one command and use easily as pwntools.

## Install

Just one step.

```shell
pip install ioctf
```

## Usage

```python
from ioctf import *
con = remote("123.123.123.123",8080)
con.sendline(b"Hello Alice!")
assert con.recvuntil(b"Bob!")==b"Hello Bob!"
con.interactive()
```

More usage in [here](https://github.com/WangZhuo2000/ioctf/blob/master/doc/ioctf_usage.md).

## Contribute

The python code is easy to modify. I hope you can pull request more feathers about io in ctf and talk to me.

## License

The source code is licensed under GPL v3. License is available [here](https://github.com/WangZhuo2000/ioctf/blob/master/LICENSE)
