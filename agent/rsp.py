import torch
import numpy as np


class RSPAgent(object):
    """Random Sample Policy Agent"""
    def __init__(self, state_dims, action_dims, **kwargs):
        self.state_dims = state_dims
        self.action_dims = action_dims

    @property
    def modules(self):
        return []

    def to_device(self, device):
        pass

    def take_action(self, state):
        return torch.from_numpy(np.random.uniform(-1, 1, self.action_dims))

    def train_batch(self, batch, warmup=False):
        feedback = {'Random Value': np.random.uniform(-1, 1)}
        return feedback
