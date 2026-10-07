# Kiter Transformer Layer Module Block #24
import torch.nn as nn

class TransformerBlock_24(nn.Module):
    def __init__(self, layer_id=24):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
