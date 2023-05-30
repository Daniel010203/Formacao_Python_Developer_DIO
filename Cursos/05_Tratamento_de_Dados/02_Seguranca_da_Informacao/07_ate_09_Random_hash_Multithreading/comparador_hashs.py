import hashlib

arquivo_01 = '07_ate_09_Random_hash_Multithreading/a.txt'
arquivo_02 = '07_ate_09_Random_hash_Multithreading/b.txt'

hash_01 = hashlib.new('ripemd160')

hash_01.update(open(arquivo_01, 'rb').read())

hash_02 = hashlib.new('ripemd160')

hash_02.update(open(arquivo_02, 'rb').read())

if hash_01.digest() != hash_02.digest():
    print(f'O arquivo: {arquivo_01} é diferente do arquivo: {arquivo_02}')
else:
    print(f'O arquivo: {arquivo_01} é igual ao arquivo: {arquivo_02}')