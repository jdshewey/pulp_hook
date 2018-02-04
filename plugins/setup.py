from setuptools import setup, find_packages

setup(
    name='pulp_hook',
    version='0.9.0',
    license='LGPLv3',
    packages=find_packages(exclude=['test', 'test.*']),
    author='James Shewey',
    author_email='jdshewey@gmail.com',
    entry_points = {
        'pulp.distributors': [
            'distributor = pulp_hook.plugins.distributors.distributor:entry_point',
        ],
    }
)
