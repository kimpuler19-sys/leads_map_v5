_OO11I0I1I0I0lII0lO = __import__('hashlib')
_l00II0II01 = 'https://pyobfuscate.com'
_III001OO10OlIII0 = _OO11I0I1I0I0lII0lO.sha256(_l00II0II01.encode('utf-8')).digest()

def _10000lOOOIIOOIlI(_III01O101OO1lO0lIO, _I01IlIII1l):
    _0OOII1I100O = bytearray()
    _l0OI1lIlII1I11OOO = 0
    while len(_0OOII1I100O) < _III01O101OO1lO0lIO:
        _0OOII1I100O += _OO11I0I1I0I0lII0lO.sha256(_I01IlIII1l + _l0OI1lIlII1I11OOO.to_bytes(8, 'big')).digest()
        _l0OI1lIlII1I11OOO += 1
    return bytes(_0OOII1I100O[:_III01O101OO1lO0lIO])
_IllIO110OOlOl0II11 = {}

def _llI0l01OIOl0I00Il(_OIlI0IOI10I101, _OOl0011lllOO111l0l):
    _OI01O1Ol0l01Il1 = (_OIlI0IOI10I101, _OOl0011lllOO111l0l)
    if _OI01O1Ol0l01Il1 in _IllIO110OOlOl0II11:
        return _IllIO110OOlOl0II11[_OI01O1Ol0l01Il1]
    _lOO1I0llOOO00OI0 = bytes((_0OO1l10O1Ol0OIl10 ^ _1IIOII0I1lII11Il10 for _0OO1l10O1Ol0OIl10, _1IIOII0I1lII11Il10 in zip(_OIlI0IOI10I101, _10000lOOOIIOOIlI(len(_OIlI0IOI10I101), _OOl0011lllOO111l0l + _III001OO10OlIII0)))).decode('utf-8', 'surrogatepass')
    _IllIO110OOlOl0II11[_OI01O1Ol0l01Il1] = _lOO1I0llOOO00OI0
    return _lOO1I0llOOO00OI0

def _10I00IOI1lO10(_I1OO1lI11lO, _OIl1II1IOOO0Il):
    _1IOlO11lI1011l0 = (_I1OO1lI11lO, _OIl1II1IOOO0Il)
    if _1IOlO11lI1011l0 in _IllIO110OOlOl0II11:
        return _IllIO110OOlOl0II11[_1IOlO11lI1011l0]
    _lIl11l0IOOIlIlllOl = bytes((_l1011lllll110l ^ _O1IlIOO0l10l0lO for _l1011lllll110l, _O1IlIOO0l10l0lO in zip(_I1OO1lI11lO, _10000lOOOIIOOIlI(len(_I1OO1lI11lO), _III001OO10OlIII0[::-1] + _OIl1II1IOOO0Il)))).decode('utf-8', 'surrogatepass')
    _IllIO110OOlOl0II11[_1IOlO11lI1011l0] = _lIl11l0IOOIlIlllOl
    return _lIl11l0IOOIlIlllOl

def _I010I1IIlIlO(_0II11llIlI, _OlI10lOOO00lO0O0):
    _II10lOOIO1llII = (_0II11llIlI, _OlI10lOOO00lO0O0)
    if _II10lOOIO1llII in _IllIO110OOlOl0II11:
        return _IllIO110OOlOl0II11[_II10lOOIO1llII]
    _I1llI0O101l = bytes((_IOOIOl0IlO00l1 ^ _O0lOOI10IOO0O0II0 for _IOOIOl0IlO00l1, _O0lOOI10IOO0O0II0 in zip(_0II11llIlI, _10000lOOOIIOOIlI(len(_0II11llIlI), _OO11I0I1I0I0lII0lO.sha256(_III001OO10OlIII0 + _OlI10lOOO00lO0O0).digest())))).decode('utf-8', 'surrogatepass')
    _IllIO110OOlOl0II11[_II10lOOIO1llII] = _I1llI0O101l
    return _I1llI0O101l
import streamlit as st
import pandas as pd
import requests
from groq import Groq
import os
from datetime import datetime, timedelta
import re
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import urllib.parse
import json
import hashlib
from bs4 import BeautifulSoup
from config import GROQ_API_KEY
from core_auth import safe_json_load, safe_json_save, load_company_profile, EMAIL_SETTINGS_FILE, FOLLOWUP_SETTINGS_FILE, CAMPAIGN_DATA_FILE, WHATSAPP_TEMPLATES_FILE, LANGUAGE_CONFIG, load_campaign_data, get_campaign_metrics, update_campaign_stats

def generate_personalized_message(company_profile, lead_data, message_type=_llI0l01OIOl0I00Il(b'\xb0\xe5\x0f\xe3\x98', b'\x17@\xce\x1a')):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        lead_name = lead_data.get(_10I00IOI1lO10(b'W\xfe@,G$\xf2\x10\xad\x9b\x97\xb8\x08', b'\xab,Q\x92'), _10I00IOI1lO10(b'\xbd32q\xa6O\xff\xfd', b'\x9ep\xc8\xd6'))
        lead_website = lead_data.get(_I010I1IIlIlO(b'\xb0+\x04\x94\xfe$\xa2', b'>4\xe8z'), _llI0l01OIOl0I00Il(b'\xc13es\xc6\xe6\xf8t\x89\xda', b'2\xefM_'))
        lead_rating = lead_data.get(_llI0l01OIOl0I00Il(b'P>\x94\xf3\xc7\xd3', b'\xc8\xc6\x10$'), _10I00IOI1lO10(b')\xc9\xfd', b'\xb2\xc8\xfe<'))
        if message_type == _I010I1IIlIlO(b'\xfe&\xaf\xd2\xd5', b'<\xd7u8'):
            prompt = f"\n            Act as a professional sales representative from {company_profile['company_name']}.\n            \n            COMPANY PROFILE:\n            - Company: {company_profile['company_name']}\n            - Product: {company_profile['product_name']}\n            - Description: {company_profile['product_description']}\n            - Special Offer: {company_profile['special_offer']}\n            - Call to Action: {company_profile['call_to_action']}\n            - Tagline: {company_profile['company_tagline']}\n            \n            LEAD DETAILS:\n            - Business Name: {lead_name}\n            - Website: {lead_website}\n            - Rating: {lead_rating}\n            \n            Create a professional, persuasive cold email with:\n            1. Subject Line (first line)\n            2. Personalized greeting using the business name\n            3. Brief introduction about {company_profile['company_name']}\n            4. Explain how {company_profile['product_name']} helps businesses like {lead_name}\n            5. Mention the special offer: {company_profile['special_offer']}\n            6. Clear call to action: {company_profile['call_to_action']}\n            7. Professional signature with sender name and company\n            \n            Make it sound natural, not like a template. Keep it concise and actionable.\n            "
        elif message_type == _llI0l01OIOl0I00Il(b'b\x876\x06\xb9K\xfd\x1a', b'\x12\xed\x97\xa7'):
            prompt = f"\n            Act as a friendly sales representative from {company_profile['company_name']}.\n            \n            COMPANY PROFILE:\n            - Company: {company_profile['company_name']}\n            - Product: {company_profile['product_name']}\n            - Special Offer: {company_profile['special_offer']}\n            - Call to Action: {company_profile['call_to_action']}\n            \n            LEAD DETAILS:\n            - Business Name: {lead_name}\n            - Website: {lead_website}\n            \n            Create a short, friendly WhatsApp message (1-3 sentences) that:\n            1. Greets the business by name\n            2. Introduces {company_profile['product_name']} briefly\n            3. Mentions the special offer: {company_profile['special_offer']}\n            4. Ends with a clear, simple call to action\n            \n            Keep it casual and conversational, not spammy.\n            "
        elif message_type == _llI0l01OIOl0I00Il(b'2Re2$tY\xd4', b'\x05\x99R\x04'):
            prompt = f"\n            Act as a professional sales representative from {company_profile['company_name']}.\n            \n            COMPANY PROFILE:\n            - Company: {company_profile['company_name']}\n            - Product: {company_profile['product_name']}\n            - Special Offer: {company_profile['special_offer']}\n            - Call to Action: {company_profile['call_to_action']}\n            \n            LEAD DETAILS:\n            - Business Name: {lead_name}\n            \n            Create a short, polite follow-up message that:\n            1. References the previous outreach\n            2. Asks if they had a chance to consider {company_profile['product_name']}\n            3. Reiterates the special offer\n            4. Includes a soft call to action\n            \n            Keep it warm and professional, not pushy.\n            "
        completion = client.chat.completions.create(model=_I010I1IIlIlO(b'\x80\xc5\x18\x14\x834\x04\t\x89\xa2M\xbc[\xbdd\x820\x97LO', b'\xd2\xdd\xab\xd8'), messages=[{_I010I1IIlIlO(b"\x82'(\xb9", b'k\xf6N\xbc'): _10I00IOI1lO10(b'\xf5\xbe\xe3\xd2', b'\xc6\x8a$\xfb'), _I010I1IIlIlO(b'\xd3\x0b\x10\xd9\x05\xc4H', b'\xe0\x9a\x1cF'): prompt}], temperature=0.7, max_tokens=1221289354 ^ 1221289126 if message_type == _llI0l01OIOl0I00Il(b'\xb9\xe6\x0f;\xc6', b'G+u\xe4') else 362393313 ^ 362393207)
        return completion.choices[791516153 ^ 791516153].message.content.strip()
    except Exception as e:
        return generate_fallback_message(company_profile, lead_data, message_type)

