import os, csv
import numpy as np
import matplotlib.pyplot as plt
model = 'LSTM-DROPOUT0.1.pt'
path2results = '../results/behavioral/'
path2figures = '../figures/perplexities/'
num_sentences = 100
sentence_types = ['sv', 'unacc', 'vs', 'which', 'top', 'objrel']
epochs = np.arange(1)
batchs = np.arange(0,500,10)
num_epochs = epochs.shape[0]
num_batchs = batchs.shape[0]
colors = ['g', 'g', 'b', 'b', 'r', 'r']
linestyles = ['-', '--', '-', '--', '-', '--']

mean_ppl_all_structures_per_epoch = np.zeros([len(sentence_types), num_epochs, num_batchs])
std_ppl_all_structures_per_epoch = np.zeros([len(sentence_types), num_epochs, num_batchs])
#mean_ppls, std_ppls = [], []
fig_per_word, axs = plt.subplots(len(sentence_types), 1, figsize=(10, 20))

for i_type, sentence_type in enumerate(sentence_types):
    print(f'Generating figure for task: {sentence_type}')
    for i_epoch, epoch in enumerate(epochs):
        for i_batch, batch in enumerate(batchs):
            print(sentence_type, epoch, batch)
            words, ppls, stds = [], [], []
            fn = 'epoch_' + str(epoch) + '_batch_' + str(batch) + '_' + model + '_' + sentence_type + '-' + str(num_sentences)
            try:
                with open(os.path.join(path2results, fn + '.ppl'), 'r') as f:
                    # ppl for entire sentence
                    line = f.readline()
                    mean_ppl, std_ppl = line.strip().split(',')
                    mean_ppl_all_structures_per_epoch[i_type, i_epoch, i_batch] = float(mean_ppl)
                    std_ppl_all_structures_per_epoch[i_type, i_epoch, i_batch] = float(std_ppl)

                    # ppl per word
                    line = f.readline()
                    while line:
                        word, ppl, std = line.strip().split(',')
                        words.append(word)
                        ppls.append(ppl)
                        stds.append(std)
                        line = f.readline()
            except:
                print("Didn't find ppl file for epoch %i batch %i" % (epoch, batch), path2results+fn+'.ppl')

    num_words = len(words)
    ppls = np.asarray([float(p) for p in ppls])
    stds = np.asarray([float(s) for s in stds])
    axs[i_type].errorbar(range(num_words), np.log(ppls), yerr=np.log(stds), label=fn)
    axs[i_type].set_xticks(range(num_words))
    axs[i_type].set_xticklabels(words)
    axs[i_type].legend(loc='upper right')
    axs[i_type].set_ylabel('Cross entropy')
    axs[i_type].set_ylim([0, 15])
plt.savefig(os.path.join(path2figures, 'perplexity_by_word.png'))

##########################
# BARPLOT FULL SENTENCES #
##########################
fig_barplot, ax = plt.subplots()
#barlist = ax.bar(sentence_types, np.log(mean_ppls), yerr=np.log(std_ppls))
#print(mean_ppl_all_structures_per_epoch.shape)
#print(std_ppl_all_structures_per_epoch)
#print(np.reshape(std_ppl_all_structures_per_epoch[0, :], (1, -1)))
for i, (t, c, ls) in enumerate(zip(sentence_types, colors, linestyles)):
#    print(t, c, ls)
    ax.errorbar(range(num_epochs*num_batchs), mean_ppl_all_structures_per_epoch[i, :].flatten(), yerr=std_ppl_all_structures_per_epoch[i, :].flatten(), label=t, color=c, ls=ls)
#    barlist[i].set_color(c)
ax.set_xticks(range(0, num_epochs*num_batchs, 2))
ax.set_xlabel('Training batch', fontsize=16)
ax.set_ylabel('Perplexity', fontsize=16)
plt.legend()
plt.savefig(os.path.join(path2figures, 'perplexity_whole_sentence.png'))
print('Saved to: ', os.path.join(path2figures, 'perplexity_whole_sentence.png'))
