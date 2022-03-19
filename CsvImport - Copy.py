import discord
import pandas as pd
import datetime
import csv


token = "hidden"

client = discord.Client()


file_csv = pd.read_csv("file location")

num_row = file_csv.shape[0]
num_col = file_csv.shape[1]
results = file_csv[["player", " class", " DKP"]]
dictionary = results.to_dict('index')
print(dictionary)
results = results.sort_values(by=[' DKP'], ascending=False)

# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    # pri
# nt(results)
    # print(num_row)


@client.event
async def on_message(message):
    valid_users = ["Rory#6052"]
    if str(message.author in valid_users):
        pass

    channels = ["dkp"]
    if str(message.channel) in channels:
        if message.content.find("!display") != -1:
            embed = discord.Embed(Title="DKP", description="DKP", color=0x00ff00)
            for row in range(num_row):
                embed.add_field(name=results.iloc[row]['player'], value=results.iloc[row][' DKP'], inline=True)
            embed.set_footer(text=f'{datetime.datetime.now().date()}')
            await message.channel.send(embed=embed)
            embed2 = discord.Embed(Title="DKP", description="DKP", color=0x00ff00)
            for row in range(num_row-25):
                embed2.add_field(name=results.iloc[24+row]['player'], value=results.iloc[24+row][' DKP'], inline=True)
            embed2.set_footer(text=f'{datetime.datetime.now().date()}')
            await message.channel.send(embed=embed2)
            embed3 = discord.Embed(Title="DKP", description="DKP", color=0x00ff00)
            for row in range(num_row-50):
                embed3.add_field(name=results.iloc[49+row]['player'], value=results.iloc[49+row][' DKP'], inline=True)
            embed3.set_footer(text=f'{datetime.datetime.now().date()}')
            await message.channel.send(embed=embed3)
    else:
        pass

client.run(token)
