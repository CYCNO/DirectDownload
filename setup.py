from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Direct_Download',
    version='0.3',
    description='A Direct Downloader Module Which Will Get Direct Download Link From Some Popular File Uploading Websites',
    author= 'CYCNO',
    url = 'https://github.com/CYCNO/DirectDownload',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    keywords=['direct download', 'anonfiles', 'mediafire','mediafire direct download','anonfiles direct download'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['Direct-Download'],
    package_dir={'':'src'},
    install_requires = [
        'beautifulsoup4',
        'requests'
    ]
)