# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['..\\main.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\data\\fish_icon.ico', 'data'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\values.json', 'run_data'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\caught_fish\\discard_gray.png', 'run_data\\images\\cv_templates\\caught_fish'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\caught_fish\\keep_orange.png', 'run_data\\images\\cv_templates\\caught_fish'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\caught_fish\\release_gray.png', 'run_data\\images\\cv_templates\\caught_fish'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\0.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\0_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\1.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\1_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\2.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\2_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\3.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\3_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\4.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\4_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\5.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\5_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\6.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\6_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\7.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\7_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\8.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\8_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\9.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\digits\\9_dark.png', 'run_data\\images\\cv_templates\\digits'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\pop_ups\\buy_orange.png', 'run_data\\images\\cv_templates\\pop_ups'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\pop_ups\\claim_green.png', 'run_data\\images\\cv_templates\\pop_ups'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\pop_ups\\close_gray.png', 'run_data\\images\\cv_templates\\pop_ups'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\pop_ups\\close_gray_2.png', 'run_data\\images\\cv_templates\\pop_ups'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\pop_ups\\close_orange.png', 'run_data\\images\\cv_templates\\pop_ups'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\pop_ups\\close_orange_2.png', 'run_data\\images\\cv_templates\\pop_ups'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\pop_ups\\extend_orange.png', 'run_data\\images\\cv_templates\\pop_ups'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\pop_ups\\ok_orange.png', 'run_data\\images\\cv_templates\\pop_ups'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\pop_ups\\x.png', 'run_data\\images\\cv_templates\\pop_ups'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\cv_templates\\time_warp\\next_morning_gray.png', 'run_data\\images\\cv_templates\\time_warp'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\gui_elements\\check_mark.png', 'run_data\\images\\gui_elements'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\gui_elements\\fish_logo.png', 'run_data\\images\\gui_elements'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\gui_elements\\pencil.png', 'run_data\\images\\gui_elements'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\gui_elements\\question_mark.png', 'run_data\\images\\gui_elements'), ('C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\run_data\\images\\gui_elements\\wood_texture.png', 'run_data\\images\\gui_elements')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Autofish-v0.1.5',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Khalid\\Mini-porject\\Autofish-Fishing-Planet\\data\\fish_icon.ico'],
)
