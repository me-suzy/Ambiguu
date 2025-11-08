# BEBE Task Recorder - Exemple Practice

Acest folder conține exemple practice de utilizare a librariei BEBE Task Recorder.

## ⚠️ IMPORTANT: Privilegii Administrator

**Toate exemplele trebuie să ruleze cu privilegii de Administrator** pentru a înregistra taste din alte aplicații.

### Cum să rulezi cu Administrator:

**Opțiunea 1: Rulează direct (scripturile vor solicita automat admin)**
```bash
python example_1_simple_record_playback.py
```
Scriptul va detecta automat dacă nu ai privilegii și va solicita repornirea ca Administrator.

**Opțiunea 2: Folosește scriptul batch**
```bash
RUN_AS_ADMIN.bat 1
```

**Opțiunea 3: Click dreapta → "Run as Administrator"**
- Click dreapta pe script
- Selectează "Run as Administrator"

## Exemple Disponibile

### 1. `example_1_simple_record_playback.py`
**Cel mai simplu exemplu** - Înregistrează și redă acțiuni de bază.

```bash
python example_1_simple_record_playback.py
```

**Ce face:**
- Înregistrează acțiuni pentru 5 secunde
- Salvează task-ul în JSON
- Redă task-ul înregistrat

---

### 2. `example_2_save_load_task.py`
**Salvare și încărcare task-uri** - Gestionează task-uri salvate.

```bash
python example_2_save_load_task.py
```

**Ce face:**
- Înregistrează un task
- Salvează în fișier JSON
- Încarcă task-ul salvat
- Listează toate task-urile salvate

---

### 3. `example_3_automation_workflow.py`
**Automatizare workflow** - Redă acțiuni de mai multe ori.

```bash
python example_3_automation_workflow.py
```

**Ce face:**
- Înregistrează un workflow complet
- Redă workflow-ul de mai multe ori
- Configurare viteze și repetări
- Ideal pentru sarcini repetitive

---

### 4. `example_4_programmatic_control.py`
**Control programatic** - Folosește callback-uri pentru feedback.

```bash
python example_4_programmatic_control.py
```

**Ce face:**
- Înregistrare cu feedback în timp real
- Redare cu feedback în timp real
- Statistici evenimente
- Control complet programatic

---

### 5. `example_5_gui_app.py`
**Interfață grafică** - Pornește GUI-ul complet.

```bash
python example_5_gui_app.py
```

**Ce face:**
- Deschide interfața grafică completă
- Toate funcționalitățile disponibile
- Cel mai ușor de folosit

---

## Instalare

Asigură-te că ai instalat libraria:

```bash
pip install bebe-task-recorder
```

## Utilizare Rapidă

### Cel mai simplu exemplu:

```python
from bebe_task_recorder import TaskRecorder, TaskPlayer, is_admin, run_as_admin
import time
import sys

# IMPORTANT: Verifică privilegii administrator
if not is_admin():
    print("Repornind cu privilegii de administrator...")
    run_as_admin()
    sys.exit()

# Înregistrare
recorder = TaskRecorder()
recorder.start_recording()
print("Fă acțiuni timp de 5 secunde...")
# Așteaptă 30 secunde sau până când utilizatorul apasă ESC/F9
for i in range(30):
    if recorder.stop_requested:
        break
    time.sleep(1)
events = recorder.stop_recording()
print(f"Am înregistrat {len(events)} evenimente")

# Redare
player = TaskPlayer()
player.play_events(events, speed=2.0)  # 2x mai rapid
```

### Pornește GUI:

```python
from bebe_task_recorder import main
main()  # Deschide interfața grafică completă
```

## Note Importante

1. **Privilegii Administrator**: **OBLIGATORIU** pentru înregistrare globală (din alte aplicații). Fără admin, doar mouse-ul funcționează, nu și tastatura.

2. **Poziții Absolute**: Libraria înregistrează poziții absolute pe ecran. Dacă muți ferestrele, pozițiile nu vor corespunde.

3. **ESC/F9**: Apasă ESC sau F9 pentru a opri înregistrarea.

4. **Viteză Redare**: Poți ajusta viteza redării (ex: `speed=2.0` = 2x mai rapid).

## Troubleshooting

### Problema: Nu înregistrează taste
**Soluție**: Rulează scriptul ca Administrator (click dreapta → Run as Administrator)

### Problema: Mouse-ul funcționează dar tastatura nu
**Soluție**: Exact problema de mai sus - trebuie privilegii Administrator

### Problema: Scriptul nu se repornește automat ca admin
**Soluție**: Rulează manual ca Administrator sau folosește `RUN_AS_ADMIN.bat`

## Suport

Pentru mai multe informații:
- GitHub: https://github.com/me-suzy/BEBE-Task-Recorder
- PyPI: https://pypi.org/project/bebe-task-recorder/
