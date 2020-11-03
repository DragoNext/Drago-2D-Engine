# Setup 
from distutils.core import setup
from Cython.Build import cythonize

import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
Cython.Compiler.Options.language_level = 3 

setup(ext_modules = cythonize('Drago2Dengine.py', 
annotate=True, 
language_level=2,
force=True,
language='mingw32',
compiler_directives=
{
'optimize.use_switch': True,
'optimize.unpack_method_calls': True}


)


)