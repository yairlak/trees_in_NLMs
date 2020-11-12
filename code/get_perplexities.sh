fn="/neurospin/unicog/protocols/LSTMology/growing_trees/code/get_perplexities.py"

qstat -q

echo "Choose queue (1: Unicog_long, 2: Nspin_long, 3: Unicog_short, 4: Nspin_short, 5: Unicog_run32, 6: Nspin_run32, 7: Unicog_run16, 8: Nspin_run16, 9:Nspin_bigM)"
read QUEUE

if [ $QUEUE -eq 1 ]
then
queue="Unicog_long"
walltime="72:00:00"
elif [ $QUEUE -eq 2 ]
then
queue="Nspin_long"
walltime="72:00:00"
elif [ $QUEUE -eq 3 ]
then
queue="Unicog_short"
walltime="02:00:00"
elif [ $QUEUE -eq 4 ]
then
queue="Nspin_short"
walltime="02:00:00"
elif [ $QUEUE -eq 5 ]
then
queue="Unicog_run32"
walltime="02:00:00"
elif [ $QUEUE -eq 6 ]
then
queue="Nspin_run32"
walltime="02:00:00"
elif [ $QUEUE -eq 7 ]
then
queue="Unicog_run16"
walltime="02:00:00"
elif [ $QUEUE -eq 8 ]
then
queue="Nspin_run16"
walltime="02:00:00"
elif [ $QUEUE -eq 9 ]
then
queue="Nspin_bigM"
walltime="72:00:00"
fi


path2models='/neurospin/unicog/protocols/LSTMology/growing_trees/code/word_language_model_2020Sep'
num_sentences=100
#for epochs in 0 1 2 3; do
for epoch in 0; do
    for batch in $(seq 0 10 2000); do  
        model=$path2models'/epoch_'$epoch'_batch_'$batch'_LSTM-DROPOUT0.1.pt'
        for sentence_type in 'sv' 'vs' 'unacc' 'which' 'top' 'objrel'; do
            output_log='logs/temp.out'
            error_log='logs/temp.err'
            job_name=$epoch'_'$batch
            CMD='python '$fn' --model '$model' --task '$sentence_type-$num_sentences
            echo $CMD | qsub -q $queue -N $job_name -l walltime=$walltime -o $output_log -e $error_log
        done
    done
done


