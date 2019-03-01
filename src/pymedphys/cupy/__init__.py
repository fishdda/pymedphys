import numpy

try:
    import cupy

    class CupyNumpyFallback:
        def __getattr__(self, key):
            try:
                return getattr(cupy, key)
            except AttributeError:
                return getattr(numpy, key)

    cp = CupyNumpyFallback()

except ImportError:
    cp = numpy
    cp.asnumpy = numpy.array
