# Kiter Transformer Layer Module Block #60
import torch.nn as nn

class TransformerBlock_60(nn.Module):
    def __init__(self, layer_id=60):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
