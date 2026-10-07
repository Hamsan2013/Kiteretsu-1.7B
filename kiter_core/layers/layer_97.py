# Kiter Transformer Layer Module Block #97
import torch.nn as nn

class TransformerBlock_97(nn.Module):
    def __init__(self, layer_id=97):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
