#!/usr/bin/python3.11
import os

def descobrir(caminho_inicial):
    extensoes = [
        # Arquivos do Sistema
        'exe', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',

        # Imagens
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw',

        # Áudios
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',

        # Vídeos
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',

        # Microsoft Office
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',

        # OpenOffice, Adobe, Latex, Markdown, etc
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md',

        # Dados estruturados e config
        'yml', 'yaml', 'json', 'xml', 'csv',

        # Bancos de dados e imagens de disco
        'db', 'sql', 'dbf', 'mdb', 'iso',

        # Tecnologias web
        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',

        # Código em C e C++
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',

        # Código fonte Java
        'java', 'class', 'jar',

        # Scripts de sistemas Windows
        'ps', 'bat', 'vb',

        # Scripts de sistemas Unix
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',

        # Outros tipos de código fonte
        'go', 'py', 'pyc', 'bf', 'coffee',

        # Arquivos compactados e Backups
        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',
    ]
    
    for dirpath, dirs, files in os.walk(caminho_inicial):
        for _file in files:
            caminho_absoluto = os.path.abspath(os.path.join(dirpath, _file))
            extensao = caminho_absoluto.split('.')[-1].lower()  # Para garantir que a extensão esteja em minúsculas
            if extensao in extensoes:
                yield caminho_absoluto

# Executado somente quando você executa o módulo diretamente
if __name__ == '__main__':
    arquivos_encontrados = descobrir(os.getcwd())
    for arquivo in arquivos_encontrados:
        print(arquivo)
