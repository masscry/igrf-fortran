#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import *

modelType = [
  'IGRF', 'IGRF', 'IGRF', 'IGRF',
  'IGRF', 'IGRF', 'IGRF', 'IGRF',
  'IGRF', 'DGRF', 'DGRF', 'DGRF',
  'DGRF', 'DGRF', 'DGRF', 'DGRF',
  'DGRF', 'DGRF', 'DGRF', 'DGRF',
  'DGRF', 'DGRF', 'DGRF', 'DGRF',
  'IGRF', 'IGRF'
]

modelYear = [
  '1900', '1905', '1910', '1915',
  '1920', '1925', '1930', '1935',
  '1940', '1945', '1950', '1955',
  '1960', '1965', '1970', '1975',
  '1980', '1985', '1990', '1995',
  '2000', '2005', '2010', '2015',
  '2020', '2020s'
]

names = ['g/h', 'n', 'm']
types = ['S1', 'i4', 'i4']

for mdl in modelYear:
    names.append(mdl)
    types.append('f4')

data = loadtxt(
  fname = 'igrf13coeffs.txt',
  dtype = {
    'names': tuple(names),
    'formats': tuple(types)
  },
  comments='#',
  skiprows=4
)

maskGVals = data['g/h'] == 'g'
maskHVals = data['g/h'] == 'h'

for index in xrange(len(modelType)):
    fullname = modelType[index].lower() + modelYear[index] + '.dat'

    print(fullname)

    gMatrix = zeros(shape=(14, 14))
    hMatrix = zeros(shape=(14, 14))
    maxNonZero = 14

    yearData = data[modelYear[index]]

    for curN in xrange(1, 13+1):
        maskCurN = (data['n'] == curN)
        for curM in xrange(0, curN+1):

            maskCurM = (data['m'] == curM)

            fullGMask = maskGVals * maskCurM * maskCurN
            fullHMask = maskHVals * maskCurM * maskCurN

            gValue = yearData[fullGMask]
            hValue = yearData[fullHMask]

            gMatrix[curN,curM] = gValue[0]

            if len(hValue) != 0:
              hMatrix[curN,curM] = hValue[0]

    for curN in xrange(1, 13+1):
      if len(gMatrix[gMatrix[curN] != 0.0]) == 0:
        maxNonZero = curN
        break

    with open(fullname, 'w') as output:    
        output.write(
          '    {}\n'.format(
              modelType[index].lower() + modelYear[index] 
          )
        )
        output.write(
          ' {} {} {}\n'.format(
            maxNonZero-1, 6371.2, modelYear[index]
          )
        )
        for curN in xrange(1, maxNonZero):
            for curM in xrange(0, curN+1):

                output.write(
                  '{} {} {} {}\n'.format(
                    curN, curM, round(gMatrix[curN,curM], 2), round(hMatrix[curN,curM], 2)
                  )
                )


