# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 16:58:11 2019
@author: Alex B
"""
elements = ['H' , 'He' , 'Li' , 'Be' , 'B' , 'C' , 'N' , 'O' , 'F' , 'Ne' , 'Na' , 'Mg' , 'Al' , 'Si' , 'P' , 'S' , 'Cl' , 'Ar' , 'K' , 'Ca' , 'Sc' , 'Ti' , 'V' , 'Cr' , 'Mn' , 'Fe' , 'Co' , 'Ni' , 'Cu' , 'Zn' , 'Ga' , 'Ge' , 'As' , 'Se' , 'Br' , 'Kr' , 'Rb' , 'Sr' , 'Y' , 'Zr' , 'Nb' , 'Mo' , 'Tc' , 'Ru' , 'Rh' , 'Pd' , 'Ag' , 'Cd' , 'In' , 'Sn' , 'Sb' , 'Te' , 'I' , 'Xe' , 'Cs' , 'Ba' , 'La' , 'Ce' , 'Pr' , 'Nd' , 'Pm' , 'Sm' , 'Eu' , 'Gd' , 'Tb' , 'Dy' , 'Ho' , 'Er' , 'Tm' , 'Yb' , 'Lu' , 'Hf' , 'Ta' , 'W' , 'Re' , 'Os' , 'Ir' , 'Pt' , 'Au' , 'Hg' , 'Tl' , 'Pb' , 'Bi' , 'Po' , 'At' , 'Rn' , 'Fr' , 'Ra' , 'Ac' , 'Th' , 'Pa' , 'U' , 'Np' , 'Pu' , 'Am']

answer = 4
while answer is not 3:
  string = ""
  answer = int(raw_input("\n>Would you like to encode (0), decode (1), or exit(3)? "))
  if answer == 0:
    input = str(raw_input("\n>Enter the text to encode: "))
    numlist = []
    for c in input:
        numlist.append(ord(c) - 32)
    
    for x in range(len(numlist)):
      string = string + elements[numlist[x]] + " "
    print ("\n>Your encoded text is:")
    print string
    
  elif answer == 1:
    string = str(raw_input("\n>Enter the text to decode: "))
    decodelist = string.split()
    decoded = ""
    
    for d in decodelist:
      decoded = decoded + str(chr(elements.index(d)+32))
    print ("\n>Your decoded text is:")
    print decoded
print ("\n>Successful exit.")
