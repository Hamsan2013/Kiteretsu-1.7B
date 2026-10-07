# Kiter Transformer Layer Module Block #28
import torch.nn as nn

class TransformerBlock_28(nn.Module):
    def __init__(self, layer_id=28):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
