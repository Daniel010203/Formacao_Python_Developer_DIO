import ctypes

atributos_acultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('14_ocultar.txt', atributos_acultar)

if retorno:
    print('Arquivo foi ocultado com sucesso!')
else:
    print('Arquivo não foi ocultado.')