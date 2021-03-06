import os

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs


    config = Configuration('feature', parent_package, top_path)

    config.add_extension('dpt', sources=['dpt.c'],
                         include_dirs=[get_numpy_include_dirs()])

    config.add_data_dir('tests')

    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(configuration=configuration)
