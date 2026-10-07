# Kiter Transformer Layer Module Block #81
import torch.nn as nn

class TransformerBlock_81(nn.Module):
    def __init__(self, layer_id=81):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
