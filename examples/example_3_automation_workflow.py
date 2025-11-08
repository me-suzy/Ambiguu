#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example 3: Automation Workflow

Acest exemplu arată cum să folosești libraria pentru automatizare:
- Înregistrează o secvență de acțiuni
- Redă-o de mai multe ori
- Cu diferite viteze
"""

from bebe_task_recorder import TaskRecorder, TaskPlayer, is_admin, run_as_admin
import time
import json
import sys

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

def record_workflow():
    """Înregistrează un workflow"""
    print("=" * 60)
    print("Înregistrare Workflow")
    print("=" * 60)
    print()
    print("Acum vei înregistra workflow-ul tău.")
    print("Exemplu: deschide Notepad, scrie ceva, salvează, închide")
    print()
    
    recorder = TaskRecorder()
    
    input("Apasă ENTER când ești gata să începi înregistrarea...")
    
    print("\n▶️  Înregistrare în curs...")
    print("   Apasă ESC sau F9 pentru a opri")
    
    recorder.start_recording()
    
    # Așteaptă până când utilizatorul oprește
    while recorder.recording and not recorder.stop_requested:
        time.sleep(0.1)
    
    events = recorder.stop_recording()
    
    print(f"\n✅ Workflow înregistrat: {len(events)} evenimente")
    return events

def automate_workflow(events, repeat_count=3, speed=1.0):
    """Redă workflow-ul de mai multe ori"""
    print("\n" + "=" * 60)
    print(f"Automatizare Workflow")
    print("=" * 60)
    print(f"   Repetări: {repeat_count}")
    print(f"   Viteză: {speed}x")
    print()
    
    player = TaskPlayer()
    
    for i in range(repeat_count):
        print(f"\n[{i+1}/{repeat_count}] Redare workflow...")
        print("   Pregătire: 2 secunde...")
        time.sleep(2)
        
        player.play_events(events, speed=speed)
        
        print(f"   ✅ Repetare {i+1} completă")
        
        if i < repeat_count - 1:
            print("   Pauză între repetări: 2 secunde...")
            time.sleep(2)
    
    print("\n✅ Toate repetările completate!")

def main():
    print("=" * 60)
    print("Example 3: Automation Workflow")
    print("=" * 60)
    print()
    
    # Opțiune 1: Înregistrare nouă
    # Opțiune 2: Încărcare din fișier
    
    choice = input("1. Înregistrare nouă\n2. Încărcare din fișier\nAlege (1/2): ")
    
    if choice == "1":
        events = record_workflow()
        
        # Salvează automat
        save = input("\nVrei să salvezi workflow-ul? (y/n): ")
        if save.lower() == 'y':
            filename = input("Nume fișier (ex: workflow.json): ").strip() or "workflow.json"
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({'events': events}, f, indent=2)
            print(f"✅ Salvat în '{filename}'")
    else:
        filename = input("Nume fișier: ").strip()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            events = data.get('events', data)
            print(f"✅ Încărcat: {len(events)} evenimente")
        except Exception as e:
            print(f"❌ Eroare la încărcare: {e}")
            return
    
    if not events:
        print("⚠️  Nu există evenimente de redat")
        return
    
    # Configurează automatizarea
    print("\n" + "=" * 60)
    print("Configurare Automatizare")
    print("=" * 60)
    
    repeat_count = int(input("Câte repetări? (default: 3): ") or "3")
    speed = float(input("Viteză redare? (default: 1.0, ex: 2.0 = 2x mai rapid): ") or "1.0")
    
    # Confirmare
    print(f"\nVei reda workflow-ul {repeat_count} ori cu viteza {speed}x")
    confirm = input("Continuă? (y/n): ")
    
    if confirm.lower() == 'y':
        automate_workflow(events, repeat_count, speed)
    else:
        print("Anulat.")

if __name__ == "__main__":
    main()

