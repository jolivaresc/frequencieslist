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
import os, csv
from collections import Counter

home = os.getcwd()
Freeling = home + '/Freeling/'

os.chdir(Freeling)

folderFreeling = os.listdir(Freeling)

words = []
lemmas = []
tags = []

for file in folderFreeling:
    with open(file) as csvFile:
        doc = csv.reader(csvFile,delimiter = ' ')
        for row in doc:
            if len(row):
                words.append(row[0])
                lemmas.append(row[1])
                tags.append(row[2][0])
                
words_D = dict(Counter(words))
lemmas_D = dict(Counter(lemmas))
tags_D = dict(Counter(tags))

os.chdir(home)