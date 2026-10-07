# Kiter Transformer Layer Module Block #13
import torch.nn as nn

class TransformerBlock_13(nn.Module):
    def __init__(self, layer_id=13):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
