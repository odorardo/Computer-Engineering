#!/usr/bin/env python3
import binascii
import sys

n=3885939818809226866639787043363807561348795134092369130950983385470901806736361565466089297128250818994339484840348246849859686706799610146322341287843148253011924185299904669597627551758155800320077912889550691379091497725128289299633986277751193246120847022674590432383681458993045745957361247628898619533833648251443916733282577886721293431036458439415555101097990025528589956459090061384778695974308595402123516471802342910395085919062194938719275688182244497225339097083024039098640715244014285827272513848016293518825950785609827464234980855575137963828480665401893527147121584763680409101485362879563673787527
e = 17

#Retrieve the message
with open("Secret_msg.txt", "r") as f:
	p = f.readlines()
#Print p
print(p) #Dang it, it's a string
#convert it in a list of integers
dec = [int(e) for e in p[0].split('\t')]
print(dec)
#The encryption is done character-wise, no way m^(e)>n, 
#no modulus should have been executed
#I simply need to do the e-th root of the integers i have retrieved
m_dec = [round(char ** (1/e)) for char in dec]
m = [chr(letter) for letter in m_dec]
#Return the array of bytes as a string
print(''.join(m))
