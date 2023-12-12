#!/usr/bin/env python3
course = "     kalulu wambua   "
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())#can strip left and right. rstrip() or lstrip()
print(course.rstrip())
print(course.lstrip())
print(course.find("kal"))#find the index of given item, if not found returns -1.
print(course.replace("k", "__"))#replaces given character.
print("kalulu" in course)#checks for given characters or names in a given string. Returns true if found, false otherwise.
print("Nesa" in course)
print("kalulu" not in course)# not operator.
