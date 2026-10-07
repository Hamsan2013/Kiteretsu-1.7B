# Kiter Transformer Layer Module Block #14
import torch.nn as nn

class TransformerBlock_14(nn.Module):
    def __init__(self, layer_id=14):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
