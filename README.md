# wowcharacternames
RNN generated World of Warcraft character names

Copy rnn.py and text_handler.py from worldofwarcraft project to here

Suggested training params:
python rnn.py --tokenize=chars --seq_length=13 --batch_size=100 --num_epochs=200 --rnn_size=100 --num_layers=4

Generate names with
python rnn.py --mode=sample
