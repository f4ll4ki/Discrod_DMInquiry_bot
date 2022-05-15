import discord

client = discord.Client()


token = '토큰'


@client.event
async def on_ready():
    print("성공")
    game = discord.Game('서버 문의 답변')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.guild is None:
        if message.author.bot:
            return
        else:
            embed = discord.Embed(colour=discord.Colour.red(), timestamp=message.created_at)
            embed.add_field(name='문의', value=message.author, inline=False)
            embed.add_field(name='수신', value=message.content, inline=False)
            embed.set_footer(text=f'" =발신 <@{message.author.id}> text "')
            await client.get_channel(975261971731603499).send(f"``이름: {message.author}``\n``고유ID: ({message.author.id})``", embed=embed)

    if message.content.startswith('=발신'):
        if message.author.guild_permissions.manage_messages:
            msg = message.content[26:]
            await message.mentions[0].send(f"관리자 **{message.author.name}**님의 답장:\n```{msg}```")
            await message.channel.send(f'`{message.mentions[0]}`발신 완료')
        else:
            return
        
client.run(token)
