"""
Python Script to Replace 'pi' in a String with '3.14' Using Recursion

This script defines a function `replacePi` that replaces every occurrence of the substring 'pi' with '3.14' in a given string, using recursion.
It demonstrates the use of recursion in Python for string manipulation and includes examples of how to use the function.

Functions:
    replacePi(s): Replace all occurrences of 'pi' with '3.14' in string 's'.
"""

def replacePi(s):
    """
    Replace all occurrences of 'pi' in string 's' with '3.14', using recursion.

    The function recursively processes each part of the string. If the first two characters of a substring are 'pi',
    they are replaced with '3.14'. Otherwise, the first character is kept unchanged. 
    The base case is reached when the string is empty or has only one character.

    Parameters:
    - s (str): The string in which the replacement is to be performed.

    Returns:
    str: A new string where all occurrences of 'pi' have been replaced with '3.14'.

    Examples:
    - replacePi("pipxxpi") returns "3.14pxx3.14"
    - replacePi("abc") returns "abc"
    """
    if len(s) == 0 or len(s) == 1:
        return s
    
    if s[0] == "p" and s[1] == "i":
        smallerOutput = replacePi(s[2:])
        return "3.14" + smallerOutput
    else:
        smallerOutput = replacePi(s[1:])
        return s[0] + smallerOutput

if __name__ == "__main__":
    # Example usage of the replacePi function
    string_to_be_replaced = "pidapipicdxcdppi"
    print(f"Replacing 'pi' with '3.14' in '{string_to_be_replaced}': {replacePi(string_to_be_replaced)}")

