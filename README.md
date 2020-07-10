# igrf-fortran
Legacy IGRF source code updated to use IGRF-13 model data.

Latest [IGRF-13 coefficients](https://www.ngdc.noaa.gov/IAGA/vmod/coeffs/igrf13coeffs.txt) defines coefficients up to 13th order
and provide them in single table form, also fortran [source code](https://www.ngdc.noaa.gov/IAGA/vmod/igrf13.f) provided with new coefficients ommited almost 
all earlier available functions to calculate L-shell and B0 parameter.

[igrf_sub.for](https://github.com/masscry/igrf-fortran/blob/main/igrf_sub.for) provided in this repository is modified to be able to process coefficients up to
13th order. Also simple python script [convert-data.py](https://github.com/masscry/igrf-fortran/blob/main/convert-data.py) is provided to convert data from single
table form to several *.dat files.
