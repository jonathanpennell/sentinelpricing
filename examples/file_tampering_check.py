

import io

from sentinelpricing.models.md5checker import MD5Checker


def create_in_memory_file():
    f = io.BytesIO()

    f.write(b"a,b,rate\n")
    f.write(b"1,4,7\n")
    f.write(b"2,5,8\n")
    f.write(b"3,6,9\n")
    return f

f = create_in_memory_file()
assert MD5Checker(f) == "d41d8cd98f00b204e9800998ecf8427e"
