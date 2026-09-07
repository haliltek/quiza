# Configure Ads

Elite Quiz supports Google AdMob for displaying advertisements within your mobile app. This guide will walk you through setting up and configuring ads to monetize your quiz application.

## Setting Up Google AdMob

### 1. Creating an AdMob Account

1. Go to [AdMob.com](https://admob.google.com/) and sign in with your Google account
2. Create a new app in the AdMob console (or link to your existing app)
3. Get your AdMob App ID for Android and iOS

### 2. Adding Ad Units

In the AdMob console, create the following ad units for your app:

- **Banner Ad**: Small rectangular ads that appear at the top or bottom of the screen
- **Interstitial Ad**: Full-screen ads that appear between app activities
- **Rewarded Ad**: Full-screen ads that users can watch to earn in-app rewards

Note down the ad unit IDs for each ad type as you'll need them for configuration.

## Configuring Ad IDs in the App

### 1. Add Ad Ids in the admin panel

1. Open the admin panel > Settings > Ads Settings
2. Select the Google Admob and add all the ad ids.

![Add Google Ad IDs](/img/app/add-googe-ad-ids.webp)

### 2. Platform-Specific Configuration

Make sure to:

- Use the correct ad unit IDs for each platform (Android/iOS)
- Replace the example IDs with your actual AdMob ad unit IDs
- Keep the format consistent with the AdMob ID structure

## Enabling Ads in Admin Panel

### 1. System Settings Configuration

1. Log into your Admin Panel
2. Navigate to **System Settings**
3. Find the **Google Ads** section
4. Enable the ads you want to display:
   - Banner Ads
   - Interstitial Ads
   - Rewarded Ads

![Google Ads 1](/img/app/google-ads-1.webp)

![Google Ads 2](/img/app/google-ads-2.webp)

### 2. Ad Display Controls

You can control:

- Which ad types are shown to users
- When ads appear during the quiz experience
- Frequency of ad display

## Ad Types and Implementation

### Banner Ads

- Appear at the top or bottom of screens
- Least intrusive to user experience
- Provide consistent ad revenue

### Interstitial Ads

- Full-screen ads shown between activities
- Higher revenue potential
- Should be used sparingly to avoid user frustration

### Rewarded Ads

- Users voluntarily watch ads to earn coins
- Best user experience as they provide value
- Higher engagement rates

## Testing Your Ad Configuration

### Before Publishing

1. **Add Test Device IDs**: Configure your device as a test device in AdMob
2. **Test All Ad Types**: Verify banner, interstitial, and rewarded ads display correctly
3. **Check Ad Loading**: Ensure ads load properly on both Android and iOS
4. **Verify Revenue Tracking**: Confirm that ad impressions are being tracked in AdMob

### Test Device Setup

Add your test device IDs to prevent accidental clicks on live ads during development:

```dart
// Add test device IDs for development
static const String testDeviceId = "YOUR_TEST_DEVICE_ID";
```

## Troubleshooting Common Issues

### Ad Not Loading

- Verify ad unit IDs are correct
- Check internet connectivity
- Ensure AdMob account is properly set up
- Verify app is approved in AdMob console

### Revenue Not Tracking

- Confirm ad unit IDs match AdMob console
- Check that ads are actually being displayed
- Verify AdMob account settings
- Allow 24-48 hours for revenue data to appear

### iOS Specific Issues

- Ensure iOS ad unit IDs are different from Android
- Verify App Store approval status
- Check iOS 14+ privacy settings compliance
