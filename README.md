<div align="center">

<div align="center">
 <img src="docs/assets/pytorch-boost-banner.svg" width="300px" style="max-width: 100%;">
</div>

**Deep Learning framework to accelerate the training of PyTorch models.**

______________________________________________________________________

<p align="center">
  <a href="https://www.pytorch-boost.ai/">Boost</a> •
  <a href="https://pytorch-boost.readthedocs.io/en/stable/">Docs</a> •
  <a href="#community">Community</a> •
  <a href="https://kswain55.github.io/pytorch-boost/stable/generated/CONTRIBUTING.html">Contribute</a>
</p>


PyTorch-Boost is a deep learning optimization library, offering a lightweight and user-friendly wrapper for custom CUDA functions. Designed to accelerate PyTorch model training and inference, PyTorch-Boost facilitates the application of high-precision and low-precision modalities— encompassing 32-bit, 16-bit, 8-bit, 4-bit, and mixed-precision training—across multiple GPUs or machines with its distributed training capabilities.

For detailed usage, installation guidelines, and more, please refer to our comprehensive documentation.

</div>

______________________________________________________________________

## Install PyTorch-Boost

Simple installation from PyPI

```bash
pip install pytorch-boost
```

<details>
  <summary>Other installation options</summary>

#### Install with optional dependencies

```bash
pip install pytorch-boost['extra']
```

#### Conda

```bash
conda install pytorch-boost -c conda-forge
```

#### Install stable version

```bash
pip install https://github.com/kswain55/pytorch-boost/archive/refs/heads/release/stable.zip -U
```

#### Install bleeding-edge

```bash
pip install https://github.com/kswain55/pytorch-boost/archive/refs/heads/master.zip -U
```
</details>

______________________________________________________________________


## Compatibility
Supported Platform:
* Linux

Supported Hardware:
* NVIDIA Hopper, Ada, Ampere, Volta, and Turing architecture
* AMD CDNA 2/3 and RDNA 2/3

Supported Software Layer:
* CUDA 11.8 - 12.1 (NVIDIA)
* ROCM 5.3 and HIP compilation tools (AMD) 

______________________________________________________________________

## Acknowledgements
We would like to thank Tim Dettmers for his work [bitsandbytes](https://github.com/TimDettmers/bitsandbytes) and the team developing [PyTorch](https://github.com/pytorch/pytorch), allowing us to make this possible. We would also like to thank NVIDIA and AMD for providng the neccessary hardware for testing. 

______________________________________________________________________


## How to cite us
If you found this library useful, please consider citing our work:

```bibtex
@article{boost2023pytorch,
  title={Boost},
  author={minyoungg, kswain55},
  journal={arXiv preprint arXiv:2023.2023},
  year={2023}
}
```