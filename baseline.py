import imageio.v3 as iio
import skimage
import matplotlib.pyplot as plt

path = "/data/bioeng/pigs/videosPenA_2018_12_04_9h04_12h14/1_Manual Record_2018-12-04 09-04-54_2018-12-04 09-17-31.mp4"

frame = iio.imread(path, index=100)

plt.imshow(frame)
plt.show()