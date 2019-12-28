#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:24:54 2019

@author: fasiltesema
"""
# this program calculates the age of an individual given the date of the birth


import datetime


def age_calculator(yr, mo, day):
    Today = datetime.date.today()
    y = Today.year - yr
    m = Today.month - mo
    d = Today.day - day
    if d < 0:
        d += 30
        m = m - 1
    if m < 0:
        m += 12
        y = y - 1
    # return y,m,d
    return 'Your age is ' + str(y) + ' years ' + str(m) + ' months ' + str(d) + ' days old'


# calculating a sample age here
print(age_calculator(1990, 11,19))
