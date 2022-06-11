#IMPORTS BALA 
import discord
from discord.ext import commands
import datetime
import numpy as np 
import os
from PIL import Image
import keras
from keras.utils import load_img, img_to_array
import cv2

#BUSCANDO E DANDO LOAD NO MODELO TREINADO
path = "C:/Users/essec/Desktop/botIAZADA/Save/"
new_model = keras.models.load_model(os.path.join(path,"modelsave.h5"))

directory = "C:/Users/essec/Desktop/botIAZADA/PokemonData"
labels = os.listdir(directory)
nb = len(labels)
print(labels)


#CRIANDO UM GERENCIADOR DE COMANDOS PARA O BOT
bot = commands.Bot(command_prefix='>', description="Classificação de Pokemon")

#CRIANDO O COMANDO DE PREDICT
@bot.command()
async def pred(ctx):
    try:
        #SALVANDO A IMAGEM ENVIADA PELO USER NO DIRETORIO LOCAL
        await ctx.message.attachments[0].save('image.jpg')
        #LENDO A IMAGEM
        image = cv2.imread('C:/Users/essec/Desktop/botIAZADA/image.jpg')
        #DANDO RESIZE NA IMAGEM
        img = cv2.resize(image, (150, 150))
        #NORMALIZANDO A IMAGEM
        img=img/255.0
        img = np.expand_dims(img, axis=0)
        #DANDO O PREDICT
        pred = new_model.predict(img)
        #PRINTANDO O PREDICT
        label = np.argmax(pred,axis=1)
        await ctx.send(labels[label[0]])
    except IndexError:
        await ctx.send("Faltou alguma coisa boy...")



# SÒ PRA FICAR BONITINHO QUANDO O BOT ESTIVER ONLINE
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Positividade", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    print('To Vivo fml')


bot.run('TOKEN DO BOT ( SE PRECISAR É SÓ ME PEDIR NO PV DO DISCORD. Conta do discord: Kz#9651 ')




