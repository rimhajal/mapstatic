<p align="center">
   MAPSTATIC <br></p>

## Overview

This module deals with nationwide energy consumption. Several illustrations are available in order to have a better understanding and visualization of these phenomenons over time.

## Installation

In order to install this package, one first has to sastisfy all the python packages indicated in the requirements.txt file in the source directory. Then, one has to run the following line in its command prompt.

```{bash}
 $ pip install git+https://github.com/rimhajal/mapstatic
```

## Documentation

A documentation of this package is available [here](https://mapstatic.readthedocs). One can find some use's examples and illustrations of ***mapstatic*** at the [gallery](?).

## Structure

A beamer presentation is stored in the `./beamer` folder alongside the necessary style file to run the file. The documentation was made using the sphinx package in the `./documentation` directory.

*Tests functions* are implemented in the `./mapstatic/tests` folder in order to assure the good development of this package. A continuous integration hook action is disposed in the `./github/workflows` folder which triggers an action at each push.

Every bit of the main code is in the `./mapstatic` folder.
