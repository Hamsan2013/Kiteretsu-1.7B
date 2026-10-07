# Kiter Transformer Layer Module Block #96
import torch.nn as nn

class TransformerBlock_96(nn.Module):
    def __init__(self, layer_id=96):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
