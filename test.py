#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright (C)  @author: jose 
    FI UNAM
    Created on Wed Apr 12 12:43:39 2017

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import os, csv,freelingFiles,xmlFiles
from collections import Counter

home = os.getcwd()

def getFreqList(options):
    Freeling = home + '/Freeling/'
    #Including stopword
    if options['stopword']:
        stopwords = [line.strip() for line in open('stopword.txt')]
            
    os.chdir(Freeling)
    
    folderFreeling = os.listdir(Freeling)
    
    frequencies = []
    
    for file in folderFreeling:
        with open(file) as csvFile:
            doc = csv.reader(csvFile,delimiter = ' ')
            for row in doc:
                if len(row):
                    if options['opt'] == 3:
                        #tags
                        frequencies.append(row[2][0])
                    elif options['opt'] == 2:
                        #Lemas
                        frequencies.append(row[1])
                    elif options['opt'] == 1:
                        if options['stopword']:
                            if row[0] not in stopwords:
                                frequencies.append(row[0])
                        else:
                            frequencies.append(row[0])
   
    return dict(Counter(frequencies))



def menu():
    try:
        option = int(input('Obtener lista de frecuencias de:\n1) Palabras\n2) Lemas\n3) Etiquetas\n'))
        if option > 0 and option < 4:
            if option == 1:
                sw = input('Incluir lista de paro [y/n]\n')
                if sw is 'y':
                    return {'opt':option,'stopword':True}
                else:
                    return {'opt':option,'stopword':False}
            else:
                return {'opt':option,'stopword':False}
              
            
        else:
            print('Opción no válida.')
    except ValueError as err:
        print(err)

#Create freeling files
#freelingFiles.Freeling()
#Convert freeling files to XML
#xmlFiles.convertXML()

#Display menu
freq = getFreqList(menu())

print('palabra\tFrecuencia')
for k,v in freq.items():
    print(k,v)






