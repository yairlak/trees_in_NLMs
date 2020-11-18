import sys, os
from sklearn.decomposition import PCA
import torch
import argparse
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../src/word_language_model')))
import data
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Extract and plot LSTM embeddings')
parser.add_argument('--model',help='Meta file stored once finished training the corpus')
parser.add_argument('--vocab')
parser.add_argument('-path2save', default='../figures/', help='Destination for the output figure')
parser.add_argument('--input', default='verbs.txt', help='Text file with two tab delimited columns with the lists of output words to contrast with the PCA')
args = parser.parse_args()
print(args)

# Load model
print('Loading models...')
print('\nmodel: ' + args.model+'\n')

#device = torch.device('cpu')
#model = torch.load(args.model, map_location=device)
model = torch.load(args.model, lambda storage, loc: storage)
model.rnn.flatten_parameters()
embeddings_in = model.encoder.weight.data.cpu().numpy()
embeddings_out = model.decoder.weight.data.cpu().numpy()
vocab = data.Dictionary(args.vocab)
print(vocab)
print(embeddings_in.shape)

# Read list of contrasted words (e.g., singular vs. plural verbs).
with open(args.input, 'r') as f:
    lines=f.readlines()
    verbs_transitive = [l.strip() for l in lines[0].split(',')]
    verbs_unaccusative = [l.strip() for l in lines[1].split(',')]
print(verbs_transitive, verbs_unaccusative)

#### Plot verb embeddings
for embeddings, embeddings_name in zip([embeddings_in, embeddings_out], ['embeddings_in', 'embeddings_out']):
    pca = PCA(n_components=2)
    pca.fit(embeddings)
    print(pca.explained_variance_ratio_)
    V = pca.components_
    X_transformed = pca.fit_transform(embeddings)

    fig, ax = plt.subplots(1, figsize = (35, 20))
    for i in tqdm(range(X_transformed.shape[0])):
        word = vocab.idx2word[i]
        if word in verbs_transitive:
            color, size, alpha = 'b', 18, 1
        elif word in verbs_unaccusative:
            color, size, alpha = 'r', 18, 1
        else:
            color, size, alpha = 'k', 8, 0.1

        ax.text(X_transformed[i, 0], X_transformed[i, 1], word, size=size, color=color, alpha=alpha)
        lim_max = np.max(X_transformed)
        lim_min = np.min(X_transformed)
        ax.set_xlim((lim_min, lim_max))
        ax.set_ylim((lim_min, lim_max))
        ax.axis('off')

    fn = os.path.join(args.path2save, 'word_' + embeddings_name  + '.png')
    fig.savefig(fn)
    print('Saved to: ' + fn)
    plt.close(fig)
