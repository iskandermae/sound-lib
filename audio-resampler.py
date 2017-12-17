
# coding: utf-8

# #### PLAN
# #Read 1 file
# #divide by 10ms
# #analyze each
# #find firs voice, trim voice
#   

# In[44]:


import scipy.io.wavfile as wavfile
import numpy as np
import samplerate
import os
import IPython
import random


# In[36]:


def load_wav_by_path(p):
    fs, wav = wavfile.read(p)
    L = 16000
    std = np.max(np.abs(wav))
    if std != 0:
        wav = np.array((wav / std * 5000), np.int16)
    if wav.size < L:
        wav = np.pad(wav, (L - wav.size, 0), mode='constant')
    else:
        wav = wav[0:L]
    return wav


# In[54]:


filenames = os.path.join('.', 'bed.wav')
wav_input = load_wav_by_path(filenames)

# Simple API
ratio = random.uniform(0.7, 1.2)
converter = 'sinc_best'
output_data_simple =np.array((samplerate.resample(wav_input, ratio, converter)), np.int16)

filenames = os.path.join('.', 'res_bed.wav')
wavfile.write(filenames, fs, output_data_simple)

IPython.display.Audio(filenames)


# In[ ]:


np.rand()

