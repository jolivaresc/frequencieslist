#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright (C)  @author: jose 
    FI UNAM
    Created on Mon Apr 10 15:53:12 2017

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
import os,errno
from moveto import MoveTo
from analyzer import Analyzer
import xmlFiles

home = os.getcwd()
def Freeling():
    src = '/folder/'
    Freeling = home+'/Freeling/'
    Analyzer.Run()
    
    if not os.path.exists(Freeling):
        try:
            MoveTo.Supermakedirs(Freeling)
            MoveTo.Folder(home,src,Freeling,'csv')
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

os.chdir(home)
Freeling()
xmlFiles.convertXML()

