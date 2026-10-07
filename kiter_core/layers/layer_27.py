# Kiter Transformer Layer Module Block #27
import torch.nn as nn

class TransformerBlock_27(nn.Module):
    def __init__(self, layer_id=27):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
