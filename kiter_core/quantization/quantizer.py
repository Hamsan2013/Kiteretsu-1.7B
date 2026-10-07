import numpy as np

class KiterQ4Quantizer:
    """Block-wise Q4_K_M quantization engine for ARM Neonis/SIMD targets."""
    def __init__(self, block_size=32):
        self.block_size = block_size

    def quantize_tensor(self, tensor_data: np.ndarray):
        num_blocks = tensor_data.size // self.block_size
        reshaped = tensor_data.reshape(num_blocks, self.block_size)
        scales = np.max(np.abs(reshaped), axis=1) / 7.0
        scales[scales == 0] = 1.0
        quantized = np.round(reshaped / scales[:, None]).astype(np.int8)
        return quantized, scales
