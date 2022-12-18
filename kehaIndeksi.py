from math import *
from random import *
print("Tere! Olen sinu uus sõber - Python!")
try:
    nimi=str(input("Sisestage oma nimi "))
except: 
    print("ValueError")
print(nimi,"oi kui ilus nimi! \n")
try:
    indeksi=float(input("!  Kas leian Sinu keha indeksi? 0-ei, 1-jah => \n"))
except:
    print("Value Error")
if indeksi==1:
    jah=print("jah")
try:
    pikkus=float(input("Kirjutage oma pikkus "))
    mass=float(input("Kirjutage oma kaal "))
    indeks=float(mass/(0.01*pikkus)**2)
    print(nimi,'!Sinu keha indeks on:',indeks,round(indeks,1))
    if indeks<16:
        print("Tervisele ohtlik alakaal")
    elif indeks<=19 and indeks>16:
        print("Alakaal")
    elif indeks<=25 and indeks>19:
        print("Normaalkaal")
    elif indeks<=30 and indeks>25:
        print("Ülekaal")
    elif indeks<=35 and indeks>30:
        print("Rasvumine")
    elif indeks<=40 and indeks>35:
        print("Tugev rasvumine")
    elif indeks>=35:
        print("Tervisele ohtlik rasvumine")
        print()
except:
    print("Value Error")
    print("Kohtumiseni,",nimi,'!Igavesti Sinu, Python!')
else:
    print("Kahju! See on väga kasulik info!")
    print()
    exit
   