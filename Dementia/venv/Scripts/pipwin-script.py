#!C:\Users\a_ade\Documents\Spring2022\CSC340-Wed-Fri-240PM-420PM\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pipwin==0.5.2','console_scripts','pipwin'
__requires__ = 'pipwin==0.5.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pipwin==0.5.2', 'console_scripts', 'pipwin')()
    )
