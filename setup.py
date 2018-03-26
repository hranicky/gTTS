from setuptools import setup, find_packages

exec(open('gtts/version.py').read())

setup(
    name='gTTS',
    version=__version__,
    author='Pierre Nicolas Durette',
    author_email='pndurette@gmail.com',
    url='https://github.com/pndurette/gTTS',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gtts-cli = gtts.cli:tts_cli'
        ]
    },
    license='MIT',
    description='Create an mp3 file from spoken text via the Google TTS (Text-to-Speech) API',
    long_description=open('README.rst').read(),
    install_requires=[
        'six',
        'bs4',
        'click',
        'requests',
        'gtts_token'
    ],
    extras_require={'tests':['pytest', 'pytest-cov', 'coveralls',
                            'testfixtures', 'mock', 'six']},
    test_suite='gtts.tests',
    python_requires=">=2.7",
    classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Multimedia :: Sound/Audio :: Speech'
    ],
)
