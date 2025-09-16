"""
CS5760 HW1 — Q4 Edit Distance
"""

def min_edit_distance(src,tgt,sub=1,ins=1,dele=1):
    m,n=len(src),len(tgt)
    dp=[[0]*(n+1) for _ in range(m+1)]
    back=[[None]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1): dp[i][0]=i*dele; back[i][0]=('D',i-1,0)
    for j in range(1,n+1): dp[0][j]=j*ins; back[0][j]=('I',0,j-1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            cs=dp[i-1][j-1]+(0 if src[i-1]==tgt[j-1] else sub)
            ci=dp[i][j-1]+ins
            cd=dp[i-1][j]+dele
            best=min(cs,ci,cd); dp[i][j]=best
            if best==cs: back[i][j]=('M' if src[i-1]==tgt[j-1] else 'S',i-1,j-1)
            elif best==ci: back[i][j]=('I',i,j-1)
            else: back[i][j]=('D',i-1,j)
    ops=[]; i,j=m,n
    while i>0 or j>0:
        op,pi,pj=back[i][j]
        if op=='M': ops.append(('MATCH',src[i-1]))
        elif op=='S': ops.append(('SUB',src[i-1],tgt[j-1]))
        elif op=='I': ops.append(('INS',tgt[j-1]))
        elif op=='D': ops.append(('DEL',src[i-1]))
        i,j=pi,pj
    ops.reverse(); return dp[m][n],ops

def print_ops(ops):
    for o in ops:
        if o[0]=='MATCH': print(" MATCH",o[1])
        elif o[0]=='SUB': print(" SUB",o[1],"->",o[2])
        elif o[0]=='INS': print(" INS",o[1])
        elif o[0]=='DEL': print(" DEL",o[1])

def main():
    src,tgt="Sunday","Saturday"
    print("Model A (Sub=1,Ins=1,Del=1):")
    dA,opsA=min_edit_distance(src,tgt,1,1,1)
    print("Distance:",dA); print_ops(opsA)
    print("\nModel B (Sub=2,Ins=1,Del=1):")
    dB,opsB=min_edit_distance(src,tgt,2,1,1)
    print("Distance:",dB); print_ops(opsB)
    print("\nReflection:")
    print("Model A favors substitutions; Model B favors insertions/deletions.")
    print("Both give the same distance here, but with different ops chosen.")
    print("Spell-check uses substitutions; DNA alignment prefers indels.")

if __name__=="__main__":
    main()
