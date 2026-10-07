# Kiter Transformer Layer Module Block #25
import torch.nn as nn

class TransformerBlock_25(nn.Module):
    def __init__(self, layer_id=25):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
