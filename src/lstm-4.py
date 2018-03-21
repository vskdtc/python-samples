from numpy import array
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Embedding

# generate a sequence from the model
def generate_seq(model, tokenizer, seed_text, n_words):
    in_text, result = seed_text, seed_text
    # generate a fixed number of words
    for _ in range(n_words):
        # encode the text as integer
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        encoded = array(encoded)
        # predict a word in the vocabulary
        yhat = model.predict_classes(encoded, verbose=0)
        # map predicted word index to word
        out_word = ''
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
        # append to input
        in_text, result = out_word, result + ' ' + out_word
    return result

# source text
data = """ Madam, Sir\n
I am delighted to applying for this positions because I am bringing\n
a wealth of knowledge to the company and teams, I am very\n
passionate, focused and I am always targeting the very best\n
making sure the company can elevate to the next level of success.\n
My track record is great and I could provide references if needed.\n
I have managed and managing technical teams, I am hands-on, I am partnering with different stakeholders, I am used to work in an agile environment, and yet I am embracing responsibilities and accountabilities.\n
Do I have the experience, skills and background as required?\n
Yes, I do, particularly the domain experience in building and releasing new startup and/or enterprise products. The experiences, skills and backgrounds cover the entire innovation and product lifecycle management. It covers research, the specification,  business plan, economic model, investments, building teams, coaching teams, mentoring teams, project and product management, MVP, software development, technology and engineering in different domains, QA and testing, stakeholder engagement, partnerships, customer engagements, executive presentations, advertising, management consulting and other topics.\n
I am a person who is leading by example, I am listening to the team, I am mentoring team members, I am conveying visions the team can relate to and get passionate about.  Obviously, I am bringing a wealth of expertise to the table.\n
Yes, I am sending this application as a result of a careful consideration, meaning I am certain I can deliver and I do have the skill sets required!\n
"""
# integer encode text
tokenizer = Tokenizer()
tokenizer.fit_on_texts([data])
encoded = tokenizer.texts_to_sequences([data])[0]
# determine the vocabulary size
vocab_size = len(tokenizer.word_index) + 1
print('Vocabulary Size: %d' % vocab_size)
# create word -> word sequences
sequences = list()
for i in range(1, len(encoded)):
    sequence = encoded[i-1:i+1]
    sequences.append(sequence)
print('Total Sequences: %d' % len(sequences))
# split into X and y elements
sequences = array(sequences)
X, y = sequences[:,0],sequences[:,1]
# one hot encode outputs
y = to_categorical(y, num_classes=vocab_size)
# define model
model = Sequential()
model.add(Embedding(vocab_size, 100, input_length=1))
model.add(LSTM(100))
model.add(Dense(vocab_size, activation='sigmoid'))
print(model.summary())
# compile network
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit network
model.fit(X, y, epochs=600, verbose=1)
# evaluate
print(generate_seq(model, tokenizer, 'I', 20))
