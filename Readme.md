# SimpleITK Notebook Answers

[SimpleITK](http://www.simpleitk.org) is an abstraction layer and wrapper around the [Insight Toolkit](http://www.itk.org) for many languages including python.

This is a collection of IPython Notebooks, that have been written to quickly answer questions, such as that from the [ITK mailing lists](http://www.itk.org/ITK/help/mailing.html). While these have been written with python and use ITK via SimpelITK, they illustrate how to use and interact with ITK classes and run ITK algorithms.


# Getting Started

For general information about installing SimpleITK please see the [SimpleITK wiki](http://www.itk.org/Wiki/ITK/Release_4/SimpleITK/GettingStarted).

## Setting Up a Python Environment

It is recommended to setup a separate Python virtual environment to run through these notebooks.

Under the best of circumstances (tested on OSX 10.9, 10.8, 10.7, RH6, Ubuntu 12) this environment can be setup with the following:

    sudo pip install virtualenv
    virtualenv ~/sitkpy --no-site-packages
    ~/sitkpy/bin/pip install ipython[all]
    ~/sitkpy/bin/pip install numpy
    ~/sitkpy/bin/pip install matplotlib

Note: On Linux platforms you may be able to obtain many of these packages as system packages which may suffice ( Ubuntu 12+).
Note: On Window platforms some of these packages need be obtained as binary downloads and installed.

### Install SimpleITK

For many common platforms, a built distribution is available as an Python egg. This can be downloading and installed with the following command:

    ~/sitkpy/bin/easy_install SimpleITK
 

As of this writing, SimpleITK version >=0.6r1 is required to run these notebooks. This version currently needs to be downloaded from [Source Forge](http://sourceforge.net/projects/simpleitk/files/SimpleITK/0.6.rc1/Python/)

### Run the environment
 
To launch:

    cd SimpleITK-Notebook-Answers
    ~/sitkpy/bin/ipython notebook --pylab=inline

# Maintainence

These notebooks are not maintained an are use just for illustrative purposes.
