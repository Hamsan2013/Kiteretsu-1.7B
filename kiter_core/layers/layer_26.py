# Kiter Transformer Layer Module Block #26
import torch.nn as nn

class TransformerBlock_26(nn.Module):
    def __init__(self, layer_id=26):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
