def gcd(a, b):
    while b!=0:
        a, b = b, a%b
    return a

def decrypt(pk, ciphertext):
   
    key, n = pk
    
    plain = [chr((char ** key) % n) for char in ciphertext]
   
    return ''.join(plain)

def encrypt(pk, plaintext):
   
    key, n = pk
  
    cipher = [(ord(char) ** key) % n for char in plaintext]
    
    return cipher

def get_private_key(e, tot):
    k=1
    while (e*k)%tot != 1 or k == e:
        k+=1
    return k

def get_public_key(tot):
    e=2
    while e<totient and gcd(e, totient)!=1:
        e += 1
    return e

m = input("Enter the text to be encrypted:")


p = 13
q = 23

print("Two prime numbers(p and q) are:", str(p), "and", str(q))


n = p*q
print("n(p*q)=", str(p), "*", str(q), "=", str(n))


totient = (p-1)*(q-1)
print("(p-1)*(q-1)=", str(totient))


e = get_public_key(totient)
print("Public key(n, e):("+str(n)+","+str(e)+")")


d = get_private_key(e, totient)
print("Private key(n, d):("+str(n)+","+str(d)+")")


encrypted_msg = encrypt((e,n), m)
print('Encrypted Message:', ''.join(map(lambda x: str(x), encrypted_msg)))


print('Decrypted Message:', decrypt((d,n),encrypted_msg))