
#COMPARISON OPERATORS
#==     Equal to
#!=     Not equal to
#<      Less than
#>      Greater than
#<=     Less than or equal to
#>=     Greater than or equal to

# The Difference Between the == and = Operators

# The == operator (equal to) asks whether two values are the same as each other.
# The = operator (assignment) puts the value on the right into the variable on the left.

# Boolean Operators
# The three Boolean operators (and, or, and not) are used to compare Boolean values.

# Binary Boolean Operators
# The and and or operators always take two Boolean values (or expressions), so they’re considered binary operators.

#The and Operator’s Truth Table

# True and True           True
# True and False          False
# False and True          False
# False and False         False

# The or Operator’s Truth Table

#True or True             True
#True or False            True
#False or True            True
#False or False           False

#The not Operator
#Unlike and and or, the not operator operates on only one Boolean value (or expression).

#The not Operator’s Truth Table

#not True                 False
#not False                True


name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')
