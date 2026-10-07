#include <cuda_runtime.h>
#include <device_launch_parameters.h>

__global__ void kiter_flash_attn_kernel(const float* Q, const float* K, const float* V, float* O, int N, int d) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < N) {
        O[idx] = Q[idx] * K[idx] + V[idx];
    }
}
