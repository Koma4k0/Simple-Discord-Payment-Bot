import discord, colorama, sys, os, json, pystyle
from discord.ui import Button, View
from discord.ext import commands, tasks
from discord import Option
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System


os.system("title Discord Payment Bot")

bot = discord.Bot(intents=discord.Intents.all())
config = json.load(open("settings.json", encoding="utf-8"))

#################################
###///---Payment Configs---\\\###
#################################
paypaluser = "Your_PayPal_Email"
ethaddy = "Your_ETH_Address"
btcaddy = "Your_BTC_Address"
ltcaddy = "Your_LTC_Address"
cashappaddy = "Your_Cashtag"
venmoaddy = "Your_Venmo_Addy"
amazoncard1 = "https://www.g2a.com/best-deals/amazon-gift-cards" # Website to purchase amazon gift cards from, you can change these to whatever you want!
amazoncard2 = "https://dundle.com/amazon/"
cryptovoucherurl = "https://cryptovoucher.io/" # Crypto Voucher Website

###############################
###///---Color Configs---\\\###
###############################
maincolor = 0xFF0000
btccolor = 0xf1c40f
ltccolor = 0x979c9f
paypalcolor = 0x0084ff
ethcolor = 0x979c9f
cashappcolor = 0x2ecc71
venmocolor = 0x3498db
amazoncolor = 0xe67e22
cryptovouchercolor = 0x7464cc

###############################
###///---Image Configs---\\\###
###############################
paypalimage = "https://seeklogo.com/images/P/paypal-logo-481A2E654B-seeklogo.com.png"
btcimage = "https://seeklogo.com/images/B/bitcoin-logo-DDAEEA68FA-seeklogo.com.png"
ethimage = "https://seeklogo.com/images/E/ethereum-logo-DE26DD608D-seeklogo.com.png"
ltcimage = "https://seeklogo.com/images/L/litecoin-logo-09A62FE1FB-seeklogo.com.png"
cashappimage = "https://seeklogo.com/images/C/cash-app-logo-A39DD086EB-seeklogo.com.png"
venmoimage = "https://cdn.discordapp.com/attachments/1136891544683696128/1141357822098018374/venmo_1.png"
amazonimage = "https://cdn.discordapp.com/attachments/1126315327488262245/1141904744969941032/amazon-dark-logo-png-transparent.png"
cryptovoucherimage = "https://cdn.discordapp.com/attachments/1152283745110458418/1155914306555232256/cryptovoucher.png"

################################
###///---Slash Commands---\\\###
################################

