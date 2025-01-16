# Used for eegAugmentation
'''
- fzy_eeg_sliding_window() 
'''

import numpy as np

def fzy_eeg_sliding_window(data, label, window_size, step_size):
    '''
    data: 2D array with shape (num_channels, num_features)
    label: single label corresponding to the data
    window_size: int
    step_size: int
    '''
    assert data.ndim == 2, 'data must be a 2D array'
    windows = []                                          # Create an empty list to store the windows    
    num_windows = int((data.shape[1] - window_size) / step_size) + 1    # Calculate the number of windows
    labels = [label] * num_windows
    for i in range(num_windows):                                        # Loop over the windows
        start, end = i*step_size, i*step_size + window_size
        windows.append(data[:, start:end])       
    return windows, labels

if __name__ == '__main__':
    # Example usage
    print(f'....Now testing sliding_window()....\n')
    data, label = np.random.randint(0,20,(10,200)), '1'
    window_size, step_size = 10, 5
    windows, labels = fzy_eeg_sliding_window(data, label, window_size, step_size)
    print(len(windows),windows); print(len(labels),labels); 