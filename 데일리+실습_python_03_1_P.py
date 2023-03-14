a='apple,rottenBanana,apple,RotTenorange,Orange'
anew=a.lower()
anew=anew.replace('rotten','')
anew=anew.split(',')
print(anew)
