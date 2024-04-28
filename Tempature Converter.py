#!/usr/bin/env python
# coding: utf-8

# In[1]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

choice = input("Enter 'C' to convert Celsius to Fahrenheit, or 'F' to convert Fahrenheit to Celsius: ")

if choice.upper() == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))
elif choice.upper() == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", fahrenheit_to_celsius(fahrenheit))
else:
    print("Invalid input. Please try again.")


# In[ ]:




