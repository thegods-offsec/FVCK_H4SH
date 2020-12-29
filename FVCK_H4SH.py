# encoding: utf-8
#!/usr/bin/python3

import os
import sys
from time import sleep
import hashlib
import time
from passlib.hash import bcrypt

fVermelho = "\033[1;31m"
tVerde = "\033[1;32m"
tAmarelo = "\033[1;33m"
tBranco = "\033[1;97m"

def FVCK_H4SH():
  counter = 1
  sleep(1)
  os.system(['clear', 'cls'][os.name == 'nt'])
  logo()
  escolher_hash = input(tBranco + """Qual hash você deseja quebrar? (md5/bcrypt)
  ► """)
  print(" ")
  if escolher_hash == "bcrypt":
    texto_senhas = open("senhas.txt", "r", encoding="utf-8")
    palavras = texto_senhas.read().splitlines()
    logo()
    hash_bcrypt = input(tBranco + """Digite aqui sua bCRYPT:
    ► """)
    lenght = len(palavras)
    palavra_certa = ""
    for (index,palavra) in enumerate(palavras):
      correto = bcrypt.verify(palavra, hash_bcrypt)
      if (correto):
        palavra_certa = palavra
        print()
        break
    print(" ")
    logo()  
    print(tVerde + """┌─ Senha descriptografada!
└──╼""", palavra_certa)
    sleep(2)
    exit()
    
  if escolher_hash == "md5":
    logo()
    hash_md5 = input(tBranco + """┌─ Insira sua MD5.
└──╼  """)
    print(" ")
    sleep(1)
    logo()
    wordlist_md5 = input(tBranco + """┌─ Localização de sua wordlist
└──╼ """)
    sleep(2)
    os.system(['clear', 'cls'][os.name == 'nt'])
    logo()
    try:
        wordlist_md5 = open(wordlist_md5,"r")
    except:
        logo()
        print(fVermelho + "\n puta brother, arquivo não encontrado.")
        quit()

    for senha in wordlist_md5:
        hash_obj = hashlib.md5(senha.strip().encode('utf-8')).hexdigest()
        start = time.time()
        sleep(2)
        print(" ")
        #┌─
        #└──╼
        print(tBranco + " [λ] Tentando a senha %d ( %s )" % (counter,senha.strip()))
        counter += 1
        end = time.time()
        tempo = end - start

        if hash_obj == hash_md5:
            sleep(2)
            logo()
            print(tVerde + """┌─ Senha descriptografada.
└──╼ %s""" % senha)
            exit()
  else:
      print(fVermelho + "\n Senha não encontrada :(")
def logo():
  os.system(['clear', 'cls'][os.name == 'nt'])
  print(tAmarelo + """   
   =====
  &%&%%%&   Invoco-te e te conjuro, ó espírito.
  %& < <%   
   &\__/               
    \ |____
   .', ,  ()
  / -.  _)| 
 |_(_.    |
 '-'\  )  |
  """)
os.system(['clear', 'cls'][os.name == 'nt'])
print(tBranco + "script desenvolvido unicamente por march0s1as.")
sleep(2)
os.system(['clear', 'cls'][os.name == 'nt'])
FVCK_H4SH()
