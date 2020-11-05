


SEED=1
for DROPOUT in 0.3;
do
CUDA_VISIBLE_DEVICES=5
cuda-memcheck --log-file /home_local/testing/cuda-memcheck-$USER-$CUDA_VISIBLE_DEVICES-$DROPOUT.log --print-level warn --print-limit 0 python main.py --cuda --vocab vocab.txt --emsize 650 --nhid 650 --dropout $DROPOUT --epochs 40 --seed $SEED --save Hebrew_dropout_$DROPOUT-seed_$SEED.pt &
done

