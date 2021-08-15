import discord
from discord.ext import commands
import os

intents = discord.Intents().default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Comando para enviar sugestões
# Pega o ID do canal e envia a sugestão do usuário 
# Utiliza o Embed pra deixar bonito
# Depois deleta a mensagem do usuário e retorna a confirmação do bot
@bot.command(pass_context=True)
async def sugestao(ctx, *, Msg='none'):
    channel = bot.get_channel(876547054577532968)
    embed=discord.Embed(title='Caixa de Sugestões', color=0xff0000, timestamp=ctx.message.created_at)
    embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
    embed.add_field(name="Mensagem:", value='```' + Msg + '```', inline=False)
    embed.set_footer(text='ID do Usuário: ' + str(ctx.author.id))
    await channel.send(embed=embed)   
    await ctx.message.delete()
    await ctx.send(ctx.author.mention + ' Sua sugestão foi enviada a admnistração.')

@bot.event
async def on_ready():
    print('Logamos com o {0.user}'.format(bot))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)  

bot.run(os.getenv('TOKEN'))