#PayPal              
@bot.slash_command(guild_ids=[config["guildID"]], name='paypal', description='send paypal')
async def paypal(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    if not str(ctx.author.id) in config["botAdminId"]:
        return await ctx.respond(embed=discord.Embed(description="Only admins can use this command.", color=maincolor))
    embed = discord.Embed(title=f"PayPal", description=f"Send **${amount} USD** to \n```{paypaluser}```",
                          color=paypalcolor)
    embed.set_thumbnail(url=f"{paypalimage}")
    await ctx.response.send_message(embed=embed)
    print(colorama.Fore.RED + 'Sent PayPal')

#BTC
@bot.slash_command(guild_ids=[config["guildID"]], name='btc', description='send btc addy')
async def bitcoin(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    if not str(ctx.author.id) in config["botAdminId"]:
        return await ctx.respond(embed=discord.Embed(description="Only admins can use this command.", color=maincolor))
    embed = discord.Embed(title=f"Bitcoin", description=f"Send **${amount}USD** to \n```{btcaddy}```",
                          color=btccolor)
    embed.set_thumbnail(url=f"{btcimage}")
    await ctx.response.send_message(embed=embed)
    print(colorama.Fore.RED + 'Sent Bitcoin')

#ETH
@bot.slash_command(guild_ids=[config["guildID"]], name='eth', description='send eth addy')
async def eth(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    if not str(ctx.author.id) in config["botAdminId"]:
        return await ctx.respond(embed=discord.Embed(description="Only admins can use this command.", color=maincolor))
    embed = discord.Embed(title=f"ETH", description=f"Send **${amount}USD** to \n```{ethaddy}```",
                          color=ethcolor)
    embed.set_thumbnail(url=f"{ethimage}")
    await ctx.response.send_message(embed=embed)
    print(colorama.Fore.RED + 'Sent ETH')

#LTC
@bot.slash_command(guild_ids=[config["guildID"]], name='ltc', description='send ltc addy')
async def ltc(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    if not str(ctx.author.id) in config["botAdminId"]:
        return await ctx.respond(embed=discord.Embed(description="Only admins can use this command.", color=maincolor))
    embed = discord.Embed(title=f"LTC", description=f"Send **${amount}USD** to \n```{ltcaddy}```",
                          color=ltccolor)
    embed.set_thumbnail(url=f"{ltcimage}")
    await ctx.response.send_message(embed=embed)
    print(colorama.Fore.RED + 'Sent LTC')

#Cashapp
@bot.slash_command(guild_ids=[config["guildID"]], name='cashapp', description='send cashapp addy')
async def ltc(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    if not str(ctx.author.id) in config["botAdminId"]:
        return await ctx.respond(embed=discord.Embed(description="Only admins can use this command.", color=maincolor))
    embed = discord.Embed(title=f"Cashapp", description=f"Send **${amount}USD** to \n```{cashappaddy}```",
                          color=cashappcolor)
    embed.set_thumbnail(url=f"{cashappimage}")
    await ctx.response.send_message(embed=embed)
    print(colorama.Fore.RED + 'Sent Cashapp')

#Venmo
@bot.slash_command(guild_ids=[config["guildID"]], name='venmo', description='send venmo addy')
async def ltc(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),

):
    if not str(ctx.author.id) in config["botAdminId"]:
        return await ctx.respond(embed=discord.Embed(description="Only admins can use this command.", color=maincolor))
    embed = discord.Embed(title=f"venmo", description=f"Send **${amount}USD** to \n```{venmoaddy}```",
                          color=venmocolor)
    embed.set_thumbnail(url=f"{venmoimage}")
    await ctx.response.send_message(embed=embed)
    print(colorama.Fore.RED + 'Sent Venmo')

#Amazon Gift Card
@bot.slash_command(guild_ids=[config["guildID"]], name='amazon', description='send amazon gift card links')
async def amazon(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),
    
):
    if not str(ctx.author.id) in config["botAdminId"]:
        return await ctx.respond(embed=discord.Embed(description="Only admins can use this command.", color=maincolor))
    embed = discord.Embed(title=f"Amazon Gift Card", description=f"Buy a **${amount}** Amazon Gift Card (Must be in USD) \n\nI will list a few website options below: \n**{amazoncard1}** \n **{amazoncard2}**",
                          color=amazoncolor)
    embed.set_thumbnail(url=f"{amazonimage}")
    await ctx.response.send_message(embed=embed)
    print(colorama.Fore.RED + 'Sent Amazon')

#Cryptovoucher.io
#Amazon Gift Card
@bot.slash_command(guild_ids=[config["guildID"]], name='crypto-voucher', description='send cryptovoucher.io')
async def amazon(ctx,
                 amount: Option(str, 'how much money you want them to send to you',
    required=True, default=None),
    
):
    if not str(ctx.author.id) in config["botAdminId"]:
        return await ctx.respond(embed=discord.Embed(description="Only admins can use this command.", color=maincolor))
    embed = discord.Embed(title=f"Cryptovoucher.io", description=f"Buy a **${amount}** Crypto Voucher (Must be in USD)\n\nYou must buy it from this website:\n**{cryptovoucherurl}**",
                          color=cryptovouchercolor)
    embed.set_thumbnail(url=f"{cryptovoucherimage}")
    await ctx.response.send_message(embed=embed)
    print(colorama.Fore.RED + 'Sent Crypto Voucher')

#Bot's Ping
@bot.slash_command(guild_ids=[config["guildID"]], name='ping', description='Sends the bots ping')
async def latency(ctx: discord.ApplicationContext):
    latency = bot.latency * 1000
    await ctx.send(f"My latency is `{latency}ms`")
    print({bot.latency})
    print(colorama.Fore.MAGENTA + 'Sent')

#Change Bot Activity
@bot.command(guild_ids=[config["guildID"]], name="activity", description="Changes the activity of the bot.")
@commands.guild_only()
async def activity(ctx, activity):
    if not str(ctx.author.id) in config["botOwnerId"]:
        return await ctx.respond(embed=discord.Embed(description="You must be an owner to use this command.", color=maincolor))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activity))
    return await ctx.respond(embed=discord.Embed(description=f"Changed activity to {activity}", color=maincolor))



print(colorama.Fore.BLUE + "██████╗░░█████╗░██╗░░░██╗███╗░░░███╗███████╗███╗░░██╗████████╗██████╗░░█████╗░████████╗")
print(colorama.Fore.BLUE + "██╔══██╗██╔══██╗╚██╗░██╔╝████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝")
print(colorama.Fore.BLUE + "██████╔╝███████║░╚████╔╝░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██████╦╝██║░░██║░░░██║░░░")
print(colorama.Fore.BLUE + "██╔═══╝░██╔══██║░░╚██╔╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██╔══██╗██║░░██║░░░██║░░░")
print(colorama.Fore.BLUE + "██║░░░░░██║░░██║░░░██║░░░██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░██████╦╝╚█████╔╝░░░██║░░░")
print(colorama.Fore.BLUE + "╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚═════╝░░╚════╝░░░░╚═╝░░░")
print(colorama.Fore.BLUE + "                                Bot Made By Koma4k                                     ")

bot.run(config["bottoken"])
