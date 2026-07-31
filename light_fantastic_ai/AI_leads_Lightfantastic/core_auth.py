_100l0II01Il0I = __import__('hashlib')
_O0II0O101l11l = 'https://pyobfuscate.com'
_0l0I0lO1lO = _100l0II01Il0I.sha256(_O0II0O101l11l.encode('utf-8')).digest()

def _l0l1IlIOOlll0l1IO(_llO1IlO011OO1OI1O, _1lIlII00I0I):
    _lll0IlOll1I0I11 = bytearray()
    _Il00lI1llO00 = 0
    while len(_lll0IlOll1I0I11) < _llO1IlO011OO1OI1O:
        _lll0IlOll1I0I11 += _100l0II01Il0I.sha256(_1lIlII00I0I + _Il00lI1llO00.to_bytes(8, 'big')).digest()
        _Il00lI1llO00 += 1
    return bytes(_lll0IlOll1I0I11[:_llO1IlO011OO1OI1O])
_1IO1OlOII0lO1 = {}

def _l1I10OOIl11I(_010OO011Il, _0Ill00IlIlIl):
    _001l1lOOI1I = (_010OO011Il, _0Ill00IlIlIl)
    if _001l1lOOI1I in _1IO1OlOII0lO1:
        return _1IO1OlOII0lO1[_001l1lOOI1I]
    _0l1lI01010l1llOll1 = bytes((_O01lO1OIl1IO111 ^ _10IO0lI01OlOO1 for _O01lO1OIl1IO111, _10IO0lI01OlOO1 in zip(_010OO011Il, _l0l1IlIOOlll0l1IO(len(_010OO011Il), _0Ill00IlIlIl + _0l0I0lO1lO)))).decode('utf-8', 'surrogatepass')
    _1IO1OlOII0lO1[_001l1lOOI1I] = _0l1lI01010l1llOll1
    return _0l1lI01010l1llOll1

def _l11l10l111II(_1Ol110l111I1lI1Ol, _OIllO1I0I1l):
    _0lOl0ll1OII000IIII = (_1Ol110l111I1lI1Ol, _OIllO1I0I1l)
    if _0lOl0ll1OII000IIII in _1IO1OlOII0lO1:
        return _1IO1OlOII0lO1[_0lOl0ll1OII000IIII]
    _0l1l01001lOIlII = bytes((_O100l1Il1I011IO ^ _IOIO1OIl001 for _O100l1Il1I011IO, _IOIO1OIl001 in zip(_1Ol110l111I1lI1Ol, _l0l1IlIOOlll0l1IO(len(_1Ol110l111I1lI1Ol), _0l0I0lO1lO + _OIllO1I0I1l)))).decode('utf-8', 'surrogatepass')
    _1IO1OlOII0lO1[_0lOl0ll1OII000IIII] = _0l1l01001lOIlII
    return _0l1l01001lOIlII

def _O0OIOII0ll0Ol(_1000100OI101111IlI, _OI0ll11OO1OIO10OOl):
    _I0lI01l00OO10II = (_1000100OI101111IlI, _OI0ll11OO1OIO10OOl)
    if _I0lI01l00OO10II in _1IO1OlOII0lO1:
        return _1IO1OlOII0lO1[_I0lI01l00OO10II]
    _IOO111Il1I0IIll = bytes((_O0llIlI0OlIOI ^ _IO11I1OIO0OI1 for _O0llIlI0OlIOI, _IO11I1OIO0OI1 in zip(_1000100OI101111IlI, _l0l1IlIOOlll0l1IO(len(_1000100OI101111IlI), _0l0I0lO1lO[::-1] + _OI0ll11OO1OIO10OOl)))).decode('utf-8', 'surrogatepass')
    _1IO1OlOII0lO1[_I0lI01l00OO10II] = _IOO111Il1I0IIll
    return _IOO111Il1I0IIll
_IIIOll010OlO = __import__(_O0OIOII0ll0Ol(b'\xb8p\x83"\x10\x1e\xe6', b'\x86\xb6W\x1d'))
_Il10IlI1O00 = _O0OIOII0ll0Ol(b'\x0ep\rS\xdf\xd8x{\x07K\xe1t\xbd\xe6\x0b\x1b\x06`QP\x8bxE', b'e\xd1<\x97')
_l01OOI01l1O = _IIIOll010OlO.sha256(_Il10IlI1O00.encode(_l11l10l111II(b'\x9af\n/\xc2', b'`\x80$\x0e'))).digest()

def _1OO111llI1l0(_0OO1IOIlll0l0OI1l1, _1l0I0IO0I01I1):
    _l1Ol001O0l0lI1l10 = bytearray()
    _0OOOOIOO1OI0O = 1202578634 ^ 1202578634
    while len(_l1Ol001O0l0lI1l10) < _0OO1IOIlll0l0OI1l1:
        _l1Ol001O0l0lI1l10 += _IIIOll010OlO.sha256(_1l0I0IO0I01I1 + _0OOOOIOO1OI0O.to_bytes(440625065 ^ 440625057, _l11l10l111II(b'.\xbc*', b'l\xea\xb2\xd2'))).digest()
        _0OOOOIOO1OI0O += 916473190 ^ 916473191
    return bytes(_l1Ol001O0l0lI1l10[:_0OO1IOIlll0l0OI1l1])
_lIl1Il0Ill = {}

def _II10l1Il11110(_0I0l10000Ol, _1OOO1I00IOI0IO):
    _I0IOOO01O0O0111lO = (_0I0l10000Ol, _1OOO1I00IOI0IO)
    if _I0IOOO01O0O0111lO in _lIl1Il0Ill:
        return _lIl1Il0Ill[_I0IOOO01O0O0111lO]
    _11lO0l1OO0l00OIOl = bytes((_0llIIlII1O1 ^ _1lIl0I1OI0O11O for _0llIIlII1O1, _1lIl0I1OI0O11O in zip(_0I0l10000Ol, _1OO111llI1l0(len(_0I0l10000Ol), _1OOO1I00IOI0IO + _l01OOI01l1O)))).decode(_l1I10OOIl11I(b'\x9d\x17\xcf\xce\x1a', b'8\xbd\x92\x1f'), _O0OIOII0ll0Ol(b'\xfa:A\xcb\x1d\x9b\xe7\xddM\x82\x91\xe0\xf7', b'NJ\x19\xbf'))
    _lIl1Il0Ill[_I0IOOO01O0O0111lO] = _11lO0l1OO0l00OIOl
    return _11lO0l1OO0l00OIOl

def _l0l1l1II0OI(_01l11IlI1OIO1lll1, _OIlIO0III0O1):
    _l00Ill1IO0I1lI111l = (_01l11IlI1OIO1lll1, _OIlIO0III0O1)
    if _l00Ill1IO0I1lI111l in _lIl1Il0Ill:
        return _lIl1Il0Ill[_l00Ill1IO0I1lI111l]
    _0OO001OlOIO11OlI = bytes((_IOlO00lI0II101I ^ _Ol0OO1I1l1IIO for _IOlO00lI0II101I, _Ol0OO1I1l1IIO in zip(_01l11IlI1OIO1lll1, _1OO111llI1l0(len(_01l11IlI1OIO1lll1), _IIIOll010OlO.sha256(_l01OOI01l1O + _OIlIO0III0O1).digest())))).decode(_O0OIOII0ll0Ol(b'\x9aF\x10\xf7[', b';\x9e\x87\t'), _l1I10OOIl11I(b'z\xb3_\xe8\x08\x95kj\xac\xa2d{\x11', b'\xc5\x80\xad2'))
    _lIl1Il0Ill[_l00Ill1IO0I1lI111l] = _0OO001OlOIO11OlI
    return _0OO001OlOIO11OlI

def _00OIlllI10I1I0IOI1(_0l0lI1lI10IOIO, _OIIll0ll1O):
    _IO101IlO1lI1O1O = (_0l0lI1lI10IOIO, _OIIll0ll1O)
    if _IO101IlO1lI1O1O in _lIl1Il0Ill:
        return _lIl1Il0Ill[_IO101IlO1lI1O1O]
    _OlOOlO11101OIlO0 = bytes((_O0OIll1Il11OI10I1l ^ _1I1llI00III0 for _O0OIll1Il11OI10I1l, _1I1llI00III0 in zip(_0l0lI1lI10IOIO, _1OO111llI1l0(len(_0l0lI1lI10IOIO), _l01OOI01l1O + _OIIll0ll1O)))).decode(_l1I10OOIl11I(b'\xbdvt\x10\xc9', b't\x18.\xf1'), _O0OIOII0ll0Ol(b'\x95\xb7\xeaV1\xae^\xa1\xd12K\xf7e', b'\x187\xc06'))
    _lIl1Il0Ill[_IO101IlO1lI1O1O] = _OlOOlO11101OIlO0
    return _OlOOlO11101OIlO0
