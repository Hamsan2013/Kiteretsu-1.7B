# Kiter Transformer Layer Module Block #22
import torch.nn as nn

class TransformerBlock_22(nn.Module):
    def __init__(self, layer_id=22):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
