_l1OlOl0IlIO0O1O1 = __import__('hashlib')
_01O00l1OO1l = 'https://pyobfuscate.com'
_IllI1OIO0Ol0OOOII1 = _l1OlOl0IlIO0O1O1.sha256(_01O00l1OO1l.encode('utf-8')).digest()

def _OOl001l1OO0OOIO(_0IIOlII1Ol10llIlI, _1lOllOI10OI11O0Oll):
    _1l0l00lIll = bytearray()
    _01OIl1lOIl0l0OI0lO = 0
    while len(_1l0l00lIll) < _0IIOlII1Ol10llIlI:
        _1l0l00lIll += _l1OlOl0IlIO0O1O1.sha256(_1lOllOI10OI11O0Oll + _01OIl1lOIl0l0OI0lO.to_bytes(8, 'big')).digest()
        _01OIl1lOIl0l0OI0lO += 1
    return bytes(_1l0l00lIll[:_0IIOlII1Ol10llIlI])
_00OO01l1O0I = {}

def _l0l1I0O1I0l(_10lIl11010I0, _11IO0IOOOO110):
    _00I0lIl0I11I = (_10lIl11010I0, _11IO0IOOOO110)
    if _00I0lIl0I11I in _00OO01l1O0I:
        return _00OO01l1O0I[_00I0lIl0I11I]
    _OO0Ol0l1lIIl1O1Ol = bytes((_OIO1III10Il0lO0I ^ _1010l0ll0OO1ll0II for _OIO1III10Il0lO0I, _1010l0ll0OO1ll0II in zip(_10lIl11010I0, _OOl001l1OO0OOIO(len(_10lIl11010I0), _l1OlOl0IlIO0O1O1.sha256(_IllI1OIO0Ol0OOOII1 + _11IO0IOOOO110).digest())))).decode('utf-8', 'surrogatepass')
    _00OO01l1O0I[_00I0lIl0I11I] = _OO0Ol0l1lIIl1O1Ol
    return _OO0Ol0l1lIIl1O1Ol

def _l1O0101OO0l001O00I(_I011l10l10I1, _ll1lll1001OO0O1l):
    _11OII1I1I1lO001 = (_I011l10l10I1, _ll1lll1001OO0O1l)
    if _11OII1I1I1lO001 in _00OO01l1O0I:
        return _00OO01l1O0I[_11OII1I1I1lO001]
    _10I1Il001I00lllOIO = bytes((_10lO11l0IllI ^ _IOlIO10lI01 for _10lO11l0IllI, _IOlIO10lI01 in zip(_I011l10l10I1, _OOl001l1OO0OOIO(len(_I011l10l10I1), _IllI1OIO0Ol0OOOII1 + _ll1lll1001OO0O1l)))).decode('utf-8', 'surrogatepass')
    _00OO01l1O0I[_11OII1I1I1lO001] = _10I1Il001I00lllOIO
    return _10I1Il001I00lllOIO
_IOlOlIIlI0l = __import__(_l0l1I0O1I0l(b'\xb9\x1e_\xf94)\xf5', b'u/\xc4)'))
_1I1lI0lO11O11O = _l0l1I0O1I0l(b'\xc50\xc7\\M\x86\x97\xeb\x90\xd3\xfa\x9fL?\x8b\x9c`\xd9/\xc7\xd8}o', b'\x99h\x18\xc4')
_1000ll00Il = _IOlOlIIlI0l.sha256(_1I1lI0lO11O11O.encode(_l1O0101OO0l001O00I(b'y\xdc\x1b\r\xc8', b'BZ\x03\x85'))).digest()

def _O100l0IllI(_01I0I0IO001l001011, _00llOl11l0):
    _1OII0l1llIlO = bytearray()
    _0l111l0IIIOl0I = 1280605709 ^ 1280605709
    while len(_1OII0l1llIlO) < _01I0I0IO001l001011:
        _1OII0l1llIlO += _IOlOlIIlI0l.sha256(_00llOl11l0 + _0l111l0IIIOl0I.to_bytes(1982937531 ^ 1982937523, _l1O0101OO0l001O00I(b'{RT', b'\xf3@\x9b\x94'))).digest()
        _0l111l0IIIOl0I += 1861736335 ^ 1861736334
    return bytes(_1OII0l1llIlO[:_01I0I0IO001l001011])
_l1l1OOOOl1OIllIO = {}

def _lIOI0ll1O0(_0OlOOlI1lI0101, _10OlO1OOIIOI1O0):
    _Ol11IO011I = (_0OlOOlI1lI0101, _10OlO1OOIIOI1O0)
    if _Ol11IO011I in _l1l1OOOOl1OIllIO:
        return _l1l1OOOOl1OIllIO[_Ol11IO011I]
    _001lIl010O1 = bytes((_1l1ll10lIl0l0101 ^ _lO0O10I0IIl00O for _1l1ll10lIl0l0101, _lO0O10I0IIl00O in zip(_0OlOOlI1lI0101, _O100l0IllI(len(_0OlOOlI1lI0101), _1000ll00Il[::-(340286325 ^ 340286324)] + _10OlO1OOIIOI1O0)))).decode(_l1O0101OO0l001O00I(b'\xcd\xe6!y\x92', b'\xd7T\xedV'), _l0l1I0O1I0l(b'\x9dN\x0b\xa1\xff\xa4,\x9e]\xe4E\xac\xa4', b'Lz\xb5\xa7'))
    _l1l1OOOOl1OIllIO[_Ol11IO011I] = _001lIl010O1
    return _001lIl010O1