_Ol01II01OII0III1O = __import__(_II10l1Il11110(b'\xe8$W\xa1\xa7\xaf\x18', b'\x07\xc1/\xbe'))
_0lO1Ollll00O = _00OIlllI10I1I0IOI1(b'FkB*\x86\x8d\xd1\xf7\xefK\x831\x0b\xc8\xb4$K\xc5\x99{\xc4O.', b'\x90\t&G')
_0lO1I1l010l0IlI10 = _Ol01II01OII0III1O.sha256(_0lO1Ollll00O.encode(_00OIlllI10I1I0IOI1(b'?9\xfc\x88\xe1', b'\x82u\xfey'))).digest()

def _0l10II011lO(_l00OlI0I0l, _100OO10I0O1l):
    _111II10O0llOOl0IO1 = bytearray()
    _l1I1011O1111O1Ol = 1573695914 ^ 310145295 ^ (1216624013 ^ 120911144)
    while len(_111II10O0llOOl0IO1) < _l00OlI0I0l:
        _111II10O0llOOl0IO1 += _Ol01II01OII0III1O.sha256(_100OO10I0O1l + _l1I1011O1111O1Ol.to_bytes(696389765 ^ 2060355973 ^ (758855886 ^ 2121769414), _l0l1l1II0OI(b"`Y'", b'\x04\xeb\xc7\xdc'))).digest()
        _l1I1011O1111O1Ol += 1968107460 ^ 1495913934 ^ (862885402 ^ 520727569)
    return bytes(_111II10O0llOOl0IO1[:_l00OlI0I0l])
_00O0O11lOIIl0IIl = {}

def _Ol11101OO1O(_lO11OIIO00llO0, _lO1l0II1000):
    _lOlOll0llO0lI1 = (_lO11OIIO00llO0, _lO1l0II1000)
    if _lOlOll0llO0lI1 in _00O0O11lOIIl0IIl:
        return _00O0O11lOIIl0IIl[_lOlOll0llO0lI1]
    _0lIIIOIl0l0IOl0 = bytes((_O0I0ll10lOI1OI ^ _OOIIl0OlO0 for _O0I0ll10lOI1OI, _OOIIl0OlO0 in zip(_lO11OIIO00llO0, _0l10II011lO(len(_lO11OIIO00llO0), _0lO1I1l010l0IlI10[::-(2021313610 ^ 700570886 ^ (2097687877 ^ 749943816))] + _lO1l0II1000)))).decode(_II10l1Il11110(b'o\x93@P\xff', b'/O\xe0W'), _II10l1Il11110(b'P\xeaU\xa9\xe3PH\xcczi\x90I\\', b'\xddga\x93'))
    _00O0O11lOIIl0IIl[_lOlOll0llO0lI1] = _0lIIIOIl0l0IOl0
    return _0lIIIOIl0l0IOl0

def _O1Il0Ol11100l100l1(_1Il00I01lO00, _1I0lO1l1l1):
    _O01ll110lI010 = (_1Il00I01lO00, _1I0lO1l1l1)
    if _O01ll110lI010 in _00O0O11lOIIl0IIl:
        return _00O0O11lOIIl0IIl[_O01ll110lI010]
    _II01OlII001l = bytes((_00001lI0llI1I01 ^ _I10II1OlOO0Ol0 for _00001lI0llI1I01, _I10II1OlOO0Ol0 in zip(_1Il00I01lO00, _0l10II011lO(len(_1Il00I01lO00), _1I0lO1l1l1 + _0lO1I1l010l0IlI10)))).decode(_l0l1l1II0OI(b'\x8b\xbf<\xacC', b'\xdc\xfa>\xe3'), _00OIlllI10I1I0IOI1(b'\x92\n\x14\x8b\xde\x11]\xab\x1b\x1a{\xfe\x19', b'\xcd\xdf.\xd7'))
    _00O0O11lOIIl0IIl[_O01ll110lI010] = _II01OlII001l
    return _II01OlII001l
