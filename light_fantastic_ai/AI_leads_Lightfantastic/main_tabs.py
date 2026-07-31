_1l1l0001llOlIIIOOO = __import__('hashlib')
_01IO1Oll1IO0 = 'https://pyobfuscate.com'
_1OlI01OOlIl0IOl0 = _1l1l0001llOlIIIOOO.sha256(_01IO1Oll1IO0.encode('utf-8')).digest()

def _OO111I0IOl0(_I00I0IOII1, _0l00O0001O1lO):
    _0OO0I1OI0IlOO = bytearray()
    _IOO1I11I1IlO0ll = 0
    while len(_0OO0I1OI0IlOO) < _I00I0IOII1:
        _0OO0I1OI0IlOO += _1l1l0001llOlIIIOOO.sha256(_0l00O0001O1lO + _IOO1I11I1IlO0ll.to_bytes(8, 'big')).digest()
        _IOO1I11I1IlO0ll += 1
    return bytes(_0OO0I1OI0IlOO[:_I00I0IOII1])
_II1O000lII0l00 = {}

def _OO1I0ll00OO1(_001lO00l11OlO01O, _OllO1l001l1IOIOO01):
    _lO0OllOIlll = (_001lO00l11OlO01O, _OllO1l001l1IOIOO01)
    if _lO0OllOIlll in _II1O000lII0l00:
        return _II1O000lII0l00[_lO0OllOIlll]
    _1ll0lO11lO1OI01 = bytes((_O01lI00lOI0Ol0 ^ _l0lO1l01I0I0OIlIlI for _O01lI00lOI0Ol0, _l0lO1l01I0I0OIlIlI in zip(_001lO00l11OlO01O, _OO111I0IOl0(len(_001lO00l11OlO01O), _OllO1l001l1IOIOO01 + _1OlI01OOlIl0IOl0)))).decode('utf-8', 'surrogatepass')
    _II1O000lII0l00[_lO0OllOIlll] = _1ll0lO11lO1OI01
    return _1ll0lO11lO1OI01

def _1lOOIlll100100O(_00OO1IlOlIlO0IIl, _lIOOlOI1OIIII):
    _100OI1l1O0O0OOIl = (_00OO1IlOlIlO0IIl, _lIOOlOI1OIIII)
    if _100OI1l1O0O0OOIl in _II1O000lII0l00:
        return _II1O000lII0l00[_100OI1l1O0O0OOIl]
    _10011l001011 = bytes((_11l01l01001l0l1 ^ _O11O1IO110llI00 for _11l01l01001l0l1, _O11O1IO110llI00 in zip(_00OO1IlOlIlO0IIl, _OO111I0IOl0(len(_00OO1IlOlIlO0IIl), _1OlI01OOlIl0IOl0 + _lIOOlOI1OIIII)))).decode('utf-8', 'surrogatepass')
    _II1O000lII0l00[_100OI1l1O0O0OOIl] = _10011l001011
    return _10011l001011

def _O00Ill1OIllO(_llO0II0l101lI1I, _1llll1O01I1):
    _I1l00IO1lI1 = (_llO0II0l101lI1I, _1llll1O01I1)
    if _I1l00IO1lI1 in _II1O000lII0l00:
        return _II1O000lII0l00[_I1l00IO1lI1]
    _0IIOIO11O00l11IOI = bytes((_O110OOl1lO0O0 ^ _I0OI1IO01IlI100I for _O110OOl1lO0O0, _I0OI1IO01IlI100I in zip(_llO0II0l101lI1I, _OO111I0IOl0(len(_llO0II0l101lI1I), _1OlI01OOlIl0IOl0[::-1] + _1llll1O01I1)))).decode('utf-8', 'surrogatepass')
    _II1O000lII0l00[_I1l00IO1lI1] = _0IIOIO11O00l11IOI
    return _0IIOIO11O00l11IOI

def _Il0I00l0OIIlO(_1l0O0lO1l1l10, _lOOIO01I1l10Oll0lI):
    _O1l1000l1IO1l = (_1l0O0lO1l1l10, _lOOIO01I1l10Oll0lI)
    if _O1l1000l1IO1l in _II1O000lII0l00:
        return _II1O000lII0l00[_O1l1000l1IO1l]
    _100lOI0lOO = bytes((_O100O0IO0l1l0OI0 ^ _l1l0Ol00O1I10O for _O100O0IO0l1l0OI0, _l1l0Ol00O1I10O in zip(_1l0O0lO1l1l10, _OO111I0IOl0(len(_1l0O0lO1l1l10), _1l1l0001llOlIIIOOO.sha256(_1OlI01OOlIl0IOl0 + _lOOIO01I1l10Oll0lI).digest())))).decode('utf-8', 'surrogatepass')
    _II1O000lII0l00[_O1l1000l1IO1l] = _100lOI0lOO
    return _100lOI0lOO
import streamlit as st
import pandas as pd
import time
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
from core_auth import save_company_profile, load_company_profile, load_history_file, get_history_files, save_to_csv, FOLDER_HISTORY, LANGUAGE_CONFIG, get_serpapi_key, get_groq_api_key, load_campaign_data, get_campaign_metrics, update_campaign_stats
from core_messaging import get_available_languages, process_all_messages_with_profile, enrich_multiple_leads, process_whatsapp_messages, generate_whatsapp_url, save_whatsapp_template, load_whatsapp_templates, delete_whatsapp_template, generate_ai_email_with_profile, generate_ai_whatsapp_with_profile, generate_followup_with_profile, generate_multilingual_message, process_multilingual_messages, create_ab_test, get_ab_test_results, load_email_settings, save_email_settings, test_email_connection, send_single_email, send_bulk_emails, validate_email_settings, prepare_webhook_data, create_zapier_webhook, load_followup_settings, save_followup_settings, generate_followup_message
from core_scraping import scrape_google_maps, format_results, process_emails_for_businesses, process_all_emails, calculate_lead_score, get_priority_from_score

def style_priority_column(df):
    try:
        styled_df = df.style.map(lambda val: _OO1I0ll00OO1(b'8\x8d\x10\xc2\t\x88o\xb1\xbc\xa7\xf9#\xd4\xe7)S\xdb\x97\x1d\xc0\x8fW\xc4C\xc5S\x17\x92\x11\x94x\x9d\x8d\xccq\x86\x7f\x7f\x0e\x98?\xd3\xf5\x12\xca\xc0\x81\x01\xae\x04\xa4\x17\xf1\xff\xdeJr\xb7B', b'\xbf\x9a\xbd\x1b') if val == _OO1I0ll00OO1(b'.\xf2\x91BO\xbf\xa7e\xfa[\xda3\xc4\xf7\xb3\xe1\xd4\xf2', b'\xddB\xb6\\') else _O00Ill1OIllO(b'\xf7\xf9\xb8\x02[\xd1\xfd\xfa\xd2\x81u0%Tt7\xfd#@r\xd4h\x8c\xce\x0f\xe7\xf6i\xaf\r=-TQQX.v\xf1y\xcc\x9dV\xb6\t\xa5l^\xf4o\x1cO\x85\x8a\x08\x853\xc4', b'\xba\x1c\xb3`') if val == _1lOOIlll100100O(b'\xdf\xc6\xed\x88\x1db\xc8p\xdbPk\xca\xf5\xfa<\x90\xe8\xf2\xa8', b'\xdb\x18iO') else _O00Ill1OIllO(b"D!k\x18\x15\xa9\x818\x16\t\x9a\xb97\x0f0.\xcdy\x99'7JZ\x18\xe0+X\x06\x96\xdeg]\xe8%u\x02GS\x91\x17\x18\x99;5\x03z2\x91\x02m4\x12\x98\x14O,-\x0ec", b'.y,\xe0') if val == _O00Ill1OIllO(b'W\xd8j\xea6\xaf\xb0\xb4$\xf2\x86\x1fu\x92Mj\xbf', b'I\x93 \xd0') else _Il0I00l0OIIlO(b'', b'\xf94\x15\x81'), subset=[_OO1I0ll00OO1(b'\xc8\xe9\x97\xbb\x07\xca\xb1\x00', b'p\xe8\x17\x91')])
        return styled_df
    except AttributeError:
        return df

def render_all_tabs(serp_api_key, groq_api_key, company_profile):
    tabs = st.tabs([_1lOOIlll100100O(b'\xe9\x18\xfc\xc3)\t\x04S\xf3\xea\x8b\x7f', b'Afw#'), _OO1I0ll00OO1(b'\xdf\xe0\x16\x10\xae)#\x03~$Y\xb9', b'\xf6\x89t\x90'), _OO1I0ll00OO1(b'\xb7\xd2\t\xc9\xb2\xa5\xe1}\x1aqp\xd5\xf2\xc3', b'\xf0\xd8\x80\xd3'), _O00Ill1OIllO(b'\xf7\xf0\xb2\xaf\x83J\x11\x02\xc4a\xed', b'\xf3\xc0oN'), _Il0I00l0OIIlO(b'\xee\x80\xb3\xfd\xa1\x83\x14\xae\xf1\xf8\xc9`\x93', b'\xb2U\xacO'), _1lOOIlll100100O(b'U>\xc4XT\xaf\x81\x97\xb0\x11\x8c\x96', b'7\x9c\xcf\xd1'), _OO1I0ll00OO1(b'\x1e(\xc0\xa2J?x\xe6\xe7^\x8eQ', b'\xa4M^e'), _O00Ill1OIllO(b'^h\x03Z\xf6\xc5M8\xa5f\xe87#', b'$7\xf3\x85'), _OO1I0ll00OO1(b'\xf2v]\x9f}n\xbf{;(\xa9\x03M\xf67\nr\xdd\x04', b'\x84\xa1\xe3\t'), _Il0I00l0OIIlO(b'\x80* 0\xdd!\x03\x87\xf4g\xb0,\x92d', b'\xb0\x14\xfd5'), _1lOOIlll100100O(b'\x82\x01\xd6\xf2*+G\x10\xa4\xedM0\xab\n\x03\xd4', b'\xe9\xfb\xac\xb9'), _OO1I0ll00OO1(b'KIuu\x9fO\xe5<\xd6R\xed\xea', b'V4\xc3g')])
    with tabs[1051311663 ^ 1051311663]:
        render_profile_tab(company_profile)
    with tabs[1155869548 ^ 1155869549]:
        render_scraper_tab(serp_api_key, company_profile)
    with tabs[907440993 ^ 907440995]:
        render_dashboard_tab()
    with tabs[112261374 ^ 112261373]:
        render_enrich_tab()
    with tabs[1027255591 ^ 1027255587]:
        render_abtest_tab()
    with tabs[2146500351 ^ 2146500346]:
        render_history_tab()
    with tabs[752421678 ^ 752421672]:
        render_email_tab(company_profile)
    with tabs[1897890985 ^ 1897890990]:
        render_whatsapp_tab(company_profile)
    with tabs[1006446788 ^ 1006446796]:
        render_multilanguage_tab(company_profile)
    with tabs[1527510396 ^ 1527510389]:
        render_followup_tab(company_profile)
    with tabs[1208539064 ^ 1208539058]:
        render_integration_tab()
    with tabs[1236095019 ^ 1236095008]:
        render_support_tab()

