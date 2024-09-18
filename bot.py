# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot

import sys
import os
import json
import asyncio

from utilities.utilities import getConfig
from utilities.tgAccount import tgAccount

MasterCryptoFarmBot_Dir = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__ + "/../"))
)

sys.path.append(MasterCryptoFarmBot_Dir)

try:
    import utils.logColors as lc
    from utils.database import Database
    import utils.modules as modules
    import config as cfg
except Exception as e:
    print(f"\033[31mThis module is designed for MasterCryptoFarmBot.\033[0m")
    print(f"\033[31mYou cannot run this module as a standalone application.\033[0m")
    print(
        f"\033[31mPlease install MasterCryptoFarmBot first, then place this module inside the modules directory.\033[0m"
    )
    print(
        "\033[31mGitHub: \033[0m\033[32mhttps://github.com/masterking32/MasterCryptoFarmBot\033[0m"
    )
    exit(1)


async def main():
    module_dir = os.path.dirname(os.path.abspath(__file__))
    log = lc.getLogger(module_dir + "/bot.log")
    Modules = modules.Module(log)
    module_name = Modules.get_ModuleName()
    log.info(f"{lc.g}🔧 {module_name} module is running ...{lc.rs}")

    bot_globals = {
        "module_name": module_name,
        "mcf_dir": MasterCryptoFarmBot_Dir,
        "module_dir": module_dir,
    }

    db = Database(MasterCryptoFarmBot_Dir + "/database.db", log)
    is_module_disabled = Modules.is_module_disabled(db, module_name)
    db.Close()
    if is_module_disabled:
        log.info(f"{lc.y}🚫 {module_name} module is disabled!{lc.rs}")
        exit(0)

    log.info(f"{lc.g}👤 Checking for Telegram accounts ...{lc.rs}")

    if not os.path.exists(MasterCryptoFarmBot_Dir + "/telegram_accounts/accounts.json"):
        log.error(f"{lc.r}└─ 🔴 Please add your telegram accounts first!{lc.rs}")
        exit(1)

    with open(MasterCryptoFarmBot_Dir + "/telegram_accounts/accounts.json", "r") as f:
        Accounts = json.load(f)

    if not Accounts or len(Accounts) == 0:
        log.error(f"{lc.r}└─ 🔴 Please add your telegram accounts first!{lc.rs}")
        exit(1)

    log.info(
        f"{lc.g}└─ 👤 {lc.rs + lc.c + "[" + str(len(Accounts)) + "]" + lc.rs + lc.g } Telegram account(s) found!{lc.rs}"
    )

    if cfg.config["telegram_api"]["api_id"] == 1234 or cfg.config["telegram_api"]["api_hash"] == "":
        log.error(f"{lc.r}🔴 Please add your Telegram API ID and API Hash to the config.py file!{lc.rs}")
        exit(1)

    bot_globals["telegram_api_id"] = cfg.config["telegram_api"]["api_id"]
    bot_globals["telegram_api_hash"] = cfg.config["telegram_api"]["api_hash"]

    while True:
        for account in Accounts:
            if "disabled" in account and account["disabled"]:
                log.info(f"{lc.y}❌ Account {account['session_name']} is disabled!{lc.rs}")
                continue

            tg = tgAccount(bot_globals, log, account['session_name'])
            web_app_data = await tg.run()
            if web_app_data is None:
                log.error(f"{lc.r}└─ ❌ Account {account['session_name']} failed to load!{lc.rs}")
                continue

            log.info(f"{lc.g}└─ ✅ Account {account['session_name']} is ready!{lc.rs}")

            print(web_app_data)


        log.info(f"{lc.g}🔄 Checking again in {getConfig('check_interval', 3600)} seconds ...{lc.rs}")
        await asyncio.sleep(getConfig("check_interval", 3600))



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print()
        print("Exiting ...")
        exit(0)
    except Exception as e:
        print(e)
        exit(1)
