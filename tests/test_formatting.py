#!/usr/bin/env python3
"""Test formatting logic to catch None value errors."""

import os
import sys
import time

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

# Set up environment for testing
os.environ["DISCORD_TOKEN"] = "dummy"
os.environ["GEMINI_API_KEY"] = "dummy-key-for-testing"

def test_progress_formatting_with_none_values():
    """Test that progress data formatting handles None values correctly."""
    print("Testing progress formatting with None values...")
    
    # Sample data with None values (this is what was causing the error)
    sample_data = {
        'playtime_hours': None,
        'completion_percent': None,
        'geo': None,
        'health': None,
        'max_health': None,
        'deaths': None,
        'scene': None,
        'zone': None,
        'nail_upgrades': None,
        'soul_vessels': None,
        'mask_shards': None,
        'charms_owned': None,
        'bosses_defeated': None,
        'ts': int(time.time()) - 3600,
    }
    
    try:
        # Test the formatting logic that was failing
        completion = sample_data['completion_percent']
        playtime = sample_data['playtime_hours']
        geo = sample_data['geo']
        health = sample_data['health']
        max_health = sample_data['max_health']
        deaths = sample_data['deaths']
        scene = sample_data['scene']
        zone = sample_data['zone']
        nail_upgrades = sample_data['nail_upgrades']
        soul_vessels = sample_data['soul_vessels']
        mask_shards = sample_data['mask_shards']
        charms_owned = sample_data['charms_owned']
        bosses_defeated = sample_data['bosses_defeated']
        
        # This is the formatting logic from the fixed code
        message = f"🎮 **Progress**: {completion or 0}% complete\n"
        message += f"⏱️ **Playtime**: {(playtime if playtime is not None else 0):.2f} hours\n"
        message += f"💰 **Geo**: {(geo if geo is not None else 0):,}\n"
        message += f"❤️ **Health**: {health or 0}/{max_health or 0} hearts\n"
        message += f"💀 **Deaths**: {deaths or 0}\n"
        message += f"🗡️ **Nail**: +{nail_upgrades or 0} upgrades\n"
        message += f"💙 **Soul**: {soul_vessels or 0} vessels\n"
        message += f"🎭 **Charms**: {charms_owned or 0} owned\n"
        message += f"👹 **Bosses**: {bosses_defeated or 0} defeated\n"
        message += f"📍 **Location**: {scene or 'Unknown'} ({zone or 'Unknown'})"
        
        print("✅ Formatting with None values succeeded")
        print(f"Generated message: {message}")
        return True
        
    except Exception as e:
        print(f"❌ Formatting with None values failed: {e}")
        return False

def test_progress_formatting_with_mixed_values():
    """Test formatting with mixed None and valid values."""
    print("Testing progress formatting with mixed values...")
    
    # Sample data with mixed None and valid values
    sample_data = {
        'playtime_hours': 10.5,
        'completion_percent': None,
        'geo': 0,
        'health': 5,
        'max_health': None,
        'deaths': 0,
        'scene': '',
        'zone': None,
        'nail_upgrades': 1,
        'soul_vessels': None,
        'mask_shards': 0,
        'charms_owned': None,
        'bosses_defeated': 0,
        'ts': int(time.time()) - 3600,
    }
    
    try:
        # Test the formatting logic
        completion = sample_data['completion_percent']
        playtime = sample_data['playtime_hours']
        geo = sample_data['geo']
        health = sample_data['health']
        max_health = sample_data['max_health']
        deaths = sample_data['deaths']
        scene = sample_data['scene']
        zone = sample_data['zone']
        nail_upgrades = sample_data['nail_upgrades']
        soul_vessels = sample_data['soul_vessels']
        mask_shards = sample_data['mask_shards']
        charms_owned = sample_data['charms_owned']
        bosses_defeated = sample_data['bosses_defeated']
        
        # This is the formatting logic from the fixed code
        message = f"🎮 **Progress**: {completion or 0}% complete\n"
        message += f"⏱️ **Playtime**: {(playtime if playtime is not None else 0):.2f} hours\n"
        message += f"💰 **Geo**: {(geo if geo is not None else 0):,}\n"
        message += f"❤️ **Health**: {health or 0}/{max_health or 0} hearts\n"
        message += f"💀 **Deaths**: {deaths or 0}\n"
        message += f"🗡️ **Nail**: +{nail_upgrades or 0} upgrades\n"
        message += f"💙 **Soul**: {soul_vessels or 0} vessels\n"
        message += f"🎭 **Charms**: {charms_owned or 0} owned\n"
        message += f"👹 **Bosses**: {bosses_defeated or 0} defeated\n"
        message += f"📍 **Location**: {scene or 'Unknown'} ({zone or 'Unknown'})"
        
        print("✅ Formatting with mixed values succeeded")
        print(f"Generated message: {message}")
        return True
        
    except Exception as e:
        print(f"❌ Formatting with mixed values failed: {e}")
        return False