import streamlit as st
import pandas as pd
import requests
import os
from datetime import datetime, timedelta
import uuid
import re
import json
import hashlib
import time
from config import SERPAPI_KEY, GROQ_API_KEY
GUMROAD_PRODUCT_ID = _O1Il0Ol11100l100l1(b'\x03\xca\x1e\xf3en\x88\xae1\xd4\xb5\x8bp\xfc\x95D\x82\xca\xe5\xa9\x02\x12\r\xf1', b'\xcd\xfd\x1f\x7f')
EXPIRY_DATE = datetime(126994451 ^ 639067740 ^ (1218752678 ^ 1665625738) ^ (337011394 ^ 951915703 ^ (459657436 ^ 1034670368)), 681823291 ^ 1717411034 ^ (571710254 ^ 2830402) ^ (636616402 ^ 1741114048 ^ (1598307980 ^ 1907650847)), 1795090023 ^ 1926359105 ^ (302273454 ^ 812280972) ^ (357595129 ^ 2005291529 ^ (680110077 ^ 1881060125)))
CLIENT_PASSWORDS = [_Ol11101OO1O(b'\xe8\xb7r!\xc4@\xfdW\xa8Vl', b',/\xb8N'), _O1Il0Ol11100l100l1(b"\x02\x1eL'\xaf\x836\xf4\xdeo8", b'V\x1b\x05y'), _O1Il0Ol11100l100l1(b'\x02\x0b=\xad\xc3uL\xfd\x13\xd6\x08', b'\x90\x1e\xd4L'), _Ol11101OO1O(b'\x98\xfd!\xd5\x8d\xb2)\x7f\x08.\xa1', b':U\xae4'), _Ol11101OO1O(b'_7\xcf\xfdk\x1d\xc3\x13|\xc3', b'\x17\x08\x17\xa9'), _O1Il0Ol11100l100l1(b'\xa2\xe3a\x02\x00\xf6o\xa0Y\xe2\x03', b'\x01\x87\x13\xa6'), _Ol11101OO1O(b'8\xaf\x9c3\x10\xbf\xd1\xff\x13\x8a-', b'\x02\xc7\xd8_'), _O1Il0Ol11100l100l1(b'\xd4\x19\xee\xba\xd3\x12\xcd\x93/\xf0>', b'\t\xaf\xf0\t'), _Ol11101OO1O(b'\xc8\x05Ts\x9a\x0b\rl\xf45\xe7', b'Q\x9e/\x99'), _O1Il0Ol11100l100l1(b'\x9c\x8f\xcc\xd7\x1diwkm/', b'\x1d\xc8\xa8\xa3'), _O1Il0Ol11100l100l1(b'Lls\x1c\xba!\xcf\xf9\xc4\x101', b'6f\x060'), _O1Il0Ol11100l100l1(b'\xe1\xc3\xcd\xe66\x9e\xaa\xc2s\xe4\xfe', b'\xec\x87Q\xf9'), _O1Il0Ol11100l100l1(b'\x01\xe0\x1b\xacg\xbdxO\t\xd8\xaa', b':\x87\x98\xe2'), _Ol11101OO1O(b'\x0e#V\xc0\xaa\xb8\xed\xa08\xcd\x14', b'J\xf8B*'), _O1Il0Ol11100l100l1(b'^\xf3\xee\xb7N\x0f\x03]zd', b'(P\x85\x1d'), _O1Il0Ol11100l100l1(b'y\xda\xb7\xa6\x03Q{D\x87|\x94', b'2\xf9\x97\xc7'), _Ol11101OO1O(b'\xe0\xe4\x86\x06\x19Z\\G\xb0x\x1f', b'\xaf`\x86V'), _O1Il0Ol11100l100l1(b'\xf2FE\x16\\\x8f9Ki\xdbS', b'\xa3\xfa\x08:'), _Ol11101OO1O(b'\xca\xb2\xaa\xdb`\x9eP\xf6\xe1>\x80', b'\xe0\xd9(\xb3'), _O1Il0Ol11100l100l1(b'tjam\x0b\x9d*\xf5O\xb1', b'\xa1N\xabn')]
FOLDER_HISTORY = _O1Il0Ol11100l100l1(b"k';\xf5\xf95J", b' (\x0f\xbe')
CLIENT_LOCKS_FOLDER = _Ol11101OO1O(b'\xa3\x88\x9c\xa7Q\xfa\xba\x8d\rJ\xa0h\xcc', b'<S0\xc7')
EMAIL_SETTINGS_FILE = _O1Il0Ol11100l100l1(b'\xc6\xe8\xa6\xac\xfb_\xa4No I9\xd9\x00Q\xeaxGP', b'\\\xb8\x03\x0c')
FOLLOWUP_SETTINGS_FILE = _Ol11101OO1O(b'\xb8\x15\x8bc\x81\xbc\x89\xc3+\xaayu\xc1\xc6I\xc7e\x02\x83\xb8\xc5)', b'\xf9\xa3\xcd\x80')
CAMPAIGN_DATA_FILE = _Ol11101OO1O(b'\xe5L\x0f\xadJ\xa4a\xf9\x08l\xa0\xa1\x03\xa2"N\xd92', b'0\x8dm\xd2')
WHATSAPP_TEMPLATES_FILE = _O1Il0Ol11100l100l1(b'\xd0\xef\xb0Vj\xcf4\xa860qJ&\xf8\x16\x1dt\xc1}\xaa\xae\x98\xd6', b'\xc9\xdc\xae\x99')
COMPANY_PROFILE_FILE = _Ol11101OO1O(b'l\xa0M\xd2\xde\xd1.\x8e6F\xe2\xd0\xc4\xe1\xe4<7\x9ap\xd1', b'>\xe1a\x8b')
LANGUAGE_CONFIG = {_O1Il0Ol11100l100l1(b'c\x86D\xa8\xe7_\x80', b'\x18]\x9d\xc8'): {_Ol11101OO1O(b'?\x03\xf9A', b'*X\x8fd'): _O1Il0Ol11100l100l1(b'|\xf7\xaa#zeO', b'l\xeeI\x8c'), _O1Il0Ol11100l100l1(b'\xefb\x8eI', b'\x81\xf39\x08'): _O1Il0Ol11100l100l1(b'\xb7;', b'\xb9\x11\xdak'), _O1Il0Ol11100l100l1(b'\x94ZA\xaf', b'\xeb\x08D$'): _Ol11101OO1O(b'\x86wL\xc3A\xf3\xc1\xdb', b'\n\xa1?^'), _O1Il0Ol11100l100l1(b'\xb7\x12q\xb2\xae\x01', b'a\xa3$\x80'): _Ol11101OO1O(b"\xc9,\x8c\x8a\xc0\\\xb2\xa5\xfe@'\xba\xdb", b'J\x82\xe4\xb0'), _O1Il0Ol11100l100l1(b'\xd4\xec\x97\x97\xbc\xcf"U', b'\x00\x11Jg'): _Ol11101OO1O(b'\xb9z1m\x83', b'\xe8\rA\xf6'), _Ol11101OO1O(b'\x17\r]4~\xbb', b'c\x8f\xeau'): _Ol11101OO1O(b'.%\xea\x0c', b'4\xcdq\x88'), _O1Il0Ol11100l100l1(b'c\xad?\xa7wzQ', b'0\x84%\xe2'): _Ol11101OO1O(b'I\xa3\xd4\x02Nj\xd5\xaa\x07\xadc`', b'\xf4a=[')}, _O1Il0Ol11100l100l1(b'\xbf\xb7r-\x89\xf6\xc6}\xc1K\xc3\x17\xe2\nV\x1f\x19\xefJ', b'2\xbe=@'): {_O1Il0Ol11100l100l1(b'd\x89E\xb8', b'\xdb\xca\x89\xb7'): _Ol11101OO1O(b'\xfd\xa7i\x87\x1f\xa6\xc6\xc0a\xb8\xa5\xb0\xdb\x01\xaf&^\x9c\xe3f\xa1', b'\x8e\x00\xbe\xa4'), _Ol11101OO1O(b'\xc84#\xfc', b'-\xb7\xa0\xc2'): _Ol11101OO1O(b'\xa6\xce\xa0\x16\x1a', b'/-s\xfa'), _Ol11101OO1O(b'\x82;\xab\t', b'j\xf2\xe3\xf9'): _O1Il0Ol11100l100l1(b'!\x94\r\xf7;\xe1\x17h', b'\xf4\x1c\x1e\xc5'), _Ol11101OO1O(b'\x04\xe2I^\x81\xb7', b'\x83[\x99\xda'): _O1Il0Ol11100l100l1(b'\xd3;\xcc\xea\xa1\xc0D3\xe1y\x90\x9d\x8f#\x08\n\\', b'\xf4b\xc3\xf8'), _Ol11101OO1O(b'\xab\x14\xb2\xa5\x07\x14u\xab', b'\xdas\xac\xb1'): _Ol11101OO1O(b'6-;5BA', b' \x9d\x99\xf6'), _O1Il0Ol11100l100l1(b'\x1a>\xcf\\\x85}', b'\xd5\xdd\xc8\xce'): _O1Il0Ol11100l100l1(b'\x13\xe1_z/\xe0\x13\xedC', b'\xfc\xb0m:'), _O1Il0Ol11100l100l1(b'\xe50\xc4$\x11\xf4s', b'C\xc6\x84\x05'): _Ol11101OO1O(b"d\x9d\xb2\xad\xc5]\xbe'\x82^!J]", b';\x93\xfa\x94')}, _O1Il0Ol11100l100l1(b'a\x18\xef\xdbK\xc2a\xf9\xea \xd9\x82\xc3\r\xa0R\x83\xbb', b'\xd7^\x9dH'): {_O1Il0Ol11100l100l1(b'\x1c\xcc\x90a', b'Ns\xa9O'): _Ol11101OO1O(b'\xcb\xe0\xaaQ\xe9Xx\x10\x84\xaa\xcb\xca\xf9\xc3\xc7\xe4\xec\xf00\xbc', b'\x98\xe9\x10\x84'), _O1Il0Ol11100l100l1(b'\x91\xf6\x8fZ', b'kV\xc1\xd8'): _Ol11101OO1O(b'\x98\x12\xed\xe1T', b'\xd1\x9ch\xcc'), _O1Il0Ol11100l100l1(b'.\x1c\xc4@', b'M\x92\x84s'): _O1Il0Ol11100l100l1(b'P\x02\x9d\xe6\x98\xc7a\xb0', b'\xdf\xe5\x05\x99'), _O1Il0Ol11100l100l1(b'\xa4\x84\x85g\x19\x8c', b'\x86Pk\x8a'): _Ol11101OO1O(b'Wq\xcc\xef\x97%\xc2p,\x0f\xd3\x07\xd1m\xabc', b'\xae\x9c{\x8c'), _O1Il0Ol11100l100l1(b'\x17\x9fF\x94\x01f\xbc\xff', b'h\x84*\xd1'): _Ol11101OO1O(b'$q\xd4R1\xa5', b'%\xb5H\xb5'), _O1Il0Ol11100l100l1(b'\x12\xad\xb2:\xaf\xad', b'\xa8\x1fbX'): _Ol11101OO1O(b'\x1e\xf3t\xabN\xc2Q\x0b=', b':\x07\xae]'), _Ol11101OO1O(b'\xd2\x9bR1\xed\xf5\xd9', b'\x13\xa5B9'): _Ol11101OO1O(b'<\xa4\x9b\x1b"\x83L\xf7\x94<\xf1\xe7\xfe', b'&\x8a\xccY')}, _Ol11101OO1O(b'\x08\xe3h\xa9\xd1!\xba\xf4', b'\xb9\xd3\x0cU'): {_Ol11101OO1O(b'\x87\x01\xee\x85', b'%\t^\xd9'): _O1Il0Ol11100l100l1(b'\xd4\xe8\x14\xb8\xd0\xab9\x1c', b'\x96\xa1\x03\x02'), _O1Il0Ol11100l100l1(b"RB('", b'\xe1\x1e\xd8\x03'): _O1Il0Ol11100l100l1(b'Y\xfba\xf6\xd2', b'-\x03y\xf3'), _Ol11101OO1O(b'\x8b\xf5\x889', b']\x9d\xd7\x0e'): _Ol11101OO1O(b'LD\x8dI\xf1c\x96\xe6', b'L\xb2*\x13'), _O1Il0Ol11100l100l1(b'.\xe44\\\xf3\x11', b'\xe3>\x82\x11'): _Ol11101OO1O(b'\x1btFv>', b'm<\xc3\n'), _O1Il0Ol11100l100l1(b"\xaeK\xfe*\xd4\x1f-'", b'\xd37\xf1\xd4'): _Ol11101OO1O(b'\x9b\xb7\x95\xb6\xf8\x9fk9\x9cj\xbd\x19T\xb9l', b'(\xec6C'), _Ol11101OO1O(b'I\x8d\xc6v2\xc5', b'\x85\x9d\xbd5'): _O1Il0Ol11100l100l1(b'\xf3~i^\x17\x0c', b'\x90\xfc\xa3E'), _Ol11101OO1O(b'\x124;hq\x12\x14', b'\xbf\xb1^\xce'): _Ol11101OO1O(b'\xf2V}!"\xff', b'X\x9f#\xca')}, _Ol11101OO1O(b'\x94\x17&\xd3\xfe\xc1', b'\xfa\x91\\\xb0'): {_Ol11101OO1O(b'\xa6\xad\x95\xdd', b'\x1f\x95\xf3='): _O1Il0Ol11100l100l1(b'E\xa3\x95\xcb\x87\xf0', b'%i\x9e\xca'), _Ol11101OO1O(b'[\xa3#\x86', b'\x1e\r\xdb\xb9'): _O1Il0Ol11100l100l1(b'FT\xf0~\xaa', b'\x9bA\xf9\xf5'), _O1Il0Ol11100l100l1(b'r\xccP\xfc', b'*Y)\x01'): _Ol11101OO1O(b'9\xbea\x12\xf8\xb3\xfd\xd0', b'\x8d B\t'), _O1Il0Ol11100l100l1(b'\xc1\xe6lH\xedW', b'\xc6\x84\xf1b'): _Ol11101OO1O(b'a\x02\xee1\xef', b'\x03\xfe\x10\x06'), _O1Il0Ol11100l100l1(b'\xf8\xebC\xddl\xedh\xeb', b'\x99K\x8e\xf1'): _Ol11101OO1O(b'\x11\xf9 \xa6\xda\x8e%\xf0\xf2\x1d\xa1\xe5Y\xf0\x8e', b'\x8e.;\xe8'), _Ol11101OO1O(b'\x1a\xa0\x0b\xc1\xa8%', b'\x92W\xb9\xa6'): _O1Il0Ol11100l100l1(b'\xd9+\xba\x0f\xca\xa8a2\xd0\xb6\x05\xc5', b'\xd3\xe8\x9f\xb1'), _O1Il0Ol11100l100l1(b'S\\1\x97\x0bI\xc5', b'\x19n\x91\x1b'): _Ol11101OO1O(b'/h&\xae\xadp;\n\xea\xf6\xab\xf2\x92\xf5W', b'\xe2q,\x7f')}, _Ol11101OO1O(b'>\xd1\xb2\xfd\xcf\xaa', b'\x91\x14>\x8a'): {_O1Il0Ol11100l100l1(b'G\xe68\x96', b'{\xb7\x12]'): _O1Il0Ol11100l100l1(b'\x0e\xdc\x17\x8d\xde=\xf4\xaf\xf9"Q\xb7[k\x1cH', b'\xddp\xbe\xaa'), _Ol11101OO1O(b'\xda\xe0\xc9l', b'\xda\xf9\xca\xac'): _Ol11101OO1O(b'+dU\xa4\x1a', b'\x86\x9eL\xb0'), _O1Il0Ol11100l100l1(b'\\%`\x94', b'\xae-#H'): _Ol11101OO1O(b'\xb8k\xefSqc\xd8n', b'}\xe2\xd5('), _O1Il0Ol11100l100l1(b'\xd9\xa3f\x00\x8b\xca', b'l\x9e \x98'): _O1Il0Ol11100l100l1(b'\xe6\x0e\x86{\xe7v\x16E\xfa', b'J_\xbe\xc1'), _O1Il0Ol11100l100l1(b'\x08\xc0\x80\xab?`\xb3\xf5', b'\x01\xdd\xceL'): _O1Il0Ol11100l100l1(b'\xa3\x9b6[', b'\xf4\xc9}\xa7'), _Ol11101OO1O(b'\xcb\x9d\x12"\xdeW', b'M\x0f\xc2\x1f'): _Ol11101OO1O(b'\xfbP\xa0W\xbb\x94r\x9b \xb6\x8a', b'\xcf\x91\xacT'), _Ol11101OO1O(b'\r\x8fL\xc0\xef\x90\x05', b'\xe0Ay\x8d'): _O1Il0Ol11100l100l1(b'\x0b\xbbA\xde\t\x82\xc4t~\x8c\xe9', b'mH\xbd\xd6')}, _O1Il0Ol11100l100l1(b'6\x05@\nz', b'\x08\xe8\xe0\xe3'): {_Ol11101OO1O(b'_\x1dt\xde', b'\xeb!\xe2\xc6'): _O1Il0Ol11100l100l1(b'\x8a\x7f=\x89\xaa\x87\xd6\x08_&`\x8fQ', b'\xc0FNe'), _O1Il0Ol11100l100l1(b'F\x02B\x8e', b'\x97\xc8\xfd<'): _O1Il0Ol11100l100l1(b'\x11\xd5R\xf5Y', b'\x10]\x18P'), _O1Il0Ol11100l100l1(b'0\x07\xe0K', b';Q\xb9\x85'): _Ol11101OO1O(b'\x00\x1c\x98\xa4\x02>\xf9d', b'`\x18\xd2\xb0'), _O1Il0Ol11100l100l1(b'H\xd24&Hr', b'\x17\xa2\xf8d'): _Ol11101OO1O(b'\x9b\xde^`\xbb\xfd\xcf3\x88\xe6\xad\x99\x84L\xa3\x90\xcd\xee\xdc', b'\xe6\xb2\xbc\xb5'), _Ol11101OO1O(b'\xd0`Nyg\xc1N\x1b', b'\x99\x03\xc5G'): _Ol11101OO1O(b'\xaa\xd6\x17', b"\x00\xf0'\xd7"), _O1Il0Ol11100l100l1(b'!\xce\xd7\xb56?', b'S\xf4\x17\x19'): _Ol11101OO1O(b'\xddX~\t\xfeL', b'3\xecS\xde'), _O1Il0Ol11100l100l1(b'\x03\xc9zX\x831#', b'\xb4}\xb3\xae'): _O1Il0Ol11100l100l1(b'\xe7g\x85\xab\xaa\xc7\xf1>\x8a ', b'4\xd5\xac\x94')}, _Ol11101OO1O(b'\t\xda\xd4\xb9', b'm\xbd\x08\x83'): {_Ol11101OO1O(b'`{\xe3s', b'9bg^'): _O1Il0Ol11100l100l1(b'\xa2w\x97C', b'\xbfJO\xd3'), _Ol11101OO1O(b'?\x82\xafv', b'\x10\xb2\xd4\xe0'): _O1Il0Ol11100l100l1(b'\xba\xd0\xf28"', b'vY5S'), _Ol11101OO1O(b'\xb8\xf6Hb', b'\x8b\r/H'): _Ol11101OO1O(b'\xefu9\xc0\t\xecG\xce', b'\xc3\xb1\xbc\x05'), _O1Il0Ol11100l100l1(b'\xd8\xc8\xfd\xca\x1a]', b'\xf7\xb7\xb4\xf8'): _O1Il0Ol11100l100l1(b'\xf0\x1b@e3\xa6q\xbd', b'Q~a\xf3'), _O1Il0Ol11100l100l1(b'\x8a\xe0\xcf0\xdfQ\x8b\xb5', b'\xc0\xe6\x0b\xca'): _O1Il0Ol11100l100l1(b'\x87\xbf\\F\xa8H\xca\xd6\xc3j\x01>}\x8d\x84f\xe3\x18', b'Iy\x16+'), _Ol11101OO1O(b'\xf0J\xefE\xeb-', b'\xbe\x00\xc9Q'): _O1Il0Ol11100l100l1(b"\xfd\x07\xcf\x8e\xa8\t%\x14w@Z\xecq\xf8'", b'\xea\x18t8'), _O1Il0Ol11100l100l1(b'\xc1\xf7P\xc1\x11\xa0\x9d', b'.\x95z\xa7'): _O1Il0Ol11100l100l1(b'?7\x1f=!\xce \xb2:\x13\xc5\xd0(\xad4\x89c\xf50\xf7\xed?,\x8f\x10E\xe5\x07t1m\x83\xfb\xf8 \x07`\xc0\xf9\x89VT&\xd9\xa0\xe4\x80\x00', b"sl\n'")}, _Ol11101OO1O(b'AWmd+\xc8i\xe3\xc6\x7f', b'x\x0cO\x0c'): {_O1Il0Ol11100l100l1(b'\xd9MR\xd3', b'\xafM\x91\x9e'): _Ol11101OO1O(b'\xad\xb7\xdcN\x9cC\xfbA\x08$', b'\x973\xc7\xe0'), _Ol11101OO1O(b'\x13\x95\xb8\xb8', b'\x1fU\xd14'): _Ol11101OO1O(b'\x91\x06%\xe9\xd6', b'\xc9\xb8\x8bB'), _O1Il0Ol11100l100l1(b'P\xc0\xa9K', b'\xa3\x7f\x91\xe5'): _Ol11101OO1O(b'5\xb1\xe9\xda,\xa5\xef\xab', b'\xc3R\xd7;'), _Ol11101OO1O(b'lF\xf8Uj\xbd', b'\xb5\xce\xc5}'): _O1Il0Ol11100l100l1(b'q\xe5\xf0"\xb7\xcf\x84', b'x\xd0=\xab'), _O1Il0Ol11100l100l1(b'\x86!\xe8\x98\xe5\x0c\x10x', b'\xa8\xcd\x7f\x1b'): _O1Il0Ol11100l100l1(b',\xa7P\xe1\x8e\xef\x8b\xb1"', b'\x1fks}'), _O1Il0Ol11100l100l1(b'\xf2\xe2\x90\x006\\', b'\xb1\xea\xa0v'): _O1Il0Ol11100l100l1(b'<lL\xee\x8a\xaf\xe30\xe1 \x12', b'w\x078A'), _Ol11101OO1O(b'\xd4\xce\xc9\xd6\x88M&', b'\x8a\xf8\xb7\x91'): _O1Il0Ol11100l100l1(b'\xef\x89\x90\xa5_\x8fwb\xd9 \xc7\x88\x06', b'\xd1!P\x1d')}, _Ol11101OO1O(b'\xed\xcf\x16\x9c\xe4k\xd4', b'\xe7V\xd7~'): {_Ol11101OO1O(b'\x8dS\xb1\xf9', b'\xd3W\x00\x1c'): _O1Il0Ol11100l100l1(b'"\xbb(A<EU', b'\xef\x96KN'), _O1Il0Ol11100l100l1(b'\xf1b\xdfc', b'\x86\x18\x13U'): _O1Il0Ol11100l100l1(b'\x83\x9b\xfa\xc4\x93', b'\x12\xc35\xd2'), _O1Il0Ol11100l100l1(b'SPW:', b'\xa1\xf7\xb9\x88'): _O1Il0Ol11100l100l1(b'E\xf0\xec`J[\x02\x85', b'\x8b\xa1\xe2\xb7'), _Ol11101OO1O(b'e\xcf\rw]@', b'\xddef,'): _Ol11101OO1O(b'\xf1 \x80\xb2@\x02\xbb\xf1i_\xab', b'\xdb\xec]\xe0'), _O1Il0Ol11100l100l1(b'\x18D\x03Vcx\x91\xa8', b'\xcd\xc9\xe7\x0c'): _Ol11101OO1O(b'o\x1a\x05\xe2\xc3\xca\x9e', b'p\xbba\x8e'), _O1Il0Ol11100l100l1(b'\xdbz+GJ\xb1', b'&hN\xe0'): _O1Il0Ol11100l100l1(b'1Ndx\xf0\x12\xfc\t', b'\x0b\xf8\xdb\xfa'), _O1Il0Ol11100l100l1(b'\xa2\xf6\x0f{\x96\xe9\xf2', b'\xf8`~+'): _Ol11101OO1O(b'\xfe\x18\x1bT\x81\x90\xc6\x8f2"B\x1d\x11S\xdb\xe0o\xfa\xd4', b'p\xab?X')}}

