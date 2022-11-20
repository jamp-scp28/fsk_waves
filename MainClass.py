import numpy as np
import scipy
import scipy.io.wavfile
import wave
import matplotlib.pyplot as plt
from fsk_utility import FSK_Utility
from config_utility import Config_Utility
from byte_utility import Byte_Utility 

#Message to be transmited
msg = "2345|026|6478796098764563"

#Convert message to bits
msg_bits = ''.join(["{0:b}".format(ord(c)).zfill(8) for c in msg])

#Declare Config params for frecuency modulation
bit_freq_map = {
    "0": 1200,
    "1": 2200
}
baud = 1200
sample_rate = 44100

#Average Frecuency
zeroCount = str(msg_bits).count('0') * bit_freq_map["0"]
oneCount = str(msg_bits).count('1') * bit_freq_map["1"]

#Aditional Data
averageFrequency = ((zeroCount * bit_freq_map["0"])+(oneCount * bit_freq_map["1"]))/(zeroCount + oneCount)
period = 1 / averageFrequency
time = (1/baud) * (zeroCount + oneCount)
speedConstant = 299775
waveLength = speedConstant / averageFrequency

print('time', time)
print('period: ',1/averageFrequency)
print('frecuency: ',1/(1/averageFrequency))
print('WaveLength: ',waveLength)

#====================================================================================
#Modulate
#Create Wave Signal
msg_signal = FSK_Utility.fsk_modulate(msg_bits, bit_freq_map, baud=baud, sample_rate=sample_rate)

#Write Signal to Wave File
Config_Utility.write_audio_file('creditCardInfo.wav', msg_signal, 3200)

#Plot Chart
Config_Utility.setup_graph(title='fsk-modulated "CreditCardMessage"', fig_size=(18,5))
plt.plot(msg_signal)
plt.margins(0.05)
plt.show()

#Message representation in Bytes
print('Binary Data: ',msg_bits)

#====================================================================================
#Demodulated
demodulate_msg = FSK_Utility.fsk_demodulate(msg_signal, bit_freq_map, baud, sample_rate)

#Bytes to String
decodedMessage = Byte_Utility.convertByteToString(demodulate_msg)

print('Decoded Message', decodedMessage)