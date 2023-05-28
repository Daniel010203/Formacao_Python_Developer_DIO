import hashlib

string = input('Digite o texto a ser gerado a hash: ')

resultado_md5 = hashlib.md5(string.encode('utf-8'))
resultado_sha1 = hashlib.sha1(string.encode('utf-8'))
resultado_sha256 = hashlib.sha256(string.encode('utf-8'))
resultado_sha512 = hashlib.sha512(string.encode('utf-8'))

print('-' * 20)
print('O hash MD5 da string é: ') 
print(resultado_md5.hexdigest())
print('-' * 20)
print('O hash SHA1 da string é: ') 
print(resultado_sha1.hexdigest())
print('-' * 20)
print('O hash SHA256 da string é: ') 
print(resultado_sha256.hexdigest())
print('-' * 20)
print('O hash SHA512 da string é: ') 
print(resultado_sha512.hexdigest())
print('-' * 20)