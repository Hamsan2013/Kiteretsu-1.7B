# Kiter Transformer Layer Module Block #98
import torch.nn as nn

class TransformerBlock_98(nn.Module):
    def __init__(self, layer_id=98):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
