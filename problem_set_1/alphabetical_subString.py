# Alphabetical Substrings 
leng=len(s)
index=0
start=0
end=0
len_str=0
while(leng-1>index):
        if s[index]<= s[index+1] and index!=leng-2:
                index +=1
        elif index==leng-2 and s[index]<=s[index+1]:
                if len(s[start:leng])>len_str:
                        new_str=s[start:leng]
                index +=1

        else:
                index +=1
                end=index
                if len(s[start:end])>len_str:
                        new_str=s[start:end]
                        len_str=len(s[start:end])
                start=index
print new_str

