# Kiter Transformer Layer Module Block #64
import torch.nn as nn

class TransformerBlock_64(nn.Module):
    def __init__(self, layer_id=64):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
