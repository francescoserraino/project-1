#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:12:07 2020

@author: uli
"""

import speech_recognition as sr

def speech():
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text

print('say yes')    
if (speech()) == 'yes':
    print('you said yes!')