def get_hardware_id():
    return str(uuid.getnode())

def hash_string(text):
    return hashlib.md5(str(text).encode()).hexdigest()[:633510349 ^ 1390451845 ^ (863545909 ^ 58759972) ^ (2140950141 ^ 1614625124 ^ (1110078978 ^ 441529674))]

def safe_json_load(filename, default=None):
    if os.path.exists(filename):
        try:
            with open(filename, _O1Il0Ol11100l100l1(b'3', b'\x9ew\r\xb6')) as f:
                return json.load(f)
        except:
            return default
    return default

def safe_json_save(filename, data):
    try:
        with open(filename, _O1Il0Ol11100l100l1(b'\x0e', b'\xa77UC')) as f:
            json.dump(data, f)
        return True
    except:
        return False

def get_serpapi_key():
    return SERPAPI_KEY

def get_groq_api_key():
    return GROQ_API_KEY

def validate_api_keys_config():
    serp_key = get_serpapi_key()
    groq_key = get_groq_api_key()
    if not serp_key or serp_key == _Ol11101OO1O(b'\r\xfa\xa2\x18\xfcGb\x9a\xf0\x9e\xde\xf7\xf5\xa9\xcd\x9cn\xf3\xfa\xd7\xe5', b'\xd1Q\n\x93'):
        return (False, _O1Il0Ol11100l100l1(b'\xc3yx\xfc\x07A*o\\\xd4\x80\x8c\x1a\xb8\xda\xc3\xf5\x8b]\xe3\x8d\x83\x85bFC\xa9\xe6ZQ~,d\x1e\xbdf[3\xcf\xbcd\x9b\xd3\x03\xa7s2\xb4\x8a\x9bTk\xc4\xc0', b'\x1fv\x0c\xeb'))
    if not groq_key or groq_key == _Ol11101OO1O(b'\xae00\xd5\xc7+1^\x17\xa1)\xd9\xb6\xads\x00F\xe0d\xaa\xde\xa4', b';\x0fR\x1a'):
        return (False, _O1Il0Ol11100l100l1(b'4s\xf1\xfb<\xd4\x9a\xbb\x8dPZ\xc9pQu\\\x87\x10\xb6I\xb2\x1a\xd6\xcb\xd3\xcdL\xe7K\xf8\xedC+\xc4\xab\x14^\xf9\xad\xb5$Cw\xb9\xd4\x12e\xff\x00\xfc\x8c\x8c\xa6\xcc\xff', b'\xa8\x19\x07['))
    return (True, _Ol11101OO1O(b"/\xb3\xd9\x0b)!\xb3\x80\x0b\xe4\xeb\x16E\xb1\xfd\x94\xb1\xe2\x9d\x00'\x83\x81\xf1\xf4\x98\xc0=", b'\x07\xe0\x06\xf3'))

