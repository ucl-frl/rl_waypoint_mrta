import pickle
import os

import numpy as np
import torch
from sklearn.datasets import make_blobs

from torch.utils.data import Dataset
from torch.utils.data.dataset import T_co


def prepare_blob_dataset(hparams) -> (np.ndarray, np.ndarray):
    city_num = hparams['city_num']
    feature_dim = hparams['feature_dim']
    sample_num = hparams['sample_num']

    samples = np.zeros((sample_num, city_num, feature_dim))
    labels = np.zeros((sample_num, city_num))

    for sample in range(sample_num):
        samples[sample, :, :], labels[sample, :] = make_blobs(city_num, feature_dim)

    return samples, labels


class BlobDataset(Dataset):
    def __init__(self, hparams):
        super(BlobDataset, self).__init__()
        self.hparams = hparams

        self.samples, self.labels = self._generate_dataset()

    def __getitem__(self, index) -> T_co:
        sample = self.samples[index]
        label = self.labels[index]

        data_pair = {'sample': sample, 'label': label}

        return data_pair

    def __len__(self):
        return len(self.samples)

    def _generate_dataset(self):
        samples, labels = prepare_blob_dataset(self.hparams)
        return torch.from_numpy(samples).float(), torch.from_numpy(labels)


# TSP dataset wrapper from https://github.com/wouterkool/attention-learn-to-route
class TSPDataset(Dataset):
    def __init__(self, filename=None, size=20, num_samples=1000000, offset=0, distribution=None):
        super(TSPDataset, self).__init__()

        self.data_set = []
        if filename is not None:
            assert os.path.splitext(filename)[1] == '.pkl'

            with open(filename, 'rb') as f:
                data = pickle.load(f)
                self.data = [torch.FloatTensor(row) for row in (data[offset:offset + num_samples])]
        else:
            # Sample points randomly in [0, 1] square
            self.data = [torch.FloatTensor(size, 2).uniform_(0, 1) for _ in range(num_samples)]

        self.size = len(self.data)

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.data[idx]