def render_profile_tab(company_profile):
    st.markdown(_Il0I00l0OIIlO(b',\xf0\x9e?\xffg\xf5\xaf/a\xe2\xb1OTF\x16\xdc\x9a\xd8\xf1n}\x06\xae,\xc7.@\xea\x8b%o\xed\xcd0\xc5\xc4\xc4\xf7\xdbLR\xe4\x9e\xa5\x90\xd9\xe3\xa5\xfd\xb9\x99W@\x04\x11\xfc\x8e', b'\xaav\x00\xc4'), unsafe_allow_html=True)
    st.markdown(_OO1I0ll00OO1(b'\xfd\x80eL%\xd40\xbds\x8eF\xd9\x80\xcbPgh\xd2\x1c\xf3\xcaf\xd3\xf7l\xc3\xc7X\x0b\xf7\xc2\'\x18Kd\xe0\xe8\xd7M\xb3ng^\xec\xa1\r>\xa9\xd0\xd17M\xf3\xc1\xf3rt\xe5\x03\xde\xedAY\xdfl\xe1\x91\xed9(e\xb9D"\x10\xde\x07"\x86\xcf\x1b\xbb', b'X\x1a\x8bz'), unsafe_allow_html=True)
    st.info(_Il0I00l0OIIlO(b"\x03\x8d\x12\xcf\xae\x008\xbc\x9f}\xaf\x06\x0eH\xe4\x17'\xde\xa1\xa2\x01\x0f\xc7\xb1N\xbdVpf\x8e\x02\xb4\xf9\xc8\xae\x01\x8d\xe4\xba\x9es\x169#\x90\xf3z\x7fp\xddy$\x85I\xab,\x80\xb6b\xd6\xd2\xcc\xf3(r\xf0\xa3IA7Y\x9d[H\x1b\x9dm\x88\xeb\xcb\x81\xfe\x87\x1a\x03\xdc\x9e\xec>:M\x07b\xf8 \xf0\xa8a\xa2\x02\xd0\xc4\x93\xdd,\x1e\x9b\xdf\xa1\xa23O\xadL\xf2\xef}\xa4J", b'\xf5h\xba\x90'))
    with st.form(_1lOOIlll100100O(b'@\xeca%\xae\x04\xdd=\xb8U\x90\xa1v\xd1\xb5a\x1f0\x19\xc1', b'G\x9d\xd0-')):
        st.markdown(_1lOOIlll100100O(b'\xf1\x8b\xa0?}\xd4\xa3\xcf\xc6V\x116S\x19ihr\xcb\xa4\xc5\xee;\xe2\xdfrr\xee\x98', b'\xd3\xb4\x88\x88'))
        col1, col2 = st.columns(1742783536 ^ 1742783538)
        with col1:
            company_name = st.text_input(_O00Ill1OIllO(b'\xfa\x08+\xfe\xff\x8b\xebc\xb4[-VV\xf7', b'\xed\xad? '), value=company_profile.get(_OO1I0ll00OO1(b'\xdfF\x14\x80s7\xde\xf3\x90\x15\xf77', b'm\x84R\xf2'), _OO1I0ll00OO1(b'', b'A\xf2\xa8R')), help=_Il0I00l0OIIlO(b"\xffW\xfb\x88'\x98\x9a\xb8\xcd\xee\x0f\x16N\xe5\r\x0fy\xe9\xc6\x8c\xc7|Ke\xe2\xee\x9f\x92)\x1e\x90\xe3-\xdf\xb4\xc6@k\xbb\xb6i\x04\xea\xb1\xb0X\xb5\xef@\x18\xea\xb3c\r%\xec", b':\x8caU'), key=_O00Ill1OIllO(b'\xf6\xa7\x87\x92\x85FM\xde\x86\x97\xdat\x8b3\xcf\xc9.\xb2}\x0c', b'\xea\x16\xe1\xed'))
            company_phone = st.text_input(_Il0I00l0OIIlO(b'$\xfb\x15f\r\x9b\xa1\xbc\xd6\xc0\xb3\xc7\xaa\x99~', b'\x0b\xe7\xb5\xc4'), value=company_profile.get(_OO1I0ll00OO1(b'V\xc4\xb2\xe98\x1e\x1cg]\xfb\x02W~', b'\xf03\xd4\x93'), _1lOOIlll100100O(b'', b'\xabg\x88\x00')), help=_Il0I00l0OIIlO(b'\xfb\xd9\x1c\xa9G\xd0\xb5\xf0B\xb9OBL\x91H\x95\x9a4@D\xaeG`\x9c', b'\x83*\xd3J'), key=_OO1I0ll00OO1(b'\x05+\xc6\xe5/\x80{r\xa9\x9a\xdb\xe0}Va\x1d\x00E\xdf\xda\x97', b'\x16\\\x05P'))
            company_email = st.text_input(_1lOOIlll100100O(b'\x07\xac\xb2\x91n}\xfb\xaf\x1amU\x10\x96\xc5\xf3', b'.\x97V$'), value=company_profile.get(_1lOOIlll100100O(b'\x08\xae\xca\x12\x19\x16\xdf\xea\xad}\x03i"', b'~f\xc2\x1a'), _1lOOIlll100100O(b'', b'*\x06\x1b\x80')), help=_Il0I00l0OIIlO(b'\xbb\x0c)\x8d\xb9|\x04\xe6\tuB\xb7\xbb20oB\x10\x1er\xfa1\xdb\x0b\xb6', b'k\x02\xf5R'), key=_O00Ill1OIllO(b'%\x94\xe2Q\x16\x05\x0b\x18!W\x19/%r_h\xa6m?hQ', b'ju\x1e}'))
        with col2:
            company_website = st.text_input(_1lOOIlll100100O(b'\xab\xa9\x9d\xd0!4?\x8a\x9a\x99\xa6\r\xa4\xa7\xd4', b'\x1d\xc1s\xbc'), value=company_profile.get(_OO1I0ll00OO1(b'4Y^"\x00\xeeR\xce\xe5{\x85\xff\xdbr\x85', b'\xe5\x0b\xe9\x06'), _Il0I00l0OIIlO(b'', b'T\xc0ak')), help=_O00Ill1OIllO(b'"\xde\xffb\xf5\xc4\xd8\x92L\r\x9e\xcb\xcf1\x82S\xe2@:g!\xd5BL', b'\xa9;\xba\n'), key=_Il0I00l0OIIlO(b'\xdf\x19M\xd0s\t\r\x0b\\\xeb\x8d\x0c\xd3\xbf\xc3\xb6\xbf)\x95\xa1\xb0\xb1s', b'\xdb\xfb\xfe\x1c'))
            sender_name = st.text_input(_1lOOIlll100100O(b' \xb2\x01\x85\xad\xbf^\xbe]\x06W\x00\x95', b'\x17\x10\xfa\xbc'), value=company_profile.get(_O00Ill1OIllO(b'\xb0\x86^\xe2R\x1b\xa7r,i\xd5', b']\x00G\xfa'), _OO1I0ll00OO1(b'', b'\x97mhg')), help=_O00Ill1OIllO(b'S\xf1\xc0\xc0\xfd\xafA\x02\xe4%\x9c_\xdd\x14\xc7\xd5\xb8\xa6\xb2\xaf\xaf\x0cq\xb4\xc8g\xc6\x91\xf3\xda\xb7', b'\x16\xf6-\xbb'), key=_1lOOIlll100100O(b'\x81\x7f\x18\x03i`\x006\xf35\xe0{\x18\x8c\x06\x12\t\xf9\x7f', b'.\x8fC\xb0'))
            company_tagline = st.text_input(_OO1I0ll00OO1(b'\x16\xbd\x90\xd8\x03i\x0c\xc0\x13\xb7\x1a|3[|', b'\xed\xda\xd3\xcc'), value=company_profile.get(_O00Ill1OIllO(b"R\x11\x86l$\xd3\xd4'\xa8\x8b\xbc\xb0\xe5\xbe[", b'\x9b\x0c5b'), _O00Ill1OIllO(b'', b')R\x80\x19')), help=_Il0I00l0OIIlO(b'\x12h\xea4\x0b\xb6\xebX9\x88\x98\x1eP&\xcf\x99a\x8b;\xf26G\xfb-61*?R\xc8', b'\xdcW\xb4['), key=_1lOOIlll100100O(b'\xca.\x8a\xc7;\xe41\xb5\r\xf0\xc7\xff<\x12\x8c', b'r[\xf3\xa2'))
        st.markdown(_OO1I0ll00OO1(b'%\xce\xa0', b'\x8b\xc5I~'))
        st.markdown(_Il0I00l0OIIlO(b'\xf3\xd3G\xef\x8bF/\xe6\x88\xbd\xeeE\xfcY\x89\x9c\xe8\x92*E\x94Qhc\x80\xf0\x0e\xc2\xa4\x83\rV', b'\x11\x04~\xf5'))
        col3, col4 = st.columns(58445704 ^ 58445706)
        with col3:
            product_name = st.text_input(_O00Ill1OIllO(b'F\x81\xbb\xa1\xa3\xc8\xc1\xcf\x14\xb7\x19u\xcd\x84c;\xb2\x80\x91\xb9`\\', b'm\xfb\xee\x9f'), value=company_profile.get(_O00Ill1OIllO(b'\x9f\xc1\xc1t\x02w&\xfb\n\xbd+\x07', b'\xb2(\x05y'), _1lOOIlll100100O(b'', b'\xe1\xfc\xfd%')), help=_Il0I00l0OIIlO(b'\x11ye\xa8@\xcf\xdc\xd1\x0e\xc8\x01QkU\xc6Yn\xe1\x86\xa6\x8d\xdd\xe6\x1b*\xf0\r\xc6\xbb', b'\x9b\x7f\xad\\'), key=_OO1I0ll00OO1(b'\x0by\x17\xdc\xb1\x04\x01+\xd4\x1f\x0f\x93\x94\xf4p\x8e7Q\x1a\xc2', b'\x9e\xfa\xcd\x89'))
            product_description = st.text_area(_Il0I00l0OIIlO(b'\x95\x8d\xd07\x8b\xfa\xb4\x16\xe0\x1c\xbe\x82\x9cXse&7p\xe51', b'\r@L\x97'), value=company_profile.get(_O00Ill1OIllO(b"Oz@S\xa5_\xc6\xa6'n\xc9\xaf\x8d\xab\x98\nJw\xb0", b'I\x0c\x17\xda'), _1lOOIlll100100O(b'', b'\x85p\x18\xf1')), help=_1lOOIlll100100O(b'b\x1c\xbd\xb6Z\x1a\xfe\x08yoQ\x943*\x89\xefz\xea\xc4\x07*\x04\xe7D\xbd\xb5\xafL5\x9a\xbe\xfab\x8a\x06C\xf5\x93\x8e\xc1(\x9bo#v', b'`B%d'), height=1503279338 ^ 1503279290, key=_1lOOIlll100100O(b'\x19Y[*\x14`s\x1ew\xf9\xeb-\xe4\xac\xb9\x13"\xbd\x95~', b'\xa6`\x80\xad'))
        with col4:
            special_offer = st.text_area(_OO1I0ll00OO1(b'G\xb8\xb3\x87!\xc6\r\xd4\xa1t\xe3\xeb\xf1f\x11', b'\xcc;2x'), value=company_profile.get(_1lOOIlll100100O(b'\xfc\x92\x80\xd8\xd2\xb7*\xadw\xbb\xc9\xe7<', b'\xbe\xd4Y\xb6'), _Il0I00l0OIIlO(b'', b'9\xe1\x0f\xdc')), help=_O00Ill1OIllO(b'\xf5\xfc~\xc7\x17\xbf\xa43\xf0\x1c\xcfk\x0c\xb67\xf2\xf5J\x85bqa\xe6|\xa8m\xa9mH\xa2\x87\x89\x1e\x99";\xd3', b'\x19&\x01\x82'), height=1511045778 ^ 1511045826, key=_O00Ill1OIllO(b'j\x8d\'\xf8p\x88\x92"E:\xd0x\x16\xea\x8b\xea\x05\x08A\xce\x9e', b'1\xd4\x9b\xaa'))
            call_to_action = st.text_input(_1lOOIlll100100O(b'\xd2\xbe\x8dP\xb45\xbd?\xac\x8e\xfd\xe0\xa5\x02T\x1b', b'\xafDw6'), value=company_profile.get(_OO1I0ll00OO1(b';\xa8\xb3\xea1t\xe0*\xae\xa5\xbd\x11\xe5\xaa', b'D\xbc\x91k'), _O00Ill1OIllO(b'', b'F\x92\x9d\xde')), help=_1lOOIlll100100O(b'\x90\xe1\x1c\xf0b\x82"\xd2\xc9\xeb\x89\xb6\xb1\xf9\x93\x88\x01\x056*e\xaa_\xe3\xdd,t6]\xa0w\xa0r\x1d_\xe2\xe3\x11"*c+\xab\xab\x1b\xc3\xfd\xdb \xb8\x1eg/\xed\xf4s)l\x9c', b'F[#\xb4'), key=_1lOOIlll100100O(b'\xa6\xa5\x1b\x97s\x89\xd3\xbdj\x9d<', b'\x8f\xabJ\xd1'))
        st.markdown(_Il0I00l0OIIlO(b'\x7fat', b'i+I\xe2'))
        st.markdown(_OO1I0ll00OO1(b'\x11I\xd8\x02\xf9\x9dE\x0e4\xfd\x01\xf2\xbe\x80\x81Y=\xa46\xd6\x11\xe2\xad\xf6', b'2\xfb8\x13'))
        col5, col6 = st.columns(1223802546 ^ 1223802544)
        with col5:
            industry = st.text_input(_O00Ill1OIllO(b'\x0b\xae\x04^E\x12\x02\x9f\xde0\x9e\xab]', b'\x07\x9ax\xc9'), value=company_profile.get(_O00Ill1OIllO(b'%,Q\\K\x86Z\xa2', b'\x9a\xd2\xfdV'), _OO1I0ll00OO1(b'', b'\xa3\x98\xa3D')), help=_OO1I0ll00OO1(b'\x8bwK\xcd\xcfO4H\xc0!6\x1f\x82\xb0\x1c\xf7\xa2\x8a\xb5\x1201_', b'F\x8b\x9a\xe6'), key=_1lOOIlll100100O(b'\xc7\xf9Z^\xf4[\x11\x12\xb2\xca14\x08pe\xcd', b'\tm\xaa\xf6'))
        with col6:
            target_audience = st.text_input(_1lOOIlll100100O(b'\xc6\x85j\xab\xec\xf9_\x9b*|\xfc\xef\x1e\x1d`', b'\x1ag\xb3.'), value=company_profile.get(_O00Ill1OIllO(b'\x85\xca\xc4\xdc\xd6w\x90\xc2X\x90?\xb8\x8e\xba\xa6', b'\x1e\xa90\xfd'), _1lOOIlll100100O(b'', b'a\xf3\x04\xed')), help=_O00Ill1OIllO(b'\xa4\xff\xb9\x0fs\xe1\xd4fEnK\xb6\x81A\xc7F\xbbS\x89w7\x00{n\xa8\x0e\x86*G\xa2G<U}]\x1cx\x19\x9a3\xdb/\xcc\xec\x87)\xaf\xa3\xd3\xc0\xaf\xc7\xaa\x8f', b'0\x8d8\x10'), key=_Il0I00l0OIIlO(b'\x98\xf0\xa2\xb2\xcf\xfc\xed !EI\xdc-\x7f', b' j\xb9\x0f'))
        st.markdown(_1lOOIlll100100O(b'\x13,\xf6', b'\x00+`\x1f'))
        if st.form_submit_button(_OO1I0ll00OO1(b'\xef\xfc>\x88\x99\xc1:g\xe3\xb9\x1b\x9c\xc9\x17&Hn\xbd\xe8H\xb6\xe0\xe1\x02\xbd', b'\xba=\xa1\x14'), type=_Il0I00l0OIIlO(b'\x013\xf7\xbf\x93\xc5\xd3', b'\x1a\xcb\xd1\x91'), use_container_width=True):
            if all([company_name, company_phone, company_email, sender_name, product_name, product_description, special_offer, call_to_action]):
                profile_data = {_O00Ill1OIllO(b'd4n\x1c\x0cv\xfdf\x9a>l\xb0', b']\x84\xa41'): company_name, _OO1I0ll00OO1(b',\xado\x8b\r"f\xcfRB\xd22\xd1', b's5\x968'): company_phone, _1lOOIlll100100O(b'2*P\xdd\x93\xc7\xecd\x1a,\xad=\xcc', b'\xcb\xd4l\x03'): company_email, _Il0I00l0OIIlO(b'Z\x95\xaaP{\r\xd0\xff\xd2N\x8b{\xd0\xdf\x01', b'\xaer1\xa9'): company_website, _Il0I00l0OIIlO(b'\x9a\x9c\x122\x1et#YV!gN', b'\xdaK\xba#'): product_name, _OO1I0ll00OO1(b'\xd2B\xafXPz\xadg\xba\xf9\xd97\xf4L\x0c5\xb54\xce', b'\xa8\x0fb\xdf'): product_description, _Il0I00l0OIIlO(b'\x05e\xb80w\xf4Cx@\x04\xc2\x1a\xd5', b'\xc2]\xb9m'): special_offer, _1lOOIlll100100O(b'>\xcb\xf6\xf0\x89\xa88~\xdd2\xf7\xb4\x19L', b'F\xb8\xec\xef'): call_to_action, _O00Ill1OIllO(b'\xe7\x8a\x85A\xef\xd4\x8b\x12\xedK!', b'$%\x0fy'): sender_name, _1lOOIlll100100O(b'I\xbdJ\xecEY\xcc\xd7\t\x88\x18]CD_', b'\xe9\xfe+\x8c'): company_tagline, _O00Ill1OIllO(b'`,>\x99\xab\x16\xd1\x9d', b'\x0e4Z8'): industry, _1lOOIlll100100O(b'\x8fd2\x1bq\x81\xc32\x16\xd5l\x06\x8c\x03\xed', b'<&f"'): target_audience}
                if save_company_profile(profile_data):
                    st.success(_OO1I0ll00OO1(b'4FHf\x18\xf8\xda5;\x12Y\xec\xa1\x9e:\xbe\x02ONbF\xebaK\xb2\xbfm\xe7\xc2\xd3\xb3*J\x04\x18\x02!l\xdc', b'&{\x02\xdb'))
                    st.balloons()
                    st.info(_1lOOIlll100100O(b"\xfbiR\xd30w\xfa\xbb\x14\xb3\x08H\x15\x81R$\x15f\\m\x83\xa9\x87\xb6\x0bVY'yH\xb6-\xf5\xe1y)\xbaA\x04\x96M\x91.\xa0jj\x19y~\xef!\xe0\xab9\x81\xca\xe96\x88\x85U\xd5q", b'\x94\xfb\x03\x06'))
                    st.rerun()
                else:
                    st.error(_O00Ill1OIllO(b'\xb0\xbc\xa1\xce\xdb:u\xf7c\xba\xd0\xcb\x89\xfe\xefEIwi{*\xech\xa2}\xf9\x9d\x10\xc0\xed\xbdhB\x8e\x8am\xe5rD\x1e\xd5\x18\xf4I\xb2.\xae{!-\xcf\x12\x1e', b'\xd4\x00M\x15'))
            else:
                st.error(_Il0I00l0OIIlO(b"S\x87\xce\xd7\x84\xfa\x9f\xfd\xf0$\x8e]\x00\x19\xd2fD8\x93q\xeb\x9f\xe3)J\xdb\xfe\xa0\x8a'N([\xfeD\xb8k\x96\x97\xc2\xd0\x8b", b'\xa6\x8e\x15\xbd'))
    with st.expander(_O00Ill1OIllO(b'\xe9\xd2\x8d\xf3eJ\x16g\xf5n&\xe4~\x18oq\x84\x8f\xbb\x18\xdc$\n\x15\xd8\x97', b'>\x0bc\xb3')):
        if all([company_profile.get(_OO1I0ll00OO1(b'M\xf3\x99\n\xd4\x91B\x1a\x9b\xb4\xb8\xed', b'\x04\xe4d[')), company_profile.get(_O00Ill1OIllO(b'\x11Z\xe4\x93\x8eOQ\xc0\xad\xfb\xc4O', b'\x87\x91k$'))]):
            st.markdown(_Il0I00l0OIIlO(b':\x8d\xf5\xbc\rg\\\xb8\x06.\xf8\x08&l\xbf\xee\x83', b'\xe7\x0c=\xc9'))
            st.markdown(f"Subject: Grow Your Business with {company_profile.get('product_name')}\n\nDear [Business Name] Team,\n\nI hope this email finds you well. I'm reaching out from {company_profile.get('company_name')}\nto introduce our {company_profile.get('product_name')} solution.\n\nWe help businesses like yours by {company_profile.get('product_description')}.\n\nAs a special offer, we're providing {company_profile.get('special_offer')}.\n\nWould you be available for a brief call to discuss how we can help?\n\nBest regards,\n{company_profile.get('sender_name')}\n{company_profile.get('company_name')}\n{company_profile.get('company_phone')}\n{company_profile.get('company_email')}")
        else:
            st.warning(_1lOOIlll100100O(b'\xbbQrj\x01|\xc9\xab\x15nP\x9e\xa7\x0f%\xe0\xafG \x80\x05+X\xab3\xcfd\x97\x95\xb7/\xf7\x8ehjl\xc2\xb8\xbb\x1e\xfd\xa8\xb9.r\xc0\x1fZ\xe3*\x85\xd6\xac#\xa4C\r\x08h4\xd1', b'?^P\xc1'))

def render_scraper_tab(serp_api_key, company_profile):
    st.markdown(_O00Ill1OIllO(b'\x0b{\xd3\xc7Y\x91P\xea<w\xc0\x18\xae\xcb\xf3O\x84\x9b\xd1\xc9\x0e7o\x8b\xa3\x95M\xd9w\xf5\x9e\xce\xc8\xbe\x8fJ0\xc2\x0c0\xe35\x90\xd9ig&u\xed\x86\xb2y\xc1/\x830-\x97\xa4\xb67', b'&\xd3q\r'), unsafe_allow_html=True)
    st.markdown(_OO1I0ll00OO1(b'\xa9\x04\x1e \xb9\xa5\x03\xc4\xe2up&O\xd8\xeb;\x17>\xb5Yo\x91T\xd0\x999\xd3\x02\xc2\x8f\xa7\xbd\x97\x18\xf2\xc1m\n^\xbbr\x82<\xb8\xb6\xf9\xa61\xabh\xb9\xbd\x19#\x8fP#\x92\x9bo\x05\x06\x8e\xb5\xdc\x03\x1ej"\xaf\x94\'\xde\xebA\xdd\xd0A\x08<`\xaf\xbc\xeb', b'\x10B\xbb\x17'), unsafe_allow_html=True)
    if not all([company_profile.get(_Il0I00l0OIIlO(b'\xd3\xe9C\xc2\xd1\xffR2\xc3\x88\xae\xa4', b'c\x01\xf1>')), company_profile.get(_O00Ill1OIllO(b'\xf1\x08\xdb\xa2L\xc9\xce:\xc5\xc6k\xfb', b'\xce_C\x8c'))]):
        st.warning(_1lOOIlll100100O(b'\xa9)\xd9\xba\x8c\x90\xed\x89\x84\x8e$:R\xb7\xa4\xc6\xd2\x16\t\xf9\x83\xf5\x8f\xcc\x19\xcb\x0bemG\xc2Cn\x9a\xd4sM\x1b:\x9a\xa0\xbeO\x03$\xcdH\xcdV \xe3\x85\xc6`<Al\xe7K\xc7\xf8A\x81&\xd9q9\x1cl\xb7\xbd', b'WW\xf8Y'))
    col1, col2 = st.columns(1800406054 ^ 1800406052)
    with col1:
        keyword = st.text_input(_O00Ill1OIllO(b'\xa1U\x15mM\xf2\xf9&LL(\xf5\xffPw\x1e{', b'\x90.wI'), _O00Ill1OIllO(b'L`\x13=\xe7\x12\xee\xa5\xecm', b'\x1e\xe2\x8d\x85'), help=_O00Ill1OIllO(b'\x01\x8eQ\xa6\t\xca<\xba\xf8\x9fD\x066\xaf\x89\x0b\xc0\x05f\x15\x95\xad\xfc\x9f\\\xfe\x08\xf8', b'F \x14\xa3'), key=_OO1I0ll00OO1(b'\x1c\x83j\x14\x04\xea\xd4\xb1\x87?K\x12\x81', b'R\xf5\xe3:'))
    with col2:
        location = st.text_input(_OO1I0ll00OO1(b'"\xc75\xef\x94M\x9b\xd9\xa1', b'g\xd7\xb4\xe7'), _OO1I0ll00OO1(b'\x08\xb3\xe6^\x14C\xfb]', b'.\x98}\x86'), help=_OO1I0ll00OO1(b"\xf3\xe2\xa0\x9e\xbb4\xfe\x00B\xf9\xd1\\A\xd6\xfcI=\xe1\xcc'\x88#\xa5\xe8l\x04\xa9\xcb\xc1", b'%-\x06\x93'), key=_OO1I0ll00OO1(b'\xc3\xee\x99\x06@&\x9a\xb6\x9e\xd8\xa3\xcc\x89v', b'yY\x04\xc1'))
    col3, col4 = st.columns(2139259884 ^ 2139259886)
    with col3:
        limit = st.slider(_Il0I00l0OIIlO(b'N\x17\xe7c)$,/S\xb9', b"'\xa7\xa9\x08"), min_value=529213285 ^ 529213280, max_value=770785868 ^ 770785918, value=1015695281 ^ 1015695291, step=387538793 ^ 387538796, key=_OO1I0ll00OO1(b'\xee\x1br\x0b\xa3\x1b\x8b\r\xb1W\x8e$', b'\xa8]\x88h'))
    with col4:
        only_no_website = st.checkbox(_OO1I0ll00OO1(b'\x8b\x92\x95f\x85\xb6+C\xb7\x1b\x92\x9d\xc3\xd9F)\x1bV\xa0W', b'\xf4\xack\xdd'), key=_Il0I00l0OIIlO(b'\xfd\xaeL\xa0uj\xb2\x16f?\xc2\xcdL\x9fG', b'Pp\xc0\xaf'))
        find_emails = st.checkbox(_O00Ill1OIllO(b"\xdd\x95\x9e\xcbL2D'!\xff#)\x83\xbe\xbb\xfb", b'\xf0?\xdd\xdf'), value=True, key=_OO1I0ll00OO1(b'\x8d\x9f\xad.m\x13\x931\xba\r\xc0', b'\xa2\xbdn\x1b'))
    if st.button(_O00Ill1OIllO(b'V\xa5\xac\x8dU\x9e-\xd2\x14\x02\xb0\x81\x1e\x1c\xd8pH\xc7V', b't\x89\xccH'), type=_1lOOIlll100100O(b'\x0e\x83pp\xde\xc9\x8e', b'\x0f\xf5\x8fx'), use_container_width=True, key=_OO1I0ll00OO1(b'\xd7\x93\x8e\xa1\xc4K4$\xc6\x83\xc0\x00G6', b'\xd2\x88\x10\xbe')):
        if not serp_api_key:
            st.error(_Il0I00l0OIIlO(b"@\x9c\x98\x13\x19\xa2\x1f\xbf\x9c\x89t>/p\x145\xea\x1a\x14\xb0(O\x07Q\xf4\xf3\xf8\x9b\x05v\xa9\x90\x93?\x16\xe90%%'\xa3\xeb\xbb\x9dSK^X\xfa\xc4\xa07\xb1.\xd2\xe0\xb1", b'.\x97\xd9\xdf'))
        elif not all([company_profile.get(_O00Ill1OIllO(b'pkG"\xa9\x99\'\xdf\x14:\x1d\x10', b'H\xf0\x0cH')), company_profile.get(_O00Ill1OIllO(b'\xb8\xce\xc2\x05\xae\xb1\x1d^b@\xed_', b'G\x8e\xc6F'))]):
            st.error(_O00Ill1OIllO(b"\x89\xa2\xd3U\x18\xdf\x13\xc5\x82\xcfjs\xce9\xba\xf8'\xe6\x0bk\x07+\x19\x1f\x99\x9d8\xd9)W\xe9\xb3d\x93r\x07\x14i\xeb\x82\x15\xedx\xa6>\xb7\t\xfe\xa4\xe3\x8a\x80\xa0\x90R\xf3n/\x08\x1e\xd3fA:\xc0\t69\xd9\xc9\xac", b'80D\x81'))
        else:
            try:
                with st.spinner(_O00Ill1OIllO(b'\xd0\x93OX,a\xd4g\xe9\x84M\x19h\x01\xc6\xa8\x16\x8f^\xa1Q\xd5\x84Gk\x91#\xf11\x88\xbf\xda8', b'\x08\xc0 \xb9')):
                    local_results = scrape_google_maps(serp_api_key, keyword, location, limit, only_no_website)
                if not local_results:
                    st.warning(_OO1I0ll00OO1(b'P\xfd\x87\xba(\xfc\xb4\x02]x8x\x00.\xc4=\x85\xc0F\x80\xf9\xce\xfa\xdf\xdb\xbc\t\xe0 l\x92\xc8/~\xad\xfd\xa8\xdd\x93?o\xfc\xc3\x11\x8a\xba\xc9\xa7\xcaX\xbf\xa9+', b'fR\x1aK'))
                else:
                    results = format_results(local_results)
                    if find_emails:
                        st.info(_Il0I00l0OIIlO(b'\xc9}F?\x80\xb3\x1c\xae\xd0\x14\xd4\xa6\x93Ue\xb2{+\xeb\x9a\xf3&\xd1D\xb5\xdd{P', b"\xcdq'\x12"))
                        email_progress = st.progress(254512055 ^ 254512055)

                        def update_email_progress(idx, total):
                            email_progress.progress((idx + (259558397 ^ 259558396)) / total, f'Searching {idx + 1}/{total}')
                        results = process_emails_for_businesses(results, update_email_progress)
                        email_progress.empty()
                    else:
                        for item in results:
                            item[_1lOOIlll100100O(b'\xa7\xd1\x80e7', b'P\xf2\xd84')] = _Il0I00l0OIIlO(b'\xd89\xe9DU\xd9\xfe\x99\xdd,FV', b'\xc5\xbckE') if item[_O00Ill1OIllO(b'jd\xb26p\xc2J', b'\xc7\x00w2')] != _Il0I00l0OIIlO(b'\xcb\xe8~aY\x1cP\xc19\x1b', b' \xb3\xae\xd1') else _Il0I00l0OIIlO(b'\x03\xfd\xa1\xe6/.\xdb\x0e\xfa\xb8', b'\x8a\x1e\xcb\x9b')
                    st.info(_OO1I0ll00OO1(b'\x9e\xe7\xb9\xa4t\xae\x8a\x8e\xc1\xc4Rx\xd9"V:b\xba\x9a\x1e\xf88\xd4gX\xfa\x13:Zzq\xbb\xff\xd9\xd3\x97\xa1uP\xddF\x07N=0\x83\xe3\x1a<2\xbf\xcd\xd7\xb9\xc6', b'\xa2\xb0\xf7\xca'))
                    ai_progress = st.progress(574200077 ^ 574200077)

                    def update_ai_progress(idx, total):
                        ai_progress.progress((idx + (1148921452 ^ 1148921453)) / total, f'Generating {idx + 1}/{total}')
                    results = process_all_messages_with_profile(company_profile, results, _O00Ill1OIllO(b'\x05c\x9bc\xf5', b'\x83]\xc9\x8a'), update_ai_progress)
                    ai_progress.empty()
                    for _ in results:
                        update_campaign_stats(_OO1I0ll00OO1(b'\x05U$+\xfeOQ\x9b', b'B\xe7\xa7o'), {})
                    df = pd.DataFrame(results)
                    email_found = df[df[_OO1I0ll00OO1(b'\xa1\xd7\xf6-`', b'vi\xd2\xdc')].str.contains(_O00Ill1OIllO(b'#', b'f\xb7\x88c'), na=False)].shape[677510662 ^ 677510662]
                    high_priority = df[df[_Il0I00l0OIIlO(b"\xdb\xd8\x077%\xb3'r", b'P\xc7\x9b\xa8')] == _OO1I0ll00OO1(b'?\xb6\xf5\x05z}(<\xb9gp\x9f\t_\xf8\x85\xba\xbb', b'\xc7)\x02\xea')].shape[1745302483 ^ 1745302483]
                    col1, col2, col3 = st.columns(545692745 ^ 545692746)
                    col1.metric(_O00Ill1OIllO(b'\x99/\x8b\x8a\xeb\xc8\x84\x85^\xfaE', b'S\x808\x8b'), len(df))
                    col2.metric(_OO1I0ll00OO1(b'4\xcd\xc2m\x91l\xf8Z%\xe9@6', b'\xfa\x05\xbc\xa1'), email_found)
                    col3.metric(_OO1I0ll00OO1(b'\x86\xf5\x0e\x90\x8dk\x9f6\xd6\xe2\xdc\xf75', b'\x0b\xa8\x9d\xb4'), high_priority)
                    styled_df = style_priority_column(df)
                    st.dataframe(styled_df, use_container_width=True)
                    filename, df_saved = save_to_csv(results, keyword, location)
                    csv_data = df.to_csv(index=False).encode(_Il0I00l0OIIlO(b'\xef\xb6\xe3!\xae', b'\t\xb30S'))
                    st.download_button(label=_Il0I00l0OIIlO(b'\xb8\t\xecN\xbew=\x95\xc4K:\xc8\xfb\x8cD4:', b'\xd53n\xf7'), data=csv_data, file_name=f'leads_{keyword.lower()}_{location.lower()}.csv', mime=_O00Ill1OIllO(b'\xa2\x15\xf9\xa3q\xa9x5', b'C\xadk\x00'), use_container_width=True, key=_OO1I0ll00OO1(b'^\x1c.q0L&\x99\xb7@\xcd\n\xc7\xa7\x1e\x82\xb6K\x0f\x82', b'\xe1\xe1\x1e\x02'))
                    with st.expander(_Il0I00l0OIIlO(b'\x0b\xa5"\x1c\x0cV\xe8G\x84p\x0c!\xdc\xba\xbdwy\xd8\xe3\x1a\xbb*\x1e\x05O\xee\x99:', b'\x86\x1a{\xb9')):
                        for idx, r in enumerate(results[:680223484 ^ 680223478]):
                            st.markdown(f"**{r['Business Name']}** - {r['Priority']}")
                            st.info(f"📧 {r['Email']}")
                            st.text_area(_OO1I0ll00OO1(b'R\x80Z\x05\x06i', b'\x19\xce\xe56'), value=r[_Il0I00l0OIIlO(b'\xd3\xda\xd8\x97\x97\x97Ay\xec\xcep\xb2_\xa9\xf5;.r\x00IZ\x8d\xda', b'\x99w\xc5Q')], height=2098412159 ^ 2098412265, key=f"pitch_{r['No']}_{idx}")
                            st.divider()
            except Exception as e:
                st.error(f'❌ Error: {str(e)}')

