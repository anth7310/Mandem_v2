CHARS = (
    (b'\xc3\xa2\xc2\x80\xc2\x99', b'\''),
    # (b'\xc3\xb0\xc2\x9f\xc2\xa4\xc2\x94', '🤔')
    # ('\xc3\xa9', 'e'),
    # ('\xe2\x80\x90', '-'),
    # ('\xe2\x80\x91', '-'),
    # ('\xe2\x80\x92', '-'),
    # ('\xe2\x80\x93', '-'),
    # ('\xe2\x80\x94', '-'),
    # ('\xe2\x80\x94', '-'),
    # ('\xe2\x80\x98', "'"),
    # ('\xe2\x80\x9b', "'"),
    # ('\xe2\x80\x9c', '"'),
    # ('\xe2\x80\x9c', '"'),
    # ('\xe2\x80\x9d', '"'),
    # ('\xe2\x80\x9e', '"'),
    # ('\xe2\x80\x9f', '"'),
    # ('\xe2\x80\xa6', '...'),
    # ('\xe2\x80\xb2', "'"),
    # ('\xe2\x80\xb3', "'"),
    # ('\xe2\x80\xb4', "'"),
    # ('\xe2\x80\xb5', "'"),
    # ('\xe2\x80\xb6', "'"),
    # ('\xe2\x80\xb7', "'"),
    # ('\xe2\x81\xba', "+"),
    # ('\xe2\x81\xbb', "-"),
    # ('\xe2\x81\xbc', "="),
    # ('\xe2\x81\xbd', "("),
    # ('\xe2\x81\xbe', ")")
)


def unicodetoascii(data):
    for _hex, _char in CHARS:
        data = data.encode().replace(_hex, _char)
    return data.decode()