def generate_fallback_message(company_profile, lead_data, message_type=_llI0l01OIOl0I00Il(b'6M\x03\xb1\x12', b'P\xe3\x1c\xcf')):
    lead_name = lead_data.get(_10I00IOI1lO10(b'\x13\xc0\xbb-\xaaZN%.\xe1w1\xb6', b'\x14\xb4;2'), _llI0l01OIOl0I00Il(b"2dr'v\x96\xbe\xcf", b'FH\x02\xf8'))
    if message_type == _llI0l01OIOl0I00Il(b']-\xf9\xe1\xdb', b'\xce5\xcb?'):
        return f"Subject: Grow Your Business with {company_profile['product_name']}\n\nDear {lead_name} Team,\n\nI hope this email finds you well. I'm reaching out from {company_profile['company_name']} to introduce our {company_profile['product_name']} solution.\n\nWe help businesses like yours grow by {company_profile['product_description']}. \n\nAs a special offer, we're providing {company_profile['special_offer']}.\n\nWould you be available for a brief call to discuss how we can help {lead_name} grow?\n\nBest regards,\n{company_profile['sender_name']}\n{company_profile['company_name']}\n{company_profile['company_phone']}\n{company_profile['company_email']}"
    elif message_type == _10I00IOI1lO10(b'I\xa6\xddp6\x91\xa4#', b'\xd1w\x8c\x1b'):
        return f"Hi {lead_name}! This is {company_profile['sender_name']} from {company_profile['company_name']}. We help businesses grow with {company_profile['product_name']}. Special offer: {company_profile['special_offer']}. {company_profile['call_to_action']}"
    else:
        return f"Hi {lead_name}! Following up on my previous message about {company_profile['product_name']}. Just wanted to check if you had any questions. We're still offering {company_profile['special_offer']}. Let me know if you're interested!"

def generate_ai_email_with_profile(company_profile, lead_data):
    return generate_personalized_message(company_profile, lead_data, _I010I1IIlIlO(b'\x01),\x85\x17', b'S}\xfa\x86'))

def generate_ai_whatsapp_with_profile(company_profile, lead_data):
    return generate_personalized_message(company_profile, lead_data, _llI0l01OIOl0I00Il(b'\xc2\xb8p\x04\xe4:0\r', b'\x89\xa0\x99\xd3'))

def generate_followup_with_profile(company_profile, lead_data):
    return generate_personalized_message(company_profile, lead_data, _10I00IOI1lO10(b'i\xea\xea\x0f\xeb\x1cG*', b'\x96\xb8\xec\xff'))

def process_all_messages_with_profile(company_profile, results, message_type=_I010I1IIlIlO(b'an\x91!C', b'\xa3o\x01\xaf'), progress_callback=None):
    from core_scraping import calculate_lead_score, get_priority_from_score
    total_data = len(results)
    for index, item in enumerate(results):
        if progress_callback:
            progress_callback(index, total_data)
        if message_type == _10I00IOI1lO10(b'L\x92\xfd\xd9\xac', b'R\xa4S\xbd'):
            message = generate_ai_email_with_profile(company_profile, item)
            item[_llI0l01OIOl0I00Il(b'\xa9 \xea\xcd\xfa/>\x914FZ!\xbf\xcdn\x9e\xfb@N3\x94%4', b'\xd0h\xae\xf2')] = message
        elif message_type == _I010I1IIlIlO(b':\xbb\xf4>\xf6\xe2FN', b'g\x1bt)'):
            message = generate_ai_whatsapp_with_profile(company_profile, item)
            item[_10I00IOI1lO10(b'\xec\xc3k\xc4\x18\xd5\x9b\xd2\x01p\xd7\x02\x1a\xdb\xcaP', b'\x02\xfe\xf5\x04')] = message
        elif message_type == _llI0l01OIOl0I00Il(b'\x8biq\xb1\x16\xd7E\xa6', b'h\x1a\xa4\xb2'):
            message = generate_followup_with_profile(company_profile, item)
            item[_llI0l01OIOl0I00Il(b'Z\x05dK\xa9\x9c\xd7\xa6k\x99m\x9ffuj\xa8u', b'\xe2Y\x8a\xf8')] = message
        item[_I010I1IIlIlO(b'}\xeba\x96`\xe2\xd6O\xdb\x12', b';\xda\x91\x94')] = calculate_lead_score(item)
        item[_10I00IOI1lO10(b'M \x0b\xf5\xa7#O\xb6', b'\xa5\xab\xdf\xa5')] = get_priority_from_score(item[_10I00IOI1lO10(b'T\xdc\xa7)f\xb3\xc2\x18\x91K', b'\xa8\xc9\xd8-')])
        time.sleep(0.3)
    return results

def get_available_languages():
    return [(key, f"{value['flag']} {value['name']} ({value['region']})") for key, value in LANGUAGE_CONFIG.items()]

