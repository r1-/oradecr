#!/usr/bin/python2

from Crypto.Cipher import AES
from Crypto.Hash import MD5
from sys import argv

import binascii

if len(argv) != 5:
    print "usage : "+argv[0]+"<Server AUTH_SESSKEY> <Client AUTH_SESSKEY> <AUTH_PASSWORD> <spare4 'T' part>"
    exit()

S_AUTH_SESSKEY=argv[1]
if len(S_AUTH_SESSKEY) != 96:
    print "Bad Server AUTH_SESSKEY format"
    exit()

C_AUTH_SESSKEY=argv[2]
if len(C_AUTH_SESSKEY) != 96:
    print "Bad Client AUTH_SESSKEY format"
    exit()

AUTH_PASSWORD=argv[3]
if len(AUTH_PASSWORD) != 64:
    print "Bad AUTH_PASSWORD format"
    exit()

SPARE4=argv[4]
if SPARE4[0]=='T':
    SPARE4=SPARE4[2:]
if len(SPARE4) == 160:
    SPARE4=SPARE4[:128]
if len(SPARE4) != 128:
    print "Bad spare4 format"
    exit()
SPARE4=SPARE4[:64]

iv='\x00'*16
password_hash=binascii.unhexlify(SPARE4)

cipher = AES.new(password_hash,AES.MODE_CBC, iv)
DEC_S_AUTH_SESSKEY=cipher.decrypt(binascii.unhexlify(S_AUTH_SESSKEY))

cipher = AES.new(password_hash,AES.MODE_CBC, iv)
DEC_C_AUTH_SESSKEY=cipher.decrypt(binascii.unhexlify(C_AUTH_SESSKEY))

key=''
for i in range(0, 32):
   key+=chr((ord(DEC_S_AUTH_SESSKEY[i+16])^ord(DEC_C_AUTH_SESSKEY[i+16])))

key_mod=MD5.new(key[:16]).digest()
key_mod+=MD5.new(key[16:]).digest()

cipher = AES.new(key_mod,AES.MODE_CBC, iv)
password=cipher.decrypt(binascii.unhexlify(AUTH_PASSWORD))

print "Password : "+ password[16:]
