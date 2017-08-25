from setuptools import setup

setup(
    name='blackmamba',
    version='0.0.13',

    description='Pythonista on steroids',
    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: iOS',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development'
    ],

    url='https://github.com/zrzka/blackmamba',
    license='MIT',

    include_package_data=True,

    author='Robert Vojta',

    packages=[
        'blackmamba',
        'blackmamba.experimental'
    ],
    package_dir={'': '.'},

    keywords=['pythonista ios']
)
