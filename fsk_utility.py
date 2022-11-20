import numpy as np

class FSK_Utility:

    def fsk_modulate(bit_str, bit_freq_map, baud, sample_rate):
        seconds_per_bit = 1 / baud
        samples_per_bit = int(sample_rate * seconds_per_bit)
        t = np.linspace(0, seconds_per_bit, samples_per_bit)
        
        # maps from bit sequence (like "10") to the modulated wave representing that "symbol"
        symbol_map = {bit_seq: np.sin(freq * 2 * np.pi * t) for bit_seq, freq in bit_freq_map.items()}

        signal = np.array([])
        bits_per_symbol = len(list(bit_freq_map.keys())[0])  # Assume all keys are the same length
        for symbol in [bit_str[i:i+bits_per_symbol] for i in range(0, len(bit_str), bits_per_symbol)]:
            #print('Symbol', symbol)
            symbol_wave = symbol_map[symbol]
            #print('symbol_wave', symbol_wave)
            signal = np.append(signal, symbol_wave)

        #print('signal returned', signal)

        return signal

    def fsk_demodulate(raw_signal, bit_freq_map, baud, sample_rate):
        seconds_per_bit = 1 / baud
        samples_per_bit = int(sample_rate * seconds_per_bit)
        t = np.linspace(0, seconds_per_bit, samples_per_bit)
        
        # maps from bit sequence (like "10") to the modulated wave representing that "symbol"
        wave_to_symbol_map = {bit_seq: np.sin(freq * 2 * np.pi * t) for bit_seq, freq in bit_freq_map.items()}
        
        bit_str = ""
        for index in range(0, len(raw_signal), samples_per_bit):
            best_symbol = ""
            highest_dot_abs = 0
            for symbol, symbol_wave in wave_to_symbol_map.items():
                raw_window = raw_signal[index:index+samples_per_bit]
                dot_abs = np.abs(np.dot(symbol_wave[0:len(raw_window)], raw_window))
                if dot_abs > highest_dot_abs:
                    best_symbol = symbol
                    highest_dot_abs = dot_abs
            bit_str += best_symbol
        return bit_str