# Kiter Transformer Layer Module Block #6
import torch.nn as nn

class TransformerBlock_6(nn.Module):
    def __init__(self, layer_id=6):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
