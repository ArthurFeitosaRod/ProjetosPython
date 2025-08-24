from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
import os
import hashlib

# Constantes
TAMANHO_CHAVE = 32  # Tamanho da chave AES-256 em bytes

def obter_chave(senha):
    chave = hashlib.sha256(senha.encode()).digest()
    return chave[:TAMANHO_CHAVE]

def salvar_nonce(nonce, caminho='nonce.bin'):
    with open(caminho, 'wb') as f:
        f.write(nonce)

def carregar_nonce(caminho='nonce.bin'):
    if os.path.exists(caminho):
        with open(caminho, 'rb') as f:
            return f.read()
    else:
        return None

def change_files(filename, cryptFn, block_size=16):
    with open(filename, 'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = cryptFn(raw_value)
            if len(raw_value) != len(cipher_value):
                raise ValueError(f'O valor cifrado {len(cipher_value)} tem um tamanho diferente do valor plano {len(raw_value)}')
            
            _file.seek(- len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)
