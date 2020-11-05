import os, csv
import matplotlib.pyplot as plt

path2results = '../results/behavioral/'
num_sentences = 100
sentence_types = ['sv', 'unacc', 'vs', 'which', 'top', 'objrel']
colors = ['g', 'g', 'b', 'b', 'b', 'r']

fig_per_word, axs = plt.subplots(len(sentence_types), 1, figsize=(30, 10))
for i_type, sentence_type in enumerate(sentence_types):
    fn_ppl = sentence_type + '-' + str(num_sentences) + '.ppl'
    with open(os.path.join(path2results, fn_ppl), 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        mean_ppl, std_ppl = reader.next()
        for row in reader:
            word, ppl, std = reader.next()
            words.append(word)
            ppls.append(ppl)
            stds.append(std)

    print(mean_ppl, std_ppl, ppls, words, stds)
    num_words = len(words)
    axs[i_type].plot(ppls)
    axs[i_type].set_yticks(range(num_words))
    axs[i_type].set_yticklabels(words)

    
