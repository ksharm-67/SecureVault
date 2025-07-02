from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from hashlib import pbkdf2_hmac

def encryptPwd(ptxt: str, salt: bytes, master: str) -> bytes:
    itr = 100000
    key = pbkdf2_hmac('sha256', master.encode('utf-8'), salt, itr, dklen=32)
    
    iv = get_random_bytes(16)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded = pad(bytes(ptxt, 'utf-8'), AES.block_size)
    
    ctxt = cipher.encrypt(padded)
    
    return iv + ctxt
    
def decryptPwd(ctxt: bytes, master: str, salt: bytes) -> str:
    itr = 100000
    key = pbkdf2_hmac('sha256', master.encode('utf-8'), salt, itr, dklen=32)
    
    iv = ctxt[:16]
    toDec = ctxt[16:]
    
    decoded = AES.new(key, AES.MODE_CBC, iv)
    
    decrypted_padded = decoded.decrypt(toDec)
    ptxt = unpad(decrypted_padded, AES.block_size)
    
    return ptxt.decode('utf-8')

