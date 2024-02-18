# -*- coding: utf-8 -*-
"""Task_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14eXkyZ5-Yl32J0WMp8s4M0d6jYiOOZQM
"""

def perfect_square(n):
  sqrt_n = int(n ** 0.5)
  return sqrt_n * sqrt_n == n

def is_fibonacci(num):
  return perfect_square(5 * num * num + 4) or perfect_square(5 * num * num - 4)

number = int(input('Enter a number:'))

if is_fibonacci(number):
  print(number, "is a fibonacci number.")
else:
  print(number, " is not a fibonacci number.")

