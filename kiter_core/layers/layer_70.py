# Kiter Transformer Layer Module Block #70
import torch.nn as nn

class TransformerBlock_70(nn.Module):
    def __init__(self, layer_id=70):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
