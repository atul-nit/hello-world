"""ffff"""
"""Strings and bytes are not directly interchangeable"""
""" Strings contain unicode, bytes are raw 8-bit values """


def main():
    # define a byte
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    # define a string
    s = "This is a string"
    print(s)

    # Try combining them
    # print(s+b)   # error.can't combine bytes and string

    # Bytes and Strings are need to be properly encoded and decoded
    # before you can work upon them

    # decoding bytes to str
    s2 = b.decode('utf-8')
    print(type(s2))
    print(s + s2)  # works as s and s2 are str type

    # encoding str to bytes
    b2 = s.encode('utf-8')
    print(type(b2))
    print(b + b2)  # works as b and b2 are bytes type

    # encode a string with UTF-32
    b3 = s.encode('utf-32')
    print(b3)


main()