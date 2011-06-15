def palin(s):        
    word_len = len(s)
    if word_len == 1:
        if s == "9":
            return "11"
        else:
            return str(int(s)+1)                
    
    if word_len % 2 == 0:        
        m = ''
    else:         
        m = s[word_len/2]
    
    h1 = (word_len / 2) - 1           
    h2 = (word_len + 1) / 2
    
    i = h1
    j = h2
    
    if m:    
        while s[i] == s[j]:
            i -= 1
            j += 1
            if i < 0: break
        
        if i < 0 or s[i] < s[j]:
            if m == '9':
                m = "0"
            else:
                m = str(int(m) + 1)
                return s[:h1+1] + m + s[h1::-1]
                    
    
    while i >= 0:
        if s[i] > s[j]:
            break
        elif s[i] < s[j]:            
            s = s[:i] + str(int(s[i]) + 1) + "0" * h1              
            break
        elif i > 0: 
            k = i - 1
            l = j + 1
            while s[k] == s[l]:
                k -= 1
                l += 1
                if k < 0: break
            if k >= 0:
                if s[k] < s[l]:
                    if s[i] == '9':
                        s = s[:i] + '0' + s[i+1:]
                    else:
                        x = str(int(s[i]) + 1)
                        s = s[:i] + x + s[i+1:]
                        break
                i = k + 1
                j = l - 1
            else:
                if s[i] == '9':
                    s = s[:i] + '0' + s[i+1:]                    
                else:
                    x = str(int(s[i]) + 1)
                    s = s[:i] + x + s[i+1:]                    
                    break
        
        else:
            if s[i] == '9':
                s = s[:i] + '1' + s[i+1:]
                m += '0'                
                break            
                                
        i -= 1
        j += 1
                
    
    return s[:h1+1] + m + s[h1::-1]
    
t = int(raw_input())

while t:
    t -= 1
    s = raw_input()        
    print palin(s)