def render_dashboard_tab():
    st.markdown(_O00Ill1OIllO(b"7\x90U\x8e\xc8'\x13\xa4P\xdb\x18\xef\xa3\x19\xe8\xb8\xd0u/\xd12\xbc\x19\xa6\xefr\x0f\xfa\x16z\xe04\xe6\x02fE\no{\xce\xd0C\x88\xb5\xed\x01\x99}?\xe0\x93a", b'\xd9&\xe4>'), unsafe_allow_html=True)
    st.markdown(_O00Ill1OIllO(b'\xdb\xf3\xe5\x1a\r\x1c7\xf7$\x95\xb2\x87\xdd\x94n\x92\xbf\xb9r\xb8\xb6}3\xf9K\x19\xd0?\x07$\x1e\xc4s3\xae\x83lp\xc1\xc2\x10H\x0c\x0b\x02\xac\x9c7}\xb1*\x9e\x06nrE\xa8\x06P\x03\x84\xeb\x10\x17', b'J\xde\xf6\x9f'), unsafe_allow_html=True)
    metrics = get_campaign_metrics()
    campaign_data = load_campaign_data()
    col1, col2, col3, col4 = st.columns(1620762105 ^ 1620762109)
    with col1:
        st.markdown(f"""\n        <div class="metric-card">\n            <div class="metric-value">{metrics['total_leads']}</div>\n            <div class="metric-label">Total Leads</div>\n        </div>\n        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""\n        <div class="metric-card" style="border-left-color: #2ecc71;">\n            <div class="metric-value">{metrics['contact_rate']:.1f}%</div>\n            <div class="metric-label">Contact Rate</div>\n        </div>\n        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""\n        <div class="metric-card" style="border-left-color: #f1c40f;">\n            <div class="metric-value">{metrics['response_rate']:.1f}%</div>\n            <div class="metric-label">Response Rate</div>\n        </div>\n        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""\n        <div class="metric-card" style="border-left-color: #e74c3c;">\n            <div class="metric-value">{metrics['conversion_rate']:.1f}%</div>\n            <div class="metric-label">Conversion Rate</div>\n        </div>\n        """, unsafe_allow_html=True)
    if campaign_data and _Il0I00l0OIIlO(b'\x8f\xe7\x979\xa15r\xd6 \xd5\xc6', b'j\x1c\xbbv') in campaign_data:
        daily_data = campaign_data[_Il0I00l0OIIlO(b'{p\xe0\xfe\x9ez\xc5\xe6\x8c%\x1e', b'\x03\x13$?')]
        dates = sorted(daily_data.keys())[-(358779595 ^ 358779589):]
        if dates:
            plot_data = pd.DataFrame({_O00Ill1OIllO(b'\xf3\xd4?\xec', b'\xc5\xa5\xf8\x11'): dates, _1lOOIlll100100O(b'L\x10\x04\xec4', b'\xab\x90\xb6*'): [daily_data[d][_OO1I0ll00OO1(b'j3\xd4\xdb\x1f', b'\xe8\xa9i\x8a')] for d in dates], _1lOOIlll100100O(b'\xd0s\xa9e\xbc\xfb\xad6\x8c', b's\x11\x07\xc2'): [daily_data[d][_Il0I00l0OIIlO(b'be\xa1ke\xa2\xb4\xf5\x95', b'\x1b=\xa9\xcc')] for d in dates], _OO1I0ll00OO1(b'\xc0\x9f7\x8e/\x1b\x88\x94y', b'g\x84\xad\xc5'): [daily_data[d][_OO1I0ll00OO1(b'j\xcf1\x0c\x9bKm\xa2\x80', b'\xd1\x92\xaf:')] for d in dates]})
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=plot_data[_1lOOIlll100100O(b'D\x1b\xaa\x9c', b'\x0e\x91\x0e9')], y=plot_data[_OO1I0ll00OO1(b'\xb5\xe3\x145\xf4', b'\x18x\x01\xc9')], name=_1lOOIlll100100O(b'\xfb\x07\xc4\x04J', b'\xba\xa6M\xcd'), line=dict(color=_Il0I00l0OIIlO(b'\xf7\x01\x9d\x11\x18\xd8\xc2', b'\xd8\x94\x98l'), width=2023847818 ^ 2023847817), mode=_OO1I0ll00OO1(b"\x17\t\xba\x1e}'\xda\xe3\x89\xe7\x0fv\x19", b'\xba*pe')))
            fig.add_trace(go.Scatter(x=plot_data[_1lOOIlll100100O(b'>d\xfb\xb2', b'\x821\xcc@')], y=plot_data[_OO1I0ll00OO1(b'\x0f\xb48\x0e\rY\xc1l\x1c', b'3PEi')], name=_1lOOIlll100100O(b'MQ\xff!h.\x7f\xf4\xae', b'>u\xfeO'), line=dict(color=_O00Ill1OIllO(b"\xff\x89:\n!'\x97", b'\x17\xa9\xfe\xc5'), width=1202331016 ^ 1202331019), mode=_1lOOIlll100100O(b'-"\xdeE^[\xda\xa1\xfe\x82\x8d\x10-', b'\xc0\x80M\xba')))
            fig.add_trace(go.Scatter(x=plot_data[_Il0I00l0OIIlO(b'\xff\xa8n\x7f', b'\x88r\xe8,')], y=plot_data[_OO1I0ll00OO1(b'wx-\xaa%\xf6W\xee\x00', b"\x89\xd3\xbd'")], name=_OO1I0ll00OO1(b'\xd0\xcf\xdae\xd8\xd3W0\xb5', b'\x17\xb2dy'), line=dict(color=_1lOOIlll100100O(b'\xce\xa4m\xe75\x98K', b'\xb6\x8d\xa4)'), width=671296295 ^ 671296292), mode=_OO1I0ll00OO1(b'\xd0\x8b\x0fr\x8a".@D"8\n\xfa', b'y\xc7\xb1\xd7')))
            fig.update_layout(title=_Il0I00l0OIIlO(b'\xc7\x17\xfe?\xf6\xf3\xf07\x99\x8e1\x98\xc6<', b'\x96w\xc1\x1f'), xaxis_title=_O00Ill1OIllO(b'U\x8f\x10\x89', b'\x83[\xcb\xee'), yaxis_title=_1lOOIlll100100O(b'_\xb9\x1d\xd7\x85', b'\xe1\x06\xd2\x04'), hovermode=_1lOOIlll100100O(b'\xb8\x8c#\x93\xee\xfbnzS', b'\xfc,\xcb{'), height=505418922 ^ 505419066)
            st.plotly_chart(fig, use_container_width=True, key=_O00Ill1OIllO(b';\xa8\xf70\x1d\xe4B\xd9\x0f\xafT\xc5<"\xb2)[\xcf6Y', b'C2\xf9\xf8'))
    if campaign_data and _Il0I00l0OIIlO(b"\xa5|c\x15!Q\xb1\xcfJ'\xddd\xe4", b'U 0\xb9') in campaign_data:
        channels = campaign_data[_O00Ill1OIllO(b'Z\xd4\xb4\xdf\x05\xcc~*\x1fr&\x05m', b'\xec\x06\xee\xa8')]
        if channels:
            channel_df = pd.DataFrame({_Il0I00l0OIIlO(b'\xe9>#\x0c7\xe73', b'c55\\'): list(channels.keys()), _OO1I0ll00OO1(b'ZNr\xceE', b',\xece\xac'): list(channels.values())})
            fig = px.pie(channel_df, values=_OO1I0ll00OO1(b'\xeb\xdc\xaf4\xfa', b'\x9c\xa4QR'), names=_Il0I00l0OIIlO(b'o\r\xceH1\x8du', b'\t2\xbc\xab'), title=_1lOOIlll100100O(b'\x0b\xf0k!\xe1\xbdh\xdc\x99\xf8\xcd\xf9#Q\xd6\x97\xb15=8', b'C\xc8\x9b\xcb'), color_discrete_sequence=[_OO1I0ll00OO1(b'"\x1a\x9eo\x88\x0eO', b'W\xa6\x05\xc7'), _O00Ill1OIllO(b'\xef:#\x94]}\xf8', b'"i\xd6\xb4')])
            st.plotly_chart(fig, use_container_width=True, key=_OO1I0ll00OO1(b'&\x92\x1a\xa2y\x9b\xec\x80\x0e\xa73\xc1\xae7\xd9\xfa\x93\x0f$Gt\xfcp\xc7\xc9w', b'|\x02g\xe9'))

def render_enrich_tab():
    st.markdown(_O00Ill1OIllO(b'\xc6@\xe6\x80\x0c\xd7\x90\x05\x8e_t!\x0fWz\xb8\xd1\xa0\xdfwiX\xe8p\xd9\xda\xc2\xf2\xe4\x170n\x8d\xe5c|W\xf4\x04\xa5vN\x00b\x9f\xab\x15\xaf/', b'\xd3\xe1E\x18'), unsafe_allow_html=True)
    st.markdown(_O00Ill1OIllO(b'\xba\xc8\xd0"\xd8\xcfa\x7fiOO\\:\xef\x85UO"t\xd72\x8aO\x11\xe1X\x0b\xa9\x9f\xf1\xa7T\xfd\xfakI\xdav\x81N\xdd\xe4R\xf0f\xf4\x8f\xada4u\xdc9\xbbS\x91\xd4X\xc0?\x08Q\xd7\x07\x81|<B\xfe\x07b\x1a', b'<-\xe7%'), unsafe_allow_html=True)
    groq_key = get_groq_api_key()
    if not groq_key:
        st.error(_OO1I0ll00OO1(b'\x8c\xd07\x1a_\xdc\x11\x91\x02A\x0fng\\\xd7B\xab\xb4\x9a\xe7\x83\xaf2C/0\xfa\x9e\x10\xe5\x85\xfcm\x9cn\xe6\xf3\xa3k\x96\xaeU\x1b\xcb\xf2\xb1\xdd[\x8d\xf1<\xcd\x87\xf0Yn^M', b'`\x82\x11A'))
    load_option = st.radio(_1lOOIlll100100O(b'b\xd9\x1d\x0b\x01\xdf\xe9x\x8e\x92', b'\xadiP\x92'), [_OO1I0ll00OO1(b'\xf2\x1ci8\xc5\xfa\x9d', b']e\x03k'), _O00Ill1OIllO(b'\xa9Q\x19\xe6\xca\xf0\x9c\x8a+o', b'\x88\xf6M^')], horizontal=True, key=_O00Ill1OIllO(b'\x8c\x9dS6I^\xd0N\x10R\x18Q\x9a\x9d\xbc\xd3\xa5\x9b', b'w\xdbo\xa6'))
    df_enrich = None
    if load_option == _O00Ill1OIllO(b'\xb3j\xb3\x88\x03\r\x15', b'G*\xb9$'):
        files = get_history_files()
        if files:
            selected = st.selectbox(_Il0I00l0OIIlO(b'/\x92A\x13o\xa7#\x889\xfbY\xaf', b'\x1a\xe8|\x06'), files, key=_Il0I00l0OIIlO(b'\x9719\xbf\xcb\xaf;\xa9\x8bUq\xca].\n5\x02\xe1', b'g\x9c\x86/'))
            if selected:
                df_enrich = load_history_file(selected)
    else:
        uploaded = st.file_uploader(_O00Ill1OIllO(b'\x8e7\xb8%w\x81\x03\x00e\xd6v', b'\xdf\xae\x8b9'), type=[_Il0I00l0OIIlO(b'\x1d\x0f\xd3', b'8\x0fjo')], key=_1lOOIlll100100O(b'\x90z\xac\xbf\x95u\xed\xe9\x9fRhui\xb1Z\xbc\x9eW', b'\x01X\xfa6'))
        if uploaded:
            df_enrich = pd.read_csv(uploaded)
    if df_enrich is not None:
        st.info(f'📊 Loaded {len(df_enrich)} leads')
        has_website = df_enrich[df_enrich[_OO1I0ll00OO1(b'\x8cj4\x85\x04vV', b'\xa2W\xc20')] != _O00Ill1OIllO(b'u\xe4C\xb3\x04\xe6\x1f\xba\xcd|', b'\xaec,\xe3')]
        if has_website.empty:
            st.warning(_1lOOIlll100100O(b'LY\xbf8%Y:\xf3\xec\xf8|M\x91\x87\xdb\xeb\x01\xa9\xcd\x1f\x19\xb4\xb1\xa1\xf5\xdd\x85\xed', b'\x05\xce\xe1\xd1'))
        else:
            st.success(f'✅ {len(has_website)} leads with websites')
            st.dataframe(has_website[[_1lOOIlll100100O(b')\xf7j\n\xd5\xfd\x9e\xdd\x9f\x122\ne', b'T%\xcf\x9a'), _O00Ill1OIllO(b'\xb4\x94\xc2Z\x84\xdb+', b'>8X\x17'), _1lOOIlll100100O(b'M\xaed&\xa5B', b'\xf6\x9b\xbf\xc1')]], use_container_width=True)
            if st.button(_O00Ill1OIllO(b'\x12N\xb3\x8e\xa5\x05\xd6\x19(\xfa\x05\x8a\x8d\xa2\x1b7\x83\x7f\xbbQ\x11', b'dN\xe6\x13'), type=_Il0I00l0OIIlO(b'\x0f \xe25#\x80\xc2', b';\xd8q\x99'), use_container_width=True, key=_1lOOIlll100100O(b'\x86\xbb\xb7\xe7\xe4\xca E\xeaF\xe3c\x9d\xd5\x17\xe5', b'/\xdeG\x10')):
                if not groq_key:
                    st.error(_1lOOIlll100100O(b'H\xfb\xbd\x018\xcc\xa4kT\x01A\x1b+\x98\xf3\xbc`*_\xe3D\x80\x89\xd2\xc1\x92U\xc7{,\xeeMF\xc7\xc5\x9f5_g\x18\xbd\xd9\xe6sI\x12\xd6\x81}\x14\xcd', b'\xb4\x10{\xc6'))
                else:
                    st.info(_1lOOIlll100100O(b'9\xf4\x04R\xee\xd5d}\x01[\x17n\xa2$\xb7n\x01w\xf0\xe1CQ\xb9_\x04\x07/\xb8\xde\xc7\xdf\xfa\xc1g(g\xe0\xac\xb7\nf:\xbb\xbb\xf9#H\x01}\xe0\xb2\x10\x86l', b'\xe6\xce(%'))
                    progress = st.progress(1571657212 ^ 1571657212)
                    status = st.empty()

                    def update_enrich(idx, total):
                        progress.progress((idx + (1326364849 ^ 1326364848)) / total)
                        status.text(f'Analyzing {idx + 1}/{total}')
                    enriched_df = enrich_multiple_leads(has_website, update_enrich)
                    progress.empty()
                    status.empty()
                    st.success(f'✅ Enriched {len(enriched_df)} leads!')
                    st.dataframe(enriched_df, use_container_width=True)
                    csv_enriched = enriched_df.to_csv(index=False).encode(_OO1I0ll00OO1(b'\x04\x07(\xae\xea', b'\xd8_b\xbc'))
                    st.download_button(label=_O00Ill1OIllO(b'R\x9cA\x7f_\xf1T,3\xbd\xbcrD\xf4\xfc\xd6\xecb*#.C\xff;\xe2tN', b'\xfd\xc6\xfe\x0c'), data=csv_enriched, file_name=f"enriched_{datetime.now().strftime('%Y%m%d')}.csv", mime=_OO1I0ll00OO1(b'\xb2\xc0\xa8\xce\xb66\x08\x08', b'n\xa6+\xdd'), use_container_width=True, key=_Il0I00l0OIIlO(b'\xce\x1ez\xd0\x81\xb8\x85\xdb\xa6\x8d\xe1\x99\xa2>j\xfbd', b'QT\xa7\x7f'))
                    if _1lOOIlll100100O(b'\x10:#\xc0\xfd\xcf^\x11', b'1\x91f\xa1') in enriched_df.columns:
                        industry_counts = enriched_df[_1lOOIlll100100O(b'C\x9b\xdd\xeaq\xae\xf3;', b'r{\xb1\xca')].value_counts().head(252807524 ^ 252807534)
                        if not industry_counts.empty:
                            fig = px.bar(x=industry_counts.values, y=industry_counts.index, orientation=_O00Ill1OIllO(b'\x1e', b'J\x08\xcb\x92'), title=_1lOOIlll100100O(b' M\xff\x7f\xb5\x83\xd63\xe8i3\x8aA\xc9', b'F\xa9)\x14'), labels={_O00Ill1OIllO(b'\x87', b'\xa1\xff\xf8\x05'): _OO1I0ll00OO1(b'\xf4w\xf3j\x0e', b'I\xc0\x83\xfe'), _OO1I0ll00OO1(b'\xb8', b'{\x12\xb7"'): _1lOOIlll100100O(b'>\xead$\x1a\xab\x15\xd8', b'\xc5\xae\x05p')})
                            st.plotly_chart(fig, use_container_width=True, key=_Il0I00l0OIIlO(b'\xb2\x95\xe4%\x8au~\xba\xb8\x13\xd2[%F', b'\x19\x8e\x93\xde'))

