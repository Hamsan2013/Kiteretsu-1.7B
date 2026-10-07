# Kiter Transformer Layer Module Block #21
import torch.nn as nn

class TransformerBlock_21(nn.Module):
    def __init__(self, layer_id=21):
        super().__init__()
        self.layer_id = layer_id
    
    def forward(self, hidden_states):
        return hidden_states
