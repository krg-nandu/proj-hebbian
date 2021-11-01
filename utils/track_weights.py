import torch
import torch.nn as nn
import torch.nn.functional as F
import os

import sys
sys.path.append('..')

from models.basic import Net
import matplotlib.pyplot as plt

# sample utility function to visualize parameter drift
def main():
    model_name = 'mnist_test'
    ckpts_dir = os.path.join('../ckpts', model_name)
    n_epochs = 10

    fig, axs = plt.subplots(6, 6)

    for epoch in range(n_epochs):
        model = Net()
        model.load_state_dict(torch.load(os.path.join(ckpts_dir, 'model_epoch_{}.pt'.format(epoch+1))))
        model = model.eval()

        # lets look at the conv 1 weights
        W = model.conv1.weight.detach().cpu().numpy()
        for k in range(32):
            axs[int(k/6), k%6].clear()
            axs[int(k/6), k%6].imshow(W[k,0])
            axs[int(k/6), k%6].axis('off')

        plt.pause(0.1)

if __name__ == '__main__':
    main()
