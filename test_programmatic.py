#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test programmatic usage of BEBE Task Recorder
"""

from bebe_task_recorder import TaskRecorder, TaskPlayer
import time

def test_recording():
    """Test recording functionality"""
    print("=" * 60)
    print("Testing TaskRecorder...")
    print("=" * 60)
    
    recorder = TaskRecorder()
    
    print("\n1. Starting recording...")
    print("   (You have 5 seconds to move mouse/type)")
    recorder.start_recording()
    
    # Wait 5 seconds for user to perform actions
    print("\n   Recording... Move mouse or type something!")
    time.sleep(5)
    
    print("\n2. Stopping recording...")
    events = recorder.stop_recording()
    
    print(f"\n✅ Recorded {len(events)} events")
    
    if events:
        print("\nFirst few events:")
        for i, event in enumerate(events[:5], 1):
            print(f"  {i}. {event['type']} @ {event['timestamp']:.3f}s")
    
    return events

def test_playback(events):
    """Test playback functionality"""
    if not events:
        print("\n⚠️  No events to playback")
        return
    
    print("\n" + "=" * 60)
    print("Testing TaskPlayer...")
    print("=" * 60)
    
    player = TaskPlayer()
    
    print(f"\nPlaying back {len(events)} events...")
    print("(This will replay your recorded actions)")
    
    response = input("\nContinue? (y/n): ")
    if response.lower() != 'y':
        print("Playback cancelled.")
        return
    
    print("\n▶️  Starting playback...")
    player.play_events(events, speed=2.0)
    print("\n✅ Playback complete!")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("BEBE Task Recorder - Programmatic Test")
    print("=" * 60)
    print()
    print("This script will:")
    print("1. Start recording for 5 seconds")
    print("2. Stop recording and show events")
    print("3. Optionally playback the recorded events")
    print()
    
    response = input("Start test? (y/n): ")
    if response.lower() != 'y':
        print("Test cancelled.")
        exit(0)
    
    # Test recording
    events = test_recording()
    
    # Test playback
    if events:
        test_playback(events)
    
    print("\n" + "=" * 60)
    print("Test complete!")
    print("=" * 60)

