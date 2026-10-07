# Kiter Transformer Layer Module Block #1
import torch.nn as nn

class TransformerBlock_1(nn.Module):
    def __init__(self, layer_id=1):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
