def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs

    config = Configuration('lib', parent_package, top_path)

    config.add_subpackage('decorator')
    config.add_subpackage('dpt')
    config.add_subpackage('fast')
    config.add_subpackage('klt')
    config.add_subpackage('nurbs')
    config.add_subpackage('pywt')

    return config

if __name__ == "__main__":
    from numpy.distutils.core import setup
    setup(configuration=configuration)
