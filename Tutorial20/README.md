## Pre-requistes

Install pyinstaller

```
pip3 install pyinstaller
pip3 install PyQt5 --user
```

## Packaging to Exe

__On Windows__
```
pyinstaller calc.py -w
```

__On MacOS__
```
pyinstaller calc.py -w --onefile
```

After executing above, change `.spec` file  

add some dependency as below.  

```calc.spec
from kivy_deps import sdl2, glew
```

Between pyz and exec paste below data.  
```
a.data += [('Code\calc.kv','E:\\guiapp\\kivy_learning\\Tutorial20\calc.kv','DATA')]
```
__Example Specfile__

```
from kivy_deps import sdl2, glew
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['calc.py'],
             pathex=['E:\\guiapp\\kivy_learning\\Tutorial20\\WorkingDirectory'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.data += [('Code\calc.kv','E:\\guiapp\\kivy_learning\\Tutorial20\\WorkingDirectory\calc.kv','DATA')]

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='calc',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,
Tree('E:\\guiapp\\kivy_learning\\Tutorial20\\WorkingDirectory')
               a.binaries,
               a.zipfiles,
               a.datas, 
               *[Tree(p) for p in
               (sdl2.dep_bins +
                glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='calc')

```
