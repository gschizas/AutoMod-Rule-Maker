# -*- mode: python -*-

block_cipher = None

import praw
praw_ini_path = praw.__path__[0] + '\\praw.ini'
print(praw_ini_path)
del praw

a = Analysis(['AutoMod Rule Maker.py'],
             pathex=['.'],
             binaries=None,
             datas=[(praw_ini_path, '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='AutoMod Rule Maker',
          debug=False,
          strip=False,
          upx=False,
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='AutoMod Rule Maker')
