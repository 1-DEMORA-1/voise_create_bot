import discord
from discord.ext import commands, tasks
import asyncio

intents = discord.Intents.default()
intents.members = True  
intents.voice_states = True  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} запущен')
    update_status.start()  

@tasks.loop(seconds=10)
async def update_status():
    """Обновляет статус бота каждые 10 секунд."""
    total_members = sum(len(guild.members) for guild in bot.guilds)
    await bot.change_presence(activity=discord.Game(f'{total_members} участников'))

@bot.event
async def on_voice_state_update(member, before, after):
    """Срабатывает, когда пользователь заходит или выходит из голосового канала."""
    if after.channel and after.channel.id == 1285898586927927327:
        # Создаем новый приватный канал
        overwrites = {
            member.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True)
        }
        
        category = after.channel.category
        private_channel = await category.create_text_channel(f'Приватка {member.name}', overwrites=overwrites)


        await member.move_to(private_channel)


        while len(private_channel.members) > 0:
            await asyncio.sleep(1)
        
        await asyncio.sleep(2) 
        

        if len(private_channel.members) == 0:
            await private_channel.delete()

@bot.event
async def on_voice_state_update(member, before, after):
    """Срабатывает, когда пользователь заходит или выходит из голосового канала."""
    if after.channel and after.channel.id == 1285898586927927327:

        overwrites = {
            member.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            member: discord.PermissionOverwrite(read_messages=True)
        }
        
        category = after.channel.category
        private_channel = await category.create_voice_channel(f'Приватка {member.name}', overwrites=overwrites)


        await member.move_to(private_channel)


        while len(private_channel.members) > 0:
            await asyncio.sleep(1)
        
        await asyncio.sleep(2)  #
        

        if len(private_channel.members) == 0:
            await private_channel.delete()


TOKEN = 'Ваш токен'
bot.run(TOKEN)