# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['ldoce5viewer.py'],
    pathex=[],
    binaries=[
        ('/opt/homebrew/lib/python3.11/site-packages/PySide6/Qt/plugins/multimedia', 'PySide6/Qt/plugins/multimedia'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libpostproc.57.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavdevice.60.1.100.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libswscale.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavcodec.60.3.100.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libpostproc.57.1.100.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libswscale.7.1.100.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libswscale.7.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavformat.60.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libswresample.4.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavfilter.9.3.100.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavformat.60.3.100.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavformat.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavutil.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavcodec.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavcodec.60.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavutil.58.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavfilter.9.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libswresample.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavdevice.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libpostproc.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libswresample.4.10.100.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavfilter.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavutil.58.2.100.dylib', '.'),
        ('/opt/homebrew/Cellar/ffmpeg/6.0_1/lib/libavdevice.60.dylib', '.')
    ],
    datas=[('ldoce5viewer/static', 'static')],
    hiddenimports=[],
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
    [],
    exclude_binaries=True,
    name='ldoce5viewer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ldoce5viewer',
)
app = BUNDLE(
    coll,
    name='LDOCE5 Viewer.app',
    icon='./ldoce5viewer/qtgui/resources/ldoce5viewer.icns',
    bundle_identifier=None,
)
