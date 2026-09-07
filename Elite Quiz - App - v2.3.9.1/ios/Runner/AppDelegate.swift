import UIKit
import Flutter
import Firebase
import Photos
import CallKit

@UIApplicationMain
@objc class AppDelegate: FlutterAppDelegate {

    var callObserver: CXCallObserver!

    let preventAnnounceView = UIView(frame: CGRect.init(x: 0, y: 0, width: UIScreen.main.bounds.width, height: UIScreen.main.bounds.height))

    // Screen recording detection
    private var screenRecordingEventSink: FlutterEventSink?
    private var isListeningForRecording = false

    override func application( _ application: UIApplication,didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        if #available(iOS 10.0, *) {
            UNUserNotificationCenter.current().delegate = self as? UNUserNotificationCenterDelegate
        }
        GeneratedPluginRegistrant.register(with: self)
        if FirebaseApp.app() == nil {
            FirebaseApp.configure()
        }

        callObserver = CXCallObserver()
        callObserver.setDelegate(self, queue: nil)

        // Setup screen recording detection channels
        setupScreenRecordingChannels()

        return super.application(application, didFinishLaunchingWithOptions: launchOptions)
    }

    private func setupScreenRecordingChannels() {
        guard let controller = window?.rootViewController as? FlutterViewController else {
            return
        }

        // Method channel for start/stop listening
        let methodChannel = FlutterMethodChannel(
            name: "com.flutterquiz/screen_recording",
            binaryMessenger: controller.binaryMessenger
        )

        methodChannel.setMethodCallHandler { [weak self] (call, result) in
            switch call.method {
            case "startListening":
                self?.startListeningForScreenRecording()
                result(nil)
            case "stopListening":
                self?.stopListeningForScreenRecording()
                result(nil)
            case "isRecording":
                result(UIScreen.main.isCaptured)
            default:
                result(FlutterMethodNotImplemented)
            }
        }

        // Event channel for screen recording state changes
        let eventChannel = FlutterEventChannel(
            name: "com.flutterquiz/screen_recording_events",
            binaryMessenger: controller.binaryMessenger
        )
        eventChannel.setStreamHandler(self)
    }

    private func startListeningForScreenRecording() {
        guard !isListeningForRecording else { return }
        isListeningForRecording = true

        NotificationCenter.default.addObserver(
            self,
            selector: #selector(screenRecordingChanged),
            name: UIScreen.capturedDidChangeNotification,
            object: nil
        )

        // Send initial state
        screenRecordingEventSink?(UIScreen.main.isCaptured)
    }

    private func stopListeningForScreenRecording() {
        guard isListeningForRecording else { return }
        isListeningForRecording = false

        NotificationCenter.default.removeObserver(
            self,
            name: UIScreen.capturedDidChangeNotification,
            object: nil
        )
    }

    @objc private func screenRecordingChanged() {
        screenRecordingEventSink?(UIScreen.main.isCaptured)
    }
    // Commented out: Screen capture protection is now managed by screen_protector package
    // override func applicationDidBecomeActive(_ application: UIApplication) {
    //     self.window?.isHidden = false
    // }
    // override func applicationWillResignActive(_ application: UIApplication) {
    //     self.window?.rootViewController?.view.endEditing(true)
    //     self.window?.isHidden = true
    // }

    // @objc private func hideScreen(notification:Notification) -> Void {
    //     configurePreventView()
    //     if UIScreen.main.isCaptured {
    //         window?.addSubview(preventAnnounceView)
    //     } else {
    //         preventAnnounceView.removeFromSuperview()
    //     }
    // }

    // private func configurePreventView() {
    //     preventAnnounceView.backgroundColor = .black
    //     let preventAnnounceLabel = configurePreventAnnounceLabel()
    //     preventAnnounceView.addSubview(preventAnnounceLabel)
    // }

    // private func configurePreventAnnounceLabel() -> UILabel {
    //     let preventAnnounceLabel = UILabel()
    //     preventAnnounceLabel.text = "Can't record screen"
    //     preventAnnounceLabel.font = .boldSystemFont(ofSize: 30)
    //     preventAnnounceLabel.numberOfLines = 0
    //     preventAnnounceLabel.textColor = .white
    //     preventAnnounceLabel.textAlignment = .center
    //     preventAnnounceLabel.sizeToFit()
    //     preventAnnounceLabel.center.x = self.preventAnnounceView.center.x
    //     preventAnnounceLabel.center.y = self.preventAnnounceView.center.y

    //     return preventAnnounceLabel
    // }
}

// MARK: - FlutterStreamHandler for screen recording events
extension AppDelegate: FlutterStreamHandler {
    func onListen(withArguments arguments: Any?, eventSink events: @escaping FlutterEventSink) -> FlutterError? {
        screenRecordingEventSink = events
        return nil
    }

    func onCancel(withArguments arguments: Any?) -> FlutterError? {
        screenRecordingEventSink = nil
        return nil
    }
}

extension AppDelegate: CXCallObserverDelegate {
    
    func callObserver(_ callObserver: CXCallObserver, callChanged call: CXCall) {
        if call.hasEnded == true {
            print("Call Disconnected")
        }
        
        if call.isOutgoing == true && call.hasConnected == false {
            print("call Dialing")
        }
        
        if call.isOutgoing == false && call.hasConnected == false && call.hasEnded == false {
            print("call Incoming")
        }
        
        if call.hasConnected == true && call.hasEnded == false {
            print("Call Connected")
        }
    }
}
