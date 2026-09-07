---
sidebar_position: 5
---

import useBaseUrl from '@docusaurus/useBaseUrl';

# App Customization

Customize the Elite Quiz App to match your brand identity and preferences.

## Branding Structure

We've organized all branding-related configurations and assets into separate folders, making it easy to modify them without missing anything. This structure also simplifies updating to newer app versions, as you only need to check for changes in the config files and update the folders.

There are two primary folders for branding customization:

1. **App Configuration** (`lib/core/config`): Contains settings for panel URL, default theme, messages, payment methods, and other app configurations.

2. **Assets Configuration** (`assets/config`): Contains all images and assets related to branding, including sounds and profile avatar images you might want to customize.

Beyond these folders, you're free to modify other assets and app code for additional flexibility. This separation makes rebranding the app straightforward for most users.

## Update App Launcher Icons

We use the `flutter_launcher_icons` package to generate launcher icons for Android and iOS. This approach makes the process quick, easy, and reproducible—especially helpful for setup and app updates.

### Setup Steps

> Tip: For optimal results, separate your logo foreground from the background.

1. Navigate to `assets/config/launcher_icons` and update these files:

   - `app_logo_icon.png`: 1024x1024 recommended
   - `background.png`: 432x432 recommended
   - `foreground.png`: 432x432 recommended

> **Image Format Note:** You can use JPG format, but you'll need to modify the `flutter_launcher_icons.yaml` file to specify the correct image format, otherwise it won't work.

2. Run the following command in your project directory to generate the icons:

```shell
dart run flutter_launcher_icons
```

3. Verify Generated Icons

   - **Android icons:** Generated in `android/app/src/main/res/`
   - **iOS icons:** Generated in `ios/Runner/Assets.xcassets/AppIcon.appiconset/`

4. Additional Options

   - For platform-specific icons, use `image_path_android` and `image_path_ios`
   - To remove alpha channel from iOS icons, add `remove_alpha_ios: true`

### Apply Changes

After generating the icons, rebuild your app to see the changes:

```shell
flutter clean
flutter pub get
flutter run
```

## Update App Logos in the App

You can customize the app logo that appears in the Splash screen, Sign in/ Sign up etc screens:

1. Navigate to `assets/config/` directory in your project.
2. Update the following images.
   - `app_logo.svg`: shown in login, sign up, otp login etc screens.
   - `placeholder.png`: shown in case of error or as a fallback in whole app. 96x96 recommended.
   - `splash_logo.svg`: shown in the splash screen.
   - `org_logo.svg`: shown in splash screen in the bottom.

You can customize image formats and control org logo visibility by modifying the configuration file:

```dart title='lib/core/config/config.dart'
// Change logo file formats (png, jpg, etc.)
const kAppLogo = 'app_logo.svg';
const kSplashLogo = 'splash_logo.svg';
const kOrgLogo = 'org_logo.svg';
const kPlaceholder = 'placeholder.png';

// Set to false to hide organization logo in splash screen
const kShowOrgLogo = true;
```

3. Then rebuild the app to see the changes.

<div style={{display: 'flex', gap: '20px', alignItems: 'flex-start'}}>
  <img
    src={useBaseUrl('/img/app/change_app_logo.webp')}
    alt="Change App Logo"
    style={{width: '30%', objectFit: 'cover'}}
  />
  <img
    src={useBaseUrl('/img/app/change_splash_and_org_logo.webp')}
    alt="Change Splash and Logo"
    style={{width: '30%', objectFit: 'cover'}}
  />
</div>

## Customize App Colors

Customize your app's color scheme to match your brand identity. We recommend using your own brand colors instead of the default Elite Quiz colors.

Navigate to `lib/core/config/colors.dart` and update the color constants with your brand colors:

```dart title='lib/core/config/colors.dart'
/// Light Theme Colors
const klBackgroundColor = Color(0xffffffff); // White color for containers, cards, lists
const klCanvasColor = Color(0xcc000000); // Black color for overlays
const klPageBackgroundColor = Color(0xfff3f7fa); // Main scaffold background color
const klPrimaryColor = Color(0xffef5388); // Primary branding color
const klPrimaryTextColor = Color(0xff45536d); // Main text color

/// Additional theme colors available in the file
```

Save the file and restart your app to see the changes

## Managing System Languages (Translations)

System languages control the interface translations for the admin panel, mobile app, and web application.

You can update, add, and edit app language translations directly from the admin panel without needing to rebuild or redeploy the app and web.

1. Go to your admin panel
2. Go to the `System Languages` section
3. Add or edit languages as needed

![Manage System Languages](/img/panel/manage_system_languages.webp)

**To modify translations**: Click on the Eye icon in the Operations Column to update or modify the translations (see number 3 in the image).

## Managing Quiz Languages

Quiz languages control the content structure of your app, including categories, subcategories, and questions. This system allows you to have completely different content structures for different languages across all quizzes.

### Key Features

- **Content Separation**: Each language can have its own category structure and questions
- **Flexible Organization**: Different content for Hindi vs English, or any other language combination
- **Language Mode Control**: Disable language mode if you only want one language

### Configuration

**To disable language mode** (single language only):

1. Go to Panel > Settings > System Configurations
2. Disable the Language Mode option

![Admin Language 1](/img/app/admin-language-1.webp)

**To manage quiz languages**:

1. Navigate to the Languages Section in your admin panel
2. Configure your desired language structure

![Admin Language 2](/img/app/admin-language-2.webp)

### Advanced Usage

:::tip Flexible Categorization
While we refer to this as "language-wise" categorization, you can actually use it for various organizational structures:

- **Classes**: Different content for Class 7 vs Class 10 students
- **Subjects**: Separate content by academic subjects
- **Regions**: Location-specific content
- **Professions**: Career-specific quiz content
- **Interests**: Interest-based content organization

The possibilities are endless for organizing your quiz content!
:::

## Additional Customization Options

### Configuration Files

You can modify additional settings and assets from:

- **`lib/core/config` folder**: Core app configurations
- **`assets/config/` folder**: Branding assets and resources

### Admin Panel Settings

Explore the admin panel for additional customization options:

- **System Utilities**: Configure quiz behavior and rules
- **System Configurations**: Advanced system settings

Take time to review all available options to fully customize your Elite Quiz experience.