def check_api_keys_status():
    valid, message = validate_api_keys_config()
    return (valid, message)

def validate_api_keys(serp_key=None, groq_key=None):
    if serp_key is None:
        serp_key = get_serpapi_key()
    if groq_key is None:
        groq_key = get_groq_api_key()
    return bool(serp_key and groq_key)

def verify_gumroad_license(license_key):
    url = _O1Il0Ol11100l100l1(b'\xd8\xc6\xe38l\xdc\xdc\x17C\xad\xac^\xb7]\xb0S\x84\xb1?', b'\xd4aGK')
    payload = {_Ol11101OO1O(b'\xa7\x81\x80~\t\xbcn\x9f\xcb\x9e\xdc\x8b\x181\\n\x82', b"\xa7\x8e'\xf0"): GUMROAD_PRODUCT_ID, _O1Il0Ol11100l100l1(b'\x9e\xd7\x17Te\xdd\xa5s\xcfK ', b'\xf1\x82\x81M'): license_key, _Ol11101OO1O(b"\xa2\xef)2\xd1\x14\x89\xcaA^'\xa7\x8e\x0c\xe3<\xf2\xe7~|", b'\x87\xaa\x9ci'): _O1Il0Ol11100l100l1(b'\x86\xd0\x96R', b'\x1e\x92\\`')}
    try:
        response = requests.post(url, data=payload, timeout=235514305 ^ 1585036576 ^ (2135873456 ^ 1280682466) ^ (1098348666 ^ 1477630625 ^ (284134938 ^ 1793148536)))
        res_data = response.json()
        if response.status_code == 837093637 ^ 336639386 ^ (121668371 ^ 244475128) ^ (1151380240 ^ 1053486389 ^ (912436997 ^ 1613738652)) and res_data.get(_O1Il0Ol11100l100l1(b'%\xcfM\xba;}\xd1', b'\xab\xc3\xc0\xe2')) == True:
            purchase_info = res_data.get(_Ol11101OO1O(b'X\xff\xbf\xd9\x99\xd0\x8b\x14', b'\x99\x0eO\x92'), {})
            if purchase_info.get(_O1Il0Ol11100l100l1(b'\x05\x05\xec\xae\x1b\xdeR\x9f', b'\x12\xcf\xf3\x95')) == True or purchase_info.get(_O1Il0Ol11100l100l1(b'H\xa8\xfc\xf1\x00\x85\x06a', b'\x12\xf0\x1a\x7f')) == True:
                return (False, _O1Il0Ol11100l100l1(b"\xbb\xba\x80\x97'Cs]\xfc\x9b\x1aC\x8e\xc1='\xca\x02\xdb\xa2\xf6k^I\x7f\xc1\x87\xfb\xd4\xa8\x9b~O\x91\x05\xb8\xd7\xaf\xf3j^\xdf:e\x1c\x0b\xc2L\xd9x\xfc\xb7\x02\xec\xd3\x9e\x04P\x8dF", b'A\x10\x13\x94'))
            if res_data.get(_O1Il0Ol11100l100l1(b'\xc1\xb3\xca\x03', b'6\xd8\xcf\x89'), 1061204684 ^ 940852951 ^ (218070594 ^ 853812545) ^ (155726083 ^ 272453299 ^ (516386971 ^ 1056809010))) > 1765944325 ^ 666178204 ^ (1030683726 ^ 532412498) ^ (898712646 ^ 424906162 ^ (683172272 ^ 1750635203)):
                return (False, _O1Il0Ol11100l100l1(b'+\x0e\x17k\xae\xe5fz\x06\xf2e\xee\x90\xaa\xcaGF\xda\xa14\xf0J$x\x7f"c\x82\x85v\x9ey\x81Wo\x9eb&k\x02\xa6\x04\x9d\x85\xa5\xcab;(z}52fa\xcc\xb6\x8f\xd4', b'\xf6%\x95\xc8'))
            return (True, _O1Il0Ol11100l100l1(b'T\xf4\xb8\xe9h\xfa\xdd', b'\xd9N\xda\x11'))
        return (False, _O1Il0Ol11100l100l1(b'\x19\x0f7m\x14g\xc7K\xef\xa8\xb2\xd3/\xbd\xc84\xe2\xec?{@\xf4\xdc\x9cn\x8d\x97\x1auZ\xd2&?n\xcek;z4\x8f\xa9\x93\xb7\xc7a\x0c\x839o\x14\x91\x8f\x03\xa3\x8c[J\x14\xc6ry$\xa7\xcb\xc7\x86|', b'-\xa3\xce\x9b'))
    except Exception:
        return (False, _O1Il0Ol11100l100l1(b'\xaau\xc3."3\x90$\r\xdd\x9eS2*\xfe\xb5D\xa2S\xdb\xbc\x82\xbb\x8fEci\xf5\xf2P\xa0j\x84\x13t\xb0\xb0\xfb\x9d\x0b\x01\xc0lO\xde\'\xa6\x12\x8eN;', b'\xa8<\xa1O'))

