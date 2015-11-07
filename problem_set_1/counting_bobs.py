# Counting Bobs

count=0
for num in range(0,len(s)-2):
    if s[num:num+3]=='bob':
        count +=1
print count
 
