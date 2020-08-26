from helpers.text import upper_name, fancy_pad, lowly_pad
from logic import is_too_long
import emoji

if __name__ == "__main__":
    name = upper_name('dror')

    padded_text = fancy_pad(name)
    final_text = lowly_pad(padded_text)
    print(final_text)

    print(f'is too long: {is_too_long(final_text)}')

    print(emoji.emojize(f'give a {name} :red_heart:'))
