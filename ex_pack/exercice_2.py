from colorama import*

def saisie():
    while 1:
        N=int(input("Donner N:"))
        M=int(input("Donner M:"))
        if 5<N<M:
            break
    return N,M

def facteurs_premiers(x):
    L=[]
    i=2
    while x!=1:
        if x%i==0:
            L.append(i)
            x=x//i
            i=2
        else:
            i+=1
    return L

def est_homogene(n,m):
    L1=facteurs_premiers(n)
    L2=facteurs_premiers(m)
    print("\nLes facteurs premiers de",n,"sont :",L1)
    print("Les facteurs premiers de",m,"sont :",L2)
    L1=list(set(L1))
    L2=list(set(L2))
    for x in L1:
        if x not in L2:
            print("\n",n,"et",m,"ne sont pas homogenes.")
            return 0
    for x in L2:
        if x not in L1:
            print(n,"et",m,"ne sont pas homogenes.")
            return 0
    print("\n",n,"et",m,"sont homogenes.")
            
            
def lancer():
    init(autoreset=True)
    print('\033[95m'+"\n**** EXERCICE 2 ****\n")
    print('\033[94m'+"Soit N et M deux nombres naturels, on dit que N et M sont\nhomogènes s'ils admettent les mêmes facteurs premiers.\n")
    print('\033[95m'+"**** ENTREES DE L'EXERCICE ****\n")
    N,M=saisie()
    print('\033[95m'+"\n**** RESULTATS DE L'EXERCICE ****")
    est_homogene(N,M)
    print("\n")
