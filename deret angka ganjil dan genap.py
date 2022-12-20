#program deret angka genap normal dan ganjil deret angkanya terbalik
n = int (input("masukkan angka : "))
g = ' '
for k in range (1,n+1):
	g += str (k) + ' '

	h = ' '
for j in range (n,0,-1):
	h += str (j) + ' '
		
	if n %2 == 0:
		print (g)
	elif n %2 != 0:
			print (h)
				
		
	
