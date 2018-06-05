#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

print("It's a good thing")
print('Python is the "bomb"')

print("""It's a "good" thing""")

print("32\u00B0")
print("==> \U00010001")

x = '   All my exes live in Texas     '

print('|'  + x.lstrip() + '|')
print('|'  + x.rstrip() + '|')
print('|'  + x.strip() + '|')
print()
print(x.lower())
print(x.upper())
print()

x = 'xyxxyyxxxyyyAll my exes live in Texasxyyyxxxyy'

print('|'  + x.lstrip('xy') + '|')
print('|'  + x.rstrip('xy') + '|')
print('|'  + x.strip('xy') + '|')
print()

x.lstrip('\n\r')

print('Texas' in x)
print()

print(dir(x), '\n')

result = 10.98 / 2.83

print("result is", result)

cave_man = 'Fred Flintstone'
city = "Bedrock"

print(cave_man, "lives in", city)

#       0           1            0       1
print("{} lives in {}".format(cave_man, city))
print(f"{cave_man} lives in {city}")
print("result is {:.2f}".format(result))

nums = [800,80,1000,32,255,400,5,5000]

for n in nums:
    print("{:4d}".format(n))
print('-' * 60)

for n in nums:
    print(f"{n:4d}")

print(f"2 + 2 is {2 + 2}")
print("2 + 2 is {}".format(2 + 2))

values = ["wombat", "koala", "honey badger", "newt"]

v1 = ",".join(values)
print(v1)

nums = [800,80,1000,32,255,400,5,5000]

v2 = ",".join( (str(n) for n in nums)  )
print(v2)




