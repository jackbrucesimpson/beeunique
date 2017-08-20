#!/usr/bin/env bash
set -u
set -e

source setup.sh

VIDEO_DIRECTORY="/Users/jacksimpson/Data/videos"
TRAINING=0
NUM_FRAMES_BATCH_PROCESS=100
N_PROCESSES=8
CHUNKSIZE=2

VIDEO_FILE_ARRAY=("$VIDEO_DIRECTORY/*.mp4")
for VIDEO_FILENAME_PATH in $VIDEO_FILE_ARRAY; do
    python2 ../src/track.py $VIDEO_FILENAME_PATH $OUTPUT_DIRECTORY $EXPERIMENT_NAME $TRAINING $NUM_FRAMES_THREAD_QUEUE $NUM_FRAMES_BATCH_PROCESS $N_PROCESSES $CHUNKSIZE
done