def render_abtest_tab():
    st.markdown(_OO1I0ll00OO1(b'P\xb3\xad\x87\xd7.\t\xd6Y\xc5`\xf7\x06\xbb\xbf\x1d\x14G\xba\xf06f\x80\xb1\xbd\xa1\xc4\x05\x9f\xdd/\xf8\xaf\x85M\xec\x1f\xc4\xbb\x87\xae\xc5E\xb3f', b' \x92.\xff'), unsafe_allow_html=True)
    st.markdown(_Il0I00l0OIIlO(b'\xebY\xf2\x12\x97.2\xb8\xdb\xf7\x06\x93\x90\x8cZ\xaeF-\x85\x12\x9c\xe6\xdf\xab\xdd\x8b\xf2\xdc\xd3z-\x05\xc7\x022\xe0\x1f*\xa3\\\xa3\xcc\xd5\xe1\xb8\xb2\x02H\xee\x97G\xa4B\xb3t"\x87\xa6s\x9e\xc8>A\x14\xdd\xc6\xee\xf4R\x1e\xaeY', b'=9\xa2\x0b'), unsafe_allow_html=True)
    with st.expander(_OO1I0ll00OO1(b'u\x7f\xf0\xbbF\xce\xce\xf5}\xf5\xc0\xac\x9a\\^\xd9]\x9f\x02\x1c', b'\x1f\xfb\xa3\xda'), expanded=True):
        test_name = st.text_input(_O00Ill1OIllO(b't\xd5\x90\xf7\x95\x03l\x0b\xe1A', b'\xdd\x00f?'), _Il0I00l0OIIlO(b'2mh\x99\xa9Y\xd53\xd7g\x84\x82\x94\xbdS\x1c\xa6', b'kn&\xc7'), key=_OO1I0ll00OO1(b'@\xa25\x91\x9d\x8a\xd5\xf09u\x0cCr\x10]', b'\xe7\xfc\xf8\x92'))
        test_type = st.selectbox(_OO1I0ll00OO1(b'X9V\x8d?\xb2\x80\x85\xf4m', b'ud\xf2Q'), [_O00Ill1OIllO(b',!O"L\x01d', b'\xebp\xba\xc6'), _OO1I0ll00OO1(b'6\x0cl\xb6\x87\x10\xe8', b"D\xbe\xa3'"), _1lOOIlll100100O(b'89\xc7', b'\xe0\x08\x8av')], key=_1lOOIlll100100O(b'\xa6v\x12\x08\xc3G\xff\xd3\x8c\xed\xaap\x819\x0f\x02', b'\x8c\xcf\x040'))
        col1, col2 = st.columns(1607552305 ^ 1607552307)
        with col1:
            variant_a = st.text_area(_OO1I0ll00OO1(b'\x02\xb0\xf6\xf5n\x94;\xd9\xc3\xef', b'7Hfi'), height=1497285892 ^ 1497285984, value=_O00Ill1OIllO(b'\x17\x87m\xbdG\x8bB\x07\xfd\x0b\x14\xf9\xeet\xce\x01\xd5D]\x92V\x06a\xfd\xd9\xf3', b'\x02w\x8a\xdf'), key=_OO1I0ll00OO1(b"\x98u2&\x0f\x98'\xea\x87", b'\x808\x87\xd2'))
        with col2:
            variant_b = st.text_area(_Il0I00l0OIIlO(b"0\xd8'\xaat\xb5k\x07S\xae", b'\xf8\xf6V\xe1'), height=1584453082 ^ 1584453054, value=_OO1I0ll00OO1(b')iY\x00\xdf\xa2\xa4l\x91X#\x80\xa3\x1c\x84e\xed\xf3&n\x0e\xf60\xe4_', b'%\x7f\xa1\xae'), key=_Il0I00l0OIIlO(b'\xa4\xa1\xad\xe4\xdaXBGb', b'\xf7\x07\x99b'))
        variant_c = st.text_area(_Il0I00l0OIIlO(b'\\\x115\xda$\xef\xfd\x9e\xc0\xdc.\xf4\xdfY\x02Ue\x151\x9e\x89', b'\xf2\xf1-\x91'), height=1329520322 ^ 1329520294, placeholder=_Il0I00l0OIIlO(b'\x9a\xcc\x101}%\xbd\xd6\xf1J\xe9{\xfc\x91\xe9\xc3\xf0n\xc5\xc7\xbe\x8a', b'\xe4\x80n:'), key=_O00Ill1OIllO(b'\x9cV\xc1rP\xe3\x9f\x1e7', b'\x90\xdb&\x0f'))
        if st.button(_Il0I00l0OIIlO(b'p4\xf5\x1e\xf8\xa7\xdbg\xd3\xb5\xf5\x0bX\x96d\xbf', b'\xaei\x14<'), type=_Il0I00l0OIIlO(b'9\x87\xee\xbc\xd4\x0br', b'\xa2\x86[\x12'), use_container_width=True, key=_O00Ill1OIllO(b'\x84\x8a\x114\xbfi\xe3\x89\xdb]p\xd9.\x82:', b'\x015\xdb\x18')):
            variants = {_Il0I00l0OIIlO(b'3', b'F\x9b4\x96'): variant_a, _O00Ill1OIllO(b'/', b'\xe3v\xdd@'): variant_b}
            if variant_c:
                variants[_Il0I00l0OIIlO(b'\x1b', b'{\xd0\xa1\x17')] = variant_c
            create_ab_test(test_name, test_type, variants)
            st.success(f"✅ Test '{test_name}' created!")
            if _Il0I00l0OIIlO(b'\x01\x89f\xf2W\x14\xdea', b'i\xa1$\x7f') not in st.session_state:
                st.session_state.ab_tests = {}
            st.session_state.ab_tests[test_name] = {_Il0I00l0OIIlO(b'k"\xa0W', b'.\xed\xdf9'): test_type, _1lOOIlll100100O(b'\xe5\x08\x80e\x1aI(\x07', b'\x93 e\x82'): variants, _OO1I0ll00OO1(b'\xcc\xee\x0eS\x14}\xb2', b'\xb9\x9aH\x0c'): datetime.now().isoformat()}
    if _OO1I0ll00OO1(b'&k\xab;\xb4\x18\xac\xdf', b'\t\x86~;') in st.session_state and st.session_state.ab_tests:
        st.subheader(_O00Ill1OIllO(b'z\xbbr*\xd3D9Zx\x115re\xd0\x13\xc4\xd1', b'\x8eC\xe0H'))
        for test_name, test_data in st.session_state.ab_tests.items():
            with st.expander(f'🔬 {test_name}'):
                st.write(f"**Type:** {test_data['type']}")
                st.write(_Il0I00l0OIIlO(b"iK\xfe\xbfs\x1a\xbf\xbcd\xd5'\xc5\x0c", b'\xaa\x96\x96\x88'))
                for variant, content in test_data[_O00Ill1OIllO(b'\xa1)\n\xdd\x9c\xa0*\x80', b'\xa8\xf6\xc0\x87')].items():
                    st.write(f'- {variant}: {content[:100]}...')
                results = pd.DataFrame({_Il0I00l0OIIlO(b'J\xf4\xce\x14e\xf0\xda', b'\xb3\x84\xa6\x13'): list(test_data[_OO1I0ll00OO1(b'\xca\xd5\xeb\xb5\xcf\xed\x86\xdd', b'k\xc3\x91X')].keys()), _1lOOIlll100100O(b'\rV\x90%', b'e4\xc0\xc3'): [1632163335 ^ 1632163381, 1847498235 ^ 1847498187, 1320117885 ^ 1320117859] if _O00Ill1OIllO(b'\xf7', b'v\x80\nA') in test_data[_1lOOIlll100100O(b'\xe7\xee\x00\xe3\xe7\xa7\xa0\x08', b'\xf1!\x1e\xba')] else [791738606 ^ 791738588, 2001969797 ^ 2001969845], _OO1I0ll00OO1(b'T\xcfEh\x9f\xee&-\xf32t', b'K\x18X\x1e'): [42.5, 38.2, 45.1] if _O00Ill1OIllO(b'a', b'"&E\xed') in test_data[_1lOOIlll100100O(b'\t\xfe\xd9\xe9[\xf4AZ', b'd\xc1\xc9z')] else [42.5, 38.2], _OO1I0ll00OO1(b'5\xcec\xda\xf0\\/\x17O\n<l\x0f\xe3\xee', b'x\xbc\xd4n'): [8.4, 6.7, 9.2] if _OO1I0ll00OO1(b'\x8b', b'\x0eW9!') in test_data[_Il0I00l0OIIlO(b'SX<\x1e\x83\xad\xdf\n', b'\xb00\xbb\x7f')] else [8.4, 6.7]})
                st.dataframe(results, use_container_width=True)
                winner = results.loc[results[_Il0I00l0OIIlO(b'\xc1L\xbd\x93=\xbd\xa2\xe0Z\x1ej\x95\x01\xc7I', b'\x1a\xbeT\xb5')].idxmax(), _1lOOIlll100100O(b'\xd4\x1b*el\x90`', b'\x1d}D\xa5')]
                st.success(f'🏆 Winner: {winner}')
                csv_results = results.to_csv(index=False).encode(_1lOOIlll100100O(b'\x8c\xed\x9d7\xcc', b'i\xb1\xc7W'))
                st.download_button(label=f'📥 Export Results', data=csv_results, file_name=f"ab_test_{test_name.replace(' ', '_')}.csv", mime=_O00Ill1OIllO(b'\x17\xe6bg`\x88\xf1\xa8', b'\xde0d\xb5'), key=f'download_ab_{test_name}')
    with st.expander(_O00Ill1OIllO(b'Y\x94pZ\xa6\xa3\xc2\xc0"\x12\xdce\x0fy\x07\xddy1\x03\x17E\x1b\x84N\x12}\x1d\xc6\xe7A\x87', b'x7t\x18')):
        st.markdown(_O00Ill1OIllO(b"0\xf3@\xbb\x01a\x18\x7f\xd9\xc6\xed\xe5\xe9\xac\xae\xed,\xf7\xc21\xa87'\xe8\x1e\xca\xe19\x15\xe7N\xeb\n\n\xc0=\xc2Zp\xa3\xd1Y\x9e\xd0\xac\x01\xa2\xc5i}\xcb\xc7q\xb6\xf8\xcc\x89<\x1dg\xda\xfd|\xda\xc1\xdchVd\x7f\xa6\x13\x92\xbfDoJ;\xfaj\xe5\x8e\\\xe2N\xe5\x8av(\x9a \x87N\x8f\x00&\xd8\x10\xbc[\xbe$C$\rm6K\xbf\x19\xa7L\x18\xad\xb2\x0b\xf1\xe7:\x04K\xde\xb6\xbf\r\x03\x1c\x10\xea\x12\x96\xb4i\x9a6\x12\r\xc8\xb1\xc3Q]G\xc6\xc1\x110GT\xa2)\x9a\xdcKj}\x0c\xfd.d\xf1\r)\xee\xcd'g\xcc\xb06\xe7M\x01\x890\x9f\xbf\xef\xe1w\xc2Ox\xaf\x8d\xf3\x1b\xe5H\x89B\x82\x1c]\xd8\xf4Q\xb1Hm\x9a\xabS\xd2\xddM\x06-\r\x13+9\xb1Z]\x8c\xe6\xcf\x94\xb7\xdeA$\xbb\xd6\xc4cAR\x18{~6\xe9\x96\xc4\xc8HQ\x98\xa9\xf9wE\x05\xe2L~\xc0c\xfb\xb6\x8c\x8f\xfa\xda\xf3\xe4:\xa1\xed\x87\x03\x03\xac\xb0\xcb\x17\xb0\xeav<\xf3\xd0\xa0\x95\xdc\xb3\xf9\xaez{\xae\xc2{`\xc0:\x1fh\xf6k\xae\xb8\x0f\x93\x86\x05\xf1\xdb\xef\x88!\x19(\xca\xf9\xfd\xad\xd6\xe6\x0b\x93\xeb\x90\xd4xL5\xe4\xd0\xf6]\xef\xdf\x1c&2x2\xcc\x1cXtRVx\xa6\xd1\x1f\x03\x06\xd2#i\xae\x9e\x18\xd3\xbb\\\xfe\x89\xfb\x97\x89\\|\x05\xef\x9a", b'\x9f.lX'))

def render_history_tab():
    st.markdown(_OO1I0ll00OO1(b'\xed\x85\xf3\xd8\tk\xbfe$j\xab\\\xf8\x85\xc6\t\xb7\x8a\xe4;\xdd\x93\x04\xb2\x8f{\x91\xeb\x87\xee4\xe6Y\x14L\xc1\xd5o\xc6(\xec', b'\x1b\xfbz!'), unsafe_allow_html=True)
    files = get_history_files()
    if not files:
        st.info(_1lOOIlll100100O(b"\xab\xc7p\x84\xabn:k\xbd\xf82/\xa0\xd44\n\xa0\x04S\x1b\xcf\x9a\xe3)\xdal'\xe21\xd1f\x9bj3])9\xbbz=P0\xd7\xc5\x90\xb1\xc5d\n\n\x82j", b'\xb7\xe5\xf6k'))
    else:
        selected = st.selectbox(_OO1I0ll00OO1(b'\xb8g\x8dR\x07\xaaWp\xdfU,\xca', b'\x1c\x08\x13\x7f'), sorted(files, reverse=True), key=_Il0I00l0OIIlO(b'\xc6\xb1\\4M\x91\xfe,\xbe\x83n\xbf\xfag', b'\xcbH\x04\x9a'))
        if selected:
            df_history = load_history_file(selected)
            st.dataframe(df_history, use_container_width=True)
            csv_data = df_history.to_csv(index=False).encode(_Il0I00l0OIIlO(b'\xd2G\x14\xc8\x05', b'\x91\r}\x1e'))
            st.download_button(label=_O00Ill1OIllO(b'\xc9\xa4\xad\\\xd7\xda\xc0\x8d\x8a\xe1h\xe5\xa7\x9fY\xc23', b'\x975+y'), data=csv_data, file_name=selected, mime=_1lOOIlll100100O(b'\xedw1\xc7\xc5\xe5\xe06', b'\xa8nNC'), use_container_width=True, key=_OO1I0ll00OO1(b'\xc7\x9d\xe8e\x0c\xc2\xd8\xce\xf9Je\x16\x9c\x85\xe7I', b'9c|\xa7'))

