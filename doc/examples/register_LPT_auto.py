"""Register a collection of images, using the log polar transform."""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

import os.path
import glob

import supreme
from supreme.config import data_path
from supreme import register
import supreme as SR
import supreme.misc

def getframes(path):
    return [supreme.misc.imread(fn,flatten=True) for fn in
            sorted(glob.glob(os.path.join(data_path,path)))]

images = getframes('toystory/*.png')[:3]
#images = getframes('test/flower*.jpg')
#images = getframes('test/olie*.jpg')
#images = getframes('reflectometer/*.png')
#images = getframes('chris/Q*.png')
#images = getframes('ooskus/dscf172*cropped.jpg')

#images = getframes('sec/*scaled*.jpg')
#images = getframes('hanno/*crop*.png')

# frames that work well: 1,2,(4),(8),(9),11,
#frames = [images[i] for i in [0,1,2,11]] # don't say a word, it's late
#frames = [images[1],images[0]] + images[2:]

print "Input image size: ", images[0].shape

frames = images
accepted_frames,tf_matrices = register.logpolar(frames[0],frames[1:],
                                                variance_threshold=0.7,
                                                angles=120,peak_thresh=5)#,window_shape=(71,71))

tf_matrices = [np.eye(3)] + list(tf_matrices)
usedframes = [frames[0]] + list(frames[i+1] for i in accepted_frames)

#print "Iteratively refining frames (this may take a while)..."
#tf_matrices = [tf_matrices[0]] + \
#              [register.refine(usedframes[0],F,tf_matrices[0],M)
#               for F,M in zip(usedframes[1:],tf_matrices[1:])]

print "Reconstructing..."
scale = 1
for m in tf_matrices:
    m[:2,:] *= scale

for u in usedframes:
    u -= u.min()
out = register.stack.with_transform(usedframes, tf_matrices)

# Astronomy
#out = register.stack.with_transform(usedframes, tf_matrices, weights=np.ones(len(usedframes)))
#T = 400
#out[out > T] = T

interp = 'nearest'
#plt.subplot(121)
#plt.imshow(images[0],cmap=plt.cm.gray,interpolation=interp)
#plt.subplot(223)
#plt.imshow(images[1],cmap=plt.cm.gray,interpolation=interp)
#plt.subplot(122)
plt.imshow(out,cmap=plt.cm.gray,interpolation=interp)
plt.xticks([])
plt.yticks([])
plt.show()

sp.misc.pilutil.imsave('/tmp/data.eps',out)