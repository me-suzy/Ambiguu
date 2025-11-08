#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example 4: Programmatic Control

Acest exemplu arată cum să controlezi programatic înregistrarea și redarea,
folosind callback-uri pentru feedback în timp real.
"""

from bebe_task_recorder import TaskRecorder, TaskPlayer, is_admin, run_as_admin
import time
import threading
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

class AutomationController:
    """Controller pentru automatizare cu feedback"""
    
    def __init__(self):
        self.recorder = TaskRecorder(callback=self.on_event_recorded)
        self.player = TaskPlayer()
        self.recorded_events = []
        self.is_recording = False
        self.is_playing = False
    
    def on_event_recorded(self, event_text):
        """Callback când se înregistrează un eveniment"""
        if self.is_recording:
            print(f"   📹 {event_text}")
    
    def on_playback_event(self, message):
        """Callback pentru redare"""
        if self.is_playing:
            print(f"   ▶️  {message}")
    
    def start_recording_with_feedback(self, duration=30):
        """Începe înregistrarea cu feedback în timp real"""
        print("=" * 60)
        print("Înregistrare cu Feedback")
        print("=" * 60)
        print(f"\nÎnregistrare pentru {duration} secunde...")
        print("Fă acțiuni (miscă mouse-ul, apasă taste)...")
        print("Apasă ESC sau F9 pentru a opri înainte de timp")
        print()
        
        self.is_recording = True
        self.recorder.start_recording()
        
        # Așteaptă durata specificată sau până când utilizatorul apasă ESC/F9
        for i in range(duration):
            if self.recorder.stop_requested:
                break
            time.sleep(1)
            if (i + 1) % 5 == 0:
                remaining = duration - (i + 1)
                print(f"   ⏱️  Timp rămas: {remaining} secunde...")
        
        self.recorded_events = self.recorder.stop_recording()
        self.is_recording = False
        
        print(f"\n✅ Înregistrare oprită: {len(self.recorded_events)} evenimente")
        return self.recorded_events
    
    def play_with_feedback(self, events, speed=1.0):
        """Redă evenimente cu feedback în timp real"""
        print("\n" + "=" * 60)
        print("Redare cu Feedback")
        print("=" * 60)
        print(f"\nRedare {len(events)} evenimente la viteza {speed}x...")
        print()
        
        self.is_playing = True
        
        # Redă într-un thread separat pentru a nu bloca
        def play_thread():
            self.player.play_events(
                events, 
                speed=speed,
                callback=self.on_playback_event
            )
            self.is_playing = False
        
        thread = threading.Thread(target=play_thread, daemon=True)
        thread.start()
        thread.join()
        
        print("\n✅ Redare completă!")

def main():
    print("=" * 60)
    print("Example 4: Programmatic Control")
    print("=" * 60)
    print()
    
    controller = AutomationController()
    
    # 1. Înregistrare cu feedback
    duration = int(input("Durată înregistrare (secunde, default: 30): ") or "30")
    events = controller.start_recording_with_feedback(duration)
    
    if not events:
        print("\n⚠️  Nu s-au înregistrat evenimente")
        return
    
    # 2. Afișare statistici
    print("\n" + "=" * 60)
    print("Statistici Evenimente")
    print("=" * 60)
    
    event_types = {}
    for event in events:
        event_type = event['type']
        event_types[event_type] = event_types.get(event_type, 0) + 1
    
    for event_type, count in event_types.items():
        print(f"   {event_type}: {count}")
    
    total_time = events[-1]['timestamp'] if events else 0
    print(f"\n   Durată totală: {total_time:.2f} secunde")
    
    # 3. Redare cu feedback
    print("\n" + "=" * 60)
    response = input("Vrei să redăm evenimentele? (y/n): ")
    if response.lower() == 'y':
        speed = float(input("Viteză (default: 1.0): ") or "1.0")
        controller.play_with_feedback(events, speed=speed)

if __name__ == "__main__":
    main()