def render_email_tab(company_profile):
    st.markdown(_Il0I00l0OIIlO(b'_\x186\x88\xd3$\xc8\x8bw\x83\xb3\x1b\xc3\x8e\x0fV\xf3\xfe\xb0Vf\xd3N\xdb\xd5\x16xj\xb8^?]\x15J\xb6\x11\x9c(\xf0\xe7\x97\xc9o o\xd6d\xe9s\x85', b'9\x98\xdc\x04'), unsafe_allow_html=True)
    groq_key = get_groq_api_key()
    if not groq_key:
        st.error(_OO1I0ll00OO1(b'\xdc\x01\x8c\x0c\xf6\xe5\xcd\xc3\xec\x04\x84\x9a\xc0\xca\xcc\x17V\xad\x16\xf9K\x0eG\x11g}\xafY\xa2%_<\x95\xa0\xcb\xfa\xef\x02\xbb\xa3\x02\x9bbz\x023\x96\x9a8B\x99\x01AC\xbf\xdeX\x00', b'\x81U\x84\xf2'))
    if not all([company_profile.get(_1lOOIlll100100O(b'\xe1\x12\xedq\xa37u\xd6\xa4}\xa8\xcc', b'\xb6\x8a\x1aL')), company_profile.get(_OO1I0ll00OO1(b'\xecR\x85\x04M\xd2\xb57W\xea#O', b'\x0f\x86U\xe2'))]):
        st.warning(_Il0I00l0OIIlO(b'-\xc5\xb5\xdd\xb2\x83\xa3\xe7I\x9c@>\xc6\xe9\xa9\xcc^\xae\x81\xdc\xd8\xa0}8j\x18p\xdc\xb3\x8a\xcat\xf8\xec\xbaD0\xd4w=3\xb9J2:b5\x18\x90\xfb\xbb\x83\xf8\xe8[\t\xcc\xfdQF^b\xfc\x8e\xdfVxD\xed\xe2\xba', b'lref'))
    saved_settings = load_email_settings()
    with st.expander(_OO1I0ll00OO1(b'\x17\xa8\xa4S4\xfc\xf1\x15\xc8GX\xa4\xd0A\xa4\x9e\xe9\x91ZX\x02\x83\x00\xea', b'\xb7\xe9\xb4\xfd'), expanded=True):
        col1, col2 = st.columns(1682498387 ^ 1682498385)
        with col1:
            smtp_server = st.text_input(_OO1I0ll00OO1(b'\xdc\x00\xb5\x88J\xe1\xa1\x87\x8b\x0b\x99s', b'\xea\x10\xa3M'), value=saved_settings.get(_Il0I00l0OIIlO(b'O\xca\xfd\x87\xea\xf1;\xcc\xc8\x0f\xc2', b'Z\xf4\xc8\xe6'), _OO1I0ll00OO1(b'2\x94\xa9`\x84\xfe\xa9j\xcdD8\x9a\x9fQ', b']\t\x9d\x9f')) if saved_settings else _1lOOIlll100100O(b"\xac<\xd0\x90\r8'?L\xb6\x91t\xc5y", b'u\x9c\xa8e'), key=_OO1I0ll00OO1(b'\xe5H\x1f>\xd0\xa0\xdb\x116\xa3\xdb', b"'\x12\xf9\xd0"))
            smtp_port = st.text_input(_1lOOIlll100100O(b'g\x14\x97\x1e\x8e\x03<\r\xb4\x06', b'\xf0r\xb3\x05'), value=str(saved_settings.get(_Il0I00l0OIIlO(b'\x0c\xc78\x15\xf2\xbf\xb6\xd0\xe9', b'\x00B\xd9\xd6'), 2095511358 ^ 2095510901)) if saved_settings else _OO1I0ll00OO1(b'\x17O\x01', b'a\x96\xa6\xf6'), key=_OO1I0ll00OO1(b'~c\xc3^\xb2\x94\xa8( ', b'\xed\x87\x0b\x81'))
        with col2:
            sender_email = st.text_input(_1lOOIlll100100O(b'Ny\xf1\x15\x08\xd5\x16\xc5IAx\xd2\x93', b'v\x0c\x83k'), value=saved_settings.get(_Il0I00l0OIIlO(b'\x8cL\xa5\x8b\xf6\xae\xbcU\xbf}\xd7\x81', b'\t\xfcm\x86'), _1lOOIlll100100O(b'', b'2\xcb/.')) if saved_settings else _1lOOIlll100100O(b'', b'm\xfd#`'), key=_Il0I00l0OIIlO(b'\xc8"F\xb1tP\xb7z\x1d\xc7\xcb\xa3', b'C\xb6$U'))
            sender_password = st.text_input(_OO1I0ll00OO1(b'\x9cH\x1c\x87ax\x87LP', b'\xf5c\xbe\x89'), type=_1lOOIlll100100O(b'\rI\xc7\xa1\xcd]\n\x1e', b'\xd0}\xbd\xde'), value=saved_settings.get(_1lOOIlll100100O(b'\xc8-\xfe\xfe\x81\xa9\xd5\x9a:\xe1\x9cuQ?\x9d', b'\xb05\xb5\xa2'), _OO1I0ll00OO1(b'', b'\xa4X\xac\xde')) if saved_settings else _OO1I0ll00OO1(b'', b'\xb2#\xd3\xf7'), key=_1lOOIlll100100O(b'M(D\xee\xae\ti\x17b\xb5<\xac~XE', b'z\xa31v'))
        use_tls = st.checkbox(_OO1I0ll00OO1(b"\xce'\xe1\xd6\xf3\xf8\xfd", b'\x87tv\x0f'), value=saved_settings.get(_O00Ill1OIllO(b'\x80C\xf5\x88f\xb8\x02', b'V\xfd\x18\x0c'), True) if saved_settings else True, key=_1lOOIlll100100O(b'\x07\xfa\x04\x1f\xcb\x08\xef', b',\xc2%\xd7'))
        use_ssl = st.checkbox(_OO1I0ll00OO1(b'z\xac\xb6\x1e\xfa"\xe5', b'\xac\xdf\x00['), value=saved_settings.get(_OO1I0ll00OO1(b'\xbe\x92\xf1\xc0\xed\xef\xd9', b'\xf2\xc6M\xfd'), False) if saved_settings else False, key=_OO1I0ll00OO1(b'\x8b=\xb9D)qN', b'\x8bt\x0f\xda'))
        if st.button(_O00Ill1OIllO(b'\xb7\xa0:\xa9t~\xd6\xe4\xc8\x1c%\xbev\xca\x07\xb2\x88\x94', b'\xbfa2='), key=_OO1I0ll00OO1(b'\xcc\xe9m\x825\\kC\xb6\xe1"/\xa6\xa4\xc5\xfdDeo', b'\xbf\x17NA')):
            settings = {_Il0I00l0OIIlO(b'A\xb9\xc7\xa2\x99OT>\xa1\x18\xd6', b'\x0ckwE'): smtp_server, _1lOOIlll100100O(b'\xa3n\xa3\xa3\xe7 ^\xcf\x95', b'\xf8!\xa1z'): int(smtp_port) if smtp_port else 1019836048 ^ 1019835611, _O00Ill1OIllO(b'\xfav\xfex\xee!\xd6\x86\xaah\xdeh', b'\xf8\xbd\xc0\xba'): sender_email, _Il0I00l0OIIlO(b'#gN\x1eh\xf0\x87\x1f\xa9\x86\xff\x85to|', b'\xb5\xb7$\xa0'): sender_password, _1lOOIlll100100O(b'O\xeeZQX\xd5\x0f', b'\xdc\x08\x91\xac'): use_tls, _OO1I0ll00OO1(b'\x1a\xd9@\x1deN\xaf', b'\x91?D\xff'): use_ssl}
            if save_email_settings(settings):
                st.success(_OO1I0ll00OO1(b'\x81D\xf6S\xbf\xa3\xc8D\x83\xf7\xc9a\x9e\x08jj\x87\xdd', b'\xdaV\x8c\xe6'))
        if st.button(_Il0I00l0OIIlO(b'\x99\x82\xa5\xa2\x1d\xa5\xf2\x9c\xbf\x8c|~\xbcL\xbf\xdd\r\x97\xa6\xdf', b'\xa2\x8e\x90r'), key=_Il0I00l0OIIlO(b'\x9d-A\xd9(\xa1 \x11\x97\x08\x18:m\xc0<\x0bH\xa6\x1b\xc3(', b'\xf8\x86N\xe1')):
            settings = {_O00Ill1OIllO(b'\xe4\x1cS\x9d&G\xf2EL\xe9"', b'\x95\x94\x19\xb6'): smtp_server, _Il0I00l0OIIlO(b'\xdf`\t\xd5@\xd9\x82\x167', b'I\xec\xda`'): int(smtp_port) if smtp_port else 1778604607 ^ 1778604148, _O00Ill1OIllO(b'\xfc\xd4\xaaFo\xe4\xcb\xf5>A\xf1\xa2', b'\x0e\x95\xc3S'): sender_email, _1lOOIlll100100O(b'\x03\xafB[\xe4\xcas|\xfb\x9d|9\xb7\xca\x12', b'^\x17\xce?'): sender_password, _1lOOIlll100100O(b',\x8bF\x8f\xabWo', b'\xacX\x0e\x9d'): use_tls, _Il0I00l0OIIlO(b'\x89\xe9\x9d\xb3\x02\x1d\xb2', b'\xfd \x887'): use_ssl}
            success, message = test_email_connection(settings)
            if success:
                st.success(f'✅ {message}')
            else:
                st.error(f'❌ {message}')
    load_option = st.radio(_OO1I0ll00OO1(b'&\x85(\xd9\xf8\xa7\xcf\xe2\xc2q', b'I\x88\xd9\xe9'), [_O00Ill1OIllO(b'W\xb5LK\xba\x02\xa4', b'\xa7\x02 \xf9'), _O00Ill1OIllO(b'\x1d\x97Lt\xa4[xA\xfb\xfa', b"'G\x87\xe2")], horizontal=True, key=_OO1I0ll00OO1(b'|\xbd\x89\xad.\xcf\xf2\x9e)\x00$Hk\x9d!\xf1/', b'\xf7t\xaf!'))
    df_email = None
    if load_option == _1lOOIlll100100O(b'\xb3_,\xb1\x00\xc7\xe3', b'\xe5\xc0/z'):
        files = get_history_files()
        if files:
            selected = st.selectbox(_O00Ill1OIllO(b'\x97K\xa3\x11\xd8I%I\x90\xad<\xa5', b'h\xd3)\xd4'), files, key=_1lOOIlll100100O(b'X\x81\\\xe9-A\x80x\xf0\xd0\xba\xeb\xddus.X', b'hy\x9bo'))
            if selected:
                df_email = load_history_file(selected)
    else:
        uploaded = st.file_uploader(_Il0I00l0OIIlO(b'\xbet\x16\x97\xea\x9f\xc5X\t\xe4\x1f', b'&;\x84\xad'), type=[_OO1I0ll00OO1(b'z2#', b"\x11'\xab@")], key=_Il0I00l0OIIlO(b'\xffn`\xf1\xa9R\x15\xcb\x0e\x19\xd5.0\xcc\xa3\xb6\x9b', b'\x13;u\xd0'))
        if uploaded:
            df_email = pd.read_csv(uploaded)
    if df_email is not None:
        valid_emails = df_email[df_email[_1lOOIlll100100O(b'\xea\xbb\xf6\x97\x96', b'\xf1\xb81p')].str.contains(_1lOOIlll100100O(b'\xd5', b'\x0c\xb1\x0f\x06'), na=False)]
        if valid_emails.empty:
            st.warning(_1lOOIlll100100O(b'\xc8\xe0Tv\x85\xd7a,\xb3Y8\x1e$x\x1aP\xbc\x04\xc7\xc2{', b'\xfdL\x80\x83'))
        else:
            st.success(f'✅ {len(valid_emails)} leads with valid emails')
            selection_df = valid_emails.copy()
            selection_df.insert(547336927 ^ 547336927, _1lOOIlll100100O(b'\x0c,?N\xb3\x10', b'\x8f\x16`;'), False)
            edited_df = st.data_editor(selection_df, column_config={_O00Ill1OIllO(b'UK\x1e\x1e\xf0\x12', b"6'0\xee"): st.column_config.CheckboxColumn(_O00Ill1OIllO(b'\xb9\xfd\x19\xd6n\xca', b'\x02\xe3 @'), default=False)}, hide_index=True, use_container_width=True, key=_1lOOIlll100100O(b'\x83\x08[\x9cT,\xea\x0b\x9d*h\x02', b'D\x19>\xae'))
            selected = edited_df[edited_df[_O00Ill1OIllO(b'\xe7\x10\xd9\xf2Q\x91', b'\x1ed\xe2\xe8')] == True]
            if not selected.empty:
                st.info(f'📌 {len(selected)} leads selected')
                st.subheader(_1lOOIlll100100O(b'$/\xf0iFk\xce\xcbHz\x0e;\xd7\x13T\xb2\x10!', b'6\xa4C\x88'))
                st.caption(_1lOOIlll100100O(b'\xf2u\x96 \xe8\xc6\t\x08\xa1\xac\x9d\xb5\xb6tt#\xec,\xd1{\xa9\xe4\x82\x7f\xce\xb3\xa7uU\x0b80\xd7\x0co\xf1B\xa2K\x8f\xb1\x94gs[\x02l\x10\t\xefl2\xc5', b'H)\x17"'))
                with st.expander(_OO1I0ll00OO1(b'\xdf\x98\x7f\xce\xe0\xd6|\xac\x07\x0ba\xfe_\x1f\xa6E\xf9\x89"^b\xd2-h\x9aX\x00l', b'\x8d\xbb\xb2{')):
                    st.markdown(f"\n                    **Company:** {company_profile.get('company_name', 'Not Set')}\n                    **Product:** {company_profile.get('product_name', 'Not Set')}\n                    **Offer:** {company_profile.get('special_offer', 'Not Set')}\n                    **CTA:** {company_profile.get('call_to_action', 'Not Set')}\n                    ")
                if all([company_profile.get(_OO1I0ll00OO1(b'\x16\xe0\xac}\x05n\xb9b\xb8og\xbd', b'I\xc6Gi')), company_profile.get(_OO1I0ll00OO1(b'\x13\x17M+\xbeD\x12\xea]\x8c\x83\xc3', b'm8\xbe\xbc'))]):
                    if st.button(_OO1I0ll00OO1(b'?\x94\xa1w\xd12J*\x80\xd5iQr\x99=:', b'\xf2\xab\x18:'), type=_OO1I0ll00OO1(b'1\x118\xb8`\xf9b', b'\xb2k\xce\xe7'), use_container_width=True, key=_OO1I0ll00OO1(b'<\xf7\xee5v\x96R\xbf"\xaduu%H\xa8', b'\xa7\x945L')):
                        if not all([smtp_server, smtp_port, sender_email, sender_password]):
                            st.error(_Il0I00l0OIIlO(b'\x87I\x84:@\xe6]\xf4\x14g\x02\xecG\xf8\xa0\xe1\x8e\xa7\x08\xcb\xd2\xe7_sF\xf5\x1bz\xa3\xa6.\xc8\x89\xac/\x1c\xa3', b'b\xc3\x1b\x8e'))
                        elif not groq_key:
                            st.error(_Il0I00l0OIIlO(b'j\xb3\xee\x8a\x18\\\xc9H\xfb\xeb\xc9\x11ho\xd3r\xe2\x111\x83\x84\x92\xc9\xdd|$\xe6\xb7\xf6\x14\xd7\xb3x\x9b\xc0\x7f\x1f\xbc\xdb\xe3\x93\xf4\xfe\xfc\xcf\x93|\x95/\xe4s', b'\xad4;T'))
                        else:
                            recipients = []
                            for idx, row in selected.iterrows():
                                if _1lOOIlll100100O(b'\xa6', b'\x85\t{e') in str(row[_OO1I0ll00OO1(b'\xf3\xc2>\xea\xaa', b'\xc2\xfa\xd3\xa4')]):
                                    lead_data = {_1lOOIlll100100O(b'\x85\xf7\x88n\x80q\xda\xaf\xde\r\x81\xd3\xa6', b'\x1f\xd9K\\'): row.get(_OO1I0ll00OO1(b'}\\B\xd8\xa8\xa3\xee0\x87e\r?\xb0', b'\t\x03\xf4\xdb'), _O00Ill1OIllO(b'', b'\xe4\xd9\xf8t')), _O00Ill1OIllO(b'}\xb2\x00\xc6\xd4X[', b'\xd0\x95\x0c#'): row.get(_O00Ill1OIllO(b'\x85\x9d\xed\x8e-\xee\x81', b'\xe6o=\xa1'), _O00Ill1OIllO(b'', b'tJg\xb0')), _O00Ill1OIllO(b'\x814\x7f\xa8\xea&', b'\xf6\x1a\xa9*'): row.get(_Il0I00l0OIIlO(b'\xf1\x89{\xe5\xf3\xcf', b'\xf3\xafw\x8e'), _O00Ill1OIllO(b'', b'\xa3\x1d\xf4r')), _O00Ill1OIllO(b'\x95Q\x08\x84\x86', b'2_.\x87'): row.get(_Il0I00l0OIIlO(b'\xbd\x80\xfcm\xac', b'\xd7\xfe\r\x8b'), _OO1I0ll00OO1(b'', b'\x19\xc6\xbf\xd1'))}
                                    personalized_email = generate_ai_email_with_profile(company_profile, lead_data)
                                    recipients.append((row[_OO1I0ll00OO1(b'\xa2\xf9\x0b.\x1c', b'\x91kuM')], personalized_email))
                            if recipients:
                                st.warning(f'Sending {len(recipients)} emails...')
                                progress_placeholder = st.empty()
                                progress_bar = progress_placeholder.progress(2100714789 ^ 2100714789)

                                def update_email_progress(idx, total, email):
                                    progress_bar.progress((idx + (1665954712 ^ 1665954713)) / total, f'Sending {idx + 1}/{total} to {email}')
                                results = []
                                for i, (email, body) in enumerate(recipients):
                                    update_email_progress(i, len(recipients), email)
                                    subject_line = body.split(_Il0I00l0OIIlO(b'\xc5', b'3\x19\x93\x89'))[1253746486 ^ 1253746486].replace(_1lOOIlll100100O(b'j\xcfdMT\x0c\x95\x99', b'a4\x93+'), _Il0I00l0OIIlO(b'', b'q3\xe8\x08')).strip() if body else _Il0I00l0OIIlO(b'"P+\xbb\x80>\xcf5\x86-\xa1\x16C\xa2DacW\x1cL;;\x8d\xd6\x1c\xb1i\xccj\x159\x91', b'\x98\x86\x05\x19')
                                    success, message = send_single_email(smtp_server, int(smtp_port), sender_email, sender_password, email, subject_line, body, use_tls, use_ssl)
                                    results.append({_Il0I00l0OIIlO(b'b\x87\n\xd3\xe0', b'+-\xd4h'): email, _O00Ill1OIllO(b'\xb5\x82\xa1;\x8e\x03', b'#;\x87G'): _O00Ill1OIllO(b't\xa44\n\xcex0', b'\xde\xfel"') if success else _Il0I00l0OIIlO(b'\xe4\xf22\\S\n', b'\xe9q\xd9\xb7'), _OO1I0ll00OO1(b'xK\x95\x86\x9d\xbc\x16', b'\x97\xa6\xb7\xec'): message})
                                    if success:
                                        update_campaign_stats(_Il0I00l0OIIlO(b'\x91Q?]h\xc9]\xf3\xdb', b'\xd5\x98\x0b\xd1'), {_OO1I0ll00OO1(b'M\xcb\x98"V\xe2F', b'\xc1\x8bB\x1e'): _Il0I00l0OIIlO(b'5\x94\x00\xe6\xac', b'3\xaa3~')})
                                    time.sleep(968236175 ^ 968236174)
                                progress_placeholder.empty()
                                results_df = pd.DataFrame(results)
                                st.dataframe(results_df, use_container_width=True)
                                success_count = len([r for r in results if r[_1lOOIlll100100O(b'w\xf6\xa9\x08VF', b'\x03\x04\x8c\xfb')] == _O00Ill1OIllO(b'3\xe0\xd7L\xe1\xf5\x83', b'\xd5\x8f\xfd\xb4')])
                                st.success(f'✅ Sent {success_count} emails')
                else:
                    st.warning(_Il0I00l0OIIlO(b'\xe3\xbb\xa3\x06VD\xf3\x80\xbe\xe0\xff\xd2\xfed\xbd\nV\x04!\xaf\xea\xce\xaa\x11\xa0\x10!wE\xb3\x8c\xa9^\xe2\x92\xb3<`\x87r\xc4\xda\xc1\xdc\x07\xb2>\xcb\xd2\x98\x15\x8cuD\xcfp\x07\xa4\xf2iD\x99p\x01', b'\x9c\x08\xa3{'))

def render_whatsapp_tab(company_profile):
    st.markdown(_OO1I0ll00OO1(b'\xdf\xed\xe4B\xbd\xb0\r\x8ch\xf0\xf0\xdc\xc4M\xd4vW\xd5I\x17~\xa8\x81o\x85\x93\x9d\x04\xd4\x89\x07\xceN,\t!\xf4q\xed\x88\xf2\x83\xa5\xcb\x10\xae\xc74\x0e\x03\x1b', b'\x98%x\x1f'), unsafe_allow_html=True)
    groq_key = get_groq_api_key()
    if not groq_key:
        st.error(_1lOOIlll100100O(b'\xd9\xbe\xb2\x05d\x0b(\xa2\xdb\xe7\xf1\x85Q\x17\x18Y\xde\x1a@m\xe5(\xd0\xf3\xc3\x1cc\x9d.\xbd`\xd4\x94\xfak\xd9\xbe\xa7L\xc9w %\x0e@Sx\xea\xfdA\rq<\xc5M\x9dB\xb6', b'\x8b\x14;\xb2'))
    if not all([company_profile.get(_1lOOIlll100100O(b'\x8c\x10$\xfe\xf8\xe9\n\xc9\xaa7\xf1\t', b'\xe3\xea-P')), company_profile.get(_Il0I00l0OIIlO(b'\xed^\xa8\xfd\xba\x84\xac\x14\xca\x18\x9f*', b'\xc6\xbd\xff\x96'))]):
        st.warning(_OO1I0ll00OO1(b'\xd4\n\xf6\x9aC\xfe\x95\x1f\x03\xacZ\xf6\xb6\xb8hx\xf4\xbc\xcb\\\x84\x88(\x15\xd9>\xa3\x8d\xd4\x10oO\xd8\x99\xc0\xfc\xf0\xfc\xf8\xa7\xfak(\xf2\xf2\x99r`\x8e\x0c\xfa\xdd\xe0\x81\xe9\xde]&\xaf\xa9v\xd9\x96\xe0k\x00\x16>\xbc\x83\xfa', b'!|\xde\xa6'))
    templates = load_whatsapp_templates()
    with st.expander(_Il0I00l0OIIlO(b'\xbf\xf2kEU\xb3\xeb\x98\x81\xa5\x7fheD\\A>\x98j\x90"\xf2b\xfe', b'bW\x18\x1a')):
        col1, col2 = st.columns(1423909304 ^ 1423909306)
        with col1:
            template_name = st.text_input(_OO1I0ll00OO1(b'\x89=\xe8F\x85y\xb1\xda\xe6\xbde\xf5\x88#', b'i\xe8\xc1\x8e'), placeholder=_1lOOIlll100100O(b'\xc5\x0fq\x11\xc4\t(\xc9\x90S\xaa', b'\x10\x1e\xa72'), key=_Il0I00l0OIIlO(b'\x87\xaf\xe9\x93\xb8;\x84\xd6J\x90\x14\xe8\x03', b'\xcfHQ='))
            template_content = st.text_area(_O00Ill1OIllO(b'\xb4\x87\xc3\xcd\xf3\x10\xec\xfe\x9e$C\xd2\xd0\xccnq~', b'\x9d\xd0\x16j'), height=1533139116 ^ 1533139144, value=_1lOOIlll100100O(b'\x1c(q\x86T\x19\xc5=}II\x90\x19N\xe3\x01g\xef\t\x8e~]]\x8f\x11\xff\x1b\x18\xce\xab\xb2\xff\x0c\xcd\x90G\xf0?\xc6\x82}T`?0\xb2\x91D\xba\xa0\xde\xf6\xffp\xa5\x85\xb5\x0b\xa4HR\xd9\xbdc\x8c\t\xb56\xda9\xeao\x81:', b'\xd7\xe8\x02\x97'), key=_Il0I00l0OIIlO(b'\xbf\xabg\xcc\x93\t>\x83\x9f\r\x83\x9b-\xd8\xf3\x8b', b'R\xce\xaf\xd7'))
            if st.button(_1lOOIlll100100O(b'\xc2\x06M\x1eW\x18k\x9b\x1am\xd7\xe7t\\\xad\x90E^', b'\xddK\xcc#'), key=_OO1I0ll00OO1(b'\xeb[\xb6M_fym\xaa\xcd\xac:\x9868=$', b'y\x07\x8e+')):
                if template_name and template_content:
                    if save_whatsapp_template(template_name, template_content):
                        st.success(_Il0I00l0OIIlO(b'\x1a[\xf3V\x1a\xf6\xc6\xe51\xad\xca\xd0\xfe\xc1{?\xf6\xca', b'PS\x17\x87'))
                        st.rerun()
        with col2:
            if templates:
                st.write(_Il0I00l0OIIlO(b'\x8f\xd6LpR\xd5~/Ge\xacVS\xcf\x88\xcc0Y\xff\x80', b'}\xd5\x1f\x8e'))
                for name in templates.keys():
                    col_a, col_b = st.columns([202758236 ^ 202758239, 1555275884 ^ 1555275885])
                    with col_a:
                        st.write(f'📝 {name}')
                    with col_b:
                        if st.button(_OO1I0ll00OO1(b'\x8b\xe8\x92\xde\xf9~\xa8', b'\x86) \xd6'), key=f'del_template_{name}'):
                            delete_whatsapp_template(name)
                            st.rerun()
    load_option = st.radio(_Il0I00l0OIIlO(b'\x80|\xaf`\xb4V\xba\x1a|\xcc', b'Nx\xcbQ'), [_O00Ill1OIllO(b'\xb4\x0fH\xfa\xd6\x12h', b'\xad$\x9f\xbc'), _O00Ill1OIllO(b'\xbf\xc3\xe0;\x0c\xcarY\xa2\xe2', b'\xc8\xc0\x16\x14')], horizontal=True, key=_O00Ill1OIllO(b'\xe1P\xa7\x18\xbcU\x0c\x80\x0e\xd1\x97\xb5\x18a', b'\xa3\xeb\xb6\xf6'))
    df_wa = None
    if load_option == _O00Ill1OIllO(b'\xd3!\x9dE\x92\x941', b'\x81\xbb\xfd\xa2'):
        files = get_history_files()
        if files:
            selected = st.selectbox(_OO1I0ll00OO1(b'\x01\xbb\xf8s\x1d\x1e\x03\xac\xe3\xce\xb1g', b'\xabL\x086'), files, key=_Il0I00l0OIIlO(b'\xa3NH\xc9\xc1c)+\xf2\xe6\x86\xd9\x1e\xa4', b'+P"\xf6'))
            if selected:
                df_wa = load_history_file(selected)
    else:
        uploaded = st.file_uploader(_OO1I0ll00OO1(b'c\xa7\xad<\xad\xcf\xdb8O\n\xdd', b'\x97 \x05}'), type=[_1lOOIlll100100O(b'\xfd\x81H', b'\x98\xdegB')], key=_Il0I00l0OIIlO(b'\x89UYM\xfe(9\x92\x13s\xfe\xdddI', b'[yEx'))
        if uploaded:
            df_wa = pd.read_csv(uploaded)
    if df_wa is not None:
        valid_phones = df_wa[df_wa[_OO1I0ll00OO1(b'\x8d\x1b\xe1t-', b'F\xe6V\xbb')] != _Il0I00l0OIIlO(b'\x0e\x08\xaf\\\x1de\xaf\x0b-M\x1b6\xaej@', b'\xa4e+\x92')]
        valid_phones = valid_phones[valid_phones[_Il0I00l0OIIlO(b'\x9d\x7f>k\x19', b'\x18\xa1\x8c\x89')].notna()]
        if valid_phones.empty:
            st.warning(_O00Ill1OIllO(b'\xd8\xaf\xa3I<\x16t\xb3="\x16\xad\xb9\x08\x15\xbeL\xf5\xe4\t\xd7K=\xad\xf3\xaa\x84x', b'\xc6\x16\x19\x94'))
        else:
            st.success(f'✅ {len(valid_phones)} leads with phone numbers')
            template_options = list(templates.keys()) if templates else []
            template_options.append(_OO1I0ll00OO1(b'D\xec\xee\x90\x93\x07', b'}\x1fr\xe0'))
            template_options.append(_OO1I0ll00OO1(b"\xe8\x9b'\x88\x01,\x11\xd4\x02\xbb\xe6H\xe5\xff\xeb\x9al\xe5`", b'_\xe3\xe1\xec'))
            selected_template = st.selectbox(_OO1I0ll00OO1(b"\x14\\w~V\xf01]\xd8\x9d\x8d'\xd3\xf1\x08\xac", b'|\x1e\xb4\xff'), template_options, key=_O00Ill1OIllO(b'\x9c|\x0c\xf3\xce]-]N|[y\xaa\xa6r~\xfb\x18', b'U\x14\x91\xf7'))
            if selected_template == _OO1I0ll00OO1(b'\xb9JvU\xbb\xf4\x06\xf4}\x92Vx\xcc\x13[v\xd8\xcf\xdf', b'\xc9\x9fQd'):
                st.info(f"📋 Using company profile: {company_profile.get('company_name')}")
                message_template = f"Hi! This is {company_profile.get('sender_name', '')} from {company_profile.get('company_name', '')}. We help businesses grow with {company_profile.get('product_name', '')}. Special offer: {company_profile.get('special_offer', '')}. {company_profile.get('call_to_action', '')}"
                st.text_area(_Il0I00l0OIIlO(b'@\x00\xd0\x9a*ft\x00', b'z#\xb6)'), value=message_template, height=1707839520 ^ 1707839556, disabled=True, key=_Il0I00l0OIIlO(b'\x9f\xc2x\x0f\xabi\xb9\x0e\x85B\xf8V\x00\x1f\xf7\x0f"\x1e', b'\xea\x05\x86E'))
            elif selected_template == _Il0I00l0OIIlO(b'+\xb7)\xe6\x92\x03', b'\xb9\xeeU"') or not templates:
                message_template = st.text_area(_O00Ill1OIllO(b'\xda\x16\xc2\xe8\x98\xe1O\x8c\x88r}x}\x89\x81\xc2w', b'\xc8\x1b\xa7s'), height=1255441937 ^ 1255442037, value=_1lOOIlll100100O(b'\xff u\xa2}\xee\xaf\xc9=\x02;\xe6\xd7\xdah\xb8l\x8cD\x94\xe9Fe\x16\x1e\xd2\x7fN3\xf7\xbdNz\x8a\xe3\x15?G\x86T\x97\xa7\xabhbk\xfd\xf3\x18\x9c \x8d\xbeH\xb1$\x8f\x03\xfczb\xd1<\xfbl\xbcR\xad\x80\xb1m\xdbf\xe3\nu+\xcb\x01&\x87\x8d\xd9\xba\xa2\x94/M\x88\xf9g\r', b'\xe25(\x16'), key=_Il0I00l0OIIlO(b'\x8f\x07\xfa\xe8"A\xef\xcfV\x9a\xce\x81i\xbab\x04S\x88I', b'\xd6$\x83Z'))
            else:
                message_template = templates[selected_template][_O00Ill1OIllO(b'=g\x1c\xffp\n8', b'\xe6\xf8\x0b\x9e')]
                st.info(f'Using template: {selected_template}')
                st.text_area(_O00Ill1OIllO(b'\xadi\xe6\xd2wS\xfb\x0f', b'?\xa4D\xef'), value=message_template, height=1016080263 ^ 1016080355, disabled=True, key=_Il0I00l0OIIlO(b't\xd2\x92\x9e\xca\xa4rf\xfd \xc1\xf6\x95\x8b\x92\xd6\xbb\xc2\x80', b'\xe4Z\xa0\xdf'))
            if st.button(_O00Ill1OIllO(b'\x90\xf9\xf68\x1b\x83\xaf\x97R\xb7\xfc`t\x87\x1a\x96\xbe,\xe7\xb5\xf5\xc6', b'\xd6\xa8x7'), type=_Il0I00l0OIIlO(b'\xa4\xf9\xd7\x8f\xd5\xb5\x95', b'/K\xac\xf1'), use_container_width=True, key=_1lOOIlll100100O(b'\xe6\x9b\xb1\xcd\xe4(\x1b\xff\xf6\xcf\x92\xc8jn\x8d\xff\xebT\xe0E', b'-\xd1\r>')):
                if not groq_key:
                    st.error(_O00Ill1OIllO(b"\x04\x1c<g\x0e)mL\xe9\xa5\xf4\xa1JaZu}Qz;,\xf6\xefbx\x13\xb1~\xb2\x81/'\xd3\xd2]\xa7q\xe4\x9c\xd6\xd5\xf6\xa0\xae\xce6\xd8\x1f\xc4\x7f3", b'\xcda^\xeb'))
                else:
                    progress = st.progress(926633447 ^ 926633447)
                    status = st.empty()

                    def update_wa_progress(idx, total):
                        progress.progress((idx + (21461270 ^ 21461271)) / total)
                        status.text(f'Generating {idx + 1}/{total}')
                    wa_results = process_whatsapp_messages(valid_phones, message_template, update_wa_progress)
                    progress.empty()
                    status.empty()
                    st.success(f'✅ Generated {len(wa_results)} messages')
                    for idx, row in wa_results.iterrows():
                        with st.container():
                            col1, col2, col3 = st.columns([1159125998 ^ 1159125996, 969510551 ^ 969510548, 1661811599 ^ 1661811598])
                            with col1:
                                st.write(f"**{row['Business Name']}**")
                                st.write(row[_O00Ill1OIllO(b'\x1c\xcb\xab\xa1\xde', b'j\xfd\x8e\x03')])
                            with col2:
                                preview = row[_OO1I0ll00OO1(b'\xb2P}\xb9Sx|\xc3\xc5h\x1e\xe1\xc0\x80\x8d\xbb', b'B\x9b\xf1\xc0')][:1909965428 ^ 1909965328] + _O00Ill1OIllO(b'a*v', b"\x98'j\x15") if len(row[_Il0I00l0OIIlO(b'N\xca#"\xd4\xcc\xb3H\xd7\xae.\x12f\xb6\'\t', b',\xd1O\x13')]) > 951961505 ^ 951961541 else row[_Il0I00l0OIIlO(b'\x9b\xc6\xc3\x0c~\xe8\x85q\xf7\x92\xdc\xd9\xcf\xb0\x03\xd2', b'\xdf\xdbf\xd4')]
                                st.write(preview)
                            with col3:
                                wa_url = generate_whatsapp_url(row[_OO1I0ll00OO1(b'\x0e\xf9j$\xce', b'^uz\xc2')], row[_Il0I00l0OIIlO(b'\xe6\xf0\x81\xfa\x86R6r\x93\xce\x81\xa9gC\x9b\xa9', b'\x02(\xa9;')])
                                st.markdown(f'<a href="{wa_url}" target="_blank"><button class="wa-button" style="width:100%">📤 Send</button></a>', unsafe_allow_html=True)
                            with st.expander(_OO1I0ll00OO1(b'\x02%`)\xd0\xdf"\xe8\xb9A\x18V:\x8eQj}', b'l\x07\x8c\x86')):
                                st.text(row[_1lOOIlll100100O(b'\x8d\xc7\x13\xf7\x96\xab\xe5xy\x93mz\xdb\x17\x03\x91', b'\xcf\x06\xf8;')])
                            st.divider()
                    csv_wa = wa_results.to_csv(index=False).encode(_Il0I00l0OIIlO(b'\xe7(\xa2}\xbe', b'f\x0e\xd3e'))
                    st.download_button(label=_O00Ill1OIllO(b'\xb8\xe5\xee$\x15\xfcj\x8f\x17h\x17\x05df\xb4M\xa3@\xa6\xac2 ', b'\xa4\x1a\xdc\xf6'), data=csv_wa, file_name=f"whatsapp_{datetime.now().strftime('%Y%m%d')}.csv", mime=_OO1I0ll00OO1(b'\xdc\x8b\x16)N\xcd\x06i', b'\xadL\\8'), use_container_width=True, key=_OO1I0ll00OO1(b'\xa5$(\xa9Hr\x12\x9f7\x80D\xfaG\xa0\xa2\xeaQ\xe9&W', b'\xbc/\xcd.'))

