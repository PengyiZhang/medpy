[![PyPI version fury.io](https://badge.fury.io/py/MedPy.svg)](https://pypi.python.org/pypi/MedPy/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/MedPy.svg)](https://pypi.python.org/pypi/MedPy/)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Downloads](https://pepy.tech/badge/medpy/month)](https://pepy.tech/project/medpy)
![travis auto-build](https://travis-ci.org/loli/medpy.svg?branch=master)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2565940.svg)](https://doi.org/10.5281/zenodo.2565940)

[GitHub](https://github.com/loli/medpy/) | [Documentation](http://loli.github.io/medpy/) | [Tutorials](http://loli.github.io/medpy/) | [Issue tracker](https://github.com/loli/medpy/issues) | [Contact](oskar.maier@gmail.com)

# 【python开发技术】【医学图像处理】MedPy 源码在windows上编译安装说明

## MedPy介绍
MedPy是一个python库，支持一系列医学图像处理操作，提供了读、写和操作任意维度大图的基本功能，包括一些n-维度常用的图像滤波器，图像特征提取器，可与scikit-learn一起使用，以及详尽的n维graph-cut程序包。

### 支持的医学图像格式

MedPy集成了SimpleITK来支持ITK的功能进行图像加载和存储。因此，可支持以下医学图像格式（关于医学图像格式可以参考[Here](https://github.com/PengyiZhang/MIADeepSSL/tree/master/MedicalImages)）：

- ITK MetaImage (.mha/.raw, .mhd)
- Neuroimaging Informatics Technology Initiative (NIfTI) (.nia, .nii, .nii.gz, .hdr, .img, .img.gz)
- Analyze (plain, SPM99, SPM2) (.hdr/.img, .img.gz)
- Digital Imaging and Communications in Medicine (DICOM) (.dcm, .dicom)
- Digital Imaging and Communications in Medicine (DICOM) series (<directory>/)
- Nearly Raw Raster Data (Nrrd) (.nrrd, .nhdr)
- Medical Imaging NetCDF (MINC) (.mnc, .MNC)
- Guys Image Processing Lab (GIPL) (.gipl, .gipl.gz)

### 支持的显微镜图像格式

- Medical Research Council (MRC) (.mrc, .rec)
- Bio-Rad (.pic, .PIC
- LSM (Zeiss) microscopy images (.tif, .TIF, .tiff, .TIFF, .lsm, .LSM)
- Stimulate / Signal Data (SDT) (.sdt)

### 可视化格式

- TK images (.vtk)

### 其它格式

- Portable Network Graphics (PNG) (.png, .PNG)
- Joint Photographic Experts Group (JPEG) (.jpg, .JPG, .jpeg, .JPEG)
- Tagged Image File Format (TIFF) (.tif, .TIF, .tiff, .TIFF)
- Windows bitmap (.bmp, .BMP)
- Hierarchical Data Format (HDF5) (.h5 , .hdf5 , .he5)
- MSX-DOS Screen-x (.ge4, .ge5)


## 相比original的medpy repo的改动 安装方式

直接采用 pip install medpy 即可实现安装，但是这样的方式安装的medpy不支持graph-cut，主要原因是graph-cut是集成在max-flow之上，而max-flow则是需要进行编译安装的，因此，这种方式安装的medpy在执行如下命令时会出现：


在windows上，maxflow是基于boost.python进行封装的，依赖boost.python环境。因此，正确的安装方式可以参考如下步骤：

- step 1： 下载boost库，并使能python，在stage/lib目录下得到对应的boost_python36-vc141-mt-x64-1_72.lib/dll

    b2.exe --with-python link=dynamic
    

- step 2: 下载medpy源码，修改setup.py，配置对应的include路径、library路径，开始安装

```
    # 修改 setpu.py 中的 maxflow 为如下

    maxflow = Extension('medpy.graphcut.maxflow',
                        define_macros = [('MAJOR_VERSION', '0'),
                                        ('MINOR_VERSION', '1')],
                        sources = ['lib/maxflow/src/maxflow.cpp', 'lib/maxflow/src/wrapper.cpp', 'lib/maxflow/src/graph.cpp'],
                        libraries = [],
                        include_dirs = ["D:\\boost_1_72_0"],
                        library_dirs = ["D:\\boost_1_72_0\\stage\\lib"],
                        extra_compile_args = ["/MD"])

    python setup.py install 

    # 会自动编译并生成对应python版本的pyd库：build\lib.win-amd64-3.6\medpy\graphcut\maxflow.cp36-win_amd64.pyd

```

- step 3: 修改环境变量PATH，能够指向maxflow.cp36-win_amd64.pyd所依赖的boost.python动态库：boost_python36-vc141-mt-x64-1_72.dll

- step 4: 有大量demos 可以参考。




------



2020-04-05




