import random
import re

concrete_nouns = [
    "sea", "ship", "sail", "wind", "breeze", "wave", "cloud", "mast", "captain", "sailor", "shark", "whale", "tuna",
    "seashell", "pirate", "lad", "girl", "gull", "reef", "shore", "mainland", "moon", "sun"
]
abstract_nouns = ["adventure", "courage", "endurance", "desolation", "death", "life", "love", "faith"]
transitive_verbs = ["command", "view", "lead", "pull", "love", "desire", "fight"]
intransitive_verbs = ["travel", "sail", "wave", "grow", "rise", "fall", "endure", "die"]
adjectives = ["big", "small", "old", "cold", "warm", "sunny", "rainy", "misty", "clear", "stormy", "rough", "lively",
              "dead"]
adverbs = ["swiftly", "calmly", "quietly", "roughly"]
interjections = ["o", "oh", "ooh", "ah", "lord", "god", "wow", "golly gosh"]
patterns = ["The 5 1 6 3s the [1].",
            "5, 5 1s 6 3 a 5, 5 [1].",
            "2 is a 5 [1].",
            "9, [2]!",
            "1s [4]!",
            "The 1 4s like a 5 [1].",
            "1s 4 like 5 [1s].",
            "Why does the 1 [4]?",
            "4 6 like a 5 [1].",
            "2, 2, and [2].",
            "Where is the 5 [1]?",
            "All 1s 3 5, 5 [1s].",
            "Never 3 a [1]."]
# rhyming scheme
# choose one word, figure rhyme, subset of nouns etc...
digits_to_lists = {
    "1": concrete_nouns,
    "2": abstract_nouns,
    "3": transitive_verbs,
    "4": intransitive_verbs,
    "5": adjectives,
    "6": adverbs,
    "9": interjections
}


def gen_verses(random_pattern1: str, random_pattern2: str):
    def _map(char):
        if str.isdigit(char):
            return random.choice(digits_to_lists[char])
        return char

    split1 = [_map(x) for x in list(random_pattern1)]
    split2 = [_map(x) for x in list(random_pattern2)]
    joined1 = "".join(split1)
    joined2 = "".join(split2)

    last_word = re.findall(r"\[(\w+)\]", joined1)[0]
    # print(last_word)
    # return re.sub(r"\[\w+\]", "yo", joined1)
    return joined1 + "\n" + joined2


def generate_poem():
    random_pattern1 = random.choice(patterns)
    random_pattern2 = random.choice(patterns)
    verses = gen_verses(random_pattern1, random_pattern2)
    print(verses)


generate_poem()
generate_poem()