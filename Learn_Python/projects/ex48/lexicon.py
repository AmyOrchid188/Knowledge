#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 06/08/13 18:23:16 (CST)
# Modified Time: 06/19/13 09:57:22 (CST)
def scan(phrase):
    words = phrase.split()
    results = []
    commands = (
        ('direction' , 'north'),
        ('direction', 'south'),
        ('direction', 'east'),
        ('direction', 'west'),
        ('verb', 'kill'),
        ('verb', 'eat'),
        ('verb', 'go'),
        ('noun', 'bear'),
        ('noun', 'princess'),
        ('noun', 'door'),
        ('stop', 'the'),
        ('stop', 'in'),
        ('stop', 'of'),
    )
    for word in words:
        if not is_number(word):
            for command in commands:
                if command[1].lower() == word.lower():
                    results.append(command)
                    break
        elif is_number(word):
            results.append(('number', word))
        else:
            results.append(('error', word))

    return results

def is_number(string):
    try:
        return int(string)
    except ValueError:
        return None
