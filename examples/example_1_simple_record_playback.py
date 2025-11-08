#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example 1: Simple Record and Playback

Acest exemplu arată cum să înregistrezi acțiuni simple și să le redai.
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

def main():
    print("=" * 60)
    print("Example 1: Simple Record and Playback")
    print("=" * 60)
    print()
    
    # Creează recorder și player
    recorder = TaskRecorder()
    player = TaskPlayer()
    
    print("1. Începem înregistrarea...")
    print("   Ai 30 secunde să faci acțiuni (miscă mouse-ul, apasă taste)")
    print("   Apasă ESC sau F9 pentru a opri înainte de timp")
    print()
    
    # Începe înregistrarea
    recorder.start_recording()
    
    # Așteaptă 30 secunde pentru utilizator să facă acțiuni
    # Sau până când utilizatorul apasă ESC/F9
    for i in range(30):
        if recorder.stop_requested:
            break
        time.sleep(1)
        if (i + 1) % 5 == 0:
            remaining = 30 - (i + 1)
            print(f"   ⏱️  Timp rămas: {remaining} secunde...")
    
    print("\n2. Oprim înregistrarea...")
    events = recorder.stop_recording()
    
    print(f"   ✅ Am înregistrat {len(events)} evenimente")
    
    if events:
        print("\n   Primele 3 evenimente:")
        for i, event in enumerate(events[:3], 1):
            print(f"      {i}. {event['type']} @ {event['timestamp']:.3f}s")
        
        # Salvează task-ul
        print("\n3. Salvăm task-ul...")
        with open("my_task.json", "w", encoding="utf-8") as f:
            json.dump({
                'version': '1.0',
                'events': events
            }, f, indent=2)
        print("   ✅ Task salvat în 'my_task.json'")
        
        # Redă task-ul
        print("\n4. Redăm task-ul...")
        response = input("   Vrei să redăm acțiunile? (y/n): ")
        if response.lower() == 'y':
            print("   ▶️  Redare în curs...")
            player.play_events(events, speed=2.0)  # 2x mai rapid
            print("   ✅ Redare completă!")
    else:
        print("\n   ⚠️  Nu s-au înregistrat evenimente")

if __name__ == "__main__":
    main()

