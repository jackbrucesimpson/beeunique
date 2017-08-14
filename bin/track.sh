#!/usr/bin/env bash
set -u
set -e

#VIDEO_DIRECTORY="/media/jack/ID3"
OUTPUT_DIRECTORY="/Users/jacksimpson/Data" #"/home/jack/Data"
EXPERIMENT_NAME="Caffeine_Unique_Tags"
TRAINING=1 # 0:False, 1:True

NUM_FRAMES_THREAD_QUEUE=200
NUM_FRAMES_BATCH_PROCESS=100
N_PROCESSES=8
CHUNKSIZE=2

# Process Videos
#VIDEO_FILE_ARRAY=("$VIDEO_DIRECTORY/*.mp4")
VIDEO_FILE_ARRAY=("/Volumes/JSIMPSON/2017-02-15_04-32-00.mp4")
for VIDEO_FILENAME_PATH in $VIDEO_FILE_ARRAY; do
    python2 ../src/track.py $VIDEO_FILENAME_PATH $OUTPUT_DIRECTORY $EXPERIMENT_NAME $TRAINING $NUM_FRAMES_THREAD_QUEUE $NUM_FRAMES_BATCH_PROCESS $N_PROCESSES $CHUNKSIZE
done
