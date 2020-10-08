def a_count(s):
    return dict([(c, s.count(c)) for c in s])
print(a_count('arara'))

