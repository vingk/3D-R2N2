# 3D Reconstruction using Deep learning 
# CMPUT 608 project 
# Vinaykumar Kulkarni
# Rong Feng

This repository contains the code for the 3D reconstruction project done for the CMPUT 608 course. Given one or multiple views of an object, the network generates voxelized ( a voxel is the 3D equivalent of a pixel) reconstruction of the object in 3D.

The project is a re implementation of R2N2 network of the paper 3D-R<sup>2</sup>N<sup>2</sup>: 3D Recurrent Reconstruction Neural Network [Choy et al., 3D-R2N2: A Unified Approach for Single and Multi-view 3D Object Reconstruction, ECCV 2016](http://arxiv.org/abs/1604.00449), with enhancement for selecting frames from the video along with background removal for better results. Original project can be found at [http://cvgl.stanford.edu/3d-r2n2/](http://cvgl.stanford.edu/3d-r2n2/).

## Installation

The package requires python3. 
You can follow the direction below to install virtual environment within the repository or install anaconda for python 3.

- Download the repository

```
git clone https://github.com/vingk/3D-R2N2.git
```

- Setup the anaconda virtual environment and installing requirements ([How to use anaconda](https://conda.io/docs/user-guide/install/index.html))

```
cd 3D-R2N2
conda create -n py3-theano python=3.6
source activate py3-theano
conda install pygpu
pip install -r requirements.txt
```
- copy the theanorc file to the `$HOME` directory

```
cp .theanorc ~/.theanorc
```


### Running demo.py

- Install meshlab (skip if you have another mesh viewer). If you skip this step, demo code will not visualize the final prediction.

```
sudo apt-get install meshlab
```

- Run the demo code and save the final 3D reconstruction to a mesh file named `prediction.obj`

```
python demo.py prediction.obj
```


## License

MIT License
