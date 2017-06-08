#! /usr/bin/env python
# -*- coding: utf-8 -*-

phrase = input("Παρακαλώ πληκτρολογήστε τη φράση που επιθυμείτε: ")

phraseSplit = ''.join(phrase[0] for phrase in phrase.upper().split())

print("Το ακρονύμιο για τη φράση '{0}' είναι : {1} ".format(phrase,phraseSplit))
