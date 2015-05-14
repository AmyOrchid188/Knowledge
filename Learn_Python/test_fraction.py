#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Junhui Liu <liujunhui08@gmail.com>
# Created Time: 11/04/14 09:32:49 (CST)
# Modified Time: 11/04/14 09:37:44 (CST)
from fractions import Fraction
gradelist = []
gradelist.append('80/100')
gradelist.append('90/100')
gradelist[0]=Fraction(gradelist[0])
gradelist[1]=Fraction(gradelist[1])
print gradelist
gradelist[0]=float(gradelist[0])
gradelist[1]=float(gradelist[1])
print gradelist
