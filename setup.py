from setuptools import setup, find_packages
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Direct-Download',
    version='0.4.4',
    description='A Direct Downloader Module Which Will Get Direct Download Link From Some Popular File Uploading Websites Like Mediafire, Anonfiles',
    author= 'CYCNO',
    url = 'https://github.com/CYCNO/DirectDownload',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    keywords=['direct download', 'anonfiles', 'mediafire','mediafire direct download','anonfiles direct download','google drive','google drive direct download link','google drive download link','megaupload','myfile','letsupload','filechan'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['Direct_Download'],
    package_dir={'':'src'},
    install_requires = [
        'wget',
        'requests'
    ]
)