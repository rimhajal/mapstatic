# Mapstatic

## Overview

This module deals with nationwide electricity consumption. Different animations are available in order to have a better visualization.

## Installation

To install this package, one has to run the following line in its command prompt.

```{bash}
 $ pip install git+https://github.com/rimhajal/mapstatic
```

## Documentation

A documentation of our package is available [here](https://mapstatic.readthedocs). 

## Structure

A beamer presentation will be stored in the `./beamer` folder alongside the necessary style file to run the file and a documentation will be made using the sphinx package in the `./documentation` directory.

*Tests functions* are implemented in the `./mapstatic/tests` folder in order to assure the good development of this package. A continuous integration hook action is disposed in the `./github/workflows` folder which triggers an action everyday at `5`a.m and at each push.

Every bit of the main code is in the `./mapstatic` folder.
