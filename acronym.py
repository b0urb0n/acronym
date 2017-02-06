import random


WORDS_FILE = '/usr/share/dict/words'
with open(WORDS_FILE, 'r') as fd:
    WORDS = [x.lower().strip() for x in fd.read().split('\n')]


def solve_acronym(acronym):
    out = []
    for letter in acronym:
        out.append(get_random_word(letter))
    return out


def get_random_word(letter=None):
    if letter:
        return random.choice([x for x in WORDS if x.startswith(letter)])
    return random.choice(WORDS)


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('acronym', help='The acronym to solve (ie. CDC)')
    args = p.parse_args()

    print ' '.join(solve_acronym(args.acronym.lower()))