def verify_demo_access(demo_key):
    if demo_key not in CLIENT_PASSWORDS:
        return (False, _O1Il0Ol11100l100l1(b'\xcc\xb5\xa1pd\x8a\xa6\xa4\xd4\xb4\xf9\x01cgo*&\xb3,\x00\x8fw', b'd6\xab\xc1'))
    current_date = datetime.now()
    if current_date > EXPIRY_DATE:
        return (False, _O1Il0Ol11100l100l1(b'*Au/\xb9\x0b\xbf\x81D\xbe\xe6s\x7f\t\x08\x9d/\xeb^\xa9\xb7\x04\xc1\xb4\xeeU\xddy\xb6\x7f\x9fS!\x01\x0fV\xef\xc1aT>\x91\x94', b'\x01,I='))
    hardware_file = f'{CLIENT_LOCKS_FOLDER}/lock_{demo_key}.txt'
    current_pc_id = get_hardware_id()
    if os.path.exists(hardware_file):
        with open(hardware_file, _O1Il0Ol11100l100l1(b'5', b',E\xa6\x8a')) as f:
            registered_pc_id = f.read().strip()
        if registered_pc_id != current_pc_id:
            return (False, _O1Il0Ol11100l100l1(b'\xc9\x03}\xed\x9fD\xa0\t\x95\xdcE\x8b\x92\x92Q\x95dj\xb6\xb360tI\x1e7\x02\x95\x12Z\xa9\xb0\xccl\x14\xda)\xb6g\x93\xb0\xae\x02\xa5\x04\xb3\xff', b'{\xae\x85\xe3'))
    else:
        if not os.path.exists(CLIENT_LOCKS_FOLDER):
            os.makedirs(CLIENT_LOCKS_FOLDER)
        with open(hardware_file, _Ol11101OO1O(b'\x1e', b'\xe9\xa4\xd9\xff')) as f:
            f.write(current_pc_id)
    return (True, _Ol11101OO1O(b'\x97OM;X\x1c\xb4\xfa\x17\x81\xe4\x91\x97E\x13', b'\xc2h\xdf\xbe'))

def check_auth_status():
    if _Ol11101OO1O(b'@B\x10\xe8\xa7@\xb9t6\xcc\x98\x9a~', b's\x01\xac:') not in st.session_state:
        st.session_state[_O1Il0Ol11100l100l1(b'\x9b\x80\x1a\x18!\xee\xc6\xdc\xb7\x9c\xdb&\xfc', b'S\x18)P')] = False
    return st.session_state[_Ol11101OO1O(b'N\xa2e9\xc0LT\xae\xc7\x95\x18\xcd\xe5', b'~\x07\x1d\xf8')]

def set_auth_status(status):
    st.session_state[_Ol11101OO1O(b'\xe1\xd1=\xb4#_\xf0A>\x17b\x9e\xe2', b'\xdd %\x9a')] = status

def save_company_profile(profile_data):
    return safe_json_save(COMPANY_PROFILE_FILE, profile_data)

def load_company_profile():
    default_profile = {_O1Il0Ol11100l100l1(b'\xba$H\xcc\xbcR\xa5e\x7f\xc7\xd0\xf9', b'\xd5\xc0H\xbf'): _O1Il0Ol11100l100l1(b"q\xab\x96P\xd6\xa5'\xae\xc3~", b'&j\xc4\xc2'), _O1Il0Ol11100l100l1(b'\x9c4Ql\x1c\xb2\xcb\n\x98;\x8f9k', b',\xbf\xf0\x87'): _Ol11101OO1O(b'%E\x13\x06\x8a\x16\x1e\xde \x19\xa2', b'TN\x99#'), _O1Il0Ol11100l100l1(b'_\x92\xc2\xe8\xf8u\xdd\xba\x91\x16\xab.~', b'%"gx'): _Ol11101OO1O(b'\x11\xd5\xbf/l\x8f\xd7\x90e|X6\x1d=\xbd\xbd\x88\xf1', b'\x98l\xb7<'), _O1Il0Ol11100l100l1(b'*.\xb4g\xb0U\x02y\x8e\xb5\x84\xb5\x1f\xdc\x8f', b'\rq\xfe\xde'): _Ol11101OO1O(b'H\xfe\xb7V\xc9\x96\x04\xee\x85\xf5\xf4|\xb1\x19\xd3&\xa8\xf3\x90\xe4\x1e', b'\xfc\xcdLl'), _Ol11101OO1O(b'\xbc>9{\xe8\x9b\xa6\xe32\xfd\xaf\xad', b'|\xe4\x8a\xaa'): _O1Il0Ol11100l100l1(b'\xa6 a\reH\xd1w\xad?\xd5\xfc\xd3\xa6\x18\\\xaf\xad\xc4\xe2\xfa\x8b', b'}\xd6`\xf3'), _O1Il0Ol11100l100l1(b'\x82\xfe\xed\x06ev\x8d\xc00y4Z\xf3\xa5>\xach>B', b'3+.\x81'): _O1Il0Ol11100l100l1(b'\x05W\xba\xed\xb6c4\x99VZ/\x13x\xe1\x1e\x89\xc0\xb5\xcdl\xcc[\x984\xa5\\\xc9[\xd1\xce\xf2\x9d\xd0ec\x13\xd7\x18|.\x0e\xb7\x8a\xbc*w5\xcf\x91h6\xa2', b'\xd9]\xd2\xd8'), _Ol11101OO1O(b'\x00\x7f\x80p\xb7\x92\xd6t\xa4\x0f\xce\x95\x16', b'\xd4Y\xd0\xe4'): _O1Il0Ol11100l100l1(b'hY1,o\x98F\xf1tq\x8e\xfb\xf1\x8fU\xbe\xa6\x03"\xea+\xe6\xa7\xbd\xa8\x8a\xea_\x03\xbeI9\xc8\xb6.\xd8\xa2\x90\xcb\\9', b'D\xa1\xbc\x1b'), _O1Il0Ol11100l100l1(b'\xdf\xd7*\xc0\x0bR<\x1e\xb4+1f\xb4\xa5', b'a\xc3)\xdb'): _Ol11101OO1O(b'\x10\x8a\x1dJ\x17\xb5m\t8C*m\xc6\x1bV\x17\xd4\x17^-\x81\xf5\xd7!\x9c\xd6', b'-,<\xdc'), _O1Il0Ol11100l100l1(b'\x04>\xbbpD\xde\xd6a`k0', b'\nFS\xd1'): _O1Il0Ol11100l100l1(b'{4\xed\x81\xbc|\xde\xde\xd2L\xf9B\x05\xe4', b'\x1e:\xd6\x18'), _Ol11101OO1O(b'x\xacf\xbb\x9c\xb3SZCL\x04\xe6\x81\xb2\xad', b'T\xd7\xb3\xb4'): _O1Il0Ol11100l100l1(b'\xd8C\x1f\xdb\xb4\x1e\x8er\x1e\xcaS\x86\x8b\xb8/LO\xc6!A6\xe9\xdc?pwN\xc1\xe3', b'V\xcd\x06N'), _O1Il0Ol11100l100l1(b'^\x86\xdd\xe7\x1a\xb2\xf1n', b'\xa4\x88\xad\xbd'): _Ol11101OO1O(b'j#\xa8\xb1\xdbz\x84W:7', b'\xce,\x95\xdc'), _O1Il0Ol11100l100l1(b'\xf51\xe0\x0e2\xfbpw6)\xe6\x85[W\xa8', b'f\xe9\xde\x14'): _O1Il0Ol11100l100l1(b"\x1bs'\xaf\x101-\x00\xa8\x83d\xfbi\xa7n6\xc8`\xf2\xfc\xa6", b'\x1d\xb5\xce\xf3')}
    return safe_json_load(COMPANY_PROFILE_FILE, default_profile)

