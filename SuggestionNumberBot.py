#created by pelllaeon :: github.com/pelllaeon
#MIT License Copyright 2020
#Written for Python 3.7
import discord #Discord API wrapper
import random #on_message requires this package
import params #Self-made module for sensitive data
import csv #for csv management
from csv import writer #may have been included above - I don't understand Python very well

client = discord.Client() #call Discord wrapper


@client.event
async def on_ready(): #once loaded in, send image and disconnect
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        if message.channel.id == params.WatchChannel:
            print(message.id)
            with open('suggestions_list.txt') as csv_file:
               csvReader = csv.reader(csv_file, delimiter=',')
               for line in csvReader:
                   pass
               newLine = line
               newLine[4] = message.id
            with open('suggestions_list_bot.txt', 'a+',newline='') as writeObj:
                csvWriter = writer(writeObj)
                csvWriter.writerow(newLine)
        else:
            return

    WatchChannel = client.get_channel(params.WatchChannel)
    if message.content.startswith('!sug') and message.channel.id==params.WatchChannel:
        useable = message.content[5:]
        print(useable)

        with open('suggestions_list.txt') as csv_file:
           csvReader = csv.reader(csv_file, delimiter=',')
           for line in csvReader:
               pass
           lastLine = line
        recentToken = int(lastLine[0])+1
        with open('suggestions_list.txt', 'a+',newline='') as writeObj:
            csvWriter = writer(writeObj)
            row = str(recentToken) +","+ useable
            print(row)
            print(message.id)
            print(message.guild.id)
            csvWriter.writerow([str(recentToken)]+[useable]+[message.author.display_name]+[message.channel.id]+[message.id]+[message.guild.id])
        await message.delete()
        await message.channel.send('Suggestion number: '+str(recentToken)+" || Credit to "+message.author.display_name +"\n"+useable+"\nBot commands: !sug - make new suggestion | !resug <number> - recall old suggestion")
    if message.content.startswith('!resug') and message.channel.id==params.PostChannel:
        useable = message.content[7:]
        print(useable)

        with open('suggestions_list_bot.txt') as csv_file:
           csvReader = csv.reader(csv_file, delimiter=',')
           for line in csvReader:
               if line[0]!=useable:
                   pass
               if line[0]==useable:
                   break
           lastLine = line
           sendValue = 'Suggestion number: '+str(lastLine[0])+" || Credit to "+lastLine[2] +"\nhttps://discordapp.com/channels/"+lastLine[5]+"/"+lastLine[3]+"/"+lastLine[4]
           print(sendValue)
        await message.channel.send(sendValue)


client.run(params.TOKEN) #execute bot actions