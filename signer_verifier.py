from rsa import encrypt_number
from sha import sha256

class Signer:
    def __init__(self, source, file=False, key_pair=None):
        if not file:
            self.signee = source if source else ""
        else:
            with open(source,'r') as f:
                self.signee = f.read().strip()
            self.filename = source
        self.key_pair = key_pair
    
    def signFile(self, encryption_function=None):
        file_sign = int(sha256(self.signee), 16)
        rsa_encrypted = encryption_function(file_sign) if encryption_function else file_sign
        signed = self.signee + f"\n\n*DS*{rsa_encrypted}*DS*"

        fsplit = self.filename.split('.')
        filename = f"{fsplit[0]}-signed.{fsplit[-1]}" if self.filename else 'signedOutput.txt'
        with open(filename,'w') as f:
            f.write(signed)
        
        return signed, filename

    def validateSign(self, filename):
        if not self.key_pair:
            with open("key.pub",'r') as f:
                self.key_pair = [int(x) for x in f.read().strip().split(',')]
            # print("No key")
            # return
        
        with open(filename,'r') as f:
            ft = f.read().split("*DS*")
        not_sign = ft[0].strip()
        sign = ft[1]
        # print(not_sign, sign)
    
        hash = int(sha256(not_sign), 16) % self.key_pair[0]
        processed_signature = (int(sign, 16) ** self.key_pair[1]) % self.key_pair[0]

        if hash == processed_signature:
            return True
        else:
            return False
        
if __name__=='__main__':
    ## Signing
    filename = input("Filename : ")
    signer = Signer(filename,file=True)
    signed, ofile = signer.signFile(encryption_function=encrypt_number)
    print(f"Outputed as {ofile}")
    # filename = input("Filename : ")
    print(f"Reloading {ofile} to validate")
    validation_result = signer.validateSign(ofile)
    print("valid" if validation_result else "invalid")