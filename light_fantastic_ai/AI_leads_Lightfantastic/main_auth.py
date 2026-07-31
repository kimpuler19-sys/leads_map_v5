_1OIII11OOOIIO = __import__('hashlib')
_OOll0IO0101 = 'https://pyobfuscate.com'
_OOlIl0OllIIlO = _1OIII11OOOIIO.sha256(_OOll0IO0101.encode('utf-8')).digest()

def _11Il10O0l0OlOlI(_1OOl00lO1IIllI, _Il0OO00011IO0):
    _01l01lIO1IOO11lI1l = bytearray()
    _lO101IO00l0lI = 0
    while len(_01l01lIO1IOO11lI1l) < _1OOl00lO1IIllI:
        _01l01lIO1IOO11lI1l += _1OIII11OOOIIO.sha256(_Il0OO00011IO0 + _lO101IO00l0lI.to_bytes(8, 'big')).digest()
        _lO101IO00l0lI += 1
    return bytes(_01l01lIO1IOO11lI1l[:_1OOl00lO1IIllI])
_110l0IO0Ol11IOI1lI = {}

def _0OI0IOI0OO0(_0ll110O0II10, _l01O00IOI0I):
    _1lII100O11 = (_0ll110O0II10, _l01O00IOI0I)
    if _1lII100O11 in _110l0IO0Ol11IOI1lI:
        return _110l0IO0Ol11IOI1lI[_1lII100O11]
    _00OO1lI1IO0 = bytes((_OOIlIl0O00 ^ _OIOOIIlIll0Ol1 for _OOIlIl0O00, _OIOOIIlIll0Ol1 in zip(_0ll110O0II10, _11Il10O0l0OlOlI(len(_0ll110O0II10), _l01O00IOI0I + _OOlIl0OllIIlO)))).decode('utf-8', 'surrogatepass')
    _110l0IO0Ol11IOI1lI[_1lII100O11] = _00OO1lI1IO0
    return _00OO1lI1IO0

def _l0l0OIlO1lIO1IO(_I0OlIII1Il1l1, _l110lOIO100):
    _10I1100lOOOOI1IlOI = (_I0OlIII1Il1l1, _l110lOIO100)
    if _10I1100lOOOOI1IlOI in _110l0IO0Ol11IOI1lI:
        return _110l0IO0Ol11IOI1lI[_10I1100lOOOOI1IlOI]
    _I0OOO01OI11l1 = bytes((_0lOO0OIIlIII0lO ^ _0lO10lI0I1Ol10I0 for _0lOO0OIIlIII0lO, _0lO10lI0I1Ol10I0 in zip(_I0OlIII1Il1l1, _11Il10O0l0OlOlI(len(_I0OlIII1Il1l1), _OOlIl0OllIIlO[::-1] + _l110lOIO100)))).decode('utf-8', 'surrogatepass')
    _110l0IO0Ol11IOI1lI[_10I1100lOOOOI1IlOI] = _I0OOO01OI11l1
    return _I0OOO01OI11l1
_O1OIl11OO000 = __import__(_l0l0OIlO1lIO1IO(b'jZ\xff2\xe9\xa2\x98', b'\x8a\xcfN\xbf'))
_00II0OO11llOOl10I = _0OI0IOI0OO0(b'\x80\x9eV>\rj\xbd\xd3\xb3\x0fc\x98\xdb\xdaI\xe4Z\x01Q?\xc6\xcb$', b'\xac\xd5\xf7\xfd')
_011IlIO101 = _O1OIl11OO000.sha256(_00II0OO11llOOl10I.encode(_l0l0OIlO1lIO1IO(b'{\xb6\xd4Is', b'\xe1x\t\xad'))).digest()

def _IllI1O01O000IIIOOI(_IOl0lI010I, _OlI10OOlO0llOO0I):
    _lI01lO0l00Il1llOO0 = bytearray()
    _lIO0O0O100I1OOl01 = 1989381632 ^ 1989381632
    while len(_lI01lO0l00Il1llOO0) < _IOl0lI010I:
        _lI01lO0l00Il1llOO0 += _O1OIl11OO000.sha256(_OlI10OOlO0llOO0I + _lIO0O0O100I1OOl01.to_bytes(952073941 ^ 952073949, _0OI0IOI0OO0(b'\xa8\xb0\xeb', b'<\xb7\x03\xd6'))).digest()
        _lIO0O0O100I1OOl01 += 141494109 ^ 141494108
    return bytes(_lI01lO0l00Il1llOO0[:_IOl0lI010I])
