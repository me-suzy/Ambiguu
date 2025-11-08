#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example usage of BEBE Task Recorder package

This script demonstrates how to use the BEBE Task Recorder programmatically.
"""

from bebe_task_recorder import TaskRecorder, TaskPlayer, main

def example_gui():
    """Run the GUI application"""
    print("Starting BEBE Task Recorder GUI...")
    main()

def example_programmatic():
    """Example of programmatic usage"""
    print("=" * 60)
    print("BEBE Task Recorder - Programmatic Usage Example")
    print("=" * 60)
    print()
    
    # Create recorder
    recorder = TaskRecorder()
    print("✅ TaskRecorder created")
    
    # Create player
    player = TaskPlayer()
    print("✅ TaskPlayer created")
    
    print()
    print("To record:")
    print("  1. Call recorder.start_recording()")
    print("  2. Perform your actions")
    print("  3. Call events = recorder.stop_recording()")
    print()
    print("To playback:")
    print("  1. Call player.play_events(events)")
    print()
    print("For GUI:")
    print("  Call main() to start the graphical interface")
    print()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        example_gui()
    else:
        example_programmatic()
        print("Run with 'python example_usage.py gui' to start GUI")

