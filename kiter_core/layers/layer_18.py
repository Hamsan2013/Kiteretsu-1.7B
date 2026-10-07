# Kiter Transformer Layer Module Block #18
import torch.nn as nn

class TransformerBlock_18(nn.Module):
    def __init__(self, layer_id=18):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
