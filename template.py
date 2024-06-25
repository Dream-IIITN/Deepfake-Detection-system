# Setup
# Begin by installing and importing some necessary libraries, including:
# remotezip to inspect the contents of a ZIP file, tqdm to use a progress bar, OpenCV to process video files, 
# and tensorflow_docs for embedding data in a Jupyter notebook.


# The way this tutorial uses the `TimeDistributed` layer requires TF>=2.10
!pip install -U "tensorflow>=2.10.0"
     

!pip install remotezip tqdm opencv-python
!pip install -q git+https://github.com/tensorflow/docs
     

import tqdm
import random
import pathlib