def load_campaign_data():
    return safe_json_load(CAMPAIGN_DATA_FILE, {_Ol11101OO1O(b'm\xf8\xe7\x06\x17v\x9c\xf8\xffAW', b'\xc1/\xb5\x1e'): 1139471837 ^ 324590463 ^ (2077649896 ^ 1497014731) ^ (1521274718 ^ 1592659599 ^ (1633755964 ^ 394069612)), _Ol11101OO1O(b'\x89?\xf86\xe3\xc8]\xd0\xe2', b'\xc9\x94\xa9\xdd'): 319196797 ^ 767953857 ^ (1610628532 ^ 1936321418) ^ (2138313059 ^ 480948619 ^ (1741050250 ^ 699507424)), _O1Il0Ol11100l100l1(b'3\xdfWD\xdb\x19\xcep\xa5', b'\xa3F!\xa9'): 150210289 ^ 708066106 ^ (38804463 ^ 597407325) ^ (1042355367 ^ 105636207 ^ (567037505 ^ 447556592)), _O1Il0Ol11100l100l1(b'\xac\xbc\x7f\x9c|\xec\x10\xac_\xa60\xcd\xb2\xb2\xea\xc5.\x14', b'\x00]\xcbW'): 718949186 ^ 1791331329 ^ (974935069 ^ 1730509597) ^ (744681493 ^ 2000753829 ^ (938692402 ^ 1911964609)), _Ol11101OO1O(b'\xa3\x89\xb2\xdd\xf4=Z\x99\x9f\x02\xa3O>\xa5f', b'Y\xc4\xed\xab'): 1552180340 ^ 1584611519 ^ (1608899290 ^ 1096839902) ^ (819041405 ^ 876075322 ^ (933354185 ^ 792009537)), _Ol11101OO1O(b'O\x19\xd8\xe9\x89\x87\xe3\xc0\xd0\x96\xb5', b'\x9f\xcd\x96\xc0'): 1974833564 ^ 1417162849 ^ (1862502273 ^ 1170107723) ^ (130490917 ^ 1373074864 ^ (1748523892 ^ 894978006)), _O1Il0Ol11100l100l1(b'\xbb\xeb\x0e\xe1-e\xb1\xae\x7f\xb4u', b'\xbd^\x9c1'): {}, _O1Il0Ol11100l100l1(b'\xfc\xbc+\x9b\xcd\x047*\xb5\xd9\xb3uh', b'\xdf ~]'): {_O1Il0Ol11100l100l1(b';\xfe}N\x00', b'Y"B\x1a'): 1903020792 ^ 1237019932 ^ (747392555 ^ 619040115) ^ (854322922 ^ 285644933 ^ (339523535 ^ 124708124)), _Ol11101OO1O(b'ez\xc26\x1c\xba@\x7f', b'\x8c\xc8\xd3\xea'): 1760276635 ^ 559768226 ^ (397399600 ^ 1827254876) ^ (1355980091 ^ 1022045935 ^ (1253812536 ^ 343059641))}})

def get_campaign_metrics():
    data = load_campaign_data()
    metrics = {}
    metrics[_Ol11101OO1O(b'*\xd3:\xd2_MHSWZB', b'\xcbxc\xc7')] = data.get(_O1Il0Ol11100l100l1(b'\n(\xfdG\xbd\xdb2\x03\x87\x08\n', b'\xec\xae\xc1\xbc'), 1854186917 ^ 1518298886 ^ (19803701 ^ 1983684605) ^ (1849964589 ^ 1318905767 ^ (1202372518 ^ 614142791)))
    metrics[_O1Il0Ol11100l100l1(b'WsO\xed\xb0\xde`\x0eR', b'4\x96\xb9\x9b')] = data.get(_Ol11101OO1O(b'b\xd3\xc6\xf15l\x0f\x90\xfc', b'(\x973\xa9'), 1766640947 ^ 1519373431 ^ (2066466888 ^ 102574574) ^ (911238265 ^ 284966484 ^ (1816620636 ^ 69129363)))
    metrics[_Ol11101OO1O(b'\x0b\x10\xbe@\xf6{\xbf\x12\xea', b'\xdd\xf2+\x17')] = data.get(_Ol11101OO1O(b'd\x1d9\xc8\xdf\x1c\xa7\xfb\x83', b'G\x92\x0c\xe4'), 50393493 ^ 786544487 ^ (1748412619 ^ 1963396088) ^ (993102136 ^ 1874830856 ^ (1050404119 ^ 1522872294)))
    metrics[_O1Il0Ol11100l100l1(b'*]\x9e\x06(\xbf\xa8\xceA]n=\xc3$\x92Z\x92;', b'r\xf0\x16\xc4')] = data.get(_O1Il0Ol11100l100l1(b'&6\x1a\xd4\xee\x13\xf6\xe3\xe4\x15\xc7\xeb\xf2\x81\x17:.\xc4', b'\x0e\xa8xG'), 1724510439 ^ 1367637115 ^ (714997390 ^ 605915495) ^ (434078886 ^ 1968352455 ^ (627777058 ^ 1881918774)))
    metrics[_O1Il0Ol11100l100l1(b'\x94\xc9\xc99\x0cK\xa1\x83\x18\xaax\xdb\xe5\xdb\xa2', b'\xc88\xb9\xf8')] = data.get(_O1Il0Ol11100l100l1(b'\xb9\x140\t`\x99%\x1b\x94\xfa\xea\xc9\xec\xf8q', b'\xc5*\x07\xaa'), 2022011448 ^ 496471194 ^ (1717325502 ^ 83755697) ^ (1496065756 ^ 1816391513 ^ (773351475 ^ 482808603)))
    metrics[_Ol11101OO1O(b'k\n1E\xf5\x95\x14&\xb27;', b'\xa9\x8c\x14\xf0')] = data.get(_Ol11101OO1O(b'1-c\xa9{^\xf3:O\xa84', b'jh\x85\xce'), 1306080119 ^ 1259490172 ^ (1295955323 ^ 597178122) ^ (621599070 ^ 1849642635 ^ (471007980 ^ 1062039363)))
    metrics[_O1Il0Ol11100l100l1(b'\xf8\xb5\xb1V\xa4\xa1\xb5\x1c\x81\xf9W\x02', b'\xd3?\xbfA')] = metrics[_O1Il0Ol11100l100l1(b'\xd0\xd2I\n\xd0\x91\xb8%\x1f', b'\xac\xcdw\x18')] / metrics[_O1Il0Ol11100l100l1(b't\xddS\xe7\xafA\xa1\x84Z\xd8 ', b'l\xe9\xee\x88')] * (557420587 ^ 483425137 ^ (527615209 ^ 713646808) ^ (726059150 ^ 1245880973 ^ (1808360305 ^ 48186493))) if metrics[_O1Il0Ol11100l100l1(b'\x16S\xd6]`e\x9eCKe\xba', b'&\x06\x98\xd1')] > 430041953 ^ 285033984 ^ (1519647113 ^ 1272675081) ^ (117570261 ^ 409845640 ^ (746626200 ^ 737736228)) else 909917600 ^ 1774884072 ^ (2105776808 ^ 1639422420) ^ (166613915 ^ 981504790 ^ (798714464 ^ 1597440217))
    metrics[_Ol11101OO1O(b'\xb4-\x88)>\xfb:Mb\xc9\x16;_', b'Flk\r')] = metrics[_O1Il0Ol11100l100l1(b'\xb1\xac\x06\x06\xbe\xccKs\xfb', b'\x15\xec\xc4b')] / metrics[_O1Il0Ol11100l100l1(b'\x9bu\x14\xe6\xd3\xbd\xd7\xd6p', b'\xc7{\xb8\xf6')] * (693709784 ^ 335667289 ^ (2053289287 ^ 619645062) ^ (1432893648 ^ 1189751215 ^ (636287689 ^ 1438358930))) if metrics[_O1Il0Ol11100l100l1(b'\x82\x13\x94L\xdd\x84W\xc7V', b'\xc4\xc9\x045')] > 771849006 ^ 1488557223 ^ (1730801401 ^ 252086415) ^ (388922651 ^ 574594676 ^ (1830411066 ^ 1184870826)) else 1299566100 ^ 1843065724 ^ (817129403 ^ 291424891) ^ (101935608 ^ 1715356078 ^ (1353211490 ^ 834725532))
    metrics[_Ol11101OO1O(b'\x05\x13\xd5\x04\xee\xf5\xf3C\x85\x12F \xd2', b'\x9e\xe9\x1e\x93')] = metrics[_Ol11101OO1O(b'\xf6\x9f\xe1\x0e\x0cp\xdc\x9f\x8c\x01\xd5\xa0\xee\xb3{V\xb1*', b'W\x075H')] / metrics[_Ol11101OO1O(b'R\xf7\xc8s\xff^\xd6e/', b'H\xfd\xae ')] * (550502130 ^ 633962921 ^ (1457338433 ^ 1727900470) ^ (373216575 ^ 2106308626 ^ (1785582486 ^ 889082611))) if metrics[_O1Il0Ol11100l100l1(b'\xa1\xc8\xa7*a\xa2;fW', b'\xca\xb5\x05\xf5')] > 773624358 ^ 410313362 ^ (1027912874 ^ 1555061190) ^ (1340089794 ^ 1996609802 ^ (106466467 ^ 1764093363)) else 650954410 ^ 700273469 ^ (1702649055 ^ 167600520) ^ (1903661286 ^ 1715983937 ^ (1326848819 ^ 1003943252))
    metrics[_Ol11101OO1O(b'L\xc7\rA\x84\x96\xaa-a\x82\x0e\x12dv\xd5', b'\xe4\xd0\x14\x81')] = metrics[_O1Il0Ol11100l100l1(b'\x80\xb2\xf0\xf8)\xc6V4@\x89+', b'\xc6\x0f\xee\xac')] / metrics[_Ol11101OO1O(b"\xd1'kD\x12\xfc])\xe7\x068", b'[\xd5"\x18')] * (114697657 ^ 1627259255 ^ (1832717157 ^ 346664061) ^ (1834568634 ^ 1285294595 ^ (1340094398 ^ 1905915317))) if metrics[_Ol11101OO1O(b'-\x10\xf2\x1an\x05\xae\x14\xde\xd6k', b'\x8d\x01Cr')] > 1630230132 ^ 2055654131 ^ (1731676231 ^ 1524574319) ^ (42666530 ^ 497688930 ^ (904914634 ^ 210448677)) else 330896600 ^ 480275582 ^ (339924342 ^ 544519065) ^ (207371472 ^ 975253890 ^ (1086169735 ^ 1307554204))
    return metrics

