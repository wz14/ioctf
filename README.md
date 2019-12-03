# IOCTF

A simple io package for ctf using python3.

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
assert con.recv(10)==b"Hello Bob!"
```

## License

The source code is licensed under GPL v3. License is available [here](https://github.com/WangZhuo2000/ioctf/blob/master/LICENSE)
