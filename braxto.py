from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
import os
import json
import asyncio

async def getListOfGroups(client):
    try:
        dialogs = await client.get_dialogs()
        groups_info = []
        for dialog in dialogs:
            if dialog.is_group or dialog.is_channel:
                entity = await client.get_entity(dialog.id)
                can_send_messages = entity.default_banned_rights is None or not entity.default_banned_rights.send_messages
                if can_send_messages:
                    group_info = {'group_id': dialog.id, 'group_name': dialog.title}
                    groups_info.append(group_info)

        return groups_info
    except Exception as e:
        print(e)
        return []
async def getMessagesFromGroup(client, group_id):
    try:
        all_messages = []
        async for message in client.iter_messages(group_id):
            try:
                all_messages.append(message)
            except:
                pass
        return all_messages
    except Exception as e:
        print(e)
        return []
async def logUserBot():
    load_dotenv()
    api_id = int(14928473)
    api_hash = "f7d70d7692a50bfa13eba01bcefce904"
    phone_number = "51913004692"
    session_name = "bot_spammer"
    client = TelegramClient(session_name, api_id, api_hash)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input('Ingrese el código de verificación: '))
    await client.send_message("@spmBrxto", f'<b>Bot encendido</b>', parse_mode="HTML")
    spammer_group = int("-4228127390")
    spammer_group2 = int("-4131181971")

    while True:
        groups_info = await getListOfGroups(client)
        messages_list = await getMessagesFromGroup(client, spammer_group)
        special_messages_list = await getMessagesFromGroup(client, spammer_group2) # MENSAJES PARA GRUPOS DONDE NO DEJAN MANDAR TEXTO LARGO O PALABRAS ESPECIALES
            
        try:
            await client.send_message("@spmBrxto", f"<b>CANTIDAD DE MENSAJES CONSEGUIDOS PARA PUBLICAR</b> <code>{len(messages_list)-1}</code>",parse_mode="HTML")
        except:
            pass
            
        try:
            for i in groups_info:
                if i['group_name'] not in ["SAFEGUARD PAMBII RAIDS🐝🚀","PAMBII RAIDS🐝🚀🔥🌏🚨","DeepLink Protocol","@SOLTRENDING | Official","PAMBII","ESO BRAD | VIP MARZO","💎 Métodos VIP 💎","LP - Derecho registral","ESO BRAD | APUESTAS GRATUITAS","MetDox","Spam Especial","Spam 2024","RESPALDO🇵🇪BINS PERU","➳𝒀𝑨𝑷𝑬 𝑫𝑬 𝑬𝑺𝑻𝑨𝑭𝑨𝑫𝑶𝑹𝑬𝑺 ✧","QUEMANDO ESTAFADORES","𝐏𝐄𝐑Ú 𝐀𝐘𝐔𝐃𝐀","Referencias Elmer 💸","🎭 CANAL MUNDO STREAMING PERÚ 🇵🇪","TU MARKETPLACE"]:

                    if i['group_name'] in ["🇵🇪🧑🏼‍💻𝙋𝙀𝙍𝙐 𝘼𝙔𝙐𝘿𝘼🧑🏼‍💻🇵🇪","BINS PERU🇵🇪","COMPRA Y VENTA🇵🇪PERU","STREAMING LATINO GO","🇵🇪🧑🏼‍💻𝘽𝙐𝙎𝙌𝙐𝙀𝘿𝘼𝙎 𝙋𝙀𝙍𝙐🧑🏼‍💻🇵🇪"]:
                        j=0
                        for message_spam in special_messages_list:
                            j+=1
                            resultado = True
                            try:
                                await client.send_message(i["group_id"], message_spam)
                            except Exception as error:
                                await client.send_message("@spmBrxto", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                                resultado = False
                            if resultado:
                                await client.send_message("@spmBrxto", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                            await asyncio.sleep(20)
                            if j==3: break
                    else:
                        j=0
                        for message_spam in messages_list:
                            j+=1
                            resultado = True
                            try:
                                await client.send_message(i["group_id"], message_spam)
                            except Exception as error:
                                await client.send_message("@spmBrxto", f'<b>Error enviando mensajes a {i["group_id"]}</b> - <code>{i["group_name"]}<code>\nCausa:{error}',parse_mode="HTML")
                                resultado = False
                            if resultado:
                                await client.send_message("@spmBrxto", f'<b>Mensaje enviado a {i["group_id"]}</b> - <code>{i["group_name"]}</code>',parse_mode="HTML")  
                            await asyncio.sleep(10)
                            if j==4: break
            await client.send_message("@spmBrxto", f'<b>RONDA ACABADA</b>', parse_mode="HTML")
            await asyncio.sleep(300) 
        except:
            pass
    
            
if __name__ == "__main__":
    asyncio.run(logUserBot())