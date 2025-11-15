name = "ada lovelace"
# Changing Case in a String with Methods
print(name.title())
# You can change a string to all uppercase or all lowercase letters like this
print(name.upper())
print(name.lower())
# Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
# The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# Adding Whitespace to Strings with Tabs or Newlines
# >>> print("Python")
# Python
# >>> print("\tPython")
#         Python
# >>> print("Languages:\nPython\nC\nJavaScript")
# Languages:
# Python
# C
# JavaScript
# >>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
# Languages:
#         Python
#         C
#         JavaScript
# >>>

# Stripping Whitespace
# >>> favorite_language = 'python '
# >>> favorite_language
# 'python '
# >>> favorite_language.rstrip()
# 'python'
# >>> favorite_language
# 'python '
# >>> favorite_language = favorite_language.rstrip()
# >>> favorite_language
# 'python'
# >>> favorite_language = ' python'
# >>> favorite_language.rstrip()
# ' python'
# >>> favorite_language.lstrip()
# 'python'
# >>> favorite_language.strip()
# 'python'
# >>>

# Removing Prefixes
