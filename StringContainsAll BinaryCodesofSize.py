class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        encontrado=[False]*(2**k)
        par=int(s[0:k],2)
        encontrado[par]=True
        com=(2**k)-1
        for i in range(k,len(s)):
            par<<=1
            par&=com
            par|=int(s[i],2)
            encontrado[par]=True
        return all(encontrado)