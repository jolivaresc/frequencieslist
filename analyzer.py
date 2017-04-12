#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright (C)  @author: jose 
    FI UNAM
    Created on Mon Apr 10 12:37:41 2017

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
from subprocess import call
import os

class Analyzer:
    @staticmethod
    def Run():
        path = os.getcwd()
        folderPath = os.getcwd()+'/folder'
        folder = os.listdir('folder')
        os.chdir(folderPath)
        freeling = []
        for file in folder:
            if file.find('csv'):
                doc = open(file)
                print('Analyzing file: '+file+'...')
                output ='output_'+file+'.csv'
                cmd = 'analyze -f es.cfg < '+file+'> '+output
                call(cmd,shell=True)
                freeling.append(output)
                doc.close()
        os.chdir(path)
        print()
        return freeling