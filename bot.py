import discord
from discord.ext import commands
import asyncio
import random
import os

TOKEN = os.environ.get('TOKEN')
PREFIX = '+'

# Fontes reduzidas (menos caracteres especiais)
FONTES = [
    "Eternal é Vida!", "🔥 Eternal é Vida 🔥", "⭐ Eternal é Vida ⭐",
    "✨ Eternal é Vida ✨", "💀 Eternal é Vida 💀", "Eternal é Vida!",
    "ETERNAL É VIDA!", "✦ Eternal é Vida ✦", "♛ Eternal é Vida ♛"
]

intents = discord.Intents.default()  # Mais leve que Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Eternal é Vida!"))

@bot.command(name='EtnX')
async def etnx(ctx):
    # Confirmação antes de destruir tudo
    await ctx.send("⚠️ Isso vai apagar TODOS os canais e criar novos. Confirmar? (digite `confirmar` em 10s)")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() == "confirmar"
    
    try:
        await bot.wait_for('message', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("❌ Comando cancelado!")
        return
    
    await ctx.send("🚀 Iniciando... (isso pode levar alguns minutos)")
    
    try:
        # Apagar canais existentes (mais rápido)
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                await asyncio.sleep(0.3)  # Delay reduzido mas seguro
            except:
                continue
        
        # Criar canais (quantidade reduzida)
        total_canais = 200  # Reduzido de 1500 para 200
        mensagens_por_canal = 30  # Reduzido de 150 para 30
        
        for i in range(total_canais):
            try:
                canal = await ctx.guild.create_text_channel(f"eternal-{i+1}")
                
                # Envia menos mensagens
                for _ in range(mensagens_por_canal):
                    fonte = random.choice(FONTES)
                    await canal.send(f"**{fonte}**")
                    await asyncio.sleep(0.2)  # Delay maior pra evitar rate limit
                
                # Progresso
                if (i + 1) % 10 == 0:
                    await ctx.send(f"📊 Progresso: {i+1}/{total_canais}")
                    await asyncio.sleep(1)
                
            except discord.errors.HTTPException:
                await ctx.send(f"⚠️ Rate limit atingido! Pausando 5s...")
                await asyncio.sleep(5)
                continue
        
        await ctx.send(f"✅ Concluído! {total_canais} canais criados com {mensagens_por_canal} mensagens cada.")
        
    except Exception as e:
        await ctx.send(f"❌ Erro: {e}")

if __name__ == "__main__":
    bot.run(TOKEN)
