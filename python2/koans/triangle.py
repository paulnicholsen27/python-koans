#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    sides_names = {1: 'equilateral', 2: 'isosceles', 3: 'scalene'}
    if not all(map(positive, [a,b,c])):
        raise TriangleError
    sm, med, lg = sorted([a, b, c])
    if not (sm + med > lg):
        raise TriangleError
    return sides_names[len(set([a,b,c]))]

def positive(num):
    return num > 0

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
