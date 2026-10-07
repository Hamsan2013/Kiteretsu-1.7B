# Kiter Transformer Layer Module Block #8
import torch.nn as nn

class TransformerBlock_8(nn.Module):
    def __init__(self, layer_id=8):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