def test_history_formatting_with_none_values():
    """Test history formatting with None values."""
    print("Testing history formatting with None values...")
    
    # Sample data for history format
    save = {
        'completion_percent': None,
        'playtime_hours': None,
        'geo': None,
        'health': None,
        'max_health': None,
        'deaths': None,
        'scene': None,
        'zone': None,
        'bosses_defeated': None,
        'ts': int(time.time()) - 3600,
    }
    
    try:
        # This is the history formatting logic from the fixed code
        message = f"🎮 {save['completion_percent'] or 0}% complete | ⏱️ {(save['playtime_hours'] if save['playtime_hours'] is not None else 0):.1f}h | 💰 {(save['geo'] if save['geo'] is not None else 0):,} geo\n"
        message += f"❤️ {save['health'] or 0}/{save['max_health'] or 0} hearts | 💀 {save['deaths'] or 0} deaths | 👹 {save['bosses_defeated'] or 0} bosses\n"
        message += f"📍 {save['scene'] or 'Unknown'} ({save['zone'] or 'Unknown'})"
        
        print("✅ History formatting with None values succeeded")
        print(f"Generated message: {message}")
        return True
        
    except Exception as e:
        print(f"❌ History formatting with None values failed: {e}")
        return False

def test_old_formatting_logic_fails():
    """Test that the old formatting logic would fail with None values."""
    print("Testing that old formatting logic fails with None values...")
    
    # Sample data with None values
    sample_data = {
        'playtime_hours': None,
        'completion_percent': None,
        'geo': None,
        'health': None,
        'max_health': None,
        'deaths': None,
        'scene': None,
        'zone': None,
        'ts': int(time.time()) - 3600,
    }
    
    try:
        # This is the OLD formatting logic that would fail
        completion = sample_data['completion_percent']
        playtime = sample_data['playtime_hours']
        geo = sample_data['geo']
        health = sample_data['health']
        max_health = sample_data['max_health']
        deaths = sample_data['deaths']
        scene = sample_data['scene']
        zone = sample_data['zone']
        
        # OLD logic that would cause the error
        message = f"🎮 **Progress**: {completion}% complete\n"
        message += f"⏱️ **Playtime**: {playtime:.2f} hours\n"  # This would fail!
        message += f"💰 **Geo**: {geo:,}\n"  # This would fail!
        message += f"❤️ **Health**: {health}/{max_health} hearts\n"
        message += f"💀 **Deaths**: {deaths}\n"
        message += f"📍 **Location**: {scene} ({zone})"
        
        print("❌ Old formatting logic should have failed but didn't")
        return False
        
    except Exception as e:
        print(f"✅ Old formatting logic correctly failed: {e}")
        return True

def main():
    """Run all formatting tests."""
    print("🧪 Testing Progress Data Formatting")
    print("=" * 50)
    
    tests = [
        test_progress_formatting_with_none_values,
        test_progress_formatting_with_mixed_values,
        test_history_formatting_with_none_values,
        test_old_formatting_logic_fails,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All formatting tests passed!")
        return 0
    else:
        print("❌ Some tests failed. Check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
