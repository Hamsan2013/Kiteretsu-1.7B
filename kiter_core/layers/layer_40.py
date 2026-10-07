# Kiter Transformer Layer Module Block #40
import torch.nn as nn

class TransformerBlock_40(nn.Module):
    def __init__(self, layer_id=40):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
