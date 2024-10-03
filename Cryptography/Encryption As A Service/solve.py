def to_bytes(h):
    return bytes.fromhex(h)

def to_hex(b):
    return b.hex()

def decrypt(enc, secret):
    """Decrypts the given encrypted flag with the provided secret."""
    msg = to_bytes(enc)
    return bytes([msg[i] ^ ((secret + i) % 256) for i in range(len(msg))])

# The encrypted flag (from showFlag output)
encrypted_flag_hex = "4958494c4002534554484c05446840094864440d4c6071321d2074750a3a7a7d"

# Flag prefix
flag_prefix = "csean-ctf{"

# Try every possible byte value for the secret
for secret in range(256):
    decrypted_flag = decrypt(encrypted_flag_hex, secret).decode(errors='ignore')
    
    # Check if the decrypted flag starts with the known prefix
    if decrypted_flag.startswith(flag_prefix):
        print(f"Found secret byte: {secret} -> Decrypted flag: {decrypted_flag}")
