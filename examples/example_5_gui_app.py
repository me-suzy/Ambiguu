#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example 5: Launch GUI Application

Acest exemplu arată cum să pornești interfața grafică completă.
"""

from bebe_task_recorder import main

if __name__ == "__main__":
    print("=" * 60)
    print("Example 5: Launch GUI Application")
    print("=" * 60)
    print()
    print("Pornind interfața grafică BEBE Task Recorder...")
    print()
    print("Funcționalități disponibile:")
    print("  - Înregistrare mouse și tastatură")
    print("  - Redare task-uri")
    print("  - Salvare/încărcare task-uri")
    print("  - Vizualizare evenimente în timp real")
    print()
    print("Apasă ESC sau F9 pentru a opri înregistrarea")
    print()
    
    # Pornește GUI
    main()