_OI111OI1OlI0 = {}

def _OIl0IOIOl10I11I1(_O100ll011III1OIlI, _10IlI0O11I010):
    _11lIIO0II0l = (_O100ll011III1OIlI, _10IlI0O11I010)
    if _11lIIO0II0l in _OI111OI1OlI0:
        return _OI111OI1OlI0[_11lIIO0II0l]
    _1OOOIO11OI1lOlIIO = bytes((_IOI0llOIO0I0Oll1 ^ _00l00l0Illl for _IOI0llOIO0I0Oll1, _00l00l0Illl in zip(_O100ll011III1OIlI, _IllI1O01O000IIIOOI(len(_O100ll011III1OIlI), _011IlIO101 + _10IlI0O11I010)))).decode(_0OI0IOI0OO0(b'\xc7\xcab3\xea', b'\xe7\xb0\x1e\xe8'), _l0l0OIlO1lIO1IO(b'-@L\xe8\xaf\x92\x07b\xc2\xf5\xef\xb2\xd0', b'\x942T\xb1'))
    _OI111OI1OlI0[_11lIIO0II0l] = _1OOOIO11OI1lOlIIO
    return _1OOOIO11OI1lOlIIO

def _0l1lI0lOl01lOOl(_O1l1O000100I10, _1Ol0IIl0IO1IlIOl0l):
    _I11Illll0Ol0OO = (_O1l1O000100I10, _1Ol0IIl0IO1IlIOl0l)
    if _I11Illll0Ol0OO in _OI111OI1OlI0:
        return _OI111OI1OlI0[_I11Illll0Ol0OO]
    _1IO1OOI1l0lll0 = bytes((_1l1I1OIIII ^ _01OI0I01O1l000lI for _1l1I1OIIII, _01OI0I01O1l000lI in zip(_O1l1O000100I10, _IllI1O01O000IIIOOI(len(_O1l1O000100I10), _O1OIl11OO000.sha256(_011IlIO101 + _1Ol0IIl0IO1IlIOl0l).digest())))).decode(_0OI0IOI0OO0(b'\xcd\xa5~\xa0P', b'\xbc\x9c\xd8\x02'), _0OI0IOI0OO0(b'\x8c\xbc\xec\x90\x01s\xa3\xcbU\xa6)/\xdc', b'\xcf\xe5w\x17'))
    _OI111OI1OlI0[_I11Illll0Ol0OO] = _1IO1OOI1l0lll0
    return _1IO1OOI1l0lll0

def _l1IOOOl0OO011I1(_0I1l01I1lI0, _lI0lI00OIO10lI):
    _ll01OI1lI0O1O = (_0I1l01I1lI0, _lI0lI00OIO10lI)
    if _ll01OI1lI0O1O in _OI111OI1OlI0:
        return _OI111OI1OlI0[_ll01OI1lI0O1O]
    _1000IOI1llOOI = bytes((_10l0Oll111 ^ _1IO101Ol0O1lI10 for _10l0Oll111, _1IO101Ol0O1lI10 in zip(_0I1l01I1lI0, _IllI1O01O000IIIOOI(len(_0I1l01I1lI0), _011IlIO101[::-(291341389 ^ 291341388)] + _lI0lI00OIO10lI)))).decode(_0OI0IOI0OO0(b'K\xd2c\xd8_', b'\xfd\xa8\xfce'), _l0l0OIlO1lIO1IO(b'\x84n\x95\xb5\xb5AV7\xcb\xbf\xd6\x9e\xce', b'\xba\x08\xb9d'))
    _OI111OI1OlI0[_ll01OI1lI0O1O] = _1000IOI1llOOI
    return _1000IOI1llOOI

