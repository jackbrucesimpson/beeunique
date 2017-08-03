# BeeUnique

Program to track bees with unique tags.

## Running the Programs

Execution scripts are located in the `bin` directory. You can modify them to point to the directory containing videos to process and where you want your data output.

#### Program 1: Track
Main tracking video that processes videos. Execute by running `bash track.sh` after modifying the following variables:
- `VIDEO_DIRECTORY` - set to the directory video files are stored in
- `OUTPUT_DIRECTORY` - set to where you want to write your data out to

#### Program 2: Overlay
Overlays tracking and tag pattern classifications onto video. Execute by running `bash overlay.sh` - you can close the window by pressing 'q', and you'll need to edit the following variables:
- `FILENAME_PATH` - set to the path of the video you want to see
- `CSV_FILE_PATH` - set to the path of the csv file that was output by the tracking program
- `CREATE_VIDEO` - 1 (True) or 0 (False): Outputs 4K video of overlaid footage but slows down the program
- `OUTPUT_VIDEO_FILE` - set to the path and filename of the video you wish to output

#### Program 3: Combine Background

Combines the background images generated by each hour-long video into a single average image for each day. Execute by running `bash combine.sh` after modifying the following variables:

## Setup

### Dependencies
- Requires Linux/MacOS
- Python 2
- OpenCV 2

### Ubuntu Installation

#### System packages
`sudo apt-get install libopencv-dev python-opencv python-pip exfat-fuse`

#### Python libraries
`pip install numpy matplotlib pandas scipy sklearn cython h5py `

#### Machine Learning Libraries

If you want to set these libraries up to run on the GPU (optional), please follow the steps [here](https://gist.github.com/jackbrucesimpson/854b76ec1a3005af3377f7b22fda1f13) rather than running the command below.

`pip install tensorflow keras`

#### Building

Run the `build.sh` script in the `bin` directory to compile the tracking library
