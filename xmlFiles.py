#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Copyright (C)  @author: jose 
    FI UNAM
    Created on Mon Apr 10 22:40:45 2017

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
import csv,os
from moveto import MoveTo
import xml.etree.ElementTree as ET
import xml.dom.minidom as mini


def convertXML():
    home = os.getcwd()
    src = '/Freeling/'
    xmlFolder = home + '/xmlFolder/'
    Freeling = home + '/Freeling/'
    MoveTo.Supermakedirs(xmlFolder)
    os.chdir(Freeling)
    folder = os.listdir()
    for file in folder:
        print('Converting '+file+' to xml')
        root = ET.Element(file)
        with open(file,'r') as csvFile:
            doc = csv.reader(csvFile,delimiter=' ')
            for row in doc:
                if len(row) != 0:
                    palabra = ET.SubElement(root,'Palabra',attrib=\
                                            {'Lema':str(row[1]),'Etiqueta':str(row[2])})
                    palabra.text = row[0]
            csvFile.close()
        
        xml_pretty = prettify(root)
        output = open(file+'.xml','w')
        output.write(xml_pretty)
        output.close()
        print()
    MoveTo.Folder(home,src,xmlFolder,'xml')
    os.chdir(home)

def prettify(elem):
    rough_string = ET.tostring(elem,'UTF-8')
    reparsed = mini.parseString(rough_string)
    return reparsed.toprettyxml(indent='    ')


    
    
    
