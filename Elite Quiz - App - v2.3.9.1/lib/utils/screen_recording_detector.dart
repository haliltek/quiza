import 'dart:async';

import 'package:flutter/services.dart';

/// Helper class for detecting iOS screen recording using native MethodChannel.
/// Uses event-based approach instead of polling for better performance.
class ScreenRecordingDetector {
  static const _methodChannel = MethodChannel('com.flutterquiz/screen_recording');
  static const _eventChannel = EventChannel('com.flutterquiz/screen_recording_events');

  static StreamController<bool>? _recordingStateController;
  static StreamSubscription<dynamic>? _eventSubscription;

  /// Stream that emits screen recording state changes (true = recording, false = not recording)
  static Stream<bool> get onRecordingStateChanged {
    _recordingStateController ??= StreamController<bool>.broadcast();
    return _recordingStateController!.stream;
  }

  /// Start listening for screen recording changes.
  /// Call this when entering a screen that needs recording detection.
  static Future<void> startListening() async {
    try {
      // Start native listener
      await _methodChannel.invokeMethod<void>('startListening');

      // Listen to event channel for recording state changes
      _eventSubscription = _eventChannel.receiveBroadcastStream().listen(
        (dynamic isRecording) {
          _recordingStateController?.add(isRecording as bool);
        },
        onError: (dynamic error) {
          // Silently handle errors - recording detection is optional
        },
      );
    } on PlatformException {
      // Platform doesn't support this feature - ignore
    }
  }

  /// Stop listening for screen recording changes.
  /// Call this when leaving the screen.
  static Future<void> stopListening() async {
    try {
      await _methodChannel.invokeMethod<void>('stopListening');
      await _eventSubscription?.cancel();
      _eventSubscription = null;
    } on PlatformException {
      // Ignore
    }
  }

  /// Check current recording state (one-time check)
  static Future<bool> isRecording() async {
    try {
      final result = await _methodChannel.invokeMethod<bool>('isRecording');
      return result ?? false;
    } on PlatformException {
      return false;
    }
  }

  /// Dispose the controller when app is closing
  static void dispose() {
    _recordingStateController?.close();
    _recordingStateController = null;
    _eventSubscription?.cancel();
    _eventSubscription = null;
  }
}
