from helpers.text import upper_name, fancy_pad, lowly_pad

if __name__ == "__main__":
    name = upper_name('dror')

    pad = fancy_pad(name)
    print(lowly_pad(pad))
