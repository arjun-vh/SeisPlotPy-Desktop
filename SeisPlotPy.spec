# -*- mode: python ; coding: utf-8 -*-
# SeisPlotPy PyInstaller Spec File - Clean Build

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Bundle the entire ui and core directories
        ('ui', 'ui'),
        ('core', 'core'),
        ('seisplotpy.ico', '.'),
    ],
    hiddenimports=[
        # Local packages
        'ui',
        'ui.seismic_view',
        'ui.header_tools',
        'ui.horizon_manager',
        'ui.dialogs',
        'core',
        'core.data_handler',
        'core.processing',
        # Scientific libraries often need explicit imports
        'scipy.special._cdflib',
        'scipy.special.cython_special',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='SeisPlotPy',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='seisplotpy.ico',
)
