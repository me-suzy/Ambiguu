# BEBE Task Recorder - PyPI Package

Acest folder conține pachetul Python pregătit pentru publicare pe PyPI.

## Structura

```
Librarie PyPi/
├── bebe_task_recorder/      # Pachetul principal
│   ├── __init__.py          # Initializare pachet
│   └── bebe_gui.py          # Codul principal
├── setup.py                  # Configurare pachet
├── MANIFEST.in              # Fișiere de inclus
├── README.md                # Documentație
├── LICENSE                  # Licență MIT
├── requirements.txt        # Dependențe
├── test_install.py          # Script de test
└── build_and_test.bat      # Script build și test
```

## Instalare Locală (pentru testare)

```bash
cd "Librarie PyPi"
python -m pip install -e .
```

Sau folosind scriptul:
```bash
build_and_test.bat
```

## Testare

După instalare, testează:
```bash
python test_install.py
```

Sau rulează aplicația:
```bash
bebe-task-recorder
```

## Build pentru PyPI

```bash
python -m pip install --upgrade build twine
python -m build
```

## Upload pe PyPI

### Test PyPI (pentru testare):
```bash
python -m twine upload --repository testpypi dist/*
```

### PyPI Real:
```bash
python -m twine upload dist/*
```

**Notă**: Vei avea nevoie de cont PyPI și token de autentificare.

## Verificare înainte de upload

1. ✅ Testează instalarea locală: `python test_install.py`
2. ✅ Verifică structura: `python setup.py check`
3. ✅ Testează build: `python -m build`
4. ✅ Verifică fișierele: `python -m twine check dist/*`

## Utilizare după instalare

```python
from bebe_task_recorder import TaskRecorder, TaskPlayer, main

# Rulează GUI
main()

# Sau folosește programatic
recorder = TaskRecorder()
recorder.start_recording()
# ... perform actions ...
events = recorder.stop_recording()

player = TaskPlayer()
player.play_events(events)
```

