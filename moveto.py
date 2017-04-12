#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright (C)  @author: jose 
    FI UNAM
    Created on Mon Apr 10 15:11:36 2017

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

#from analyzer import Analyzer
#f=Analyzer.Run()
import os, shutil
from distutils.dir_util import mkpath


class MoveTo:
    @staticmethod
    def Folder(home, srcfolder, dstfolder,str):
        path = home + srcfolder
        MoveTo.Supermakedirs(dstfolder)
        files = os.listdir(path)
        files.sort()
        for f in files:
            if f.find(str) is not -1:
                src = path+f
                dst = dstfolder+f
                shutil.move(src,dst)
                print(f+' was moved to '+dstfolder+'\n')
    
    @staticmethod
    def Supermakedirs(path):
        mkpath(path)
    