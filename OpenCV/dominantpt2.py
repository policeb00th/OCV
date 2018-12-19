import struct
import codecs
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 5
 
print ('reading image')
im = Image.open('/home/diptanshu/Documents/OpenCV/10.jpeg',"r")
im = im.resize((150, 150))      # optional, to reduce time
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

print ('finding clusters')
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
print ('cluster centres:\n', codes)

vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

index_max = scipy.argmax(counts)                    # find most frequent
peak = codes[index_max]
#colour = ''.join(chr(int(c)) for c in peak).encode('hex')
#''.join(chr(int(c)) for c in peak) 
colour=codecs.encode(b"''.join(chr(int(c)) for c in peak)",'hex')
print ('most frequent is %s (#%s)' % (peak, colour))
