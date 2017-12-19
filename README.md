# wowcharacternames
RNN generated World of Warcraft character names

**If you just want the generated names, they're in new_names.json, new_names2.json etc.**

The names are sorted alphabetically. You can open these files in a text editor (or just in the browser).


To train an RNN to do this:
 - download and extract this repo
 - copy rnn.py and text_handler.py from my worldofwarcraft project to the directory you placed the above
 - pip install any missing dependencies
 - run python rnn.py to train (adjust params as needed, see below)

Suggested training params:
python rnn.py --tokenize=chars --seq_length=13 --batch_size=100 --num_epochs=200 --rnn_size=100 --num_layers=4

Generate names with:
python rnn.py --mode=sample
