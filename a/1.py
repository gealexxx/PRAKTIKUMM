def BinToDec(binNum):
    decNum = 0
    power = 0
    while binNum > 0:
        decNum += 2**power*(binNum%10)
        binNum //= 10
        power += 1
    return decNum
binNum = int(input("Masukkan Bilangan BINER : "))
print ("Decimal Number : ", str(BinToDec(binNum)))
print ("Angka DECIMAL dari", binNum, "Adalah ", BinToDec(binNum))
