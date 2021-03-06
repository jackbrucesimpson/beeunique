import numpy as np
import cv2
import os
import sys
import time

from Processor.Video.frameprocessor import FrameProcessor
from Processor.Video.stream import Stream

def main():
    start_time = time.time()
    if len(sys.argv) != 10:
        print("Need input video, output directory, experiment name, and training arguments")
        sys.exit(1)

    video_path = sys.argv[1]
    output_directory = sys.argv[2]
    experiment_name = sys.argv[3]
    is_training = bool(int(sys.argv[4]))
    overwrite_raw = bool(int(sys.argv[5]))
    num_frames_thread_queue = int(sys.argv[6])
    num_frames_batch_process = int(sys.argv[7])
    n_processes = int(sys.argv[8])
    chunksize = int(sys.argv[9])

    print('Processing video: ', video_path)

    fp = FrameProcessor(video_path, output_directory, experiment_name, is_training, overwrite_raw, num_frames_batch_process, n_processes, chunksize)
    stream = Stream(video_path=video_path, queue_size=num_frames_thread_queue).start()

    while stream.processing_frames():
        frame = stream.read()
        fp.append_frame_process(frame)

    if len(fp.all_frames_data['list_frames_batch']) > 0:
        fp.parallel_process_frames()
    fp.output_data()

    end_time = time.time()
    print('Execution time in seconds:', end_time-start_time)

if __name__ == "__main__":
    main()
