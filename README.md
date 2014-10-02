cpp-mc-tools
============

### Requirements

* [numpy, scipy, matplotlib](http://www.scipy.org/)
* [root](http://root.cern.ch/drupal/)
* [SLHALib-2.2](http://www.feynarts.de/slha/)

### Install

Make sure that 'root-config' is callable, e.g. by sourcing your root version.

Then simply type "make".

To install SLHALib-2.2, here is what works on my local desktop with gcc 4.8.0

    wget http://www.feynarts.de/slha/SLHALib-2.2.tar.gz 
    tar xvfz SLHALib-2.2.tar.gz
    cd SLHALib-2.2
    ./configure FFLAGS=-fPIC FC=gfortran
    make 
    make install

To compile slhalib.pyx, you first need to do the above (or equivalent), and then

   python cython-setup.py build_ext --inplace 