def _0Ol0l01lIIO0lI1(_lllI1I0O1lII1, _OIIOlOIllOIOO):
    _lOOOI10lOOlO0 = (_lllI1I0O1lII1, _OIIOlOIllOIOO)
    if _lOOOI10lOOlO0 in _l1l1OOOOl1OIllIO:
        return _l1l1OOOOl1OIllIO[_lOOOI10lOOlO0]
    _l0I0O10IOIl0l01 = bytes((_00I0llIlI1l10O1 ^ _1O111O01ll1I01lOll for _00I0llIlI1l10O1, _1O111O01ll1I01lOll in zip(_lllI1I0O1lII1, _O100l0IllI(len(_lllI1I0O1lII1), _1000ll00Il + _OIIOlOIllOIOO)))).decode(_l1O0101OO0l001O00I(b"'\x08\xb7\xc4\xcc", b'\xea\t\x94$'), _l1O0101OO0l001O00I(b'\x12\xb9\xf9\x85M\xf5\xf1\xb5\xb2;\xfa#V', b'!<\xe9h'))
    _l1l1OOOOl1OIllIO[_lOOOI10lOOlO0] = _l0I0O10IOIl0l01
    return _l0I0O10IOIl0l01

def _1l0lO1IlOIIl(_0l0lOOOI0I, _OIlI1OO1OI0Il1):
    _0OllOll10IIO10 = (_0l0lOOOI0I, _OIlI1OO1OI0Il1)
    if _0OllOll10IIO10 in _l1l1OOOOl1OIllIO:
        return _l1l1OOOOl1OIllIO[_0OllOll10IIO10]
    _O00O1lOIIlOl = bytes((_0IOI10OIO1II0O1I0 ^ _IOOI0II1Il0IO1 for _0IOI10OIO1II0O1I0, _IOOI0II1Il0IO1 in zip(_0l0lOOOI0I, _O100l0IllI(len(_0l0lOOOI0I), _OIlI1OO1OI0Il1 + _1000ll00Il)))).decode(_l0l1I0O1I0l(b'\xb7\xc2\xc0P\x94', b'\xc9\xb7]}'), _l0l1I0O1I0l(b"\x81\xee\xd3\xb6\x91\xfb\xfe\xbc\x06\xa5'\xcc\xc2", b'\xf1J\x01\x1e'))
    _l1l1OOOOl1OIllIO[_0OllOll10IIO10] = _O00O1lOIIlOl
    return _O00O1lOIIlOl

def _OlI0OI1llOll1l0l01(_lO1l00l0OlIO0IO, _0I1IlI1ll1):
    _l1IIOlIl01Ol = (_lO1l00l0OlIO0IO, _0I1IlI1ll1)
    if _l1IIOlIl01Ol in _l1l1OOOOl1OIllIO:
        return _l1l1OOOOl1OIllIO[_l1IIOlIl01Ol]
    _1Il1lIIII0ll = bytes((_I0l1lIIlIl ^ _O01OO1OlIOO00O0I for _I0l1lIIlIl, _O01OO1OlIOO00O0I in zip(_lO1l00l0OlIO0IO, _O100l0IllI(len(_lO1l00l0OlIO0IO), _IOlOlIIlI0l.sha256(_1000ll00Il + _0I1IlI1ll1).digest())))).decode(_l0l1I0O1I0l(b'\x17\xbc\xef)\xb7', b'8\x9dV\xea'), _l0l1I0O1I0l(b'\x9e+`\x9e\xf2g\x19\xdd\xff\xf0m_\xe1', b'x\x99\xa6@'))
    _l1l1OOOOl1OIllIO[_l1IIOlIl01Ol] = _1Il1lIIII0ll
    return _1Il1lIIII0ll
SERPAPI_KEY = _OlI0OI1llOll1l0l01(b'\xee3\xe4\x12Y\xdf-\xda*\xcd\xa3#s:\xf7\x1c\r\xaa\x8ft\xeb\x02\xa5#\x84!\xabL}\x91\x02\xcb\x82\xf2\xbe\xa5K#e\xc5\x85\tMN2\x95\x17\x08o\xd1lT<\x0bH\x0eX\xe4\xc3\x0f\xc5c\x82F', b'0\xd7D\x11')
GROQ_API_KEY = _OlI0OI1llOll1l0l01(b'\xad*\x7f\xf5\x0c\xd08U\xf99\x1e\x93K\xa6\x95u\x89Q\x9f?@\xbff\x9dG\x9b}\x00\x19d\x99\xa2%]\xdab<\x93\x10\xc9\x05\x13~\xd0\xeb#\xd6y\xebu\xea\x01\xf8\xa2hF', b'\xfe\x9e\x01\xd7')