
num_sentences=100
for sentence_type in 'sv' 'vs' 'unacc' 'which' 'top' 'objrel'; do
    python get_perplexities.py --task $sentence_type-$num_sentences &
done