def render_multilanguage_tab(company_profile):
    st.markdown(_Il0I00l0OIIlO(b'{\x87I\x8ao \xe4\x91\xf1\xc3\xe6\x8b\x11\xb7t|\xbf\xff\xaa\xe14N\xe7\x86@\xc7\x14\xab*\x94\xc0\xef\x1aE\x0c-\x98\x89w b\x14\\\xfe\tirJD\xf6\x96\x04>0\x18\xad%', b'HD\xc5\xc6'), unsafe_allow_html=True)
    st.markdown(_OO1I0ll00OO1(b"\xde\x9e\xc2\xa8\x1ba\x00\xbe\xa0\x98\xb7\x13sO\xd6Kd\xe8s'\x0eh\x86\xbe\r\x82\x95Zq\xaf\x02\xd1\xb8\x18e\xd3Wx\xc3\x8cCM6\xb4\x05.A\x05\x01\x0ck\xadSIV:=3\xba\x1a\x82\xf9h\xc9\x84\x12\xf0<zJ\xf5\xa0\xb6\x986/\x97\x99\xdb4\x8b\x0f.\xd6", b'\xebs\x1eZ'), unsafe_allow_html=True)
    groq_key = get_groq_api_key()
    if not groq_key:
        st.error(_OO1I0ll00OO1(b'\xb72\xf9\x1bN,\x0e\x96\xa0^"\xca\xa9\xbc\xf1_\xc9\x82AmN\x00\xcb$2\x0e!Ix\x16\x1d\xb4*\xc0?\n+\xc9\xa5\x1cY\xa0\n}\x0fjeu\'w\x07>\x1a\x1e\xacf\xdcU', b'\xb4\xe8k\xed'))
    if not all([company_profile.get(_O00Ill1OIllO(b'\xd1hN0\xe2\xb1G\xc8\xcd\x9b\xa1\x8b', b'\xcb\x82DH')), company_profile.get(_O00Ill1OIllO(b'e=\x94\xcb\xdd\xa8r2\xbb{\xe1\xfb', b'M7\xe2\x01'))]):
        st.warning(_Il0I00l0OIIlO(b"\\\x9e\\\tM\xd2\xc6J\xc5\xe0N\xf1Q\x18\xaedw\xda]\x9f4\x82\x07q]\xa2kF&\xb5\xad\x02e*T\xe0\x13tlh\x1d\xb7\x86dY\xf8|&\xb6T\x97\xf6j\xd1'\xbfh\x0e1,U\xe7\x95$\xaf\x88\xdf\xa9X+\x1f", b'\xf1&\xc9\xf8'))
    st.subheader(_1lOOIlll100100O(b'\xdb-y\xb4w"\xd8\x98\x94\xc9\xb4\xb8\xf2$\x8d\x0f"aR\xcd', b'\xf8\rT$'))
    lang_options = get_available_languages()
    col1, col2 = st.columns([1876213012 ^ 1876213014, 52756978 ^ 52756979])
    with col1:
        selected_language = st.selectbox(_Il0I00l0OIIlO(b"\x9f'\r\xa6@\xaa\x06\t\xfb\xf4\n\x9f\x14\xac\x81\xafa\xd1U\xc2\xf83j", b'\xaa\x97\xf3#'), options=[lang[1206169933 ^ 1206169933] for lang in lang_options], format_func=lambda x: dict(lang_options)[x], key=_O00Ill1OIllO(b'p\xdf\x9c\x97\xa16\x8d\x19"O}\xaa\xf7\x88\xd8\xfa5', b'\xe5\xfa\xdd\x01'))
    with col2:
        message_type = st.selectbox(_OO1I0ll00OO1(b'\xa2\xa2!i\x86\xe9*\xc1\x9a\xf7\xec\xcf\r', b'I\xd7\xa2>'), [_1lOOIlll100100O(b'\x07\x16\xe3u\x11', b'\xfb\x83\xe6\xb8'), _O00Ill1OIllO(b'J\xdb\x10\tg5\xdc/', b'\xf8\xb2V\x7f'), _Il0I00l0OIIlO(b'\xde\xe9\xf0\x0f\x8e\xba\x94A', b'\n\x01_\xbd')], format_func=lambda x: x.capitalize(), key=_OO1I0ll00OO1(b'\x93\x8b7\xd8\xba\x0034\xa41\x18\xf9\x821\x97', b'\x1b\x15IR'))
    lang_info = LANGUAGE_CONFIG.get(selected_language, LANGUAGE_CONFIG[_O00Ill1OIllO(b'\x18\x1a\xe3Mc\xba3', b'P\xe1\xde\xf9')])
    st.info(f"\n    **{lang_info['flag']} {lang_info['name']}**\n    - Region: {lang_info['region']}\n    - Formal Greeting: {lang_info['formal']}\n    - Casual Greeting: {lang_info['greeting']}\n    - Sign-off: {lang_info['signoff']}\n    ")
    st.subheader(_O00Ill1OIllO(b'\xba\xf8FoKx\x010\xe2\xf43r\xbf\x97\xfc\x91\x9c', b'\x8e7\x93,'))
    load_option = st.radio(_O00Ill1OIllO(b'\xaa\xc5~\x96\x86\x107\xc5\x87h', b'\xdeV\xdb\xdc'), [_1lOOIlll100100O(b'\xceV\x12\xaf\xb2\xd1;', b'\xc0\x12~\xb2'), _Il0I00l0OIIlO(b'$LG\xba\x11\x0e\xd9.E\xda', b'B\x0cA\xf4')], horizontal=True, key=_1lOOIlll100100O(b' \xc9\xc1\xd8\xecW\xd6\xe6\xb9\x81\x00\xe5LL\xa9-\x1e', b'9Q\xbcM'))
    df_multi = None
    if load_option == _Il0I00l0OIIlO(b'\xf9\xacYG\xa2M\x11', b'\x9d\x7f\x95\xdd'):
        files = get_history_files()
        if files:
            selected = st.selectbox(_1lOOIlll100100O(b'"\x9c\xf1(\x04p\xbaO\x99\x0f{\xf9', b'\x15Y+\xc6'), files, key=_1lOOIlll100100O(b'\xeeA\xf2<\xa1kJ\x0b\xe6iB\x1dxo\xb6\x1d9', b'\x81S\xcf['))
            if selected:
                df_multi = load_history_file(selected)
    else:
        uploaded = st.file_uploader(_1lOOIlll100100O(b'\x1a\xad\x17\xd4\xb5\xac\xfb\xd4\x99\r\xda', b'4\xb6\xba\x8a'), type=[_Il0I00l0OIIlO(b'\xc0!s', b'\xd2\x03\xb0\xae')], key=_1lOOIlll100100O(b'\x90\x17\xdb\x80\xe7$\x93\xe7<\x8bW\x15\x99\xfeTPy', b'\x99\xc7#\xee'))
        if uploaded:
            df_multi = pd.read_csv(uploaded)
    if df_multi is not None:
        st.info(f'📊 Loaded {len(df_multi)} leads')
        st.dataframe(df_multi.head(), use_container_width=True)
        if st.button(f"🚀 Generate {lang_info['name']} Messages", type=_OO1I0ll00OO1(b'\xf6\x9d}\xec\xb4=\x84', b'\xa8P\x8c\x8f'), use_container_width=True, key=_Il0I00l0OIIlO(b'\x94\xe2\xbb\xda\x9a\x08\xdf\xe1n\xec\x1d\x06\x87\xd5\x01\x99!7\xa3Tj\x1fH', b'6u\xb3\xc7')):
            if not groq_key:
                st.error(_OO1I0ll00OO1(b'0c\xbb\xa3\xdd\xe9\xca\xc9x\xaew\x83\xa4"8\xdd\x1b\x91C\x84\xc5\x86\xbb\xd0B@$9\x93\xd2\x80\x1d\x9fv\xc3\x1a\xa8\xc6\x06\xde\xe6g\x07\x98F/R\x94\x17J\x10', b'N\xda\xed\x00'))
            elif not all([company_profile.get(_OO1I0ll00OO1(b'\xea\x97u\x7f\x83NS#%q\x10\x06', b'\xb0\xca\x07H')), company_profile.get(_O00Ill1OIllO(b'Iu\xc7\xab\x94 \xfa\xa3L|\xc0\x9f', b'l\x87\x06\xc3'))]):
                st.error(_1lOOIlll100100O(b'\xf5\xe5`\xd1F?\xa2\xa2\x9aa\x0b\xb48t\xa4d\x19"fw\xe3\xe6[\x7f\xe9g\xb6\xa9\x0ca\xd2"$\xa3:\xbe#m\x19f\xb7!\xe3B|\xb3\xe4\xa1\xfc\xbd\x8b79\x8aR\x1d)\xab2Z\xb4\xd20^.+\xb9\xe8\n\xcdG', b'Ok\x7f\x8b'))
            else:
                st.info(f"🌍 Generating {lang_info['name']} messages for {len(df_multi)} leads...")
                progress = st.progress(2115414164 ^ 2115414164)
                status = st.empty()

                def update_multi_progress(idx, total):
                    progress.progress((idx + (803602005 ^ 803602004)) / total)
                    status.text(f"Generating {idx + 1}/{total} in {lang_info['name']}")
                results = df_multi.to_dict(_OO1I0ll00OO1(b'\xaf\x1a\xe0\x81\x812?', b'\xe5*EO'))
                results = process_multilingual_messages(company_profile, results, selected_language, message_type, update_multi_progress)
                progress.empty()
                status.empty()
                st.success(f"✅ Generated {len(results)} messages in {lang_info['name']}!")
                display_df = pd.DataFrame(results)
                message_column = _1lOOIlll100100O(b"\xbd,\xae\x03\xa2\x0f\xa30\xcaD\xb8\x07\xc8\xb8\xf8Z-\xa3\xb2O\xf0'\x80", b'\xb0X<v') if message_type == _Il0I00l0OIIlO(b'\xcf1\xcf\xd4\x1d', b'\x8e\x05\xd4\x92') else _OO1I0ll00OO1(b'\xd8U\x1d~A\xa4\xc9]\x93\x81"\x81\xca?|\x02', b'\xd99\xaeF') if message_type == _OO1I0ll00OO1(b'S\xdc\xbb\xa4&e@\xb3', b'\xb8\xd8D\x97') else _1lOOIlll100100O(b'\xfdG\xf1k)N\x95\xa3\x16\xef\xcd\xe9{\x1bdF\xdd', b'@\t%a')
                if message_column in display_df.columns:
                    display_cols = [_O00Ill1OIllO(b'`[O\xb0z\xc6yV\xc5\x89\x8e6\x8d', b'v\x01\xb7='), _Il0I00l0OIIlO(b'2\n"gs', b'\x9a\xf6L\xa8'), _Il0I00l0OIIlO(b'w\xe6\x1aG\x00', b'&>\x022'), message_column, _1lOOIlll100100O(b'\xfe\x89\xdaI\xfaec\x8e', b'\x1a\x9e\x96\xb4')]
                    display_df = display_df[display_cols]
                    st.subheader(f"📝 {lang_info['flag']} Messages in {lang_info['name']}")
                    for idx, row in display_df.iterrows():
                        with st.expander(f"✉️ {row['Business Name']} - {row['Language']}"):
                            if message_type == _OO1I0ll00OO1(b'\xf3[\xcf|\x85', b'\xcdW~\xac'):
                                st.info(f"📧 Email: {row['Email']}")
                            else:
                                st.info(f"📱 Phone: {row['Phone']}")
                            st.text_area(f"Message in {row['Language']}:", value=row[message_column], height=543791628 ^ 543791812 if message_type == _O00Ill1OIllO(b'\x12\xbd\x8a\x00\x17', b'\x84\xaf\xe8C') else 1015227860 ^ 1015227824, key=f'multi_msg_{idx}')
                    csv_multi = display_df.to_csv(index=False).encode(_Il0I00l0OIIlO(b'\xedP\xc4\x9b\x0b', b'8U4\xca'))
                    st.download_button(label=f"📥 Download {lang_info['name']} Messages (CSV)", data=csv_multi, file_name=f"multilingual_{selected_language}_{datetime.now().strftime('%Y%m%d')}.csv", mime=_Il0I00l0OIIlO(b"\xc4\x18\xae\xa9H7'\xf3", b'\xa7v$\xf1'), use_container_width=True, key=_Il0I00l0OIIlO(b't=.p\x02\x83l\x85\x9e4S\xe5\x9e\x16', b'\xda\x93A\x9e'))
                    st.info(f"\n                    📊 **Generation Stats:**\n                    - Total messages: {len(results)}\n                    - Language: {lang_info['flag']} {lang_info['name']}\n                    - Message Type: {message_type.capitalize()}\n                    - Region: {lang_info['region']}\n                    ")
    with st.expander(_OO1I0ll00OO1(b'\x0eE9\xea\x0e\x01$\x19x\xda<_\x1cp\xfdo\xe8j\xac\xbe\x0c\xeb\x18v\x9b\xa2\xe6\x8c\xd4', b'\xdcu<}')):
        st.markdown(_1lOOIlll100100O(b'p\x16\xff\ng\x9a\x1b"\x0c\xa2\xd4\x92\xd9\xd8\xd8\x02\xb414/\x02F\xdb\\Ji\x92\xc1\xd0\xa7\xf1vO', b'_\x95\xe2I'))
        col1, col2 = st.columns(530354640 ^ 530354642)
        with col1:
            st.markdown(_Il0I00l0OIIlO(b'\xa6m= Zq\x01\x92\xea\xf3\xe9%@', b'\x12\\\x86\x89'))
            st.markdown(_Il0I00l0OIIlO(b',i\x0e\x9b\xcd\xc7\xb7\xc4\xd6\xfcU\x84`\x7f\x8b\xce\xfd\xc4\xf2\xa9\xca\x85\xda\xc7\x9b(h\xdb\xf0\xaf\xf33L\xc5"A\xeeF\xaf\xff\x17\x08\xa2TG\xb5\xb5\xf9\xf2^\x81<\x01\x82\x96\x930If\x0c\xed\x82T\x9e\xecT\x0f\x89\xff\x81O-\\\xd0XB\x9b\xcc\x1d\x06\xfb\xe9\xce\x92\xccc\xfa\xceu\xa6\x92\x05Z\xb0\xc1 U\x84~*C\x9a]\xc4$\xbbG\x82\xa4\xce\x17\r\xf09\x19g\xdf\xd8\xb3\x9ft=\xa8D\xb7yg\xc6\xce{\xa8\xdd\xc3\x0e:\xb4u\x9a\xc4v^\x80l\xef\x8e\x00<\xef\x07|7\x0c\x9e\x1bQ\xb8k\xd9\xb4F\xe7Gw&\xe4]\xa4\xdd\xb9\xd1\x88\xf4\x81JL\xa0\x80\xe6\xd3N\x9e\xfc\xba\x86<\xf7&\xb5)\x02X\xcd+\xe8d\x80}v(\x06\xbdi\x87\xab\xaad\x89\xac\x15\xb4,M\x07\xf5\xaffc\x1e#', b'\x91\xd8\x94\x9d'))
            st.markdown(_Il0I00l0OIIlO(b'\x14\x06N\x1cc:{\x15\\l\xe5f>\xa9\xcd\x19\xb7\xd0', b'\x1d\xeb\xd2\xa5'))
            st.markdown(_OO1I0ll00OO1(b'\xfet\xb6Ez1\xcbRz.\x87?\x1ei\xfe\xab\x95\xc2\xfc\xe8\x9c%\x16X\xae\xc2\xa7\x12\xd7\x8b\x93\xf6oo\x14\xb8\xa4z*\xd9\xa8\xff!\xb0>\r\x8a\xc8sT\xac\x11\xeakY\xc4\xac\x15e\\\xc9\x16{\xe7\xc2\x11\xa5\xec\xe0U\xcf~\r^\xa4w\x0fI\xd4=\xd2\xe2\xcb\xdc\x01\xa3\xcf(\n2V\xb7\xab\xb7\xd4r>\xaft\x11s4I\xd2\x0b\xe1\xc719j-\x81\xde\x00H\x1cjh\xb5eZ\xb7\xc3\xb6\x13\xf9_B\x8f\xe4V\xa7\x9aF\xbc\xc8\x8f\xdd2\xe6Z\xf8\x169\xb0\t.\x10\xba\x9e\xb8\xb9\x93X\xb7\xbdB\xfb\x002\xf7CC^\x19\xea?nj\xb8^t\xb3J\x0f\xf5<\xed/\xaeR(\xbc\xcc\xd8#\xd0t\x8a\xa6\x15\xad\\]F$\xbc\xfa\x952\x1f\xc7\x16\xf1lWd\xf7\x82\x1c\xaa\xf0\x81\xafS\xc2\xfa\x02\xa37\x81(\xfdp\xab\x0cc\xac7\xfd\x9fW\xc8\xec\xe6R# \x1c\x98\x80', b'\x04B\xdaB'))
        with col2:
            st.markdown(_1lOOIlll100100O(b'\xfb\xb6\xb0\xcfz\xeab\x82f`\x1d\xcd\xf2\xc9Tn\xbbs2\x15\xb13\xcdgq', b'\xe4\x16\xdaL'))
            greetings_data = []
            for key, info in LANGUAGE_CONFIG.items():
                greetings_data.append({_OO1I0ll00OO1(b'#\x8d\xb0\xc74\x06p\x07', b'G\xb9\xff\xef'): f"{info['flag']} {info['name']}", _O00Ill1OIllO(b'\xc4\xc0I\x0fj\x08[\xe4', b'\x86\x15\xc8b'): info[_Il0I00l0OIIlO(b'\xc13T\x94\xa1\x14r\xff', b'o$q\x1c')], _O00Ill1OIllO(b'\xa9\xbbN\xafs\xfb', b'\xc1H\x15\xa7'): info[_OO1I0ll00OO1(b'G\xbf0\xe1\xffV', b'3\xb5\xce\xf0')], _Il0I00l0OIIlO(b'w\xd3\x97\tHP\xa86', b'p50('): info[_Il0I00l0OIIlO(b'(\xc2bi6\x99t', b'\x82\xe0\x7f\xeb')]})
            st.dataframe(pd.DataFrame(greetings_data), use_container_width=True)
    with st.expander(_O00Ill1OIllO(b"\xd9\xfe<\xe5\x98g\x93Kp`m\x8d$\xbf\x1a\xd1\xb9D\xe4?\xdbF.\xd7\xc9'\xb1\x7fj\xc4_\x0e\xd0\t\x93>\xb4", b'$y[/')):
        st.markdown(_OO1I0ll00OO1(b'\xcb\x95PN\x89\x7f\xca\x92\x9b\xa3J\xcb\xd6\xf0}\x82\x93\xc5\x02\xfbcU\x1bCX\x1fqn\xa0"\x90\xacK(\xd2U\xa1\xdc\x8b\x8f\x1a\x91\xc0%\xdfU\xab"\x0f\xcc,\xb6\xefW+\xdf\xdeG\xb7\xe7\xee\x08!\xd2\x1a\x94\xcd\xbb\xdc4\x0f\xed\x1b2\x16v\x1dKe\xa7\xdc\xfc\x1d\x97\xfb\xe1\xf4w\x86N\x9b\xdc\xac"i\x17\tg\x81\xfb\xd9\xb9\'\x9a%\xc4]\xc2.\x17\xa0\xa6 \xfc\xaf^\xbc\xba/?^\xb9\x18\xce`a\xa9\x0eB\xc3\xb2\x998N\xcb\x82?\x9a.GZ\xb7\xf2o/&s\xb0\'\xa3\xbe\xf5\x84\xb0\xa0\xa8\x86O\xa3\xe4pT;\x82X\xa68\xf5?v\x05\x83$O\'2\xfb\xb4\x06\x12\xd5w\x94\xbc\x1e.5>\xd5\x9a7\x0cA{q\xdb(\x10\xc5\x18l\xb6\x83\xad?\x9a!\xe6\xd9x\xd0\xd9\x12\xad\xfbx\xb9\xe4~\xad\xf9\x86`9\x118\xad\x12\xeb\x0e\x92\xe0b\xce\xfa\x1c\xf1\x8fgw\xcf\xe7\x85\x98\x08\xfd\xac\xcd\xb5\xfb\xa5\x0c\x1c\x9fFL\x08\xcf\x92g\x1cd\xfc\xb2>\xc0\x92\x1e\x05\xe9\xe8D\xbc\xefO\xb1yp\xacQ95c`\x84\nM\xcf\x8d\x02>\x87p\xfboB\xf6\xcer\x8d\xd5<\xbc\r\x8b\xcco\xac\xc5h\x99\xf2V\x8fL\xa0\xa1S\xe3\xb6\xe7o\xef\xd2\xc7~j6\xaf\x07\\W\x80\x17\xf3vn\xccE\x91\xa0\xc5\x92V\xf0\x18\x8e \x13\xfaD\x856}\xe2\xbbI\xb0\x92I\xbf\x1c3 H\x91\x07\xa2fRMd\\d\xcdJ\x0c\xcd\xd4\xc2/\xdb\x93\xee\x9c\x07\xa2\x96\xf3\xa5-\xedHO:\x16q;^\x10q]\xd0\x04\x82D\x13^qnqR\x94\x81\xc0ARf;9\xc9\xa92\x00\xf8X\r3\xe2\x94L1-P\xb1=v\xc1\xfa\x9f\x06\x96P\x19l\x10\x88E0\xfa\x9f\x9d-\x9aL{6x\x04\x97\x11x\xe1I<\xcchn_\xba`N\xaf\xd7{\xf1K3\x97\xf5\xa9!cA=\x8e`\xf5\xa3\xd2U\xe4^\xe7e\xd1)!-N\xf1\xaaX\x97N\xbf\xca\xfb\xe4R\x98\x06\xa3\x16T?\xe3\xac\xd4bZ\x88?\xf0\xf6\x81\x00\x98\x19NFC#\x9a\xdd\xf3\x1e\x94\xab\x8a6.\x02\x07\x89\x12\xc4`\xe1\\$\\n\xa2}\x8d\xd9if\xa9\xb8M\x8eBC\xd2K\x90\nb\xa6\xf1\xcd\xa1g\x02A\x86\xba\xf8O\t%\xf7\xc0\xdf\x11:\xf2z\xd7\xdf\x86\xca\xcc.\xadx\xca\xae\xb0\xc6\xc7:o[\'\xdb~\xfe\xb8\xe8\xa3\'\xba\x8aRB\thk\x94\xca\xff\xf0\x87<\xc17\x9a`^\x81\xb1K\xe07\xdc\x14\xbf\x93\xfa~`9\x94\xed(\xaa\x8b7\x06_23\x94\x81W\x96\x8c3\x8f\xedl\xaf\xb1\x1c\xbbVx\xcdO\xc9c>\xca\xe0*\xe6+\x14\xa6\xa0/\xb9\xd6\x7f\x07E\xfa\xb9\\2\xe2\xcb\xfb\xbd\xa0\xc7\xf1-\x98S\x9b[\xb0\x92\x03V\x90\xe1\xc6A\x9e\x12<W\x19\x8b\xa48<<\xbe]\x06\x91;\xa3\xe9\xcd\xf5\xdd\xd5\xa2!\xad\x13%\xe3\xa2\xbb\xad\x8e\xa3\x18x\xcc\xc5\xd8\xc2QV9\xfc\x14\xf6\xa7p|\xef\x149\xe9\xaf\x16\x01m\x9eF\xc37\xd4\xf4\x0c\x8d\x17\x99f\x94\x11}X\xd8\x85Q\x91wq\xee\x0c2\xfe\x90w\x16\x156j\xbe\x042m\xc3\xa6\xa6r\xe7\xdb9\xeb\xa7p\xa6\xcdL\xbb\xf2\xe9\xe6y&\x94\xe7XTig\x85\xe5\xfc\x1fO\xf5\xc4\x0b#O\xccm\x00\xc5\x072\xf4\xcc\xff\xe3\x1c\xa6\xdc/\x87\x88O\xb6\xd0`C\x06\x14\xd3%\xf0.-\x80\'\xd6_\x92\xf5\xee+qU5{\xc6\xb1l\xcc\xc1P)\xf6\x1e\xe7X]_\xf5\xacF2\xc6\xc8\xce\xc3\x1d\xb1\xf7\x914\xf5\xba\xc5\xb9\xde|\x8e\x15`\x8f\xd6\xadIo\xfa\xec\x8e"\xf9\xfb#\x93\xe7\xda\x85\xd1c@\x7f2\xf9\x1a\x88\x16i8T\xdb\xd6Xfe\xf7|Jh\x80\'\xb1!\xc0\xc4\x1d\x01\xdf\x1aM~\xe8V\x91#~+\xc7\x1dE\xf4\xf91\xe4\xe9k;r=\xa8\x82^\xe1}\x1dga\xffJ\x04\x152\x05\xcf\xe1~\x89@\x9b<F\xea\xe8\xa2#\x89\x9f\x91\x8c\xb9\x06\xd8\xe3\x91\x82>tt*\xe3c{/\x19\xff\t\xe2@\x84\xe8qG\xfeN[\x9cd\x9a\x0f1y\xf7/\x11\x0b\x1d/\x92\x89\x10\xaf\x97\x93]\x18\xbb\x84\xdct\xb2\x90mv\xea\x05\xd7\xb0\xfeN\n\x9c\tlg\x97\xfer\xd7\x80o<\xd1\x1ef\xa4ee\xc3}!V\xf1\xfd\xb2\xb9\x165\xdf\xef\x80\x85m\x85;\xb6\xc4\xaa<#\xbf\x9dL\xc4\x18\xe9T\xad\xfa\xb2eOq.\xa6\x0f\x92\xd9\xe1\x90\xbe\xd1D\xaa\x979\x08)\xa4A7\xe1\xefQ\xb7\xdc0\xfe', b'\xd6\x98\rM'))

