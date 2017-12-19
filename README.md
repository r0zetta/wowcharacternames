# wowcharacternames
RNN generated World of Warcraft character names

If you just want the generated names, they're in names.txt, names2.txt, etc.
The json files (names.json, names2.json) are just easier to use programitically, but they're also sorted alphabetically. You can open these in a text editor.


To train the RNN:
 - download and extract this repo
 - copy rnn.py and text_handler.py from my worldofwarcraft project to the directory you placed the above
 - run python rnn.py to train (adjust params as needed, see below)

Suggested training params:
python rnn.py --tokenize=chars --seq_length=13 --batch_size=100 --num_epochs=200 --rnn_size=100 --num_layers=4

Generate names with:
python rnn.py --mode=sample
