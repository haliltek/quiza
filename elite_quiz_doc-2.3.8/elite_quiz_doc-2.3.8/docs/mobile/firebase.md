---
title: Authentication Setup
sidebar_position: 4
---

This guide provides instructions for integrating Firebase Authentication into your App.

Before proceeding, ensure you have completed the initial [Common Firebase Configuration](../common_firebase_config).

#### Prerequisites

- You should have already changed your [app’s package name](../mobile/configuration.md#change-the-package-name).
- If you want to go with Option 1 for setup, you must have Firebase CLI installed and you must be logged in to your account.

## Option 1: Automated Setup with FlutterFire CLI

The FlutterFire CLI offers the quickest method for configuring Firebase in your project. It relies on the underlying Firebase CLI for its operations.

### 1. Install FlutterFire CLI

If you have not already installed the CLI, run the following command in your terminal:

```sh
dart pub global activate flutterfire_cli
```

### 2. Configure Your Project

To link your Flutter application with your Firebase project, run the command below. Replace `<your-project-id>` with the actual Project ID from your Firebase project settings.

```sh
flutterfire --configure project=<your-project-id>
```

Follow the interactive prompts in your terminal to select the target platforms and complete the configuration.

---

## Option 2: Manual Firebase Configuration

If you prefer to configure your project manually, follow the platform-specific instructions below.

### Android Configuration

1. Navigate to the **Project Overview** in the Firebase console and click the **Android icon** to launch the setup workflow.
2. In the **Package name** field, enter your application's package name.
3. Optionally, provide an **App nickname**.
4. Click **Register app**.
5. Download the generated `google-services.json` file.
6. Move the `google-services.json` file into the `android/app/` directory of your Flutter project.
7. Click **Next** on the remaining on-screen instructions in the Firebase console to complete the setup.

<details>
  <summary>Click to view Android Setup Screenshots</summary>
  
  ![Add Android](/img/app/addAndroid.webp)
  ![Add Android 2](/img/app/addAndroid2.webp)
  ![Add Android 3](/img/app/addAndroid3.webp)
  ![Add Android 4](/img/app/addAndroid4.webp)
  ![Add Android 5](/img/app/addAndroid5.webp)
  ![Add Android 6](/img/app/addAndroid6.webp)
</details>

### iOS Configuration

1. Navigate to the **Project Overview** in the Firebase console and click the **iOS icon** to launch the setup workflow.
2. In the **Apple bundle ID** field, enter your app's Bundle ID. You can find this in your Xcode project under `ios/Runner.xcodeproj/project.pbxproj`.
3. Optionally, provide an **App nickname** and **App Store ID**.
4. Click **Register app**.
5. Download the generated `GoogleService-Info.plist` file.
6. Move the `GoogleService-Info.plist` file into the `ios/Runner/` directory of your Flutter project.
7. Click **Next** on the remaining on-screen instructions in the Firebase console to complete the setup.

<details>
  <summary>Click to view iOS Setup Screenshots</summary>
  
![Add iOS](/img/app/addIos.webp)
![Add iOS 2](/img/app/addIos2.webp)
![Add iOS 3](/img/app/addIos3.webp)
![Add iOS 4](/img/app/addIos4.webp)
![Add iOS 5](/img/app/addIos5.webp)
![Add iOS 6](/img/app/addIos6.webp)
</details>

---

## Post-Setup Configuration

After the initial setup, additional platform-specific steps are required for authentication services to function correctly.

### 1. Android: Add SHA Fingerprints

For Google Sign-In and other authentication methods to work securely, you must add your app's SHA certificate fingerprints to your Firebase project.

1. Generate the SHA-1 and SHA-256 fingerprints for both your **debug** and **release** keystores.
2. Navigate to your Firebase project's **Project Settings** \> **General**.
3. Scroll down to the **Your apps** card, select your Android app, and add the fingerprints under **SHA certificate fingerprints**.

    **Important:** You must add fingerprints for all build and distribution scenarios. This typically includes:
        - Two SHA keys from your debug keystore for development.
        - Two SHA keys from your release keystore for publishing.
        - Two SHA keys from the Google Play Console after your app is published (closed/open testing, production).

    A total of six SHA fingerprints are required for authentication to work in all the scenarios.
4. After adding the fingerprints, **re-download** the `google-services.json` file and replace the existing one in your `android/app/` directory.

### 2. iOS: Configure a URL Scheme

To handle authentication callbacks from services like Google Sign-In, you must configure a custom URL scheme for your iOS app.

1. Open the `ios/Runner/GoogleService-Info.plist` file and locate the `REVERSED_CLIENT_ID` key. Copy its string value.

2. In Editor, open `ios/Runner/Info.plist`.

3. Replace `YOUR_REVERSED_CLIENT_ID` with the value you copied within the main `<dict>`.

    ```xml
    <key>CFBundleURLTypes</key>
    <array>
        <dict>
            <key>CFBundleTypeRole</key>
            <string>Editor</string>
            <key>CFBundleURLSchemes</key>
            <array>
                <string>YOUR_REVERSED_CLIENT_ID</string>
            </array>
        </dict>
    </array>
    ```

### 3. Admin Panel: Connect Firebase Account

To allow the admin panel to communicate with Firebase, you must provide it with a private service account key

1. In your Firebase project, go to [Project Settings > Service accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk).
2. Click **Generate new private key** and download the file.
3. In your Admin Panel, go to **Settings \> Firebase Configurations** and upload the downloaded key file.

## Verifying the Integration

To confirm that Firebase has been configured correctly, **restart your application** and test the following functionalities:

- **User Registration:** Ensure new users can successfully create an account.
- **User Login:** Verify that existing users can sign in.
- **Social Authentication:** Test sign-in with external providers like Google or Apple.

### Troubleshooting

If you encounter issues, review your application logs and the Firebase console for specific error messages. Most problems can be resolved by carefully verifying that:

- All configuration files (`google-services.json`, `GoogleService-Info.plist`) are correctly placed.
- The necessary SHA fingerprints and URL schemes have been correctly added.
- The service account key has been updated in the Admin Panel.

Revisiting the setup steps and ensuring each one was completed accurately will often resolve common integration issues.