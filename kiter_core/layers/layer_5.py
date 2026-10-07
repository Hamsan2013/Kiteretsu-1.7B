# Kiter Transformer Layer Module Block #5
import torch.nn as nn

class TransformerBlock_5(nn.Module):
    def __init__(self, layer_id=5):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