def render_followup_tab(company_profile):
    st.markdown(_1lOOIlll100100O(b'\xce\xfe\x0e\x8d\x16$\xcbA\xe5l>\x05\xa6{\xcf\xd2\xee\xb0\xa0e\xcc6hI|\x05\xc4\xc4\xb5\x86<\xc8\x11\xbb\x9c\x96=\x87\x9d@q\xf2\x86\xb6f0>\x0c\xf3\x12\x01\x15', b'\ne\xa3('), unsafe_allow_html=True)
    groq_key = get_groq_api_key()
    if not groq_key:
        st.error(_1lOOIlll100100O(b'jk\x18\x00#R\xfd=\xe1\xbd\xb4=\xe1x\xaa\x9e\x03\x7f\x0b<\xc54\x96\x1eR\x002\x16r\x8c\xb8\xd7DP\xddC\xcb\xb4\xd9;U`\xfd\x83\xe6\xe3/\xc6\x93\xfe\\\xfa\x9bx\xd8g\xeb3', b'\x95\xe0t\xd8'))
    if not all([company_profile.get(_O00Ill1OIllO(b'\x0b"\x97\'\xd8\xef\xd9\xdb\x812$\xd1', b'\xfa\xf7\x91\xd8')), company_profile.get(_O00Ill1OIllO(b'\xae\xc1T\x8f[\xdb\xcdP\xcb\x19\x94T', b'\xbd\xb8s\x05'))]):
        st.warning(_OO1I0ll00OO1(b"\xe9)\xc3\n\xe8\xb8\xb3G\x11^W\xfc\xe37\xb2\xf6\xb92\xa8\xcf\r'\xfa\xdb\xfd\x8c\x96\x83\x08e\xf9\xa5\xd1\xd0K\t\tm_\x83+\x81\xb6v}\xfb\xdaJ\xb1u\xc2\x92\x93\x125\xae\x0f\x9b\x868\xaa\x8d[\x98?\x1c\x08\xb1\x8b\x80r", b'\x1b\xa4\xde\xb7'))
    followup_settings = load_followup_settings()
    with st.expander(_OO1I0ll00OO1(b'\x0e9\x0fE\xa0\x10\xf5\x87\xa7v\xd1\xb1\xa2\x1a\xbd', b's\x83\x12['), expanded=True):
        enabled = st.checkbox(_O00Ill1OIllO(b'c\xe9:\x04\xf5\x9f\xfd\xd82\x16\x98\xaaB\xfd\x81[\x7f*\xb4\x84=', b'\xd3\xd2\xf7o'), value=followup_settings.get(_Il0I00l0OIIlO(b'vZ\xd5\xc8\xf7\x9e\xea', b'.\x03\x85,'), False), key=_O00Ill1OIllO(b'\x18\xcd\xeaWh\x8e\xb8\xbf\xad\xb1 \xdd@\xa6U\x19', b'\xb4\xfb\x8d\xd6'))
        max_followups = st.number_input(_1lOOIlll100100O(b'F<\xe0\xe5N\xe8\x19\x13BN>\x86W\xbfI', b'\xc9\x9d\xb4V'), min_value=1826114199 ^ 1826114198, max_value=164553769 ^ 164553763, value=followup_settings.get(_OO1I0ll00OO1(b'\xf0&6\xe6\xb1N\xa3#k\x14n\xa0\x91', b'\xb1\xa6\xccj'), 1235387961 ^ 1235387962), key=_Il0I00l0OIIlO(b'\xf1\t0B\t\xadZw\xbfR\x94\xb37', b';\x82\xdfo'))
        delay_days = st.number_input(_1lOOIlll100100O(b'\xad\xd6\xbf\x91\xbb\xb9\x17h\xd6F\x17\xcd\xa3', b'k\x18\xc2\xec'), min_value=1338111472 ^ 1338111473, max_value=589828494 ^ 589828489, value=followup_settings.get(_O00Ill1OIllO(b'b\xbd?\xb0\xca\xd3\xe0\n#\xd4', b'T\x1cZ\xb4'), 578675701 ^ 578675703), key=_OO1I0ll00OO1(b'\xe8Xi\x0f\x05\xaei\xc1\xb9\x8a', b'\xfa\x19/\xa0'))
        if st.button(_O00Ill1OIllO(b'iPV\x1d(\xac\xde\xa5\x17\xc1\xe0*,\xc9\x94\xad8]', b'\xff\xe5;\x88'), key=_OO1I0ll00OO1(b':\x06\x84\xea<d\xaf\xf1\xee\x9d;f\x86\x9avr1\xf2L\xaf\x11\x87', b'%\xc1M\xad')):
            followup_settings[_1lOOIlll100100O(b'\xcfqcEC\xf6\x94', b'7\xaa\xd9\xfa')] = enabled
            followup_settings[_Il0I00l0OIIlO(b'\x1d\x03\xc0=q\xfeC\x14\x17\x0fj\\\xd1', b'\x02~\xabZ')] = max_followups
            followup_settings[_Il0I00l0OIIlO(b'\xa4J\xeb\xc6\xba\xa1>\x12|Z', b'\xa6\x03\xd0_')] = delay_days
            if save_followup_settings(followup_settings):
                st.success(_O00Ill1OIllO(b'\xfc\xac\xfc\xf9W\x08B\x0fz0\xb9\xcd\x1f\xa1\xff\x0c\xb9\xd3', b'\xcf2\n\xac'))
    load_option = st.radio(_O00Ill1OIllO(b'\xc8\xe2-\x82\x8f\xa0z=@\x0c', b'g\x98\x10\xfe'), [_O00Ill1OIllO(b':\xcb\xf6\xe9a#9', b'p2V\x08'), _O00Ill1OIllO(b'\x19\x1b\x0ch\x02\x82Ix\xf5M', b'm\x89\xdd/')], horizontal=True, key=_OO1I0ll00OO1(b'\xc2\\_\x17\x9d\x08\xfbH,\xf7\x83\xaa\xbe\x94', b'?kK\xe0'))
    df_fu = None
    if load_option == _O00Ill1OIllO(b'8\xeb(4r]\xab', b'\xd8\x91\x8a\xee'):
        files = get_history_files()
        if files:
            selected = st.selectbox(_OO1I0ll00OO1(b"\x87\xe1\x97\xcb\x00[\xdd[hR\xa4'", b'\xa53\x14|'), files, key=_1lOOIlll100100O(b'\n\xb6\x9a\x86NG\r\x99\xe9\xa3\x8eD\xdc\xcc', b'd\xb2uJ'))
            if selected:
                df_fu = load_history_file(selected)
    else:
        uploaded = st.file_uploader(_O00Ill1OIllO(b'\x0b\x15K\xa5\x9f(\xea\x8b\x03<\x16', b'\x811L\xe4'), type=[_1lOOIlll100100O(b'\x92~1', b'\t\x01Y\xb0')], key=_Il0I00l0OIIlO(b'\x86\x0b~\x1dm\xca\xaa\xe80\xcb\xcd\r\x9a-', b'\xc1 {\x17'))
        if uploaded:
            df_fu = pd.read_csv(uploaded)
    if df_fu is not None:
        st.info(f'📊 {len(df_fu)} leads loaded')
        if st.button(_Il0I00l0OIIlO(b'\x0b\xf1\x00."\xa9\xe9\xb3\xce{x\x1eR\x10\xb4\xdc\xa6\x8e\x05\xa4\x9bu\x89H', b'\xe9\xc5\xe1\xab'), type=_1lOOIlll100100O(b'DE\x13G\x19\xda\xfc', b'\x11X\xbbX'), use_container_width=True, key=_Il0I00l0OIIlO(b'\xd3p)\xc1d\xdb\xfc^A\x06A\x82T\x88\x95h\xc5\xf6', b'\xb2\x87L\xc5')):
            if not groq_key:
                st.error(_O00Ill1OIllO(b'\x19\xce\xbcEf\xb8\x8cb\xa7\xbd\x0e\xcc\x8fw=\x80\xeb\x91 c\xab/\xc9/\xfcO1\x08\x1c\xed4g\x8b\x9eW&H\xa9DD\xe7\x1dT\x9c\x11\xdc\xca\x87}\x10\xca', b'I\xd1/>'))
            elif not all([company_profile.get(_1lOOIlll100100O(b'\x03\xea\x05\xd2U\xfc0\xe9\xba\xda\x00~', b'\x01Z:5')), company_profile.get(_1lOOIlll100100O(b'G\x0c+\x14\xa3\xfe\xcb\xa2Cp\x91\xbe', b'\xa3\x06|\x19'))]):
                st.error(_O00Ill1OIllO(b'\xa0\x01\xdb\xe2Y=\xdc\'\x8bs\xb2c\x06\xc0v\x90\x85\xbc\x03\x0c\xf7\x9fKy\x01\xbc"\xe5d\x04;\t\xccCv\x83\x00\x1c\xad\xe4]\'\xb1\x18\xe1\xb7tPr6I`\x1c\x8cR\xaau\x89\x96\xcb>\x9ciD\xc9V\xdb\x17`\x17\xf5', b'\x048C|'))
            else:
                progress = st.progress(1893145115 ^ 1893145115)
                status = st.empty()
                fu_results = []
                for idx, row in df_fu.iterrows():
                    status.text(f"Generating for {row.get('Business Name', 'Lead')}")
                    progress.progress((idx + (1809144820 ^ 1809144821)) / len(df_fu))
                    lead_data = {_1lOOIlll100100O(b'\xaa\xfeL\xb3>\x08\xf2&\xbeT\x10JJ', b'\x0fy\x15\xc7'): row.get(_Il0I00l0OIIlO(b'7qI\x8d\xf3J\xb3\x8e0\x16\x06`\xa7', b'\x17\x0bg\x0b'), _OO1I0ll00OO1(b'', b'\xc9\xb5R9')), _1lOOIlll100100O(b'\xd5o\xa1\xaf\xc7', b'\xf3\xed\xc3\xb2'): row.get(_1lOOIlll100100O(b'\xfa\xbe5Nj', b's\xa8\x075'), _Il0I00l0OIIlO(b'', b'c\x10+.')), _O00Ill1OIllO(b'=\xa9t\xd8+', b'\xe3\x86\xcbJ'): row.get(_Il0I00l0OIIlO(b'L\xc1\xd9D\x1c', b'NM\t\x8a'), _Il0I00l0OIIlO(b'', b'(\xde\x8f2')), _OO1I0ll00OO1(b'\x06\xd5\x8e"\xd4\xda\r', b'\xcb\xef\xcd\xfb'): row.get(_1lOOIlll100100O(b'\xbc\xf3]\xe3\x89\xcc%', b'\x9a\xcd\x92\xf5'), _OO1I0ll00OO1(b'', b'\xef\x85\xe4\xab')), _OO1I0ll00OO1(b'\x86\xe7\xa7VX\x0e', b'\xa98v\xd2'): row.get(_Il0I00l0OIIlO(b'`I\xc3{\xf0\xd4', b'\xe3\x8a\xd7C'), _Il0I00l0OIIlO(b'', b'\x87(9,'))}
                    followup = generate_followup_with_profile(company_profile, lead_data)
                    fu_results.append({_OO1I0ll00OO1(b',\xce\x02a\xc0?Xo\xf3\xd7NI\x1a', b'\xffx&\x17'): row.get(_1lOOIlll100100O(b'\x9d\xf9\x0cU\x0c`\xbe\x00E\x17\xb4\x90%', b'\xc3$\xef\xa4'), _1lOOIlll100100O(b'', b'h\xe2\x9a\xe0')), _1lOOIlll100100O(b'\xa4}\xd21\xcc', b't\x05\xad\xac'): row.get(_O00Ill1OIllO(b'\xeb\xb0"uB', b'bsf\x92'), _1lOOIlll100100O(b'', b'6\xf7\xc0x')), _O00Ill1OIllO(b'oB\x15\xdeN', b'\xb8\xe1AZ'): row.get(_OO1I0ll00OO1(b'\xa7\xffE~\xfd', b'\x9a*\xce\xc1'), _O00Ill1OIllO(b'', b'\xd1d=\x05')), _1lOOIlll100100O(b'\xfa{\x07\xb1\xaa\\\x86{"\xa5\xe2\xb5N\xd8^^;', b'Tj\xfd3'): followup})
                    time.sleep(0.3)
                progress.empty()
                status.empty()
                fu_df = pd.DataFrame(fu_results)
                st.dataframe(fu_df, use_container_width=True)
                csv_fu = fu_df.to_csv(index=False).encode(_O00Ill1OIllO(b';y0\xa8\x12', b'\nk\x0e\xe7'))
                st.download_button(label=_1lOOIlll100100O(b' \xb0\xccX\\`\xf2\x97\x00\x9a\x8e,\xff9\xdd\xa3\xae~\x97&\xdb\xa2\x01\xb0', b'5\xf0\x802'), data=csv_fu, file_name=f"followup_{datetime.now().strftime('%Y%m%d')}.csv", mime=_OO1I0ll00OO1(b'\xf0\x89\xb1\xe1\xde\xb7\xafh', b'\xb0\xb7\xa4z'), use_container_width=True, key=_O00Ill1OIllO(b'n,\x85\x8exc\x02\xc4\xe2 Ssy\x18\xeb\x06*<', b'9Kl\x82'))

