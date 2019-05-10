oikearivi=open("oikearivi.txt", "r")
maaliporssi=open("maaliporssi.txt", "r")
veikkaus=open("veikkaus.txt", "r")

oikearivi=oikearivi.readlines()
maaliporssi=maaliporssi.readlines()
veikkaus=veikkaus.readlines()

def pisteet (veikkaus, oikearivi, maaliporssi):
    pojot = 0
    #pisteet sarjataulukosta
    for joukkue in range(20):
        veikattu = veikkaus[joukkue]
        oikea = oikearivi.index(veikattu)
        pojot = pojot +20 - abs(joukkue-oikea)
    
    #pisteet potkuista ja cup-voittajista
    potkutVeikkaus = veikkaus[27]
    potkutOikea = oikearivi[21]
    liigaCupVeikkaus = veikkaus[29]
    liigaCupVoittaja = oikearivi[23]
    faCupVeikkaus = veikkaus[31]
    faCupVoittaja = oikearivi[25]

    if potkutOikea.lower==potkutVeikkaus.lower:
        pojot = pojot + 20
    if liigaCupVeikkaus.lower==liigaCupVeikkaus.lower:
        pojot = pojot + 20
    if faCupVeikkaus.lower==faCupVoittaja.lower:
        pojot=pojot + 20
    #Pisteet maalintekijöistä
    for i in range(21, 25):
        maalintekija = veikkaus[i]
        if maalintekija in maaliporssi:
            maalit = maaliporssi.index(maalintekija)+1
            maalipisteet = int(maaliporssi[maalit])
            pojot = pojot + maalipisteet            

    return pojot

print("Pisteet: ", pisteet(veikkaus,oikearivi, maaliporssi))
		

