#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test script pentru a verifica instalarea pachetului"""

def test_import():
    """Test import"""
    print("Testing imports...")
    try:
        from bebe_task_recorder import TaskRecorder, TaskPlayer, BebeGUI, main
        print("✅ All imports successful!")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_version():
    """Test version"""
    print("\nTesting version...")
    try:
        from bebe_task_recorder import __version__
        print(f"✅ Version: {__version__}")
        return True
    except ImportError as e:
        print(f"❌ Version error: {e}")
        return False

def test_classes():
    """Test classes"""
    print("\nTesting classes...")
    try:
        from bebe_task_recorder import TaskRecorder, TaskPlayer
        
        # Test TaskRecorder
        recorder = TaskRecorder()
        print("✅ TaskRecorder created successfully")
        
        # Test TaskPlayer
        player = TaskPlayer()
        print("✅ TaskPlayer created successfully")
        
        return True
    except Exception as e:
        print(f"❌ Class creation error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("BEBE Task Recorder - Package Test")
    print("=" * 60)
    print()
    
    results = []
    results.append(test_import())
    results.append(test_version())
    results.append(test_classes())
    
    print("\n" + "=" * 60)
    if all(results):
        print("✅ All tests passed! Package is ready.")
    else:
        print("❌ Some tests failed. Please check the errors above.")
    print("=" * 60)

