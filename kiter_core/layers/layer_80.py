# Kiter Transformer Layer Module Block #80
import torch.nn as nn

class TransformerBlock_80(nn.Module):
    def __init__(self, layer_id=80):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
