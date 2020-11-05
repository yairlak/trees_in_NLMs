#!/usr/bin/env python
import sys
import os
import torch
import argparse
import lstm
#print(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../word_language_model')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'word_language_model')))
import data
import numpy as np
import h5py
import pickle
import pandas
import time
import copy
from tqdm import tqdm
from torch.autograd import Variable

parser = argparse.ArgumentParser(
    description='PyTorch PennTreeBank RNN/LSTM Language Model')
parser.add_argument('--model', type=str, default='../data/trained_models/LSTM/hebrew/hidden650_batch64_dropout0.1_lr20.0.pt')
parser.add_argument('--task', default = 'sv-100')
parser.add_argument('--vocabulary', default='../data/trained_models/LSTM/hebrew/vocab.txt')
parser.add_argument('--path2results', default='../results/behavioral/')
parser.add_argument('--eos-separator', default='</s>')
parser.add_argument('--unk-token', default='<unk>')
parser.add_argument('--use-unk', action='store_true', default=False)
parser.add_argument('--lang', default='he')
parser.add_argument('--cuda', action='store_true', default=False)
parser.add_argument('--uppercase-first-word', action='store_true', default=False)
args = parser.parse_args()
print(args)

stime = time.time()

def feed_input(model, hidden, w):
    inp = torch.autograd.Variable(torch.LongTensor([[vocab.word2idx[w]]]))
    if args.cuda:
        inp = inp.cuda()
    out, hidden = model(inp, hidden)
    return out, hidden
def feed_sentence(model, h, sentence):
    outs = []
    for w in sentence:
        out, h = feed_input(model, h, w)
        outs.append(torch.nn.functional.log_softmax(out[0]).unsqueeze(0))
    return outs, h

# Vocabulary
vocab = data.Dictionary(args.vocabulary)

# Sentences
sentences = [l.rstrip('\n').split(' ') for l in open('../data/stimuli/' + args.task + '.txt', encoding='utf-8')]

# Load model
print('Loading models...')
print('\nmodel: ' + args.model+'\n')
model = torch.load(args.model, map_location=lambda storage, loc: storage)  # requires GPU model
model.rnn.flatten_parameters()
# hack the forward function to send an extra argument containing the model parameters
model.rnn.forward = lambda input, hidden: lstm.forward(model.rnn, input, hidden)
model_orig_state = copy.deepcopy(model.state_dict())
model.load_state_dict(model_orig_state)
stime = time.time()

if args.lang == 'it':
    init_sentence = " ".join(['Ma altre caratteristiche hanno fatto in modo che si <unk> ugualmente nel contesto della musica indiana ( anche di quella \" classica \" ) . <eos>',
    'Il principio di simpatia non viene abbandonato da Adam Smith nella redazione della " <unk> delle nazioni " , al contrario questo <unk> allo scambio e al mercato : il <unk> produce pane non per far- ne dono ( benevolenza ) , ma per vender- lo ( perseguimento del proprio interesse ) . <eos>'])
elif args.lang == 'he':
    init_sentence = " ".join(['ה בית ה תחתון של ה פרלמנט של ה פדרציה ה רוסית מ שנת 1993 נקרא גם הוא דומה , ה דומה של רוסיה . <eos> ב מקום ש הייתה בו כבר ב <unk> תנועת ā ארוכה , היא הפכה ב תקופות ה קדומות של ה עברית ל תנועת o , ב תהליך ה מכונה ה מעתק ה כנעני . <eos> ב המשך בוחרים מתוך ה משפחה את ה מבחן אשר לו רמת ה מובהקות ה מתאימה , ו אז אפשר ל גשת ל ביצוע ה ניסוי . <eos>'])
    #init_sentence = " ".join(['ה בית ה תחתון של ה פרלמנט של ה פדרציה ה רוסית מ שנת 1993 נקרא גם הוא דומה , ה דומה של רוסיה . <eos> ב מקום ש הייתה בו כבר ב <unk> תנועת ā ארוכה , היא הפכה ב תקופות ה קדומות של ה עברית ל תנועת o , ב תהליך ה מכונה ה מעתק ה כנעני . <eos> ב המשך בוחרים מתוך ה משפחה את ה מבחן אשר לו רמת ה מובהקות ה מתאימה , ו אז אפשר ל גשת ל ביצוע ה ניסוי . אבא אמר ש <eos>'])
    init_sentence = "<eos> הילד אכל גלידה . "
else:
    raise NotImplementedError("No init sentences available for this language")

hidden = model.init_hidden(1) 
#init_out, init_h = feed_sentence(model, hidden, init_sentence.split(" "))
init_out, init_h = feed_sentence(model, hidden, "<eos>")

##############
# FEED MODEL #
##############
log_p_next_word = np.zeros((len(sentences), len(sentences[0])))
for i, s in enumerate(tqdm(sentences)):
    #out = None
    out = init_out[-1]
    hidden = init_h 
    for j, w in enumerate(s):
        if w not in vocab.word2idx and args.use_unk:
            print('Unknown word: ', w)
            w = args.unk_token
        # store log_p of the next word before presenting it
        log_p_next_word[i, j] = out[0, 0, vocab.word2idx[w]].data.item()
        inp = Variable(torch.LongTensor([[vocab.word2idx[w]]]))
        if args.cuda:
            inp = inp.cuda()
        out, hidden = model(inp, hidden)
        out = torch.nn.functional.log_softmax(out[0]).unsqueeze(0)

mean_ppl = np.mean(np.exp(-np.mean(log_p_next_word, axis=1)))
std_ppl = np.std(np.exp(-np.mean(log_p_next_word, axis=1)))
mean_ppl_per_word = np.exp(-np.mean(log_p_next_word, axis=0))
std_ppl_per_word = np.exp(-np.std(log_p_next_word, axis=0))

fn_ppl = os.path.join(args.path2results, args.task + '.ppl')
with open(fn_ppl, 'w') as f:
    f.write(f'{mean_ppl}, {std_ppl}\n')
    for w, ppl, std in zip(sentences[0], mean_ppl_per_word, std_ppl_per_word):
        f.write(f'{w}, {ppl}, {std}\n')

print(mean_ppl)
print(mean_ppl_per_word)

