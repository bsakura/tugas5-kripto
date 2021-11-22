import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def multiplicative_inverse(e, tointent):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = tointent

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + tointent


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    tointent = (p-1) * (q-1)

    e = random.randrange(1, tointent)

    g = gcd(e, tointent)
    while g != 1:
        e = random.randrange(1, tointent)
        g = gcd(e, tointent)

    d = multiplicative_inverse(e, tointent)

    return ((e, n), (d, n))

def generate_keys():
    done = False
    primes_file = open('primes.txt','r')
    primes = primes_file.readlines()

    while not done:
        r1 = random.randint(50,100)
        r2 = random.randint(50,100)

        p = int(primes[r1])
        q = int(primes[r2])
        
        if len(str(p*q)) % 2 == 0:
            done = True
    
    n = p * q
    toitent = (p-1) * (q-1)

    searching = True
    while (searching):
        e = random.randrange(2, toitent)
        if(gcd(e, toitent) == 1):
            searching = False
    
    # e = 79
    # toitent e
    found = False
    k = 1
    while not found:
        d = (1 + (k*toitent)) / e
        if (d % 1 != 0):
            k += 1
        else:
            found = True
            d = int(d)

    with open('key.pub', 'w') as f:
        f.write(f"{str(n)},{str(e)}")
        f.close()

    with open('key.pri', 'w') as f:
        f.write(f"{str(n)},{str(d)}")
        f.close()

    return n,e,d


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def encrypt_number(text):
    n, e, d = generate_keys()

    res = int(text) ** d
    res = res % n
    res = hex(res)

    return res

def decrypt(pk, ciphertext):
    key, n = pk
    aux = [str(pow(char, key, n)) for char in ciphertext]
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)

def generatePrime(n):
   odds = range(3, n+1, 2)
   sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds], []))
   return [2] + [p for p in odds if p not in sieve]

primeList = generatePrime(1000)


if __name__ == '__main__':


    p = random.choice(primeList)
    q = random.choice(primeList)

    public, private = generate_key_pair(p, q)
    print(public, private)
    public = (public[0], public[1])
    print (public)


    message = "ayam kecil"
    encrypted_msg = encrypt(public, message)

    print(" - Your encrypted message is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    print(" - Your message is: ", decrypt(private, encrypted_msg))