def render_integration_tab():
    st.markdown(_OO1I0ll00OO1(b'\x9e\xeczc\x9fh\xbdc\xa9\x7fd\x84`\xff\xd0<S\x04\xc6\x7fM\x870z\xe3\xf5\xb5m\x1c\x0eo\x14V9\x02\xaa\x86\xd2\x92%\x15\xe0eX\xf1EF_F', b'M\x1dJZ'), unsafe_allow_html=True)
    with st.expander(_1lOOIlll100100O(b'\xdd\xfe\xbf\x92\x812\xce\x0f\x00v\x0c\x10', b'\x0b\x9b\xed{'), expanded=True):
        webhook_url = st.text_input(_O00Ill1OIllO(b'\xcf\x1a\xca\xab\x86\x8c\x92\xb8\xd4\x02Qd', b'-\xcaa\xe2'), placeholder=_Il0I00l0OIIlO(b'd#K\x1b\xf4F\xca:\xa4\x8f[\xb9\xc4\xdf\xe9\xe6\x02\x8a\x89\xcam\x91\xb2Q\xc2%\xcb\x14\xfa', b'\xe7xc\x9c'), key=_O00Ill1OIllO(b'%\xfc\xbe\x96^VP\xe6L=\xe4', b'\xf2V\xaa\xc0'))
        if webhook_url:
            load_option = st.radio(_1lOOIlll100100O(b'T\x9b\x1e\x18\xe4\xe4\x93\x86\x8a!', b'~p\n\x94'), [_O00Ill1OIllO(b'\xa6w\xf5\xe1\x9fx\x8d', b'\xbb\xa6I\x9c'), _1lOOIlll100100O(b'\x8c\xf4\xaa\xa7\x81\xdd\xbb\xf5\xa0\xc4', b'I\xb9\x80\xd2')], horizontal=True, key=_O00Ill1OIllO(b'\xdd\xdc\n\xb1\xde\xbc\xe1Z\xfd\x1cf\x0b\xe7J', b'\xd6N\xde\x14'))
            df_wh = None
            if load_option == _O00Ill1OIllO(b"\xbc\xf5\xfb\x8e'E3", b'\xb4]\xe5\x9d'):
                files = get_history_files()
                if files:
                    selected = st.selectbox(_O00Ill1OIllO(b'v0#\xc6\xc1\xe7yLS`\xda\x0f', b'WN\xbeu'), files, key=_Il0I00l0OIIlO(b'\xedF\x98!\x19,\xd1\x01\x1d\x9aN\xa1\x03B', b'\xcd\xb2\xe4\x9b'))
                    if selected:
                        df_wh = load_history_file(selected)
            else:
                uploaded = st.file_uploader(_1lOOIlll100100O(b'`\xaf^\xe2\xea\xc4\xf4\xf74,S', b'AI\xbad'), type=[_1lOOIlll100100O(b'\xdc\xf4\x00', b'E\xb7\xe0\xec')], key=_Il0I00l0OIIlO(b'\x96S\xccV\x15\x04m\xc6\xfc\x00\x86\x8d\xbf\xda', b'N\xb9\xec"'))
                if uploaded:
                    df_wh = pd.read_csv(uploaded)
            if df_wh is not None:
                st.dataframe(df_wh.head(), use_container_width=True)
                if st.button(_OO1I0ll00OO1(b'-\x7f\xdeW\x90\xaa\x83Cc\xfa\x8d\xc18\x15\xd6y\x8f\x9c\x80\xe6', b'\x15\xdb\xab\xe4'), type=_Il0I00l0OIIlO(b'\x8e\x16\xe7\xd6(fY', b'\xf2\x9fc\x0c'), use_container_width=True, key=_O00Ill1OIllO(b'\xf6\x9c\x9d\x95\x82^\xb0\xcd\x15\x08\xbap', b'\\\xa9\xa0\xfe')):
                    success_count = 199353116 ^ 199353116
                    progress = st.progress(983768712 ^ 983768712)
                    for idx, row in df_wh.iterrows():
                        payload = prepare_webhook_data(row.to_dict(), _O00Ill1OIllO(b'Y\xbf(\xd5\x9d\x8b\xbf\xdf\x1c\xdd\x83', b'\xcdY\x9cA'))
                        success, message = create_zapier_webhook(webhook_url, payload)
                        if success:
                            success_count += 1243230037 ^ 1243230036
                        progress.progress((idx + (1012636896 ^ 1012636897)) / len(df_wh))
                    progress.empty()
                    st.success(f'✅ Sent {success_count} leads to webhook')
    with st.expander(_OO1I0ll00OO1(b"\xb0\xe7\xcc\xe15\x12\xec<YJi('%\xee", b't\xf7\x14r')):
        crm_type = st.selectbox(_1lOOIlll100100O(b'\xe4Q\x1b%\xcb\xb6#\x82#\xf2.', b'U/R\xea'), [_1lOOIlll100100O(b'm\xf3\xfb\xa3\x93\xfbl', b'\xa0\xeb\x0b\xa8'), _1lOOIlll100100O(b'\x99\xdcg"\xdb\x9fd\xdd\xd9\xbb', b'w\t\xf9\xd6'), _OO1I0ll00OO1(b'KBf\xb4\x81\x8d>V\xba', b']B\xd3f')], key=_Il0I00l0OIIlO(b'v\xeb\xf9n\x07\xf4\xd1P', b'N\xbe\xc9\xe1'))
        load_option = st.radio(_OO1I0ll00OO1(b'\xc1\xf1\x84\\\x15\xddrV\xe4\x84', b'\xbac\xf6\x7f'), [_1lOOIlll100100O(b'aR\xab\xa8\x9b:\xe5', b'\x0bn\xb5\x88'), _O00Ill1OIllO(b'l!\xd3\xb3\xf2\xa7\xdel\x12\x98', b'\xa1L\xbd\xbb')], horizontal=True, key=_Il0I00l0OIIlO(b'5\x18\xe1\x17\xb1\x828\xc6\x85K\xa6\x8d\xc1\x14\xc6', b'J\\1@'))
        df_crm = None
        if load_option == _Il0I00l0OIIlO(b'\xdd\xfc\x8a+\x82I/', b'\xf0\x81\x14w'):
            files = get_history_files()
            if files:
                selected = st.selectbox(_Il0I00l0OIIlO(b'\x02\xa1\x1a\x04\x80\xd5\x1f:\x19\xd15\xc2', b'\xb3\xbd\x16m'), files, key=_OO1I0ll00OO1(b',\xbeT[\\\xca\xcc|\xb8\x10\t\xdb\x85\xce\xa1', b'\xe0\x18k#'))
                if selected:
                    df_crm = load_history_file(selected)
        else:
            uploaded = st.file_uploader(_1lOOIlll100100O(b"\x18\xa3\xf0TO'\xb3\x14\xe2\x1d&", b'\xa7\x0f\xb0\xe1'), type=[_1lOOIlll100100O(b'\xe4q\xf1', b':\x14\xdb\xed')], key=_Il0I00l0OIIlO(b'+\xb3\xb6\x14"\x81_\xd0\x8c\r\x8fK9-\xc0', b'S\x8d(\xe4'))
            if uploaded:
                df_crm = pd.read_csv(uploaded)
        if df_crm is not None:
            st.write(_O00Ill1OIllO(b'i\xc8,\x8a\xfd\xa3~G\xd6T\xa7\xcbF\x8b\x9f<\xa8n\xc8\xce\x8d', b'\x0b9\xd6\xd4'))
            col1, col2 = st.columns(1107133548 ^ 1107133550)
            with col1:
                name_col = st.selectbox(_OO1I0ll00OO1(b'd\x87\xb9yc\x0euH\xf6\x84(\x10a\xaa', b'\x9c\x9d\xed0'), [_1lOOIlll100100O(b'', b'\xa9M\x00\xb3')] + df_crm.columns.tolist(), key=_O00Ill1OIllO(b'\x10\xa4s\xcar.\xcekD\x18A\x8f', b'\xde{IW'))
                email_col = st.selectbox(_1lOOIlll100100O(b'F\xa9\x87\xe1*\x8c', b'\xf1\x11\x86>'), [_1lOOIlll100100O(b'', b'\xfd\x17UY')] + df_crm.columns.tolist(), key=_O00Ill1OIllO(b')\xa0\x0f\xa1\xed\x95\xe5\xa1\xf8K\x8b*\xe6', b'Q\xe9\xe9\xf6'))
            with col2:
                phone_col = st.selectbox(_1lOOIlll100100O(b'm\xddA\x9a]3', b'\x9d\xb5%v'), [_Il0I00l0OIIlO(b'', b'S]\xe4\r')] + df_crm.columns.tolist(), key=_Il0I00l0OIIlO(b'\x18!v\x99\xc5.\xbb\x02\xed\x9e\x19\x9f\xad', b'iG\x9bM'))
                website_col = st.selectbox(_O00Ill1OIllO(b'\xcd\xd5.Y\x1a\xb5O\xfa', b'\xdd1nb'), [_1lOOIlll100100O(b'', b'\xe3U\xd0\xb9')] + df_crm.columns.tolist(), key=_1lOOIlll100100O(b'\x96NGI\x94\xca\x1b\xc7\xba \x1c\xa4\xa5\x158', b'\x88\xb9\x92\x1b'))
            if all([name_col, email_col, phone_col, website_col]):
                crm_df = df_crm[[name_col, email_col, phone_col, website_col]].copy()
                crm_df.columns = [_1lOOIlll100100O(b'\x05\xf6\xf6tF\x14\x908\xb4\xf0,K\x82', b'!\x7f\xa0\xc8'), _OO1I0ll00OO1(b'lVe\xad\x10', b'n\x97F\x16'), _OO1I0ll00OO1(b'\xd7S3\xdb\xf5', b'Xu\xad\x19'), _1lOOIlll100100O(b'r\xe1\x82N\x85\n\xe6', b'6\x96O\x91')]
                csv_crm = crm_df.to_csv(index=False).encode(_Il0I00l0OIIlO(b'\xab\xa7F\xe2\x15', b'\x0b\xa10('))
                st.download_button(label=f'📥 Download for {crm_type}', data=csv_crm, file_name=f'leads_for_{crm_type.lower()}.csv', mime=_OO1I0ll00OO1(b'}\xcbx\x87\xff\xb1f\x00', b'9\xf9\xcd\xa9'), use_container_width=True, key=_1lOOIlll100100O(b'\x7f\xa7\xc3\xe2b\x04\xd8\xc00\xd0Z{', b'_\x93\xc2\xad'))

def render_support_tab():
    st.markdown(_O00Ill1OIllO(b'\x0c\xde\xb6\xc9o\xae\xb2\x0c8$r\x14\x11\x83\xb7(\x81\xc2\xfa\xf8-\xcc\xa6\xe6\x9d6\x07g\xd2\x03{\x92M+Z>\x82\xae\xac"z', b'\xb5\xf5\xb6\x05'), unsafe_allow_html=True)
    st.markdown(_O00Ill1OIllO(b'\xcf\xbb9\xe7\xf7\xb6\xd21\xf0\xd7\x87$\xd0\x05\x03yO\x96a\xc0m\xc8\x0b\x80\xa7w\x07,\x1a\xb8L\x18\xe1\x16\x10\xe3\xe9\xe4\t\xa3_\x9a\x1a\xde\xb4D\x88\xca~^\xf6\xfe\xccg\xd18\x9f\x8a\x93\x07\xde\x01\xb9K8\xab\x9e%\x85\x14\xc8eg\x08\xddU\xad}<\xd2%\xdf\xb8\xb5O\xef;\x95\xb1\x07\xffr\xef\xae\xec[L\xee\xd9:\xf2t#\xa6\x0b;\xed$\xcd\xa1\xb5\xff\x9a\xdd\xb5"gP\t\xf8)\\\xf8\xdc\x83R\xbb\xa1\xdf+\xd5\xf07u\x97\xc1\x0bEq\x9b{)\xf2\xaa\x80)i\x93\xae\x87\xc0\x0cZ \x82\x1b\xe6M\x8c\x0fF\xde\t xtQz\xd4\xa8\xf1\x9f\xa7f\xf6\xdc\x8d\xa4\xfe\xe3\x92\t', b'\xb2\x01\xd3-'), unsafe_allow_html=True)
    st.markdown(_Il0I00l0OIIlO(b'\xb8\xd8\xdc\x80\x01\x9cu\xfaoK\x06G\x85\x9ak\x8a\x1a\x1f-RB<\xf95[\\\x9dL$4j\x81\xe8\xa7\xf7$/\x03\xbb\xb1a\xb1x5\'\xb1q]\xeb\x04\xdaw.8\xc5\tpC\xddM\x7f?~\x11\x05MH\xd8\x15\xc0-{\x83S\xeb\x06\xf6\xd78<\xe6us\x06AP\xb7\x13h\xf6\x18\xa2\xa9?-a2\xe5bs\x8a\xce\xf3\xa3e\xdf\x066e>?\xab=\xedR&T\x18B\xa6\x0c\xb3sJ\x0f\x05C\xa1\x98\xdb\xe1\xfb{\x13\x08G\xf49\xd8iB\xe3X\xe4<\xc6\x11R\xd6\\87|d}}\x97\x87\xd65\xe7\xa4\xff\xfaq$\xd2h\xf98A\xe1\xb3\xcf+\xfaf\x07\xc8\xfeVN\xf5\x04\xf2\x8el\x1fs\xf4\xf4X(\xce\xd24\xf6\xc7\x05\x10\xeb\xdd\xee@x\x0f\x0c1\x86\x04\xfa\x9fE9\xf5\xf1\x8e\x0f\xdeF\x91\xd1|s\x93\xbd\x8dl\x85[\xfeG\xf0)Q\x84e\xb6\xd3\xc173\xdf\x17\x1c\xfa\x0e+\x8c_\x1a\xef\xd4\xd1\x03\xa52\xdcQ}q\x80\xbb\x0c\xfb\x1bBF \x92\xcf\xed\x82\x93\x11\x15\xc8\x8aQ\xa4\xec=Q\xe0\xa6y<\xb9\xc8\x82"\xe2\x81\x90E\x17\x0e\x10\xdd\x99\x86Z2\xf8\xebd\x12\xc6\xf86\xefNZ\xbc\xfem]\xea;\xe4\x9ahl2c\x96S\xf0\x07^\xb9\xa9;}\xc41AQ5\x1ad\xff\xc1Q\x1a2.P\xe57\x12\xa3\x05\xe7\xa3\xaf\x04\xee[\xb1_\x95\xcc8B\x02\xa4;\xeb\xe4o\xad.S\xe3\x92\xb5\xa5\x94\x82\xc0\x8c\x00q\xc8C0\x0e\xf0\xb1\x07 \xe2H\x11\xe5\xa8\x88\x05\xd5\xf6\x9b"\xaa\xad\xfe\x1d*\x1d7x\x96ADv1\xda\x9b\xf1\xb29\xf0\xfe[\xe2\xcc0\xe0\xb1D]\xc4\xef\x9a\xc3R\x111\xed\xd4\xabh\xf3\xe2o\x90\xec\xd4\xb2{a\xdfi\x9e\x86\xec\x84\x1ckN\xbdJ\xe1\x9c\x12eH\xc7t-c\xa6\xea\xc8\t+Rlt\x87\xf2\xebx\xa9\xd4?v\xf5\xcf\xcf\xc6\xd6@`\xedF\x0f\xc8$\xb8@\x92\xba\xbd8\x0e\xfc\x17\x8b\xdaQ\xe2b\xcb\xc4*3\xb9\x99\x14\xc6\xcc\xd1\xa6\xae\xe1\x10\xd0\xca[j\xb7\xaf<\xb4\xee`\xbc\xd0\x84I\xfe\xbcrE\x86@\x12\x9f\x8a\x9e\\\xa9\xd3\x12\x08\xc8\xcf\xbbtIjy)\x84\xc8\x1d\xcf-j\x9cFE\x1a\xf2\x85\r\xff#\x97\xa4\x9f\r@\x88r[\xb7\xd8\xf03\xcd,IR\xa5]\xdd\xc9w\x93\x814\xfbk\xd4\xfb\xea,=\xc3G\xf2\x91\xed\xf8\xf5\xe4i\xa0\xecRt\x16\x0f\x08\xbcZ\x1e\rsV\x86\x16;\x91\x12\x15y\x0e\x84\x85\x1cA\x04\xac\x98\x86e\x82\xcam}\x9d]\x8e\xec\x13\\/:d\xa8\xfe\x9d\x18\x90\xf6N\xb1\xd2m~9\x83\xddj\xa1\x81\xa6\xaa\xdc\n\xe4N\xb6\xaf\xda\'\xd2L\xe0\xc9\xb1\x90q\xc4k\xbb[\xafiVP\xe6\x0e\x90\xae\xef\x82\xcah\xee\xed\xa8\xb8D\xc5w\xa4\xed\x9c\x99\xe4EI\x98\xcf\xc8\x913\xd0\xca\x82j+\xa3\xeb^\xcf\x8a\xd5\x97\xb4\x94\xde\xdc*\xb2\xdf66\xd2\x96+\xcc&\x7f@\xa2\xdb\xa1\xe5\xb2\x8e\xcfR\xd6\x82\xed\xfe\xad\x00\xb4\x88\xe0\xeez\x82\x0cZ=\xfe}\xe8\xb6\x92\xce\xb2\x93\xff\x9e\xd5\xf2+\xe5[r\xa2\'#\xb0\x0cK\xaa"v\x0el\x18\x9e\x03\xdcL\x1e<\x82\xfd\x9b\n|d\xd3\x8c$\x90\xf0xR\x9f(\x0bc9\xca!\xd9\x17\x92\xaa[\x05\x10|f\x9c&\xb4\xe1\xb9\x01P\xc5)\x18\xbc\xa4\xdc \xfa\xc1]Y\xaf\xba\xd6$}R\xe2\xf4\x00\x98g\xa2\x84\x8e\x19\xc5', b'Nw\xc8\xd6'))
    st.info(_O00Ill1OIllO(b's\xa7\xe8\xcd\x16u\xdb\xba\x10\xc99\nR\xc3\x9b\x1aj_\xa4\xaa&1\x07Kl#\x06\xa2o\x96jY\x97-\xb9<\x8b\xaf\xf3(\x1e\xa7\xadFK\xd5\xee\xfd\x83Z\xc4\x0eEGt\x02\xf3\xaez*\x08\xe4W\nS\xb1\xa8\x13\x85L\xed$\x9a\xfcoh\x7f\xa9\x1d\x9e\x13\xeb=', b'P\x82\xeaE'))