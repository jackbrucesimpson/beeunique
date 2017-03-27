import cv2
import os

class BGImage:
    def __init__(self):
        self.num_frames_averaged = 0
        self.frame_bg_sample_freq = 20
        self.sum_matrix_bg = None

    def update_bg_average_image(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self.sum_matrix_bg is None:
            self.sum_matrix_bg = gray.astype(np.float64)
        else:
            self.sum_matrix_bg += gray.astype(np.float64)
        self.num_frames_averaged += 1

    def output_bg_image(self):
        clahe = cv2.createCLAHE(clipLimit=10.0, tileGridSize=(9,9))
        img = self.sum_matrix_bg / self.num_frames_averaged
        img_uint8 = self.sum_matrix_bg.astype(np.uint8)
        clahe_img = clahe.apply(img_uint8)

        filename = 'bg' + '.png'
        file_output = os.path.join(self.output_directory, filename)

        cv2.imwrite(file_output, clahe_img)
