def upper_name(a_name):
    return a_name.upper()


def fancy_pad(text):
    return f'**{text}**'


def lowly_pad(text):
    return f'__{text}__'


if __name__ == "__main__":
    name = upper_name('dror')

    pad = fancy_pad(name)
    print(lowly_pad(pad))
