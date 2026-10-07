# Kiter Transformer Layer Module Block #9
import torch.nn as nn

class TransformerBlock_9(nn.Module):
    def __init__(self, layer_id=9):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