def _1I01l0llIIIlOlI(_I1l10I0101I0IOO, _Oll000O01O0ll):
    _0I11O1OO00I = (_I1l10I0101I0IOO, _Oll000O01O0ll)
    if _0I11O1OO00I in _OI111OI1OlI0:
        return _OI111OI1OlI0[_0I11O1OO00I]
    _IOOlI1110Ol1110I = bytes((_Oll1II00Ol0OI ^ _l0Ol1I1Illl for _Oll1II00Ol0OI, _l0Ol1I1Illl in zip(_I1l10I0101I0IOO, _IllI1O01O000IIIOOI(len(_I1l10I0101I0IOO), _Oll000O01O0ll + _011IlIO101)))).decode(_l0l0OIlO1lIO1IO(b'\xb5\xaa\xc1\xce\x87', b'7C\xe6\xf2'), _0OI0IOI0OO0(b'$\x91\xf1B5\xde\x0c\xde4\xda\xe5\xa9\xfb', b'\xb7vf\x8d'))
    _OI111OI1OlI0[_0I11O1OO00I] = _IOOlI1110Ol1110I
    return _IOOlI1110Ol1110I
import streamlit as st
from datetime import datetime
from core_auth import verify_gumroad_license, verify_demo_access, check_auth_status, set_auth_status, EXPIRY_DATE

