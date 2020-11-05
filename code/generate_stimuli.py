import lexicons, argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--sentence-type', type=str, default='objrel')
parser.add_argument('--num-sentences', type=int, default=100)
parser.add_argument('--seed', type=int, default=1)
args = parser.parse_args()

# Load lexicon
hebrew_lexicon = lexicons.hebrew_lexicon()
sentences = []

np.random.seed(args.seed)


if args.sentence_type == 'sv':
    verb_type = 'unergative'
    noun_type = 'humans'
    while len(sentences) < args.num_sentences:
        number = ['singular', 'plural'][int(np.random.randint(2, size=1))]
        #number = 'singular'
        gender = ['masculine', 'feminine'][int(np.random.randint(2, size=1))]
        #gender = 'masculine'

        # NOUN
        num_tokens = len(hebrew_lexicon['nouns'][noun_type][number][gender])
        IX_noun = np.random.randint(num_tokens)
        noun = hebrew_lexicon['nouns'][noun_type][number][gender][IX_noun]

        # VERB
        num_tokens = len(hebrew_lexicon['verbs'][verb_type][noun_type][number][gender])
        IX_verb = np.random.randint(num_tokens)
        verb = hebrew_lexicon['verbs'][verb_type][noun_type][number][gender][IX_verb]

        # PLACE
        num_tokens = len(hebrew_lexicon['places'])
        IX_place = np.random.randint(num_tokens)
        place = hebrew_lexicon['places'][IX_place]

        # SENTENCE
        sentence = ['אתמול', 'ה', noun, verb, 'ב', place]
        if sentence not in sentences:
            sentences.append(' '.join(sentence))



if args.sentence_type == 'unacc':
    verb_type = 'unaccusative'
    while len(sentences) < args.num_sentences:
        number = ['singular', 'plural'][int(np.random.randint(2, size=1))]
        #number = 'singular'
        gender = ['masculine', 'feminine'][int(np.random.randint(2, size=1))]
        #gender = 'masculine'
        noun_type = ['humans', 'objects'][int(np.random.randint(2, size=1))]

        # NOUN
        num_tokens = len(hebrew_lexicon['nouns'][noun_type][number][gender])
        IX_noun = np.random.randint(num_tokens)
        noun = hebrew_lexicon['nouns'][noun_type][number][gender][IX_noun]

        # VERB
        num_tokens = len(hebrew_lexicon['verbs'][verb_type][noun_type][number][gender])
        IX_verb = np.random.randint(num_tokens)
        verb = hebrew_lexicon['verbs'][verb_type][noun_type][number][gender][IX_verb]

        # PLACE
        num_tokens = len(hebrew_lexicon['places'])
        IX_place = np.random.randint(num_tokens)
        place = hebrew_lexicon['places'][IX_place]

        # SENTENCE
        sentence = ['אתמול', 'ה', noun, verb, 'ב', place]
        if sentence not in sentences:
            sentences.append(' '.join(sentence))

if args.sentence_type == 'vs':
    verb_type = 'unergative'
    noun_type = 'humans'
    while len(sentences) < args.num_sentences:
        number = ['singular', 'plural'][int(np.random.randint(2, size=1))]
        #number = 'singular'
        gender = ['masculine', 'feminine'][int(np.random.randint(2, size=1))]
        #gender = 'masculine'

        # NOUN
        num_tokens = len(hebrew_lexicon['nouns'][noun_type][number][gender])
        IX_noun = np.random.randint(num_tokens)
        noun = hebrew_lexicon['nouns'][noun_type][number][gender][IX_noun]

        # VERB
        num_tokens = len(hebrew_lexicon['verbs'][verb_type][noun_type][number][gender])
        IX_verb = np.random.randint(num_tokens)
        verb = hebrew_lexicon['verbs'][verb_type][noun_type][number][gender][IX_verb]

        # PLACE
        num_tokens = len(hebrew_lexicon['places'])
        IX_place = np.random.randint(num_tokens)
        place = hebrew_lexicon['places'][IX_place]

        # SENTENCE
        sentence = ['אתמול', verb, 'ה', noun, 'ב', place]
        if sentence not in sentences:
            sentences.append(' '.join(sentence))

