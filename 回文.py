s=input("Enter a string: ")
l=len(s) #輸入字串的長度
i=0
lmax=""
while i<=l:		  
	j=l	#把j設定為字串的長度		
	while i<=j:
		w=s[i:j] # w=整個字串開始由最後往前遞減
		if w==w[::-1]: #如果"由左往右=由右往左""
			if len(w)>len(lmax):
				lmax=w #如果有更長的回文，更新回文的總長
		j=j-1
	i=i+1

print("Longest palindrome substring is: %s"%(lmax))
print("Length is: %d"%(len(lmax)))