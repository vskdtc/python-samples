import gpg
import os

# Encryption to public key specified in rkey.
rkey = "0xDEADBEEF"
text = "Something to hide."
plain = gpg.core.Data(text)
cipher = gpg.core.Data()
c = gpg.core.Context()
c.set_armor(1)
c.op_keylist_start(rkey, 0)
r = c.op_keylist_next()
c.op_encrypt([r], 1, plain, cipher)
cipher.seek(0, os.SEEK_SET)
ciphertext = cipher.read()

# Decryption with corresponding secret key
# invokes gpg-agent and pinentry.
plaintext = gpg.Context().decrypt(ciphertext)

# Matching the data.
if text == plaintext[0].decode("utf-8"):
    print("Hang on ... did you say *all* of GnuPG?  Yep.")
else:
    pass