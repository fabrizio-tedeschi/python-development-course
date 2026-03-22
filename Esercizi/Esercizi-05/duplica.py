#Apertura dei file necessari con modalità associate
fin = open("files/primo.txt", "r")
fout = open("files/duplica-out.txt", "w")

#Lettura di tutte le linee del primo file e scrittura sul secondo
lines = fin.readlines()
fout.writelines(lines)