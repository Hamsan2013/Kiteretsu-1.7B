# Kiter Transformer Layer Module Block #3
import torch.nn as nn

class TransformerBlock_3(nn.Module):
    def __init__(self, layer_id=3):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
