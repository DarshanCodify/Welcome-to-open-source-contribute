#!/usr/bin/env python
# coding: utf-8

# In[1]:


def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    """Main function to check if a number is prime."""
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

if __name__ == "__main__":
    main()


# In[ ]:




