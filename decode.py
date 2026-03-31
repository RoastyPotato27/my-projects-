text = input("string: ")

def detect_type(st):
    st_clean = st.replace(' ', '').lower()

    if all(c in '01' for c in st_clean):
        print("Its binary.\n")
        print(binary_to_text(st_clean))

    elif all(c in '0123456789abcdef' for c in st_clean):
        print("Its hex.\n")
        print(hex_to_text(st_clean))

    elif all(c in '01234567o' for c in st_clean):
        print("Its octal.\n")
        print(octal_to_text(st))

    else:
        print("Unknown format.")

def binary_to_text(st):
    chars = [st[i:i+8] for i in range(0, len(st), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def hex_to_text(st):
    return bytes.fromhex(st).decode("utf-8")

def octal_to_text(st):
    parts = st.split()
    text = ''
    for p in parts:
        if p.startswith('o'):
            text += chr(int(p[1:], 8))
        else:
            text += chr(int(p, 8))
    return text

detect_type(text)

