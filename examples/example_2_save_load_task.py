#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example 2: Save and Load Tasks

Acest exemplu arată cum să salvezi și să încarci task-uri din fișiere JSON.
"""

from bebe_task_recorder import TaskRecorder, TaskPlayer, is_admin, run_as_admin
import json
import time
import sys
from pathlib import Path

# Verifică și solicită privilegii de administrator
if not is_admin():
    print("=" * 60)
    print("⚠️  ATENȚIE: Privilegii Administrator Necesare")
    print("=" * 60)
    print()
    print("Pentru a înregistra taste din alte aplicații,")
    print("acest script trebuie să ruleze ca Administrator.")
    print()
    print("Repornind cu privilegii de administrator...")
    print()
    run_as_admin()
    sys.exit()

def save_task(events, filename):
    """Salvează un task în fișier JSON"""
    task_data = {
        'version': '1.0',
        'created': time.strftime('%Y-%m-%d %H:%M:%S'),
        'event_count': len(events),
        'events': events
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(task_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Task salvat în '{filename}'")

def load_task(filename):
    """Încarcă un task din fișier JSON"""
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"✅ Task încărcat din '{filename}'")
    print(f"   Versiune: {data.get('version', 'N/A')}")
    print(f"   Creat: {data.get('created', 'N/A')}")
    print(f"   Evenimente: {data.get('event_count', len(data.get('events', [])))}")
    
    return data['events']

def main():
    print("=" * 60)
    print("Example 2: Save and Load Tasks")
    print("=" * 60)
    print()
    
    recorder = TaskRecorder()
    player = TaskPlayer()
    
    # Înregistrare
    print("1. Înregistrare task nou...")
    print("   Ai 30 secunde să faci acțiuni")
    print("   Apasă ESC sau F9 pentru a opri înainte de timp")
    recorder.start_recording()
    
    # Așteaptă 30 secunde sau până când utilizatorul apasă ESC/F9
    for i in range(30):
        if recorder.stop_requested:
            break
        time.sleep(1)
        if (i + 1) % 5 == 0:
            remaining = 30 - (i + 1)
            print(f"   ⏱️  Timp rămas: {remaining} secunde...")
    events = recorder.stop_recording()
    
    if not events:
        print("   ⚠️  Nu s-au înregistrat evenimente")
        return
    
    print(f"   ✅ {len(events)} evenimente înregistrate")
    
    # Salvare
    task_file = "example_task.json"
    print(f"\n2. Salvăm task-ul în '{task_file}'...")
    save_task(events, task_file)
    
    # Încărcare
    print(f"\n3. Încărcăm task-ul din '{task_file}'...")
    loaded_events = load_task(task_file)
    
    # Redare
    print("\n4. Redăm task-ul încărcat...")
    response = input("   Vrei să redăm? (y/n): ")
    if response.lower() == 'y':
        player.play_events(loaded_events, speed=2.0)
        print("   ✅ Redare completă!")
    
    # Listă task-uri salvate
    print("\n5. Task-uri salvate în directorul curent:")
    task_files = list(Path('.').glob('*.json'))
    if task_files:
        for task_file in task_files:
            print(f"   - {task_file.name}")
    else:
        print("   (Niciun task salvat)")

if __name__ == "__main__":
    main()

