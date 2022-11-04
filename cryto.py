import os

#os.system("python -m pip install cryptography")


from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


from cryptography.hazmat.primitives.asymmetric import rsa


# Generate the RSA private key
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)




message = b"secret text"
ciphertext = key.public_key().encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        algorithm=hashes.SHA256(),
        label=None
    )
)

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
plaintext = key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(plaintext == message)
print(key)
print(key.private_bytes())
print(key.key_size)
print(key.private_numbers())
print(key.public_key().public_bytes())
print(key.sign)
print(message)
print(ciphertext)
print(plaintext)