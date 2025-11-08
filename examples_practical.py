#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemple practice de utilizare a librariei BEBE Task Recorder

Aceste exemple demonstrează diferite moduri de utilizare a librariei.
"""

import time
import json
from pathlib import Path
from bebe_task_recorder import TaskRecorder, TaskPlayer, main

# ============================================================================
# EXEMPLU 1: Înregistrare simplă și redare
# ============================================================================

def exemplu_1_simplu():
    """Exemplu simplu: înregistrează și redă acțiuni"""
    print("=" * 60)
    print("EXEMPLU 1: Înregistrare simplă și redare")
    print("=" * 60)
    
    # Creează recorder
    recorder = TaskRecorder()
    
    print("\n1. Pornire înregistrare...")
    print("   Ai 5 secunde să muți mouse-ul sau să tastezi ceva!")
    recorder.start_recording()
    
    # Așteaptă 5 secunde pentru acțiuni
    time.sleep(5)
    
    print("\n2. Oprire înregistrare...")
    events = recorder.stop_recording()
    
    print(f"\n✅ Înregistrat {len(events)} evenimente")
    
    if events:
        print("\n3. Redare acțiuni...")
        player = TaskPlayer()
        
        response = input("   Vrei să redai acțiunile? (y/n): ")
        if response.lower() == 'y':
            player.play_events(events, speed=2.0)
            print("✅ Redare completă!")
    
    return events


# ============================================================================
# EXEMPLU 2: Salvare și încărcare task-uri
# ============================================================================

def exemplu_2_salvare_task():
    """Exemplu: salvează și încarcă task-uri"""
    print("\n" + "=" * 60)
    print("EXEMPLU 2: Salvare și încărcare task-uri")
    print("=" * 60)
    
    # Înregistrează un task
    recorder = TaskRecorder()
    print("\n1. Înregistrare task...")
    recorder.start_recording()
    time.sleep(3)  # 3 secunde pentru acțiuni
    events = recorder.stop_recording()
    
    print(f"✅ Înregistrat {len(events)} evenimente")
    
    # Salvează task-ul
    task_file = Path("my_task.json")
    task_data = {
        'version': '1.0',
        'created': time.strftime('%Y-%m-%d %H:%M:%S'),
        'event_count': len(events),
        'events': events
    }
    
    with open(task_file, 'w', encoding='utf-8') as f:
        json.dump(task_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Task salvat în: {task_file}")
    
    # Încarcă task-ul
    print("\n2. Încărcare task...")
    with open(task_file, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    loaded_events = loaded_data['events']
    print(f"✅ Task încărcat: {len(loaded_events)} evenimente")
    
    # Redă task-ul încărcat
    print("\n3. Redare task încărcat...")
    response = input("   Vrei să redai task-ul? (y/n): ")
    if response.lower() == 'y':
        player = TaskPlayer()
        player.play_events(loaded_events, speed=2.0)
        print("✅ Redare completă!")
    
    return task_file


# ============================================================================
# EXEMPLU 3: Redare cu viteze diferite
# ============================================================================

def exemplu_3_viteze_diferite():
    """Exemplu: redare cu viteze diferite"""
    print("\n" + "=" * 60)
    print("EXEMPLU 3: Redare cu viteze diferite")
    print("=" * 60)
    
    # Creează un task simplu (sau încarcă unul existent)
    recorder = TaskRecorder()
    print("\n1. Înregistrare task scurt...")
    recorder.start_recording()
    time.sleep(2)
    events = recorder.stop_recording()
    
    if not events:
        print("⚠️  Nu s-au înregistrat evenimente. Adaugă câteva acțiuni.")
        return
    
    player = TaskPlayer()
    
    print("\n2. Redare cu viteze diferite:")
    print("   - Viteză normală (1.0x)")
    print("   - Viteză rapidă (2.0x)")
    print("   - Viteză foarte rapidă (5.0x)")
    
    response = input("\n   Vrei să testezi vitezele? (y/n): ")
    if response.lower() != 'y':
        return
    
    speeds = [1.0, 2.0, 5.0]
    for speed in speeds:
        print(f"\n   ▶️  Redare la {speed}x viteza...")
        player.play_events(events, speed=speed)
        time.sleep(1)  # Pauză între redări
    
    print("\n✅ Test viteze complet!")


# ============================================================================
# EXEMPLU 4: Analiză evenimente
# ============================================================================

def exemplu_4_analiza_evenimente():
    """Exemplu: analizează evenimentele înregistrate"""
    print("\n" + "=" * 60)
    print("EXEMPLU 4: Analiză evenimente")
    print("=" * 60)
    
    # Înregistrează un task
    recorder = TaskRecorder()
    print("\n1. Înregistrare task...")
    recorder.start_recording()
    time.sleep(3)
    events = recorder.stop_recording()
    
    if not events:
        print("⚠️  Nu s-au înregistrat evenimente.")
        return
    
    # Analizează evenimentele
    print(f"\n2. Analiză: {len(events)} evenimente înregistrate")
    
    event_types = {}
    for event in events:
        event_type = event['type']
        event_types[event_type] = event_types.get(event_type, 0) + 1
    
    print("\n   Tipuri de evenimente:")
    for event_type, count in event_types.items():
        print(f"   - {event_type}: {count}")
    
    # Durata totală
    if events:
        total_time = events[-1]['timestamp'] - events[0]['timestamp']
        print(f"\n   Durată totală: {total_time:.2f} secunde")
    
    # Evenimente de mouse
    mouse_events = [e for e in events if e['type'].startswith('mouse')]
    print(f"   Evenimente mouse: {len(mouse_events)}")
    
    # Evenimente de tastatură
    keyboard_events = [e for e in events if e['type'].startswith('key')]
    print(f"   Evenimente tastatură: {len(keyboard_events)}")
    
    print("\n✅ Analiză completă!")


# ============================================================================
# EXEMPLU 5: Callback pentru monitorizare
# ============================================================================

def exemplu_5_callback():
    """Exemplu: folosește callback pentru monitorizare în timp real"""
    print("\n" + "=" * 60)
    print("EXEMPLU 5: Callback pentru monitorizare")
    print("=" * 60)
    
    # Funcție callback care afișează evenimentele
    def callback(event_text):
        print(f"   📍 {event_text}")
    
    # Creează recorder cu callback
    recorder = TaskRecorder(callback=callback)
    
    print("\n1. Înregistrare cu monitorizare în timp real...")
    print("   (Evenimentele vor fi afișate pe măsură ce apar)")
    recorder.start_recording()
    
    time.sleep(5)  # 5 secunde pentru acțiuni
    
    events = recorder.stop_recording()
    print(f"\n✅ Înregistrare completă: {len(events)} evenimente")


# ============================================================================
# EXEMPLU 6: Workflow complet - Automatizare task
# ============================================================================

def exemplu_6_workflow_complet():
    """Exemplu: workflow complet pentru automatizare"""
    print("\n" + "=" * 60)
    print("EXEMPLU 6: Workflow complet")
    print("=" * 60)
    
    print("\nAcest exemplu demonstrează un workflow complet:")
    print("1. Înregistrare task")
    print("2. Salvare task")
    print("3. Încărcare task")
    print("4. Redare task de mai multe ori")
    
    # Pasul 1: Înregistrare
    print("\n--- PASUL 1: Înregistrare ---")
    recorder = TaskRecorder()
    print("Pornește înregistrarea...")
    recorder.start_recording()
    
    print("Ai 5 secunde să efectuezi acțiunile pe care vrei să le automatizezi!")
    for i in range(5, 0, -1):
        print(f"   {i}...", end='', flush=True)
        time.sleep(1)
    print()
    
    events = recorder.stop_recording()
    print(f"✅ Înregistrat {len(events)} evenimente")
    
    if not events:
        print("⚠️  Nu s-au înregistrat evenimente. Workflow oprit.")
        return
    
    # Pasul 2: Salvare
    print("\n--- PASUL 2: Salvare ---")
    task_name = input("Nume task (sau Enter pentru 'my_automation'): ").strip()
    if not task_name:
        task_name = "my_automation"
    
    task_file = Path(f"{task_name}.json")
    task_data = {
        'version': '1.0',
        'created': time.strftime('%Y-%m-%d %H:%M:%S'),
        'name': task_name,
        'event_count': len(events),
        'events': events
    }
    
    with open(task_file, 'w', encoding='utf-8') as f:
        json.dump(task_data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Task salvat: {task_file}")
    
    # Pasul 3: Încărcare
    print("\n--- PASUL 3: Încărcare ---")
    with open(task_file, 'r', encoding='utf-8') as f:
        loaded_data = json.load(f)
    
    loaded_events = loaded_data['events']
    print(f"✅ Task încărcat: {len(loaded_events)} evenimente")
    
    # Pasul 4: Redare
    print("\n--- PASUL 4: Redare ---")
    response = input("Câte ori vrei să redai task-ul? (default: 1): ").strip()
    try:
        loop_count = int(response) if response else 1
    except ValueError:
        loop_count = 1
    
    speed_input = input("Viteză redare (default: 2.0): ").strip()
    try:
        speed = float(speed_input) if speed_input else 2.0
    except ValueError:
        speed = 2.0
    
    player = TaskPlayer()
    
    print(f"\n▶️  Redare task '{task_name}' de {loop_count} ori la viteza {speed}x...")
    for i in range(loop_count):
        print(f"\n   Redare #{i+1}/{loop_count}...")
        player.play_events(loaded_events, speed=speed, loop_count=1)
        if i < loop_count - 1:
            time.sleep(1)  # Pauză între redări
    
    print("\n✅ Workflow complet finalizat!")


# ============================================================================
# EXEMPLU 7: GUI Application
# ============================================================================

def exemplu_7_gui():
    """Exemplu: rulează interfața grafică"""
    print("\n" + "=" * 60)
    print("EXEMPLU 7: Interfață grafică")
    print("=" * 60)
    
    print("\nPornire interfață grafică...")
    print("(Folosește GUI-ul pentru înregistrare și redare)")
    
    main()  # Rulează GUI


# ============================================================================
# MENIU PRINCIPAL
# ============================================================================

def main_menu():
    """Meniu principal pentru exemple"""
    examples = {
        '1': ('Înregistrare simplă și redare', exemplu_1_simplu),
        '2': ('Salvare și încărcare task-uri', exemplu_2_salvare_task),
        '3': ('Redare cu viteze diferite', exemplu_3_viteze_diferite),
        '4': ('Analiză evenimente', exemplu_4_analiza_evenimente),
        '5': ('Callback pentru monitorizare', exemplu_5_callback),
        '6': ('Workflow complet', exemplu_6_workflow_complet),
        '7': ('Interfață grafică (GUI)', exemplu_7_gui),
    }
    
    while True:
        print("\n" + "=" * 60)
        print("BEBE Task Recorder - Exemple Practice")
        print("=" * 60)
        print()
        print("Alege un exemplu:")
        print()
        for key, (name, _) in examples.items():
            print(f"  {key}. {name}")
        print()
        print("  0. Ieșire")
        print()
        
        choice = input("Alegere: ").strip()
        
        if choice == '0':
            print("\nLa revedere!")
            break
        elif choice in examples:
            name, func = examples[choice]
            try:
                func()
            except KeyboardInterrupt:
                print("\n\n⚠️  Oprit de utilizator")
            except Exception as e:
                print(f"\n❌ Eroare: {e}")
                import traceback
                traceback.print_exc()
        else:
            print("\n⚠️  Alegere invalidă!")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("BEBE Task Recorder - Exemple Practice")
    print("=" * 60)
    print()
    print("Acest script conține exemple practice de utilizare")
    print("a librariei BEBE Task Recorder.")
    print()
    
    main_menu()