def render_auth_screen():
    current_date = datetime.now()
    st.title(_0l1lI0lOl01lOOl(b'\xc4k\xe7\x01\xcf\xe9\x0e\x8c\xcc\x8c\xeeV\x86G\x17,\xdc,\x8d\xdai\xbd\x17\xb3\xbe.L\xa8\x92\xca\xd2', b'L\xe3\xdb\xec'))
    st.caption(_1I01l0llIIIlOlI(b'\x8a\x12\xfa\xb2w-\xa6\xab\xac\x03\xbbr\xc0\xb4\xed\xa2L{\xa4\x08\x9b\xc1y\x94\xe4\x86 MpS\xe8,\xc4\xa1\xe6K\x17\xd9\xbaZU\xb2 \rv-', b'@-a\x9f'))
    st.markdown(_1I01l0llIIIlOlI(b'\x84\xce\x89', b'\x8c\x98\xca\x88'))
    auth_tab1, auth_tab2 = st.tabs([_1I01l0llIIIlOlI(b'\xcb0\xdc~\x95\xb6#1\xc8\xb3\x9e\xda\x08u\xe2\xf2\xa7dq\xae\x96\xfer', b'[\xb43\x03'), _OIl0IOIOl10I11I1(b'\xa0\x00\xb9\xad\xe4;\x95.\x1fD\xba\xbam#l\xf1r\x07\x13}', b'\x1d\xfd\x95@')])
    with auth_tab1:
        st.subheader(_l1IOOOl0OO011I1(b'&{U\x89\x0b\xba\t\x02\xaf\xba#U\xbb\x93u\xc7Qa\xd5=4\xa9\xfa\x83\x8b\x7f\x19', b'\x0f\xad\xf7d'))
        st.markdown(_l1IOOOl0OO011I1(b'#\xc5\x1aN\x9d)l\x8d6\xef#\x045\xb6\xdf^\x071\xedc\xf2-', b'\x16\xa3\xff\x88'))
        gumroad_input = st.text_input(_l1IOOOl0OO011I1(b'\x92m\xeb\xf7\xd3\xd5q\x89\xdf\xfe\x04\xe0', b'\x14\xfdE\xdb'), type=_0l1lI0lOl01lOOl(b'J\x8c>b\xe0!\x8cW', b'\xfc\xc5h['), placeholder=_1I01l0llIIIlOlI(b'\xb3\xa3\xa1\x92\xc1\xf1\xb9\x95^P\x1f\xdf\xd2\xcb\x90\xa5:\xc0\xde', b'\xdehH_'), key=_l1IOOOl0OO011I1(b't{^\x03y\x03B57\x95a5L', b'*\x06\xf7{'))
        if st.button(_0l1lI0lOl01lOOl(b'W\xd7<\xd4\x94\x13ex\xd9\x13&o\x91', b'\x15\x8f\xe6}'), type=_OIl0IOIOl10I11I1(b'\x90\xfd\xb7\xd2\xa6\xaea', b'\x8fwJ0'), use_container_width=True, key=_l1IOOOl0OO011I1(b'.o\xe9\xef\xc8\xde\xfb\xf3.\x83\xc6\\\xf7\x03{E\xb0Q1', b'v\x8cy\x06')):
            if not gumroad_input:
                st.error(_0l1lI0lOl01lOOl(b'RBC\xc9\xc2\x8f\x9c\x8c\x98e\x0e\xef\xd3tP\xd3\xebg\xe0\x07\xddAY-\x9aF7\x11\xbd', b'\xc7\xba\xac\xda'))
            else:
                with st.spinner(_l1IOOOl0OO011I1(b'\xd2\xdd\xcc\x02Jo\xf4\x00aS\xf9\xb2( \xcb\x80\xa4\xe0>\xab', b'\rpC\xb4')):
                    is_valid, message = verify_gumroad_license(gumroad_input)
                    if is_valid:
                        set_auth_status(True)
                        st.success(_OIl0IOIOl10I11I1(b'\xdcR\xd7}\x10\x9fh.Q\xf0TLKK\xe3\x89\xec\xb8;r\x9f(\x8ex\xd0Y\x07', b'd\xa9\x95\x16'))
                        st.rerun()
                    else:
                        st.error(f'❌ {message}')
    with auth_tab2:
        st.subheader(_OIl0IOIOl10I11I1(b'\xa6%\xe7\xbcq\x10_\xcb\xd2\xed\x8b\xcd\x92h\\\xed`\x83.\xa7', b'\xec\x93\xc5\xdd'))
        if current_date > EXPIRY_DATE:
            st.error(_0l1lI0lOl01lOOl(b'Vd\x05\x14\x1c\xefo\x81\xfa\xbcI\x00\xe4\xae\xb15\x15j\xd1\x0c[\\/\xf7\x00\x00z\xd6}\x19W~\xbax5\xcc\xc0\xde\x11\x1a)\xd0\xcf\x83\xf6L\xa2\xd4/\xe4\x80\x1d\x06w,\xdc\xa7\x19\x13\xa6\x0f\x1c \xe5fi\xa9\xffa>\xc1\xac\xf5u\x10Q\x83\x97i3\x1f\xae', b'\xb5K\xd1|'))
        else:
            days_left = (EXPIRY_DATE - current_date).days
            st.info(f'⏳ {days_left} days remaining in premium')
            demo_input = st.text_input(_1I01l0llIIIlOlI(b'\x0b\xfd\x10\x1a\x8b\xb5\x8f\x19\x11\xa2\x1a\x9aZ]', b'&\x1ei\x07'), type=_OIl0IOIOl10I11I1(b'\xbe\xbe7\xcaq}\xa2\xda', b'6\x19S\xb9'), placeholder=_1I01l0llIIIlOlI(b'\x99\xd0\xbfY\xa9\xd6\x83\xb0q\x9d', b'\x10c\x8cm'), key=_0l1lI0lOl01lOOl(b'.u\xe0\x98\x14\xde\x05\xc1\rn', b'\x1c\xf3\xa4X'))
            if st.button(_0l1lI0lOl01lOOl(b'\x92\xf5\xbe\xfc\xde\xf8\xa0\xbf\xdb CJ\xb6S\xbe\x84*I:', b'\x1b\\(\xee'), type=_1I01l0llIIIlOlI(b'\xf6\x86\xef3\xce9\xa1', b'\xbd\xa2\xdd\x16'), use_container_width=True, key=_1I01l0llIIIlOlI(b'd\x10\xc9\xca\xfe\xa5.\x99\xbd\xaa\x8b\x97E', b'\xd8\xe3D\x9c')):
                if demo_input:
                    is_valid, message = verify_demo_access(demo_input)
                    if is_valid:
                        set_auth_status(True)
                        st.success(f'✅ {message}')
                        st.rerun()
                    else:
                        st.error(f'❌ {message}')
                else:
                    st.error(_l1IOOOl0OO011I1(b'\x0eb\xc5}\xcb\x9d\xc1U>\xcc]\xd9s\xef\x95\xc8\x92\xfbS\x10\xec+7\x90V\x07\x04\xccW', b'q\xfcmG'))