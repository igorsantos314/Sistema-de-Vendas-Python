import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": [
    "tkinter", 
    "sqlite3",
    "classDataBase",
    "interfaceVendas",
    "interfaceContabilidade",
    "interfaceListaProdutos",
    "interfaceCadastroProduto",
    "ModulePrint"
    ]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="IGTEC - Sistema de Vendas",
    version="1.0.0",
    description="Sistema de Vendas",
    options={"build_exe": build_exe_options},
    executables=[Executable("interfaceMenu.py", base=base, icon="icon.ico")]
)