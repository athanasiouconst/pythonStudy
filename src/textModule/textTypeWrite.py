#! /usr/bin/env python
# -*- coding: utf-8 -*-

filename = "costas.txt"
fileout = open(filename,"w")

text = {"proedros":"Nikolaou", "melos1":"Petrou", "melos2":"Ioannidou"}

textSpace=" "
fileout.write(text["proedros"])
fileout.write(textSpace)
fileout.write(text["melos1"])
fileout.write(text["melos2"])
fileout.close()
