import os, csv
import numpy as np
import matplotlib.pyplot as plt

path2results = '../results/behavioral/'
path2figures = '../figures/perplexities/'
num_sentences = 100
sentence_types = ['sv', 'unacc', 'vs', 'which', 'top', 'objrel']
colors = ['g', 'g', 'b', 'b', 'b', 'r']

mean_ppls, std_ppls = [], []
fig_per_word, axs = plt.subplots(len(sentence_types), 1, figsize=(10, 20))
for i_type, sentence_type in enumerate(sentence_types):
    words, ppls, stds = [], [], []
    fn = sentence_type + '-' + str(num_sentences)
    print(f'Generating figure for task: {fn}')
    with open(os.path.join(path2results, fn + '.ppl'), 'r') as f:
        # ppl for entire sentence
        line = f.readline()
        mean_ppl, std_ppl = line.strip().split(',')
        mean_ppls.append(float(mean_ppl))
        std_ppls.append(float(std_ppl))

        # ppl per word
        line = f.readline()
        while line:
            word, ppl, std = line.strip().split(',')
            words.append(word)
            ppls.append(ppl)
            stds.append(std)
            line = f.readline()

    num_words = len(words)
    ppls = np.asarray([float(p) for p in ppls])
    stds = np.asarray([float(s) for s in stds])
    axs[i_type].errorbar(range(num_words), np.log(ppls), yerr=np.log(stds), label=fn)
    axs[i_type].set_xticks(range(num_words))
    axs[i_type].set_xticklabels(words)
    axs[i_type].legend(loc='upper right')
    axs[i_type].set_ylabel('Cross entropy')
plt.savefig(os.path.join(path2figures, 'perplexity_by_word.png'))

##########################
# BARPLOT FULL SENTENCES #
##########################
fig_barplot, ax = plt.subplots()
barlist = ax.bar(sentence_types, np.log(mean_ppls), yerr=np.log(std_ppls))
for i, c in enumerate(colors):
    barlist[i].set_color(c)
plt.savefig(os.path.join(path2figures, 'perplexity_whole_sentence.png'))
