
num_sentences=100
for sentence_type in 'sv' 'vs' 'unacc' 'which' 'top' 'objrel'; do
    python generate_stimuli.py --sentence-type $sentence_type --num-sentences $num_sentences > ../data/stimuli/$sentence_type-$num_sentences.txt &
    #python generate_stimuli.py --sentence-type $sentence_type --num-sentences $num_sentences > ../data/stimuli/$sentence_type-$num_sentences.txt &
done
