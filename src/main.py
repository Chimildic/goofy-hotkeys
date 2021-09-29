from os import path
from dotenv import load_dotenv
load_dotenv("client/.env")
load_dotenv("client/dev.env")

#TODO: add program version
if not path.isdir("client"):
    import sys
    from shutil import copytree

    base_path = getattr(sys, '_MEIPASS', path.dirname(path.abspath(__file__)))
    res_path = path.join(base_path, "client")
    copytree(res_path, "client")
else:
    #TODO: check if already starting other instance 
    from script_service import ScriptService
    ScriptService().start_listening()
