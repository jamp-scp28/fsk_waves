import matplotlib.pyplot as plt
import scipy.io.wavfile

class Config_Utility:
    def setup_graph(title='', x_label='', y_label='', fig_size=None):
        fig = plt.figure()
        if fig_size != None:
            fig.set_size_inches(fig_size[0], fig_size[1])
        ax = fig.add_subplot(111)
        ax.set_title(title)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
    
    def write_audio_file(filename, filedata, sample_rate):
        scipy.io.wavfile.write(filename, sample_rate, filedata)
    
    def read_audio_file(filename):
        return scipy.io.wavfile.read(filename)