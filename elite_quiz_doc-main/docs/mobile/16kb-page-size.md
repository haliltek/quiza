---
title: 16 KB Page Size Compatibility
sidebar_position: 9
---

import useBaseUrl from '@docusaurus/useBaseUrl';

# 16 KB Page Size Compatibility

Google Play requires all new apps and updates targeting Android 15+ devices to support 16 KB page sizes starting November 1, 2025.

### At a glance

- **Required for:** Elite Quiz **v2.3.5 and earlier** (when publishing to Android 15+)
- **Not required for:** **v2.3.6+** (coming soon; includes 16 KB support out of the box)
- **Why:** Newer devices use 16 KB memory pages; apps must be compatible to avoid issues and meet Play requirements

## What is 16 KB page size?

Android historically used 4 KB memory pages. As devices ship with more RAM, manufacturers are adopting larger pages like 16 KB. Android 15 adds platform support for 16 KB devices so apps can run reliably and benefit from performance gains.

## Performance benefits

The 16 KB page size requirement brings significant performance improvements:

- **Faster app launches:** See improvements ranging from 3% to 30% for various apps
- **Improved battery usage:** Experience an average gain of 4.5%
- **Quicker camera starts:** Launch the camera 4.5% to 6.6% faster
- **Speedier system boot-ups:** Boot Android devices approximately 8% faster

## Version compatibility

:::info
**Important:** This compatibility requirement applies to Elite Quiz versions **v2.3.5 and earlier**. If you are using **v2.3.6 or later**, this update is **not required** as the compatibility has already been built into the app.
:::

:::warning
**Note:** Version 2.3.6 is not yet released but will be available very soon. Once released, all new installations and updates will automatically include 16 KB page size compatibility.
:::

## Why this matters

Without 16 KB page size compatibility, your app might not function correctly on newer Android devices that use the larger page size. This could result in:

- Poor performance on newer devices
- Inability to publish updates to Google Play Store after November 1st, 2025

## Implementation Instructions

If you're using Elite Quiz v2.3.5 or earlier, you'll need to make the following changes to ensure 16 KB page size compatibility. These changes involve updating your Android build configuration.

### Required Changes

#### 1. Update Android Build Configuration

You need to modify the `android/app/build.gradle` file with the following changes:

```gradle title="android/app/build.gradle" {3,22-25}
android {
    namespace "com.wrteam.flutterquiz"
    compileSdkVersion 36  // Changed from 35

    compileOptions {
        coreLibraryDesugaringEnabled true
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }

    kotlinOptions {
        jvmTarget = '1.8'
    }

    sourceSets {
        main.java.srcDirs += 'src/main/kotlin'
    }

    defaultConfig {
        // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
        applicationId "com.wrteam.flutterquiz"
        minSdkVersion flutter.minSdkVersion  // Changed from 23
        targetSdkVersion 36  // Changed from 35
        ndkVersion "29.0.14033849"  // Changed from "26.1.10909125"
        versionCode flutterVersionCode.toInteger()
        versionName flutterVersionName
        multiDexEnabled true
    }
    // ... rest of your configuration
}
```

#### Key Changes Explained:

1. **`compileSdkVersion`**: Updated from `35` to `36` to support the latest Android features
2. **`minSdkVersion`**: Changed from hardcoded `23` to `flutter.minSdkVersion` for better Flutter compatibility
3. **`targetSdkVersion`**: Updated from `35` to `36` to target the latest Android version
4. **`ndkVersion`**: Updated from `"26.1.10909125"` to `"29.0.14033849"` for better native code support

#### 2. Verify Gradle Wrapper Version

Ensure your Gradle Wrapper uses Gradle 8.7 (all distribution). Open `android/gradle/wrapper/gradle-wrapper.properties` and confirm the `distributionUrl` line is:

```properties title="android/gradle/wrapper/gradle-wrapper.properties"
distributionUrl=https\://services.gradle.org/distributions/gradle-8.7-all.zip
```

#### 3. Update Gradle Settings Plugins

Update plugin versions in `android/settings.gradle` to ensure toolchain compatibility:

```groovy title="android/settings.gradle" {3-4}
plugins {
    id 'dev.flutter.flutter-plugin-loader' version '1.0.0'
    id 'com.android.application' version '8.6.0' apply false  // was 8.5.2
    id 'org.jetbrains.kotlin.android' version '2.1.0' apply false  // was 2.0.0
    id 'com.google.gms.google-services' version '4.3.15' apply false
    id 'com.google.firebase.crashlytics' version '2.8.1' apply false
}
```

Changes made:

- **Android Gradle Plugin**: 8.5.2 → 8.6.0
- **Kotlin Android plugin**: 2.0.0 → 2.1.0
- Quote style normalized to single quotes (no functional impact)

#### 4. Update Flutter Dependency

Update `flutter_pdfview` in `pubspec.yaml` to ensure compatibility with the newer Android toolchain and rendering fixes:

```yaml title="pubspec.yaml"
dependencies:
  # ... other dependencies
  flutter_pdfview: ^1.4.3 # was ^1.4.1+1
```

### Implementation Steps

1. **Open your project** in Android Studio or your preferred IDE
2. **Navigate to** `android/app/build.gradle`
3. **Apply the changes** shown above
4. **Clean and rebuild** your project:
   ```bash
   flutter clean
   flutter pub get
   flutter build apk --release
   ```
5. **Test your app** thoroughly to ensure all functionality works correctly
6. **Build and publish** your updated app to Google Play Store

## Verify Compatibility

After applying the changes, verify that your app is recognized as 16 KB compatible:

### Option A: Follow Android’s official guidance

Use Google’s verification methods to test on a 16 KB environment and validate behavior:

- Set up a 16 KB emulator image or enable the 16 KB developer option on supported Pixel devices
- Use the `adb shell getconf PAGE_SIZE` check and (if needed) backcompat toggles
- Refer to: [Support 16 KB page sizes](https://developer.android.com/guide/practices/page-sizes)

### Option B (Recommended): Check with LibChecker

LibChecker shows per-app page size info on-device:

1. Install LibChecker from its official repository: [https://github.com/LibChecker/LibChecker](https://github.com/LibChecker/LibChecker)
2. Rebuild and install your app on the same device
3. Open LibChecker → find your app → check reported page size; it should display 16 KB
4. If it shows 4 KB, review the steps above and ensure all toolchain versions are updated

<img
src={useBaseUrl('/img/app/check_16kb_alignment.png')}
alt="LibChecker indicating 16 KB for Elite Quiz App"
style={{width: '30%', objectFit: 'cover'}}
/>

## Additional Resources

For more technical details about the 16 KB page size requirement, visit the [official Android Developers blog post](https://android-developers.googleblog.com/2025/05/prepare-play-apps-for-devices-with-16kb-page-size.html).
