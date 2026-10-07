# Kiter Transformer Layer Module Block #20
import torch.nn as nn

class TransformerBlock_20(nn.Module):
    def __init__(self, layer_id=20):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
