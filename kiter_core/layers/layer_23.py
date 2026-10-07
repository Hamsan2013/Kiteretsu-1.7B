# Kiter Transformer Layer Module Block #23
import torch.nn as nn

class TransformerBlock_23(nn.Module):
    def __init__(self, layer_id=23):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
