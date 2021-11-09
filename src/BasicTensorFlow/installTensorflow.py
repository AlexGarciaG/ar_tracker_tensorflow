import os

TENSORFLOW = "2.3.0"
TFMODELS = "2.5.1"
TFIO = "2.5.1"

os.system('pip uninstall tensorflow -y')
os.system('pip uninstall tensorflow -y')

os.system('pip uninstall tensorflow-io -y')
os.system('pip uninstall tf-models-official -y')


#os.system('pip install tensorflow-io=={0}'.format(TFMODELS))
#os.system('pip install tf-models-official=={0}'.format(TFMODELS))
os.system('pip install tensorflow=={0}'.format(TENSORFLOW))
os.system('pip install tensorflow-io')
os.system('pip install tf-models-official')

import tensorflow as tf;
print(tf.__version__)