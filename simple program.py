#!/usr/bin/env python
# coding: utf-8

# In[2]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    num = int(input("Enter a number to calculate its factorial: "))
    result = factorial(num)
    print(f"The factorial of {num} is: {result}")

if __name__ == "__main__":
    main()


# In[ ]:




