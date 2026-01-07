import io

from sentinelpricing.models.md5hash import MD5Hash


def create_in_memory_file():
    f = io.BytesIO()

    f.write(b"a,b,rate\n")
    f.write(b"1,4,7\n")
    f.write(b"2,5,8\n")
    f.write(b"3,6,9\n")
    return f


data_file = create_in_memory_file()
assert MD5Hash(data_file) == "d41d8cd98f00b204e9800998ecf8427e"
