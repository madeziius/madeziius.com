import hashlib
#Simple implementation of RSA, with digital signatures
#for code to work you have to make a file you want to encrypt manually in the same directory of the code

#A keys with RSA
p1 = ZZ.random_element(2**100,2**101).next_prime()
q1 = ZZ.random_element(2**100,2**101).next_prime()
n1 = q1*p1
f1 = (p1-1)*(q1-1)
F1 = Zmod(f1)
e1 = F1.random_element()
while not e1.is_unit()==true:
    e1 = F1.random_element()
d1 = e1**-1

#B keys with RSA
p2 = ZZ.random_element(2**100,2**101).next_prime()
q2 = ZZ.random_element(2**100,2**101).next_prime()
n2 = q2*p2
f2 = (p2-1)*(q2-1)
F2 = Zmod(f2)
e2 = F2.random_element()
while not e2.is_unit()==true:
    e2 = F2.random_element()
d2 = e2**-1
#Encryption
def cifra(c) :
    return ZZ(Zmod(n2)(c)**e2)
#Decryption
def descifra(c) :
    return ZZ(Zmod(n2)(c)**d2)

#Encryption of the from signature
def cifraSignature(c) :
    return ZZ(Zmod(n1)(c)**d1)
#Decryption Hash form signature
def descifraSignature(c) :
    return ZZ(Zmod(n1)(c)**e1)

#The hash funcion used for signature generation, using md5
def hashfunc (lista) :
    string = ''.join(map(str, lista))
    m = hashlib.md5()
    m.update(string)
    digest = m.digest()
    return digest

while true:
    cmd = raw_input("cifra [fichero] / descifra [fichero] / exit: ")
    accion = cmd.split()[0]
    if len(cmd.split())>1:
        fichero = cmd.split()[1]
    if accion == 'cifra':
        f_de_cifrar = open(fichero,"r")
        f_cifrado = open(fichero + ".cifrado","w+")
        f_signature = open(fichero + ".cifrado.signature","w+")
        plainText = f_de_cifrar.read()

        # making the signature of A
        hashOfMessage = hashfunc(plainText)
        numberSignat = ZZ([ ord(c) for c in hashOfMessage ] , 256)
        listSignat = numberSignat.digits(n1)

        #Encrypting the signature with A's private key d1,n1
        listCifradaSignat = [ cifraSignature(c) for c in listSignat ]
        numberCifradoSignat = ZZ(listCifradaSignat , n1)

        #Encryption of the message with B's public key e2,n2
        numero = ZZ([ ord(c) for c in plainText ] , 256)
        lista = numero.digits(n2)
        listaCifrada = [ cifra(c) for c in lista ]
        numeroCifrado = ZZ(listaCifrada , n2)


        f_cifrado.write(''.join([ chr(c) for c in numeroCifrado.digits(256)]))
        f_signature.write(''.join([ chr(c) for c in numberCifradoSignat.digits(256)]))
        f_de_cifrar.close()
        f_signature.close()
        f_cifrado.close()
    elif accion == 'descifra':
        f_de_descifrar = open(fichero,"r")
        f_descifrado = open(fichero + ".descifrado","w+")
        f_signat_para_descifrar = open(fichero + ".signature","r")


        #Dencrypting the message with B's Private key d2,n2
        numeroCifrado = ZZ([ ord(c) for c in f_de_descifrar.read() ] , 256)
        listaDescifrada = [descifra(c) for c in numeroCifrado.digits(n2) ]
        numeroDescifrado = ZZ(listaDescifrada , n2)

        hashFromMessage = hashfunc(plainText)
        plainText = ''.join([ chr(c) for c in numeroDescifrado.digits(256) ])

        #Dencrypting A's signature with A s public key e1,n1
        numberCifradoSignat = ZZ([ ord(c) for c in f_signat_para_descifrar.read() ] , 256)
        listDescifradaSignat = [descifraSignature(c) for c in numberCifradoSignat.digits(n1) ]
        numberDescifradoSignat = ZZ(listDescifradaSignat , n1)

        hashFromSignature = ''.join([ chr(c) for c in numberDescifradoSignat.digits(256) ])

        #Validating Signature
        if hashFromSignature == hashFromMessage:
            print hashFromMessage
            print hashFromSignature
            print "Siganture is Valid!"
        else:
            print "Signature invalid!"
        f_descifrado.write(plainText)
        f_de_descifrar.close()
        f_descifrado.close()
        
    elif accion == 'exit':
        break
    else:
        print "comando incorrecto"
