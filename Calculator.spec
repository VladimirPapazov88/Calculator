# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['calc.py'],
             pathex=['/Volumes/My Files/Python_ПРОЕКТЫ/Calculator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Calculator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='res/icon.icns')
app = BUNDLE(exe,
             name='Calculator.app',
             icon='res/icon.icns',
             bundle_identifier=None)
