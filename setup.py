import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='searchallpdf',  
     version='0.1.0',
     scripts=['searchallpdf'] ,
     author="Géry Casiez",
     author_email="gery.casiez@gmail.com",
     description="Search for terms in all pdf in current and sub folders.",
     long_description=long_description,

     long_description_content_type="text/markdown",
     url="https://github.com/casiez/searchallpdf",
     packages=setuptools.find_packages(),
     install_requires=[ 'pdfminer', 'argparse'],

     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License"
     ],

 )