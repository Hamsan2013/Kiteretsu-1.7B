# Kiter Transformer Layer Module Block #2
import torch.nn as nn

class TransformerBlock_2(nn.Module):
    def __init__(self, layer_id=2):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