if args.sentence_type == 'which':
    verb_type = 'transitive'
    noun_type = 'humans'
    while len(sentences) < args.num_sentences:
        number1 = ['singular', 'plural'][int(np.random.randint(2, size=1))]
        #number1 = 'singular'
        gender1 = ['masculine', 'feminine'][int(np.random.randint(2, size=1))]
        #gender1 = 'masculine'

        # NOUN1
        num_tokens = len(hebrew_lexicon['nouns'][noun_type][number1][gender1])
        IX_noun1 = np.random.randint(num_tokens)
        noun1 = hebrew_lexicon['nouns'][noun_type][number1][gender1][IX_noun1]

        number2 = ['singular', 'plural'][int(np.random.randint(2, size=1))]
        #number2 = 'singular'
        gender2 = ['masculine', 'feminine'][int(np.random.randint(2, size=1))]
        #gender2 = 'masculine'

        # NOUN2
        num_tokens = len(hebrew_lexicon['nouns'][noun_type][number2][gender2])
        while True:
            IX_noun2 = np.random.randint(num_tokens)
            if IX_noun2 != IX_noun1:
                break
        noun2 = hebrew_lexicon['nouns'][noun_type][number2][gender2][IX_noun2]

        # VERB
        num_tokens = len(hebrew_lexicon['verbs'][verb_type][noun_type][number2][gender2])
        IX_verb = np.random.randint(num_tokens)
        verb = hebrew_lexicon['verbs'][verb_type][noun_type][number2][gender2][IX_verb]

        # SENTENCE
        sentence = [hebrew_lexicon['which'][number1][gender1], noun1, verb, 'ה', noun2]
        if sentence not in sentences:
            sentences.append(' '.join(sentence))

if args.sentence_type == 'top':
    verb_type = 'transitive'
    noun_type = 'humans'
    while len(sentences) < args.num_sentences:
        number1 = ['singular', 'plural'][int(np.random.randint(2, size=1))]
        #number1 = 'singular'
        gender1 = ['masculine', 'feminine'][int(np.random.randint(2, size=1))]
        #gender1 = 'masculine'

        # NOUN1
        num_tokens = len(hebrew_lexicon['nouns'][noun_type][number1][gender1])
        IX_noun1 = np.random.randint(num_tokens)
        noun1 = hebrew_lexicon['nouns'][noun_type][number1][gender1][IX_noun1]

        number2 = ['singular', 'plural'][int(np.random.randint(2, size=1))]
        #number2 = 'singular'
        gender2 = ['masculine', 'feminine'][int(np.random.randint(2, size=1))]
        #gender2 = 'masculine'

        # NOUN2
        num_tokens = len(hebrew_lexicon['nouns'][noun_type][number2][gender2])
        while True:
            IX_noun2 = np.random.randint(num_tokens)
            if IX_noun2 != IX_noun1:
                break
        noun2 = hebrew_lexicon['nouns'][noun_type][number2][gender2][IX_noun2]

        # VERB
        num_tokens = len(hebrew_lexicon['verbs'][verb_type][noun_type][number2][gender2])
        IX_verb = np.random.randint(num_tokens)
        verb = hebrew_lexicon['verbs'][verb_type][noun_type][number2][gender2][IX_verb]

        # SENTENCE
        sentence = ['את', 'ה', noun1, 'ה', hebrew_lexicon['this'][number1][gender1], 'ה', noun2, verb]
        if sentence not in sentences:
            sentences.append(' '.join(sentence))


if args.sentence_type == 'objrel':
    verb_type = 'transitive'
    noun_type = 'humans'
    while len(sentences) < args.num_sentences:
        number1 = ['singular', 'plural'][int(np.random.randint(2, size=1))]
        #number1 = 'singular'
        gender1 = ['masculine', 'feminine'][int(np.random.randint(2, size=1))]
        #gender1 = 'masculine'

        # NOUN1
        num_tokens = len(hebrew_lexicon['nouns'][noun_type][number1][gender1])
        IX_noun1 = np.random.randint(num_tokens)
        noun1 = hebrew_lexicon['nouns'][noun_type][number1][gender1][IX_noun1]

        number2 = ['singular', 'plural'][int(np.random.randint(2, size=1))]
        #number2 = 'singular'
        gender2 = ['masculine', 'feminine'][int(np.random.randint(2, size=1))]
        #gender2 = 'masculine'

        # NOUN2
        num_tokens = len(hebrew_lexicon['nouns'][noun_type][number2][gender2])
        while True:
            IX_noun2 = np.random.randint(num_tokens)
            if IX_noun2 != IX_noun1:
                break
        noun2 = hebrew_lexicon['nouns'][noun_type][number2][gender2][IX_noun2]

        # VERB
        num_tokens = len(hebrew_lexicon['verbs'][verb_type][noun_type][number2][gender2])
        IX_verb = np.random.randint(num_tokens)
        verb = hebrew_lexicon['verbs'][verb_type][noun_type][number2][gender2][IX_verb]

        # SENTENCE
        sentence = [hebrew_lexicon['this'][number1][gender1], 'ה', noun1, 'ש', 'ה', noun2, verb]
        if sentence not in sentences:
            sentences.append(' '.join(sentence))

punctuation = '?' if args.sentence_type in ['which'] else '.'
[print(s + ' ' + punctuation) for s in sentences]
