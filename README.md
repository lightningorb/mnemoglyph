# BIP39 Hieroglyph Encoder/Decoder

This Python script encodes and decodes BIP39 seed phrases into pairs of Unicode Egyptian hieroglyphs. It provides a fun and unique way to represent seed phrases while maintaining compatibility with BIP39 standards.

It was created (as a joke) after [Tuur Demeester posted to twitter](https://twitter.com/TuurDemeester/status/1637114902019014657):

> "Ancient Egyptian titanium tablet, est. 1,400 B.C., speculated to be a 24 word seed phrase."

Followed by a picture of an Egyptian tablet.

## Requirements

- Python 3.6 or higher
- `mnemonic` package: `pip3 install mnemonic` or `pip3 -r src/requirements.txt`

## Usage

The script provides two modes of operation: encoding and decoding.

### Encoding

To encode a BIP39 seed phrase into hieroglyphs, use the `-e` or `--encode` flag followed by the seed phrase:

```
python3 src/seed_phrase_hieroglyphs.py encode "pistol maple dutch crunch cereal lawsuit song glory excite breeze canyon"
```

The script will output the corresponding hieroglyphs.

### Decoding

To decode a sequence of hieroglyphs into a BIP39 seed phrase, use the `-d` or `--decode` flag followed by the hieroglyphs:

```
python3 src/seed_phrase_hieroglyphs.py decode "𓀔𓀫𓀐𓀼𓀈𓀣𓀆𓀧𓀄𓀬𓀏𓀱𓀙𓀹𓀌𓀜𓀉𓀶𓀃𓀜𓀄𓀎"
```

The script will output the corresponding seed phrase.

## Limitations

This implementation supports only the English BIP39 word list. The hieroglyphs are mapped to the words using a deterministic algorithm, and the number of hieroglyphs can be easily adjusted to support other languages or BIP39-compatible word lists.

This repo was created as a joke, and should not be used for anything.

## License

This project is released under the GPL-3 License. See the `LICENSE` file for more details.
