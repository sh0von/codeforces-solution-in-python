s = input()
while '--' in s:
	s =  s.replace('--', '2')
while '-.' in s:
	s = s.replace('-.', '1')
while '.' in s:
	s = s.replace('.', '0')
print(s)