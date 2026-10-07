# Kiter Transformer Layer Module Block #50
import torch.nn as nn

class TransformerBlock_50(nn.Module):
    def __init__(self, layer_id=50):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
