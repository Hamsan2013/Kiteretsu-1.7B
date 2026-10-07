# Kiter Transformer Layer Module Block #7
import torch.nn as nn

class TransformerBlock_7(nn.Module):
    def __init__(self, layer_id=7):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
