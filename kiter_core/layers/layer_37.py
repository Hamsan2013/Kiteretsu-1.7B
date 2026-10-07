# Kiter Transformer Layer Module Block #37
import torch.nn as nn

class TransformerBlock_37(nn.Module):
    def __init__(self, layer_id=37):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
