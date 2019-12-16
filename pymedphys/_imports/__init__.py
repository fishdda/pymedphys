# pylint: disable = import-error

import importlib

import apipkg

EXTERNAL_EXPORTS = (
    "matplotlib.pyplot",
    "matplotlib.path",
    "matplotlib.patches",
    "matplotlib",
    "mpl_toolkits.mplot3d.art3d",
    "mpl_toolkits",
    "numpy",
    "shapely.affinity",
    "shapely.geometry",
    "shapely",
    "pymssql",
    "jupyterlab_server",
    "keyring",
    "packaging",
    "yaml",
    "scipy.interpolate",
    "scipy.special",
    "scipy.optimize",
    "scipy.ndimage.measurements",
    "scipy.ndimage",
    "scipy.signal",
    "scipy",
    "pandas",
    "dbfread",
    "pydicom.uid",
    "pydicom.dataset",
    "pydicom.sequence",
    "pydicom.filebase",
    "pydicom",
    "pynetdicom",
    "tqdm",
    "dateutil",
    "PIL",
    "imageio",
    "skimage",
)

apipkg.initpkg(
    __name__,
    {**{item: item for item in EXTERNAL_EXPORTS}, **{"plt": "matplotlib.pyplot"}},
)

THIS = importlib.import_module(__name__)
IMPORTABLES = dir(THIS)

# This will never actually run, but it helps pylint know what's going on
if "numpy" not in IMPORTABLES:
    import matplotlib.pyplot
    import matplotlib.pyplot as plt
    import matplotlib.path
    import matplotlib.patches
    import matplotlib
    import mpl_toolkits.mplot3d.art3d
    import mpl_toolkits
    import numpy
    import shapely.affinity
    import shapely.geometry
    import shapely
    import pymssql
    import jupyterlab_server
    import keyring
    import packaging
    import yaml
    import scipy.interpolate
    import scipy.special
    import scipy.optimize
    import scipy.ndimage.measurements
    import scipy.ndimage
    import scipy.signal
    import scipy
    import pandas
    import dbfread
    import pydicom.uid
    import pydicom.dataset
    import pydicom.sequence
    import pydicom.filebase
    import pydicom
    import pynetdicom
    import tqdm
    import dateutil
    import PIL
    import imageio
    import skimage

    raise ValueError("This section of code should never run")