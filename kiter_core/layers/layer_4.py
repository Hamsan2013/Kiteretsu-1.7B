# Kiter Transformer Layer Module Block #4
import torch.nn as nn

class TransformerBlock_4(nn.Module):
    def __init__(self, layer_id=4):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
