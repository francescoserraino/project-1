#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:12:07 2020

@author: uli
"""

import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = sr.Recognizer()    
with sr.Microphone() as source:
    print("Enter anything: ")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)