def update_campaign_stats(action, lead_data):
    campaign_data = load_campaign_data()
    today = datetime.now().strftime(_Ol11101OO1O(b'\x99\x1b\xbaN\xaf\x0eM9', b'{\xa6\x9f\x10'))
    if today not in campaign_data[_Ol11101OO1O(b'\x9d\x98\x8eC\x13\xf9\x98V\r\xdf\xef', b'\xbd]\xf9\x13')]:
        campaign_data[_Ol11101OO1O(b'\xb8\x8e\xd1@Y\xe4\xf1\x1c\xe3?\xe5', b'\xcfwL\xb8')][today] = {_Ol11101OO1O(b',\x9cM\xca\xd6', b'\x19\x9d\xed\xb9'): 1411225596 ^ 511677808 ^ (1601651314 ^ 99245095) ^ (1286386322 ^ 140009458 ^ (1036734562 ^ 1774232027)), _O1Il0Ol11100l100l1(b'Xz,\t+\x1f\x9c\x94\x96', b'i\xd2c:'): 119637262 ^ 1180151243 ^ (1678569012 ^ 575684851) ^ (2108509818 ^ 75296621 ^ (111737824 ^ 2018761973)), _Ol11101OO1O(b'\x10Z\xb5C\xe7\xe9\x16\x9e_', b'y\xdf\\h'): 1048898804 ^ 61305756 ^ (1085114413 ^ 370296618) ^ (1431838980 ^ 1054446161 ^ (420532110 ^ 420293812)), _Ol11101OO1O(b'\\\x17\x01\xcf^d\xa3\xf9', b'\x86cz/'): 150804832 ^ 1854515348 ^ (2031018634 ^ 841155527) ^ (1542596461 ^ 1542972429 ^ (723092226 ^ 105189595))}
    if action == _Ol11101OO1O(b'\xe7\xa8W&\xf4\xd4\x1d;', b'\xa1>.k'):
        campaign_data[_O1Il0Ol11100l100l1(b'd\x082\xf0\x9b\xa8\x14\t\x90\xf0\x9e', b'\x1avO\xf1')] += 1449190301 ^ 279537692 ^ (200262924 ^ 1302011851) ^ (1575193756 ^ 84941084 ^ (447637951 ^ 1122020728))
        campaign_data[_O1Il0Ol11100l100l1(b'\x86?\x84\xa67\xab\xa1V\xab\xc0\xda', b'6\xe1\x01U')][today][_O1Il0Ol11100l100l1(b'\xfc\x89u\xc8\xf2', b'\xbbx\xfe\xba')] += 1310623853 ^ 647399461 ^ (1313478056 ^ 1313709197) ^ (1779487942 ^ 144503770 ^ (1737716267 ^ 1838210139))
    elif action == _O1Il0Ol11100l100l1(b'\xeaK\x9b\xb0E\xa8r\n\x92', b'<\xbb\xed='):
        campaign_data[_Ol11101OO1O(b'\x9e\xcf\x13{\xb2\xa0\x84\x19R', b'n$B\xda')] += 1836404727 ^ 1794441736 ^ (1368350899 ^ 1245023176) ^ (627290343 ^ 1116928151 ^ (910756412 ^ 1300423881))
        campaign_data[_O1Il0Ol11100l100l1(b'\xd4NL0\xf7t\x90\xf0]b\xe4', b'=\t%\xa9')][today][_Ol11101OO1O(b'\xcc\xd0S\xabf-\xff\xfa\x9d', b'\xd1\xeajG')] += 108147485 ^ 1883546326 ^ (907292874 ^ 57350619) ^ (252561037 ^ 1544240515 ^ (883262285 ^ 619364504))
        if _Ol11101OO1O(b'\xf85\x12\x9f\xbc2\xb2', b'&\x7fEw') in lead_data:
            campaign_data[_Ol11101OO1O(b'W\xe7\xc2\xc5oY\xc3\n\xfe\xe7\xb0\xe4\xe2', b'\xf8m\xdeV')][lead_data[_O1Il0Ol11100l100l1(b'\xe4\xb9\x84\x95\xa1^\x8c', b'\xf1\xdf\xcf\xad')]] = campaign_data[_O1Il0Ol11100l100l1(b'a\x92J/\x0f\x90\x16+\xab\xdcsg\x13', b'\xb1\xaa\x98\xa9')].get(lead_data[_Ol11101OO1O(b'\xa6\r\xe1)+\x16\xbe', b'\x89\x00$\x12')], 1772807790 ^ 1043780198 ^ (1209573576 ^ 1587890472) ^ (869808625 ^ 1311071771 ^ (714628289 ^ 373614275))) + (253633824 ^ 1926374995 ^ (214807891 ^ 2120618545) ^ (2054558404 ^ 1995718937 ^ (1208356412 ^ 1273231857)))
    elif action == _O1Il0Ol11100l100l1(b'\x0f\xa7\x05 \x94H\xfd\x81', b'\x05\xda\x8c\x1c'):
        campaign_data[_Ol11101OO1O(b'{Az1\xe6\xfaj+5', b'\xf2C\xe5\xd9')] += 1232011094 ^ 20714929 ^ (1510267893 ^ 374691935) ^ (704324658 ^ 528290645 ^ (25242671 ^ 855929348))
        campaign_data[_O1Il0Ol11100l100l1(b"db'\x80\xe0--\xe1Z\xbc\x02", b'[\xc80a')][today][_O1Il0Ol11100l100l1(b'\xf8\x10\xac\xbd\x7f\xabr\xa9\x89', b'\x13\xe8C\x18')] += 191877034 ^ 1555138425 ^ (1963617622 ^ 576033876) ^ (2138889982 ^ 1779528745 ^ (795504771 ^ 981887876))
    elif action == _O1Il0Ol11100l100l1(b'\xe7\xfb\x1a^\xc3\xbd\xc01', b'\xa6yW['):
        campaign_data[_O1Il0Ol11100l100l1(b'\x9cC\xc3\x1e\xf4^\xae\x95\xcc\x9f\xcf{-\xab\xbf\x81\x10\xd8', b'7\xd9*\xb7')] += 97529984 ^ 1214467062 ^ (1346251912 ^ 1792468609) ^ (890927291 ^ 2071112797 ^ (1020539001 ^ 99046881))
        campaign_data[_Ol11101OO1O(b'H\x82\x04\x98\x02\xb8\x06\xa7O\xef\xaf', b'\x1f\x19\xc0\x16')][today][_Ol11101OO1O(b'(\x02\x06@A\x16U\x10', b'!@te')] += 1910097557 ^ 1266077529 ^ (772520268 ^ 1407867129) ^ (624041167 ^ 1969930521 ^ (1106147704 ^ 1459113174))
    elif action == _O1Il0Ol11100l100l1(b'\xd7\x00!\x9a\x95\x12-', b's\xaf\xb8\xa1'):
        campaign_data[_Ol11101OO1O(b'`\xa7)q\x8b\x07-\x9c\xde\x97\xe4rs\xde\xf5', b's\xa8\xd2y')] += 337418496 ^ 626449294 ^ (926927058 ^ 1788008110) ^ (943911691 ^ 460126955 ^ (1350785829 ^ 524946998))
    elif action == _O1Il0Ol11100l100l1(b'\xf3\x027\xc7q\xdd_r#\xd4', b'\x880\x8c\x80'):
        campaign_data[_Ol11101OO1O(b'\xb9\xa7\xafI\n3\x9e\xe7\x02\xc9#', b'\x1d\x1c\xe5\x17')] += 288085407 ^ 843970259 ^ (509861948 ^ 1572713153) ^ (620382074 ^ 1340469095 ^ (1633404195 ^ 1794907278))
    safe_json_save(CAMPAIGN_DATA_FILE, campaign_data)
    return campaign_data

def save_to_csv(results, keyword, location):
    if not os.path.exists(FOLDER_HISTORY):
        os.makedirs(FOLDER_HISTORY)
    timestamp = datetime.now().strftime(_O1Il0Ol11100l100l1(b'T_p\xd6\x14o#qy\x96$\x89\xda', b't\xd4\xb7\x12'))
    filename = f'{FOLDER_HISTORY}/leads_{keyword.lower()}_{location.lower()}_{timestamp}.csv'
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    return (filename, df)

def get_history_files():
    if not os.path.exists(FOLDER_HISTORY):
        os.makedirs(FOLDER_HISTORY)
        return []
    return [f for f in os.listdir(FOLDER_HISTORY) if f.endswith(_O1Il0Ol11100l100l1(b'=_l\xb0', b'\xc0\x00&%'))]

def load_history_file(filename):
    full_path = os.path.join(FOLDER_HISTORY, filename)
    return pd.read_csv(full_path)