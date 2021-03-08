# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:24:37 2021

@author: GHOLAMrezaNAMALEK
"""

from os import environ
from os.path import join, exists, dirname


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    from numpy.distutils.system_info import get_info
    
    config = Configuration('cust_mkl_fft', parent_package, top_path)
    
    mkl_root = environ.get('MKLROOT', None)
    if mkl_root:
        pass
    else:
        try:
            mkl_info = get_info('mkl') #return a empty dic
            print(mkl_info)
        except:
            mrl_info = dict()
    
    mkl_include_dirs = mkl_info.get('include_dirs', [])
    mkl_library_dirs = mkl_info.get('library_dirs', [])
    mkl_libraries = mkl_info.get('libraries', ['mkl_rt'])
    
    pdir = dirname(__file__)
    wdir = join(pdir, 'sources')
    mkl_info = get_info('mkl') #not used in following
    
    try:
        from Cython.Build import cythonize
        sources = [join(pdir, '_custPydfti.pyx')]
        have_cython = True    
    except ImportError as e:
        have_cython = False
        sources = [join(pdir, '_pydfti.c')]
        if not exists(sources[0]):
            raise ValueError(str(e) + '. ' + 
                             'Cython is required to build the initial .c file.')
            
    config.add_extension('_custPydfti', '_custPydfti.pyx')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
configuration()  