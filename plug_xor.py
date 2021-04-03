# pylint: disable=import-error
from mate import add_plugins, command


def sxor(s1, s2):
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


@command(option="xor")
def bitwise_string_xor(self, str1, str2):
    """A bitwise xor operation for two strings."""
    return {"result": sxor(str1, str2).__repr__()}


add_plugins(modules=[bitwise_string_xor])
