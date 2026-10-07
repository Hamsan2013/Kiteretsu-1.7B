# Kiter Transformer Layer Module Block #36
import torch.nn as nn

class TransformerBlock_36(nn.Module):
    def __init__(self, layer_id=36):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
