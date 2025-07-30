# نویسنده سورس : سید محمد حسین موسوی رجا
# روبیکا : @O_and_ONE_01
# تلگرام : @Hacker123457890
from fast_rub import Client,Update,filters
import json,random,httpx,fake_useragent
bot=Client("anymamus_bot")
def open_file(name_file,type_file="dict"):
    try:
        with open(name_file,"r",encoding="utf-8") as file:
            return json.load(file)
    except:
        if type_file=="dict":
            with open(name_file,"w",encoding="utf-8") as file:
                file.write("{}")
            return {}
        else:
            with open(name_file,"w",encoding="utf-8") as file:
                file.write("[]")
            return []
def save_file(name_file,data):
    with open(name_file,"w",encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
list_ids=open_file("list_ids.json","list")
ids=open_file("ids.json")
i_send=open_file("i_send.json")
warns=open_file("warns.json")
bans=open_file("bans.json","list")
list_bans=open_file("list_bans.json",type_file="list")
CHAT_ID_owner="b0IS2Uw0DAc04aa76508d5d7640fa51f"
def chek_fohsh(text:str):
    with httpx.Client() as cl:
        kg=cl.get(f"https://api.parssource.ir/fohsh/?text={text}/",timeout=30,headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json",
})
        return ((kg).json())['result']['is_foshs']
@bot.on_message_updates(filters=filters.is_user())
async def main(message:Update):
    TEXT_MESSAGE=message.text
    CHAT_ID=message.chat_id
    GUID=message.sender_id
    if (GUID in list_bans) or (CHAT_ID in list_bans) or (CHAT_ID in bans):
        await bot.send_text(f"""✉️ پیام جدید از لیست ممنوعه ❌ :
{str(message)}""",CHAT_ID_owner)
        return None
    if CHAT_ID==CHAT_ID_owner and TEXT_MESSAGE.startswith("بن "):
        c_g=TEXT_MESSAGE.replace("بن ","")
        list_bans.append(c_g)
        save_file("list_bans.json",list_bans)
        await message.reply("کاربر با موفقیت بن شد ❌")
    await bot.send_text(f"""✉️ پیام جدید :
{str(message)}""",CHAT_ID_owner)
    await bot.add_commands('my_id',"آیدی شما برای ارسال چت ناشناس از بقیه به شما")
    await bot.set_commands()
    await bot.delete_commands()
    if TEXT_MESSAGE in ['ربات','/start']:
        await bot.add_listkeypad("100","Simple","شناسه چت من")
        await bot.send_message_keypad(CHAT_ID,"""سلام دوست عزیز 👋
برای ارسال پیام ناشناس لطفا شناسه چت ناشناس را مثل زیر وارد کنید :
/start?id=1234567890""",reply_to_message_id=message.message_id)
        await bot.delete_listkeypad()
    elif TEXT_MESSAGE in ["/my_id","شناسه چت","شناسه چت من","شناسه چتم"]:
        if not (CHAT_ID in list_ids):
            id_random=""
            for t in range(10):
                id_random+=str(random.randint(0,9))
            list_ids.append(CHAT_ID)
            ids[CHAT_ID]=id_random
            save_file("ids.json",ids)
            save_file("list_ids.json",list_ids)
        await message.reply("شناسه چت شما :")
        await message.reply(f"/start?id={ids[CHAT_ID]}")
    elif TEXT_MESSAGE.startswith("/start?id="):
        id=TEXT_MESSAGE.replace("/start?id=","")
        if id in ids.values():
            if (CHAT_ID in ids)==False or (ids[CHAT_ID]!=id):
                i_send[CHAT_ID]=id
                save_file("i_send.json",i_send)
                await message.reply("✉️ پیام خودت رو وارد کن :")
            else:
                await message.reply("اینکه آدم گاهی با خودش حرف بزنه هم خوبه :) اما اینجا نمیتونی با خودت حرف بزنی")
        else:
            await message.reply("خطا ! آیدی نامعتبر میباشد ❌ لطفا آیدی را درست وارد کنید.")
    else:
        if CHAT_ID in i_send:
            for t in ['@',"https://","http://",".com",".ir",".org"]:
                if t in TEXT_MESSAGE:
                    if CHAT_ID in warns:
                        warns[CHAT_ID]+=1
                    else:
                        warns[CHAT_ID]=1
                    await message.reply(f"""ارسال لینک/فحش در پیغام مجاز نیست ❌
اخطار های شما : {warns[CHAT_ID]}/3
در صورت پر شدن اخطار ها شما از ارسال پیام با ربات محروم میشوید.""")
                    if warns[CHAT_ID]==3:
                        bans.append(CHAT_ID)
                        warns[CHAT_ID]=0
                        await message.reply("شما به دلیل پر شدن اخطار هایتان از ربات بن شدید ❌ پشتیبانی ربات : @O_and_ONE_01")
                    save_file("bans.json",bans)
                    save_file("warns.json",warns)
                    return None
            if chek_fohsh(TEXT_MESSAGE):
                if CHAT_ID in warns:
                    warns[CHAT_ID]+=1
                else:
                    warns[CHAT_ID]=1
                await message.reply(f"""ارسال لینک/فحش در پیغام مجاز نیست ❌
اخطار های شما : {warns[CHAT_ID]}/3
در صورت پر شدن اخطار ها شما از ارسال پیام با ربات محروم میشوید.""")
                if warns[CHAT_ID]==3:
                    bans.append(CHAT_ID)
                    warns[CHAT_ID]=0
                    await message.reply("شما به دلیل پر شدن اخطار هایتان از ربات بن شدید ❌ پشتیبانی ربات : @O_and_ONE_01")
                save_file("bans.json",bans)
                save_file("warns.json",warns)
                return None
            for g,i in ids.items():
                if i==i_send[CHAT_ID]:
                    await bot.send_text(f"""✉️ پیام جدید داری :

{TEXT_MESSAGE}""",g)
                    await message.reply("پیامت با موفقیت ارسال شد ✅")
                    del i_send[CHAT_ID]
                    save_file("i_send.json",i_send)
                    return None
bot.run()
# نویسنده سورس : سید محمد حسین موسوی رجا
# روبیکا : @O_and_ONE_01
# تلگرام : @Hacker123457890
