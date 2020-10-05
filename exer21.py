from pygame import mixer

mixer.init()

# definir caminho do arquivo mp3, pois aqui sugere que o arquivo esta no mesmo diretorio
mixer.music.load('exer21.mp3')
mixer.music.play()

input('Agora você escuta?')
