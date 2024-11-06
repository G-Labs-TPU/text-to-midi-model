from mido import MidiFile, MidiTrack, Message
import json

def json_to_midi(json_data):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Parse JSON and create MIDI events
    for note_data in json_data["notes"]:  # Assuming JSON has a "notes" list
        note = note_data["note"]
        duration = note_data["duration"]
        velocity = note_data["velocity"]

        # Note on
        track.append(Message('note_on', note=note, velocity=velocity, time=0))
        # Note off after duration
        track.append(Message('note_off', note=note, velocity=velocity, time=duration))

    # Save MIDI file
    midi_file_path = 'output.mid'
    midi.save(midi_file_path)
    return midi_file_path
