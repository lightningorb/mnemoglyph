import argparse
import itertools
from mnemonic import Mnemonic

mnemo = Mnemonic("english")

generate_hieroglyphs = lambda n: [chr(code) for code in range(0x13000, 0x13000 + n)]

hieroglyph_list = generate_hieroglyphs(64)

assert len(mnemo.wordlist) == 2048, "BIP39 word list should contain 2048 words"
assert len(hieroglyph_list) >= 64, "At least 64 hieroglyphs are required"

hieroglyph_pairs = list(itertools.product(hieroglyph_list, repeat=2))

word_to_hieroglyph = dict(zip(mnemo.wordlist, hieroglyph_pairs))
hieroglyph_to_word = dict(zip(hieroglyph_pairs, mnemo.wordlist))

encode_seed_phrase = lambda seed_phrase: "".join(
    ["".join(word_to_hieroglyph[word]) for word in seed_phrase.split()]
)

decode_seed_phrase = lambda encoded_seed_phrase: " ".join(
    [
        hieroglyph_to_word[(h1, h2)]
        for h1, h2 in [
            encoded_seed_phrase[i : i + 2]
            for i in range(0, len(encoded_seed_phrase), 2)
        ]
    ]
)


def main():
    parser = argparse.ArgumentParser(
        description="Encode and decode BIP39 seed phrases to hieroglyphs"
    )
    parser.add_argument(
        "operation",
        choices=["encode", "decode"],
        help="Operation to perform (encode/decode)",
    )
    parser.add_argument("input", help="Seed phrase to encode or hieroglyphs to decode")

    args = parser.parse_args()

    if args.operation == "encode":
        encoded_seed_phrase = encode_seed_phrase(args.input)
        print(f"Encoded seed phrase: {encoded_seed_phrase}")
    elif args.operation == "decode":
        decoded_seed_phrase = decode_seed_phrase(args.input)
        print(f"Decoded seed phrase: {decoded_seed_phrase}")


if __name__ == "__main__":
    main()