def generate_multilingual_message(company_profile, lead_data, target_language=_10I00IOI1lO10(b"\x8c'\xbd\x99\x16L\xe9", b'\xd8W\xf6"'), message_type=_I010I1IIlIlO(b'\xf8\x19\xdf\\\xb1', b'\xb1~\xfc0')):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        lead_name = lead_data.get(_10I00IOI1lO10(b'\x86\xe7%9\xe8Dd\x02B\xa2\xb8\x02\x1c', b'\x94\x81YU'), _10I00IOI1lO10(b'>c\xca_Z\x04&\x84', b'\x9f\x8eA\x17'))
        lead_website = lead_data.get(_I010I1IIlIlO(b'\xd0\x15@\xc4\x1c5\x87', b',\xf5\\\xd6'), _llI0l01OIOl0I00Il(b'\x18\xbc\xde\xad\xbbwh\x01\x02q', b'Cqp='))
        lead_rating = lead_data.get(_10I00IOI1lO10(b' \xba\x8f,(\x99', b'\xc2\xa6\x97\x85'), _10I00IOI1lO10(b'\xdfE\x11', b'\xea\x98\tG'))
        lang_info = LANGUAGE_CONFIG.get(target_language, LANGUAGE_CONFIG[_I010I1IIlIlO(b':\xff\x18eGb\xb4', b'\x1a\xab\xf8\xbb')])
        lang_name = lang_info[_llI0l01OIOl0I00Il(b'\x85\xcb\x98\x1c', b'\xe4\x8f\x9c\x90')]
        lang_code = lang_info[_I010I1IIlIlO(b'\x1a\x0e}\xce', b'\r\xdd\xf3\x86')]
        if message_type == _llI0l01OIOl0I00Il(b'8\xcb=\xa5x', b'\xe1\xdcT\xb2'):
            prompt = f"\n            Act as a professional sales representative from {company_profile['company_name']}.\n            \n            COMPANY PROFILE:\n            - Company: {company_profile['company_name']}\n            - Product: {company_profile['product_name']}\n            - Description: {company_profile['product_description']}\n            - Special Offer: {company_profile['special_offer']}\n            - Call to Action: {company_profile['call_to_action']}\n            - Tagline: {company_profile['company_tagline']}\n            \n            LEAD DETAILS:\n            - Business Name: {lead_name}\n            - Website: {lead_website}\n            - Rating: {lead_rating}\n            \n            TARGET LANGUAGE: {lang_name} (Language Code: {lang_code})\n            \n            Create a professional, persuasive cold email in {lang_name} language with:\n            1. Subject Line (first line) in {lang_name}\n            2. Personalized greeting using the business name in {lang_name}\n            3. Brief introduction about {company_profile['company_name']} in {lang_name}\n            4. Explain how {company_profile['product_name']} helps businesses like {lead_name} in {lang_name}\n            5. Mention the special offer: {company_profile['special_offer']} in {lang_name}\n            6. Clear call to action: {company_profile['call_to_action']} in {lang_name}\n            7. Professional signature with sender name and company in {lang_name}\n            \n            Make it sound natural and culturally appropriate for {lang_name} speakers.\n            Use appropriate formal/informal tone for the culture.\n            Keep it concise and actionable.\n            \n            Return ONLY the email content in {lang_name}, nothing else.\n            "
        elif message_type == _10I00IOI1lO10(b"\x1b*\x84\x1c'o)\x18", b'\xedo{\xaf'):
            prompt = f"\n            Act as a friendly sales representative from {company_profile['company_name']}.\n            \n            COMPANY PROFILE:\n            - Company: {company_profile['company_name']}\n            - Product: {company_profile['product_name']}\n            - Special Offer: {company_profile['special_offer']}\n            - Call to Action: {company_profile['call_to_action']}\n            \n            LEAD DETAILS:\n            - Business Name: {lead_name}\n            - Website: {lead_website}\n            \n            TARGET LANGUAGE: {lang_name} (Language Code: {lang_code})\n            \n            Create a short, friendly WhatsApp message in {lang_name} language (1-3 sentences) that:\n            1. Greets the business by name in {lang_name}\n            2. Introduces {company_profile['product_name']} briefly in {lang_name}\n            3. Mentions the special offer: {company_profile['special_offer']} in {lang_name}\n            4. Ends with a clear, simple call to action in {lang_name}\n            \n            Keep it casual and conversational, not spammy.\n            Make it culturally appropriate for {lang_name} speakers.\n            \n            Return ONLY the message in {lang_name}, nothing else.\n            "
        elif message_type == _llI0l01OIOl0I00Il(b'\xa5u\x84\xc64\xe0\x1b=', b'%\x14/\x01'):
            prompt = f"\n            Act as a professional sales representative from {company_profile['company_name']}.\n            \n            COMPANY PROFILE:\n            - Company: {company_profile['company_name']}\n            - Product: {company_profile['product_name']}\n            - Special Offer: {company_profile['special_offer']}\n            - Call to Action: {company_profile['call_to_action']}\n            \n            LEAD DETAILS:\n            - Business Name: {lead_name}\n            \n            TARGET LANGUAGE: {lang_name} (Language Code: {lang_code})\n            \n            Create a short, polite follow-up message in {lang_name} language that:\n            1. References the previous outreach in {lang_name}\n            2. Asks if they had a chance to consider {company_profile['product_name']} in {lang_name}\n            3. Reiterates the special offer in {lang_name}\n            4. Includes a soft call to action in {lang_name}\n            \n            Keep it warm and professional, not pushy.\n            Make it culturally appropriate for {lang_name} speakers.\n            \n            Return ONLY the message in {lang_name}, nothing else.\n            "
        completion = client.chat.completions.create(model=_10I00IOI1lO10(b'l\x94]J\xa7\xb3~:\xb2\xb7\xeb\x15\x03J\x91\x1e3\xd0\x82n', b'k\x03\xe6\xbb'), messages=[{_I010I1IIlIlO(b'\x90C\x03\xf0', b'\xcb\xac\x90\xd2'): _10I00IOI1lO10(b'=\x93\x08~', b'\x187w4'), _I010I1IIlIlO(b'\xee\xfe\xea,I"}', b'\x82\x04"\xc9'): prompt}], temperature=0.7, max_tokens=1600492612 ^ 1600493012 if message_type == _I010I1IIlIlO(b'\x83\xf6\xd1\x85\x90', b'\xb6\n\x81\x19') else 1365562096 ^ 1365561912)
        return completion.choices[583964265 ^ 583964265].message.content.strip()
    except Exception as e:
        return generate_multilingual_fallback(company_profile, lead_data, target_language, message_type)

def generate_multilingual_fallback(company_profile, lead_data, target_language, message_type=_10I00IOI1lO10(b';\xaf\xc1h\x03', b'\x8b\x1e\xf4!')):
    lead_name = lead_data.get(_10I00IOI1lO10(b'b\xa9\xcd=\xf5\xc3\xeb\xfem\xcc,a\xf4', b'\x929\xdbu'), _10I00IOI1lO10(b'\xb4\x82\x04\x1bN\x8cA8', b'\x07q\x9d\xf5'))
    lang_info = LANGUAGE_CONFIG.get(target_language, LANGUAGE_CONFIG[_llI0l01OIOl0I00Il(b'\x05\x89g\xe4b\xa9\x1c', b'\xef\xf4^b')])
    if message_type == _llI0l01OIOl0I00Il(b'P\xd8\x10\n\xda', b'hY\xae\xa8'):
        return f"Subject: Grow Your Business with {company_profile['product_name']} [{lang_info['flag']} {lang_info['name']}]\n\n{lang_info['formal']} {lead_name} Team,\n\nI hope this email finds you well. I'm reaching out from {company_profile['company_name']} to introduce our {company_profile['product_name']} solution.\n\nWe help businesses like yours grow by {company_profile['product_description']}. \n\nAs a special offer, we're providing {company_profile['special_offer']}.\n\nWould you be available for a brief call to discuss how we can help {lead_name} grow?\n\n{lang_info['signoff']},\n{company_profile['sender_name']}\n{company_profile['company_name']}\n{company_profile['company_phone']}\n{company_profile['company_email']}"
    elif message_type == _10I00IOI1lO10(b'"]\xdaS/v\xf2p', b'\xdeMy?'):
        return f"{lang_info['greeting']} {lead_name}! This is {company_profile['sender_name']} from {company_profile['company_name']}. We help businesses grow with {company_profile['product_name']}. Special offer: {company_profile['special_offer']}. {company_profile['call_to_action']} [{lang_info['flag']}]"
    else:
        return f"{lang_info['greeting']} {lead_name}! Following up on my previous message about {company_profile['product_name']}. Just wanted to check if you had any questions. We're still offering {company_profile['special_offer']}. Let me know if you're interested! [{lang_info['flag']}]"

def process_multilingual_messages(company_profile, results, target_language=_llI0l01OIOl0I00Il(b'j"\xa6\'\xc1\x10\xf5', b'\xa5\xab`\xd6'), message_type=_I010I1IIlIlO(b'^/J\x0b\x12', b'\xa1}\xc6\xd1'), progress_callback=None):
    from core_scraping import calculate_lead_score, get_priority_from_score
    total_data = len(results)
    for index, item in enumerate(results):
        if progress_callback:
            progress_callback(index, total_data)
        message = generate_multilingual_message(company_profile, item, target_language, message_type)
        if message_type == _I010I1IIlIlO(b'\x8f\xfcl-\x8c', b'\x8fk/\xff'):
            item[_llI0l01OIOl0I00Il(b'\x14\xf7\x13s\ni4b\x0f\x00\xc3\xe6\x8fzH\x14\x90\xb0\xee\xbb=~\xec', b'/\xf4\x01]')] = message
        elif message_type == _10I00IOI1lO10(b'\xe0\xc4\xa8,\xfc\xac_i', b'\xa6\xe6\xb54'):
            item[_10I00IOI1lO10(b'\xa5\xd5o\xa9\xdb\xeb\x04\xc2\x8d\xb3L\x98\x11\xecA~', b']\x01\xdd\x90')] = message
        elif message_type == _10I00IOI1lO10(b'\x17\xf4\xe0?\xaf[[2', b'Cv\xf7c'):
            item[_llI0l01OIOl0I00Il(b'1 \x1crz\xfc\xb9\xb7\xb7?\xaa\xba\xbf/\xfc\x1d&', b'\x87\xaa\xbc\x83')] = message
        item[_llI0l01OIOl0I00Il(b'mJ\xe5\x86{\xe83\xb5', b'\x08;\xb1\xd8')] = LANGUAGE_CONFIG.get(target_language, LANGUAGE_CONFIG[_llI0l01OIOl0I00Il(b'\xf6d4\xe6<\xf0Q', b'\xd8\xad0\x17')])[_10I00IOI1lO10(b'\t\xfaD\xa0', b'\\\x1e\x17\x1e')]
        item[_llI0l01OIOl0I00Il(b'\xa5H\xd3M\xb9\xb8\xda\x8d\x89\x0b_E\x03', b'|\x8a\xd1Y')] = target_language
        item[_llI0l01OIOl0I00Il(b'\xb5\xffSL\xecE\xdcI\x1ba', b'\xd2\xc8\xb8\x1f')] = calculate_lead_score(item)
        item[_10I00IOI1lO10(b'Q\xf2\x11\xa1)\x9fu5', b'=\xa6\xae\x05')] = get_priority_from_score(item[_llI0l01OIOl0I00Il(b'\xcew\x81j\x9eQ\xbd\xf6|V', b'?D\xb4\xc1')])
        time.sleep(0.3)
    return results

