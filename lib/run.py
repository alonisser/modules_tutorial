def upper_name(a_name):
    return a_name.upper()


def fancy_pad(text):
    return f'**{text}**'


if __name__ == "__main__":
    name = upper_name('dror')

    print(fancy_pad(name))