def enrich_lead_with_website(business_name, website_url, business_details=_I010I1IIlIlO(b'', b'\xedI\xf1\xf4')):
    if not website_url or website_url == _10I00IOI1lO10(b'\xc2\x9c\x04jU\xac\xcbb\xc1\xd9', b'\x83\xea\xf2\x16'):
        return {_10I00IOI1lO10(b'\xa0\xbc4\xf0\xa5\xb3Z\x14', b'\xd6b\x8d\x92'): _10I00IOI1lO10(b'3\xc3\xd8R\xac\x9d\xdb', b'\x91\x9bA8'), _llI0l01OIOl0I00Il(b' f\xbc\xaa\xab{I>\x00', b'\xc1\xe3=\xac'): _10I00IOI1lO10(b'\x9a\x93|\xd8\x02x\x8b', b'\x8d\xbb/\xbb'), _llI0l01OIOl0I00Il(b'T\x96\t\x07\xa1\x80\x1e', b'N\xae\xa1\xce'): _10I00IOI1lO10(b'\x9f14\xfb=)\x92', b'5du\x1c'), _I010I1IIlIlO(b'\x9ce1\x01"\xb4\x15AP\xd4\xb0', b'\x1c\xb7\xfa\xe8'): [_I010I1IIlIlO(b';7\xbfiS+\xfb', b'\xc7\xe1\xf5g')], _llI0l01OIOl0I00Il(b'\x8c\xb4^kTM\xf0\xe2\xce5', b'\x1c\x89\xbb\xf3'): [_I010I1IIlIlO(b'\xc3\x04\x94\xf2\xd6\t\xcf', b'&\x88\xd8p')], _10I00IOI1lO10(b'\n\xd1\x83-\x83\xe0\xe1\xd4Ld\x9ay', b'*?\x8b\xdd'): {}}
    try:
        headers = {_10I00IOI1lO10(b'v}>Y\x14p\xec,4\xab', b'v\xd4;\xeb'): _I010I1IIlIlO(b"\x11]Q\xa5\x18\xce\x8ao\xb5\xe7O\x1fd \xe2\x8c6\xf3\xb2\xf3o\x13\xb7N\xbf\xe4\xda:'\x86a\xa5\x9d/\x07\xbc\\^\xfc\x14_\x0fC\xc7e\x9aF\x18\xa4\xc5\xad\x85ER)\x99\xc9\x0b\xdf\xa6", b'\xa9\xd6c\x0f')}
        response = requests.get(website_url, headers=headers, timeout=1395497832 ^ 1395497826)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, _I010I1IIlIlO(b'\xae\xc4\n AM\xfd?A\x14\xe9', b'=\xa1\x02z'))
        for script in soup([_10I00IOI1lO10(b'\\\x19-\x10S\x88', b'\xd3\xa4\xf9%'), _I010I1IIlIlO(b'\xf3\x83\xb5S\xfd', b'\xe5\xe9\xeb\x1f')]):
            script.decompose()
        text_content = soup.get_text()
        text_content = _10I00IOI1lO10(b'Y', b'\xd6\t`\x1c').join(text_content.split())
        text_content = text_content[:1448938252 ^ 1448940620]
        client = Groq(api_key=GROQ_API_KEY)
        prompt = f'\n        Analyze this business website content and extract the following information:\n        \n        Business Name: {business_name}\n        Website: {website_url}\n        \n        Website Content:\n        {text_content}\n        \n        Please provide a JSON-like response with these fields:\n        1. industry: (e.g., "Restaurant", "Tech", "Healthcare")\n        2. employees: (estimate: "1-10", "11-50", "51-200", "200+")\n        3. revenue: (estimate: "<$100k", "$100k-$500k", "$500k-$1M", "$1M+")\n        4. pain_points: (list of 3-5 potential pain points)\n        5. tech_stack: (list of technologies they might be using)\n        6. social_media: (dict with platforms and handles if found)\n        7. content_quality: (score 1-10)\n        8. mobile_friendly: (Yes/No)\n        9. seo_score: (estimate 1-10)\n        \n        Return ONLY valid JSON format.\n        '
        completion = client.chat.completions.create(model=_llI0l01OIOl0I00Il(b'8\xb2\xe3\x95>+\xb8\x189@V"M\x9f\x87\x91\x1e-\xa6\x05', b'\x03\xce\x1c7'), messages=[{_llI0l01OIOl0I00Il(b';\x1b\\\xc7', b'\xaf\xd7\xe9Q'): _I010I1IIlIlO(b'\xd5\x91\x8c\xab', b'P9\xcd\xa1'), _10I00IOI1lO10(b'&\x01\x84U\x8a\xf3\xd3', b'\x94u\xee@'): prompt}], temperature=0.3, max_tokens=1721002798 ^ 1721002498)
        response_text = completion.choices[1670962203 ^ 1670962203].message.content.strip()
        try:
            json_match = re.search(_10I00IOI1lO10(b'\xa09\x81Ck\x86', b'\xb3LR{'), response_text, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass
        return {_I010I1IIlIlO(b'\xda)\xe1!|\x10\x04#', b'\xab\x8f\xe4\xa5'): _llI0l01OIOl0I00Il(b'\xc1\x87\xe3\xce\xca\x87)1', b'r\xd3(e'), _llI0l01OIOl0I00Il(b'7v\xc5\xa0\xc7M\x84Hh', b'\xa7\xf1x\xb8'): _llI0l01OIOl0I00Il(b'\xdbu\xf4\x14A\xd2\xf5', b'\xf3\t\x10\xec'), _llI0l01OIOl0I00Il(b'\x8f szc\xe0\x84', b'\xa3Y]f'): _10I00IOI1lO10(b'|E#\xaf\xce\xe6\xa8', b'!\xabr\xa5'), _10I00IOI1lO10(b'\xaa\xe1\xf1{{Z\x1a\xb1S\x87=', b'\x10\xd7\x1bx'): [_llI0l01OIOl0I00Il(b'\x87\x06\x8a\x0eI\x9b\x01', b'f\xf2\xdd\xb4')], _I010I1IIlIlO(b"{\xa7'?\x97Y{\x1a\xcf\x90", b'6\xdc\x8a\x0c'): [_I010I1IIlIlO(b'k\xbc==\x92\x01;', b'!\xc9M\x9e')], _llI0l01OIOl0I00Il(b'\xbb/^Q\xd7%\x84*\xae\xa8y{', b'\xdcuS\x83'): {}, _10I00IOI1lO10(b'*\xa4\xceQ/P\xa6\x9f(\x12>Kq\xa1t', b'\xfa\xf5\xce\xd5'): 291542583 ^ 291542578, _10I00IOI1lO10(b"\xaf(\xcb'G\xdcE\x97\x089\x84\x03\t\xdb\x02", b'\\\xc7<\xef'): _llI0l01OIOl0I00Il(b'U\xa1\x00\x9b_0P', b'\xc0\xec\xa1W'), _llI0l01OIOl0I00Il(b'OKk\xbd\xa3\x87 \xe5\xd9', b'{!\xd22'): 158677439 ^ 158677434}
    except Exception as e:
        return {_10I00IOI1lO10(b"\xceU'd3\xa2\xa7\xc2", b'\x83\xd7\x02\xd8'): _10I00IOI1lO10(b'\xab\xf8^\x0ch', b'\xfca\xf90'), _I010I1IIlIlO(b'U\xe03\xc5\xa4W\xa3\xa4\xbd', b'\xce\x00\x11b'): _10I00IOI1lO10(b'?\x88\xd2\x99$', b't\xd9\xf4\x10'), _llI0l01OIOl0I00Il(b'\xce\xd7Qtug<', b'u\xd2\xec\t'): _I010I1IIlIlO(b'\x08\xabJ\x7fm', b' d[\xdd'), _I010I1IIlIlO(b'\xeb\xa7\xa5H\xd8\xd72\xed\x10\xb5G', b'\xa0V1\xe6'): [_10I00IOI1lO10(b'+\x0f\x90<\x1a', b'\xa5B~\x03')], _llI0l01OIOl0I00Il(b'I\x01}\x14\\9\xb0+\x15s', b'\xaa\x8a\x12B'): [_I010I1IIlIlO(b'N\r\xa9\xea\xcc', b'\x10\x8a\x1e\xce')], _I010I1IIlIlO(b'jL<\xf2\xfcC\xc5\xcb]\np\xbe', b'\xa7\xbf\xb4!'): {}, _I010I1IIlIlO(b'T\xb8BP\x1a', b'Q\x8er\xcc'): str(e)}

def enrich_multiple_leads(leads_df, progress_callback=None):
    enriched_data = []
    total = len(leads_df)
    for idx, row in leads_df.iterrows():
        if progress_callback:
            progress_callback(idx, total)
        business_name = row.get(_10I00IOI1lO10(b'\x89E\xc4@{6\xf1\xf9\xeam*\xd6\xea', b'\xd0\xf7\x14\xe4'), _10I00IOI1lO10(b'', b'p\x8c\xdbk'))
        website = row.get(_llI0l01OIOl0I00Il(b'A}\xd4\x90\xaa\xe0\x1f', b'fd\x02='), _I010I1IIlIlO(b'', b'}\x0c\xcb`'))
        if website and website != _10I00IOI1lO10(b'\xa27P\x01\xec\x974\x98\x18\xa4', b'\x83n\xf0\x14') and (website != _I010I1IIlIlO(b"\x9c>\x15\xb1\xb9;N\x00'\xfe\x04B\xba\x14\xce\xb4g\x08\x9e", b'\x8a\xce9\xc5')):
            enrichment = enrich_lead_with_website(business_name, website, f"Address: {row.get('Address', '')}, Rating: {row.get('Rating', '')}")
        else:
            enrichment = {_10I00IOI1lO10(b'[\x81\xef\n\x04~\xb6\xd7', b'\xa2\x94}\xa0'): _I010I1IIlIlO(b'\xf5Y0I\xedz9\xe5M\x91', b"\x06\xa8\xa3'"), _I010I1IIlIlO(b'\x16\x14\x8d\x90\xd4\x1d7m\x8d', b'{\xaeYG'): _llI0l01OIOl0I00Il(b'\x80\xfa\xb4\xc0\xc4\x10W\xa6\xf3\xa4', b'\n\x11\xdb\xee'), _llI0l01OIOl0I00Il(b'mn\x96\xd2A\xf6\x07', b"\xc5S'_"): _10I00IOI1lO10(b"\xe8'\\\x0eK\xff\x8a\xfaJy", b'\xb7\x82A9'), _10I00IOI1lO10(b'\x99\xa3^\x00E\xb7y.B.\xde', b'\xb8\xf3\x8f\xde'): [_llI0l01OIOl0I00Il(b'7\x1c\xa6\xf2\x1e\xe7\n1s<', b'\x8e\x9e\xf5(')], _llI0l01OIOl0I00Il(b'\x7f\xb1\xbbM\x18y\xf2\xa9`U', b'\xbd\xc8\x12\x18'): [_llI0l01OIOl0I00Il(b')tUf\xd5-\x86K\x96\x08', b'v\xdci\xc6')], _llI0l01OIOl0I00Il(b'\x86\x8c\xe04\xb8\x11\xac\t?\x97\x90b', b'\xc5w\xb3\xfd'): {}}
        enriched_data.append({_llI0l01OIOl0I00Il(b'0+\xb0\xf5gaNu>\x1d\x1f\xd4I', b'\xc86\x17\xff'): business_name, _10I00IOI1lO10(b'\xa07r\xc1J\xaf\xa6\xe9', b'\x94C\xdbY'): enrichment.get(_I010I1IIlIlO(b'\xdf\x9c\xf7\x05\xed\x19b\xc4', b'<\xb34P'), _I010I1IIlIlO(b'IX#Z\xf3\xea\x8b', b'\xe3\x0b\xf0e')), _10I00IOI1lO10(b'\x89\x1bi\xec\x1aE\xc25h', b'\xb3d\x98\x83'): enrichment.get(_10I00IOI1lO10(b'+A\xecub\xb4hW\x89', b'\x9b\xcc\xc4\x7f'), _10I00IOI1lO10(b'<q\xf7\xcc\x9f])', b'\xa2\xdf,|')), _llI0l01OIOl0I00Il(b'\xbb\xf9\x8f$I\xd2\xcd', b'F]\x1bU'): enrichment.get(_10I00IOI1lO10(b"eu\xc4\xfa'W/", b'\x1e\xb2\xf3x'), _llI0l01OIOl0I00Il(b'\xd7\xcb\xef\xaau\xc8\xaf', b'Q\xc2 c')), _llI0l01OIOl0I00Il(b'\x06\x9b\xa1y\xbf\xd2\xa3\xb2\x9a \x19', b'\x0f\xcd\xe3\xbd'): _llI0l01OIOl0I00Il(b'#\xa6', b'Hl\xfc\x14').join(enrichment.get(_I010I1IIlIlO(b'\xb0\x1c~\x88\x019|\x82\x0c^\xf6', b'\xad\xa1\xd8-'), [_llI0l01OIOl0I00Il(b'\xce\x1bo,\xee\xc2+', b'\x9c\xc7\x9a;')])[:1654154816 ^ 1654154819]), _10I00IOI1lO10(b'\xc2\xe6\x9c\x87y\xe2\xb3\x04\xcdx', b'4}\x17\xed'): _10I00IOI1lO10(b'\x88\x91', b'\xf4\xee\xb9\xea').join(enrichment.get(_I010I1IIlIlO(b')Z0t\x1c=\xb8\xc7F6', b'X\xea\xc9\xd7'), [_I010I1IIlIlO(b'\x88\xdb\xf4\xd6\xc9\xc8\xb3', b'w\xc1\x98\x1d')])[:865456438 ^ 865456437]), _10I00IOI1lO10(b'P\x89\xa0\xd7\x90\x9b\x9f\x97\xd1\x9dYqb\x9b\xef', b'\xac\x9b\xd2\xf2'): enrichment.get(_10I00IOI1lO10(b'\x02\xa7vs\xbdx\xf4\x04Z&a\xa0\x8ft\x97', b'\xd3\x0c\x1d.'), 1125470755 ^ 1125470755), _I010I1IIlIlO(b'\xfcx\xfb\r?\xe0iz\r%\x0b3\xa0\x03/', b'D\xa0H>'): enrichment.get(_llI0l01OIOl0I00Il(b"\x8e\x8b./\xcd\xd7\xaa)d\xcf\x07P\x1e'\x87", b'1))\xe4'), _I010I1IIlIlO(b'\x7f\xc3\xf8E d\x98', b'r\xc3H[')), _I010I1IIlIlO(b'\x1eG\xf1.\xdc\x04\xf7\x01\xee', b'b\x8c#\x12'): enrichment.get(_I010I1IIlIlO(b'\xf6rB@\x8bM\x0e\x90\xba', b'\xacAE\xe4'), 981708986 ^ 981708986)})
        time.sleep(0.5)
    return pd.DataFrame(enriched_data)

def generate_whatsapp_message(business_name, phone, message_template, business_details=_I010I1IIlIlO(b'', b'}\xe0\x9f\x87')):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        prompt = f"\n        Act as an expert sales representative. Create a unique, personalized WhatsApp message for a business named '{business_name}'.\n        \n        Base message template (use this as inspiration, but make it unique):\n        {message_template}\n        \n        Business Details:\n        - Name: {business_name}\n        - Phone: {phone}\n        - {business_details}\n        \n        Requirements:\n        1. Keep it short and concise (1-3 sentences max)\n        2. Start with a warm greeting using the business name\n        3. Make it sound natural and conversational\n        4. Include a clear call-to-action\n        5. Do NOT use generic placeholders\n        6. Make it unique for each business\n        7. Keep the tone professional but friendly\n        8. Include a specific reason why you're reaching out\n        \n        Return ONLY the WhatsApp message text, nothing else.\n        "
        completion = client.chat.completions.create(model=_I010I1IIlIlO(b'\xc7\xb4\xb5\xfc\xd2J\xa7\xa5|\xb21Zj$\xbb\xfft\x0f\xdeq', b'\xe2.\xa9G'), messages=[{_llI0l01OIOl0I00Il(b'\x08`*B', b'\x1fA\xe4A'): _llI0l01OIOl0I00Il(b'L\xda\xb1\x95', b'\x1b\xd0\xed\xcc'), _I010I1IIlIlO(b'\xe3L\xb3\xaf\xa2\xc9\xa9', b'sUD\xe6'): prompt}], temperature=0.8, max_tokens=463183768 ^ 463183868)
        return completion.choices[351362184 ^ 351362184].message.content.strip()
    except Exception:
        return f'Hello {business_name}! {message_template[:100]}'

def generate_whatsapp_url(phone_number, message):
    clean_phone = re.sub(_I010I1IIlIlO(b'\x1f\xc9lY]\x1d|', b'm\xa6\xcd\xad'), _10I00IOI1lO10(b'', b'\xd1\xd28\x0b'), str(phone_number))
    if not clean_phone.startswith(_llI0l01OIOl0I00Il(b'\xf8', b'@?\x8e\xa6')):
        if len(clean_phone) == 1107118506 ^ 1107118496:
            clean_phone = _llI0l01OIOl0I00Il(b'O}', b'gc\x8e\xf2') + clean_phone
        else:
            clean_phone = _llI0l01OIOl0I00Il(b'\xf0', b'\tR\xbbq') + clean_phone
    encoded_message = urllib.parse.quote(message)
    return f'https://wa.me/{clean_phone}?text={encoded_message}'

def process_whatsapp_messages(df, message_template, progress_callback=None):
    total = len(df)
    results = []
    for index, row in df.iterrows():
        if progress_callback:
            progress_callback(index, total)
        business_name = row.get(_llI0l01OIOl0I00Il(b'\xd6W\x11*\xe9\x8b\x14\x9c\x0e%\xd6yt', b'2[\xbc"'), _10I00IOI1lO10(b'\x05\xb2\x80\x02:\x12Z\x95', b'\x01u\xedy'))
        phone = row.get(_I010I1IIlIlO(b'N\xd1\x8fV\xba', b':\x92\xffO'), _llI0l01OIOl0I00Il(b'', b'\x10\xfb\x7f\xa2'))
        rating = row.get(_llI0l01OIOl0I00Il(b"mI[\xa0'\xca", b'\x99X\x03\x8f'), _10I00IOI1lO10(b'\x0f\xd8t', b'B$C\xfe'))
        address = row.get(_I010I1IIlIlO(b'\x19l\x15(m\x89f', b'\xa2\x0f\x88\xa8'), _I010I1IIlIlO(b'\xd4\xb3\xad', b'\xff~\xd5\xd1'))
        business_details = f'Rating: {rating}, Address: {address}'
        whatsapp_message = generate_whatsapp_message(business_name, phone, message_template, business_details)
        whatsapp_url = generate_whatsapp_url(phone, whatsapp_message)
        results.append({_I010I1IIlIlO(b'\x14\xf8\x1f\x9c;\xddT-\xcc\xb1-m\xb8', b'\x8d%\xb2\xb3'): business_name, _I010I1IIlIlO(b'-aBn\xc1', b"\x91'\x04\xc0"): phone, _10I00IOI1lO10(b"\xd4*-\xff\x87TG4'\x9cK\x88\x83r\x06:", b'\x02\x03\xad>'): whatsapp_message, _llI0l01OIOl0I00Il(b'\xc5S\xa1\x19\x04\x12kv\xff\x13]\x89', b'5\xe83\x96'): whatsapp_url})
        time.sleep(0.3)
    return pd.DataFrame(results)

def save_whatsapp_template(template_name, template_content):
    templates = safe_json_load(WHATSAPP_TEMPLATES_FILE, {})
    templates[template_name] = {_10I00IOI1lO10(b'\xccH?xwkr', b'\xe6\xdb\x10\x83'): template_content, _llI0l01OIOl0I00Il(b'u\x10\x8d\n\xb4lu', b'\xe2\xaf\t:'): datetime.now().isoformat(), _10I00IOI1lO10(b'R\x80}$\xa2\x1f\xc1', b'C-)\xef'): datetime.now().isoformat()}
    return safe_json_save(WHATSAPP_TEMPLATES_FILE, templates)

def load_whatsapp_templates():
    return safe_json_load(WHATSAPP_TEMPLATES_FILE, {})

def delete_whatsapp_template(template_name):
    templates = safe_json_load(WHATSAPP_TEMPLATES_FILE, {})
    if template_name in templates:
        del templates[template_name]
        return safe_json_save(WHATSAPP_TEMPLATES_FILE, templates)
    return False

def save_email_settings(settings):
    return safe_json_save(EMAIL_SETTINGS_FILE, settings)

def load_email_settings():
    return safe_json_load(EMAIL_SETTINGS_FILE, None)

def send_single_email(smtp_server, smtp_port, sender_email, sender_password, recipient_email, subject, body, use_tls=True, use_ssl=False):
    try:
        msg = MIMEMultipart()
        msg[_llI0l01OIOl0I00Il(b'\x80\x0f\x15\x8b', b'\xe8\xab\x8f\x1e')] = sender_email
        msg[_llI0l01OIOl0I00Il(b'>\xb6', b'\x7fd\x14{')] = recipient_email
        msg[_10I00IOI1lO10(b'\\\x12\x14\x90\x94C\xe7', b'L\xfb\x81\x1a')] = subject
        msg.attach(MIMEText(body, _I010I1IIlIlO(b'\xe6\xc16H\x82', b'\xe3`\xe58')))
        if use_ssl:
            server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        else:
            server = smtplib.SMTP(smtp_server, smtp_port)
            if use_tls:
                server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return (True, _llI0l01OIOl0I00Il(b'\xfe\xda\xdd\xbb\xc2\xb5\xad3\x89\xccw\x00)\xf4\xe0\xff\xba\xc0\x97\xf0\xa7\x97\x00', b"\xaeX\xe8'"))
    except smtplib.SMTPAuthenticationError:
        return (False, _llI0l01OIOl0I00Il(b'To<2\x12d\xdcpu\x12\x1c)\xc2@\x8b_\xf6\xc6\x81\xb4:\x87`\x9c4?\x91\x8d\xb0&,>\xaf\xb4H^\xfe\x06\xa1#,\xfcF\x82\xd6^\xa0\x8dW\xe9R^:0\x82\xc1\xe0\x90\xdb', b'M\x98\xe1k'))
    except smtplib.SMTPRecipientsRefused:
        return (False, _10I00IOI1lO10(b'\x9d\x8d\x1f\x8c\xe5\xb3L>>$\xc1, a\xa1\xf2\xa5@%{F\xe2\x9c\x07_5\xbc-\x16\xe3\xbc\x81\xb7\xce0\xb9', b'8\xc9\xab\xdd'))
    except smtplib.SMTPServerDisconnected:
        return (False, _10I00IOI1lO10(b'\x87\xab\x94\xc7\xd6\xa80\xf9\x96\xedK4\xa9\xf9`\xee\xb3\xa8\x13\xb6\xf8\xd5\xb8Y\xa6\x08\x1a p\x8e\xc1\xda\xa0', b' \xf5R\xbd'))
    except Exception as e:
        return (False, f'Error sending email: {str(e)}')

def send_bulk_emails(smtp_server, smtp_port, sender_email, sender_password, recipients, subject, body, use_tls=True, use_ssl=False, delay_between=1796839333 ^ 1796839335, progress_callback=None):
    results = []
    total = len(recipients)
    for i, recipient in enumerate(recipients):
        if progress_callback:
            progress_callback(i, total, recipient)
        if not recipient or _10I00IOI1lO10(b'L', b'\x07g\xa1H') not in recipient:
            results.append({_I010I1IIlIlO(b'\x17\xb4\xac>\xdf', b'LH\xe0\xe8'): recipient, _10I00IOI1lO10(b'\xea\x05d\xf98\xaa', b'-956'): _llI0l01OIOl0I00Il(b'\xad\x19z\xe6\x8ar', b"\xa0\xdc\xa3'"), _llI0l01OIOl0I00Il(b'v3L\xa8\x0e\x0f\x8e', b'\x08Q^\x1b'): _llI0l01OIOl0I00Il(b'\xa1\xb3]~\xf2=3\xa45\xe7\xfe?\xdf\xf7O}\x16\xcc\xd92y', b'\xc9{\xd0t')})
            continue
        success, message = send_single_email(smtp_server, smtp_port, sender_email, sender_password, recipient, subject, body, use_tls, use_ssl)
        results.append({_10I00IOI1lO10(b'0\xd3B\x94\xf9', b'\x8f4\xd3A'): recipient, _llI0l01OIOl0I00Il(b'4VP&|V', b'P\x85S\xdc'): _10I00IOI1lO10(b'\xf3\x81\xbd\x9b\x81fp', b'i\xd4\x11\x89') if success else _I010I1IIlIlO(b'\xd82B\xa5w\xb1', b'\xb7f\xc8\xe9'), _I010I1IIlIlO(b').\xa8f\xfb\xf9\xdd', b'(\xd1\xfb\xd2'): message})
        if i < total - (2131778926 ^ 2131778927):
            time.sleep(delay_between)
    return results

def validate_email_settings(settings):
    required_fields = [_I010I1IIlIlO(b'\xfa\xdc\xbc\xee\x0fG\xa1\xd1\xb7\xfc\x0c', b'\xa2I\xfe\xd6'), _llI0l01OIOl0I00Il(b'o\x84c\xf1\xd4\xea\xa2\xf6\xc1', b'\x8ac\xdc\x00'), _llI0l01OIOl0I00Il(b'\x83\x15\xe6\x12\x9d\x1c\xcc\x8b\x8a^\xc5s', b'6\x1f\x8c\x88'), _I010I1IIlIlO(b'\x02\xf4\xb1\xcd\xc9\x16\x933\xffP\x9c\xa4.%\xd0', b'\xed\xb9\xc2\xbf')]
    for field in required_fields:
        if not settings.get(field):
            return (False, f'Missing required field: {field}')
    try:
        port = int(settings[_llI0l01OIOl0I00Il(b'\x15\xd0\xf8`]\xfb;XI', b'N\xe1\x8bW')])
        if port not in [2140816091 ^ 2140816066, 1506430513 ^ 1506430944, 1931684150 ^ 1931684733, 421544334 ^ 421546067]:
            return (False, _10I00IOI1lO10(b'\xaa\xde\x08\xda\xd9J\x7f\x96\xf4L52\xe5P\xbf\xd5\xed\x0b\xdd!\xbf\x1d\xd8v\x14\x16\x17\xa4rU\x97\x06M\x14m/3]2x\x06=2\xef\xe1H!\xb7W\xdd\x8b', b'JUE\xf8'))
    except ValueError:
        return (False, _llI0l01OIOl0I00Il(b"N\x7f\xfd\x17\xed]\xcf\x8a\xe5B\x04^#<\\,n\xe3'\xd8\x90W\xda\rM\x8c", b'\x12\xd1Ye'))
    if not re.match(_I010I1IIlIlO(b'\xe6\xaa\\\x91\xfaO\x0f\xb8\x1a\x9f\xfa\x1bw@\xaai\xb2"0Q\x03\xceCH\xb5\r\x1e7\xebp~\x15b\xa8"\xe3O\xcd\xa8\xb1\x06\xd8\xd4w\xd1 \xe7\x8d', b'|\x82g\x1f'), settings[_I010I1IIlIlO(b'\xf4\xc4\x82\xa3\xd4\x15\xd8\x7fUl\x81Q', b'\\Pr\xea')]):
        return (False, _I010I1IIlIlO(b'\x12\xdc@\xf4\xbb\xd6\x95\x85J\xfa\xcc8\xa9\xe0\x94\xff\xe9m\xa0\x00\xe0\x17=9\xfc\xca`', b'\x04\xcfHT'))
    return (True, _I010I1IIlIlO(b'n9\x95\xb0\x0eD\x0f\xb1^\xc2\x89\x00=\x91', b'z\x97\t\x91'))

def test_email_connection(settings):
    try:
        if settings.get(_llI0l01OIOl0I00Il(b'\x8b56x\x16{9', b'f\xedL\xf3'), False):
            server = smtplib.SMTP_SSL(settings[_llI0l01OIOl0I00Il(b'Z\x86\xdc\xd4\x04V\x81\x8d\xb1XF', b'X\x8e\x97e')], int(settings[_I010I1IIlIlO(b'd\xef\x0e\x8ff}\xbd\x87\x94', b'o][\x8a')]))
        else:
            server = smtplib.SMTP(settings[_I010I1IIlIlO(b'\xfa\x81\xc1\x9e;_\xd1\xddP[\xc5', b'\xe7\x81\xd2f')], int(settings[_10I00IOI1lO10(b'\x82H\x03\xa7\x0b\xb9\x18\xd1\x02', b'5\xdc\x83\x94')]))
            if settings.get(_10I00IOI1lO10(b'o\xaf\x1f\x02m\x04X', b'\xda7D\x82'), True):
                server.starttls()
        server.login(settings[_llI0l01OIOl0I00Il(b'\xce q7g"O\xad\xb46\xde\xad', b'\xde\xe6\xc2\xb6')], settings[_llI0l01OIOl0I00Il(b'\x81v\xbe\x9dNa>\xed\xe3\xe5\xa8U\xc7"2', b'\x08#\xf0\xf7')])
        server.quit()
        return (True, _llI0l01OIOl0I00Il(b'\xe3\xc6\xe3k\xe85$N\x9d\xe6\x00kj)7)d\xfb\x82\xb2\x11\xfd', b'N^\xd5\xc1'))
    except Exception as e:
        return (False, f'Connection failed: {str(e)}')

def load_followup_settings():
    return safe_json_load(FOLLOWUP_SETTINGS_FILE, {_llI0l01OIOl0I00Il(b'\xcfq\xc4\x1c\x9a\x1a\xfe', b'\xd4\xcc{\xb0'): False, _llI0l01OIOl0I00Il(b'd\x95 E\x12\xbb\xb7T6\xbc\xf5\x085', b'M\xd8A\x8a'): 1996662794 ^ 1996662793, _10I00IOI1lO10(b'}\xd3\xdb%S7\xb4\x17IZ', b'\x89\xd88\xa1'): 1731746583 ^ 1731746581})

def save_followup_settings(settings):
    return safe_json_save(FOLLOWUP_SETTINGS_FILE, settings)

def generate_followup_message(business_name, original_message, followup_number):
    try:
        client = Groq(api_key=GROQ_API_KEY)
        prompt = f'\n        Create a follow-up message for {business_name}.\n        \n        Original message: {original_message[:200]}\n        Follow-up number: {followup_number} (Day {followup_number * 2})\n        \n        Requirements:\n        1. Keep it short and professional\n        2. Reference the previous message briefly\n        3. Add new value or insight\n        4. Include a soft call-to-action\n        5. Sound like a real person, not automated\n        \n        Return ONLY the message text.\n        '
        completion = client.chat.completions.create(model=_I010I1IIlIlO(b'\xcb\xfd\xa1l\xea\x91\xa3@\x08\x06\x04Y\xc0\x10\xe3j[\x03\x0e\xaf', b'\x8c\xc9\xc9\x07'), messages=[{_llI0l01OIOl0I00Il(b']o\xa6\xb9', b"\x99'o\r"): _I010I1IIlIlO(b'\xd8T[%', b'\t\xe6`\xd5'), _llI0l01OIOl0I00Il(b'\x8fn\xa3\x03\xbbL\x11', b"\xbb'\xd3A"): prompt}], temperature=0.7, max_tokens=568899323 ^ 568899181)
        return completion.choices[1409931844 ^ 1409931844].message.content.strip()
    except:
        return f'Hi {business_name}! Just following up on my previous message. Let me know if you have any questions.'

def save_campaign_data(campaign_data):
    return safe_json_save(CAMPAIGN_DATA_FILE, campaign_data)

class ABTest:

    def __init__(self, test_name, test_type):
        self.test_name = test_name
        self.test_type = test_type
        self.variants = {}
        self.results = {}

    def add_variant(self, variant_name, content):
        self.variants[variant_name] = {_llI0l01OIOl0I00Il(b'\xdb\xc4\x89\x99\xcfH\x95', b'\x17\x0f7\xe6'): content, _10I00IOI1lO10(b'\xa1U\x8e\x11', b')\xc4@b'): 1295185128 ^ 1295185128, _llI0l01OIOl0I00Il(b'\x1az\xf0\xb7\x9f', b'\xa0!\xc7\x0b'): 1994829713 ^ 1994829713, _10I00IOI1lO10(b'vl\xc32\xa6\xb5', b'\xcdU\x83o'): 161373010 ^ 161373010, _llI0l01OIOl0I00Il(b'\x1a}M\xdb\xf3\x91!\xa4\xc9', b'2\xe0\xdc\x9d'): 1471821582 ^ 1471821582}

    def record_send(self, variant_name):
        if variant_name in self.variants:
            self.variants[variant_name][_10I00IOI1lO10(b'\x90\xc1\x9b\x02', b'\x82\xaboR')] += 427637157 ^ 427637156

    def record_open(self, variant_name):
        if variant_name in self.variants:
            self.variants[variant_name][_10I00IOI1lO10(b'\xe1b\xa4\xcd/', b'\xd0\x13@=')] += 296558819 ^ 296558818

    def record_click(self, variant_name):
        if variant_name in self.variants:
            self.variants[variant_name][_I010I1IIlIlO(b'\xa3y\\\x85\xb1!', b'Dc\xbe\x01')] += 329881611 ^ 329881610

    def record_response(self, variant_name):
        if variant_name in self.variants:
            self.variants[variant_name][_llI0l01OIOl0I00Il(b'3\x90\xfcJ\xd7\x9c\x9b\x95r', b'(\x83\x11\x95')] += 1162846369 ^ 1162846368

    def get_performance(self):
        results = []
        for variant, data in self.variants.items():
            sent = data[_I010I1IIlIlO(b'\xb2\xf6\x14\xa3', b'\xf3+AH')]
            open_rate = data[_I010I1IIlIlO(b'\x94\tE\xac\x98', b'i@\xce.')] / sent * (731386936 ^ 731386972) if sent > 1461711223 ^ 1461711223 else 526869971 ^ 526869971
            click_rate = data[_10I00IOI1lO10(b'J\x05\xb5\xde\xddG', b'SX\x1f\\')] / sent * (1137497574 ^ 1137497474) if sent > 109658793 ^ 109658793 else 1326950865 ^ 1326950865
            response_rate = data[_I010I1IIlIlO(b'`\x1a\x81\x15\x91\xe4\x14\xdc(', b'\xf8/\x0f\xfb')] / sent * (2041818074 ^ 2041818046) if sent > 2107824074 ^ 2107824074 else 960977854 ^ 960977854
            results.append({_10I00IOI1lO10(b"\t'k\xa1\xae\xbb\x8c", b'\xcd\xda\xdf!'): variant, _10I00IOI1lO10(b';w\xba\xf5', b'\x91\xccG\x1d'): sent, _I010I1IIlIlO(b'\x081|#\x15G\xa7\x89\xa9i\x0e', b'w}]_'): round(open_rate, 645841758 ^ 645841756), _llI0l01OIOl0I00Il(b'\xfb\xfe\xdf\xe8J\x15\xa5\x0e2\x1fL\xed', b'I\x98\xcb\xa3'): round(click_rate, 1409301293 ^ 1409301295), _I010I1IIlIlO(b'\xd5\xdb\x1e\x0fY?k4\xd6\xd6\xa4\xcd\x87\xab5', b'\x16\xfain'): round(response_rate, 1716294793 ^ 1716294795)})
        return pd.DataFrame(results)

    def get_winner(self):
        df = self.get_performance()
        if not df.empty:
            return df.loc[df[_10I00IOI1lO10(b'\xed\x1e\xe5\xb3\x92\xa60\x92\x86Ocb\x912\r', b'I\x1b\xcf\x8f')].idxmax(), _I010I1IIlIlO(b'\xd8"!\x82\xb0k\xe7', b'\xbe\x97\xe7z')]
        return None
AB_TESTS = {}

def create_ab_test(test_name, test_type, variants):
    test = ABTest(test_name, test_type)
    for name, content in variants.items():
        test.add_variant(name, content)
    AB_TESTS[test_name] = test
    return test

def get_ab_test_results(test_name):
    if test_name in AB_TESTS:
        return AB_TESTS[test_name].get_performance()
    return None

def prepare_webhook_data(lead_data, action_type):
    webhook_payload = {_I010I1IIlIlO(b'\xf8\x91#\x1fO\xb1\xa7Qx', b'+\xb2\x81\xe2'): datetime.now().isoformat(), _llI0l01OIOl0I00Il(b'\xf3\xfc\xf8\x93\x84\x13', b'\r1#\x8e'): action_type, _10I00IOI1lO10(b'4\xbd\x90\xd5', b's\x138v'): {_I010I1IIlIlO(b"\x18k\x98\x1c\x18I\xa6\xae\xd6\xe8\xc6\x8a'", b'BO4Q'): lead_data.get(_I010I1IIlIlO(b'\x1f.\x90\x88\xda!\xa00\xf3\x8bz\x9b~', b'\x01\xd9\x96l'), _llI0l01OIOl0I00Il(b'', b'f\x1f\xc9j')), _I010I1IIlIlO(b'j@\xbfL\xa5', b'\x01\xbdCf'): lead_data.get(_llI0l01OIOl0I00Il(b'_\x92]\xd4\xb9', b'X\xa5\x8fF'), _10I00IOI1lO10(b'', b'9\x96\x89\x02')), _10I00IOI1lO10(b'\xc1"\xb2M\x8e', b'Kh\x93\xd7'): lead_data.get(_llI0l01OIOl0I00Il(b'\xd2\xfd\xe9\xf4|', b'\x0c\xab\x03\xb1'), _llI0l01OIOl0I00Il(b'', b'\x8b\xe7\xf4V')), _llI0l01OIOl0I00Il(b'\xa0\xf1\x1f\xa2{\xd3\xbc', b'\x905\xab?'): lead_data.get(_10I00IOI1lO10(b'{\x8b\xbc\xaaz\xe2\x02', b'(\xf5\xf4\xe6'), _llI0l01OIOl0I00Il(b'', b'\xef\x1a\xb6\xbb')), _I010I1IIlIlO(b'\x85\xbf\xc0rw\xa8', b'\xd0H%\xde'): lead_data.get(_10I00IOI1lO10(b'\xf2\xa1\x9a*\xddu', b'\xbc\x0e\xc1i'), _10I00IOI1lO10(b'', b'\x0b\x19\xff\x8f')), _llI0l01OIOl0I00Il(b'9\xdc\xb9a\x80\xb1\x82', b'_\x1c\xa7\xfe'): lead_data.get(_10I00IOI1lO10(b';!!8\n\xb4\xa2', b'\xa7\x07\xaa~'), _10I00IOI1lO10(b'', b'#<[\x94')), _10I00IOI1lO10(b'\x02x\x02c\x060S[', b'/\xb4\xac1'): lead_data.get(_I010I1IIlIlO(b'5\xfc\xdeUE\x83\x99\xe2', b'\xa4\x04\x8f\xea'), _I010I1IIlIlO(b'j\xf2\xac|\xea\xc0', b'\xcb\xcc_\x80')), _10I00IOI1lO10(b'{\x8e\xf7\xd3b\xe8\x04\x8e\xa90', b'\xa9\xd9{\xeb'): lead_data.get(_I010I1IIlIlO(b'\xf6wV\xe1\xf0d\xd0v\xc8$', b'\xb3?y/'), 492770346 ^ 492770346)}, _llI0l01OIOl0I00Il(b'\x9d\xc2\xc3\x08\x19\x87\x91', b'OHG8'): lead_data.get(_llI0l01OIOl0I00Il(b'\xae\x9fB\xda\x00\xc3+\xfa\xbb\xc7&\x04\x05lk\xc6\xd8o_\xb46e\x85', b',S\xdf\xa4'), _I010I1IIlIlO(b'', b'=\xfaf9')), _I010I1IIlIlO(b'~%\xc2\xc4\x16j', b'\xa8\xfe\xd2\xa0'): _10I00IOI1lO10(b"\xc2\x02\x84\xad\xae\x81+A\x0bB\xa4'\x92\xe9\x07E\x992G\xa2\xfc\\\xf0o\xae\xc7", b'\x93W\xf1\xb7')}
    return webhook_payload

def create_zapier_webhook(webhook_url, data):
    try:
        response = requests.post(webhook_url, json=data, timeout=564017087 ^ 564017057)
        return (response.status_code == 496745505 ^ 496745705, response.text)
    except Exception as e:
        return (False, str(e))