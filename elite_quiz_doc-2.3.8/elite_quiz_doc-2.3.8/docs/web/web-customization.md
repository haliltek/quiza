---
sidebar_position: 7
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Web Customization

Elite Quiz allows for extensive customization of the user interface and branding elements.

## Changing Name

To change the name:

1. Go to Admin Panel > Profile and change the value of **appName**

![Change App Name](../../static/img/web/appname.png)

## Changing Logo

**To change logo, favicon, Firebase, footer data, quizplay images, etc:**

1. Go to Admin Panel -> Web Settings -> Settings

![Web Settings](../../static/img/web/websettings.png)

### Setting SEO Meta Tags

1. Go to .env file to configure SEO meta tags

![Meta Tags](../../static/img/web/meta.png)

### Changing Favicon Icon

Note: Please set your favicon icon as `favicon.ico` name and format is only ico set. You can use this tool to convert image to ico: [Favicon Generator](https://www.favicon-generator.org/)

1. Go to public folder -> favicon.ico

![Favicon](../../static/img/web/favicon.png)

## Changing Application Colors

To change the application colors:

1. Add your colors in Admin Panel -> Web Settings -> Settings

![Theme Colors](../../static/img/web/theme-color.webp)

2. To change dark mode primary color

![Dark Mode Primary Color](../../static/img/web/darkprimarycolor.png)

## Changing Application Font

To change the application font:

1. Go to YOUR_APP_FOLDER/src/style/global.css and add your font as shown in the image
2. You can get fonts from [Google Fonts](https://fonts.google.com/)

![Change Font](../../static/img/web/changeFont.png)

## PWA Settings

PWA is use for user can install your website as a app in mobile device or computer
1. To change the PWA settings: Go to .env file


![PWA Settings](../../static/img/web/pwa.png)

## Adding Slider on Homepage

To add or modify sliders on the homepage:

1. Go to admin panel -> web settings -> slider

![Add Slider](../../static/img/web/addslider.png)

## Adding Badge Images

To add or modify badge images:

1. Go to admin panel -> Settings -> Badges Settings

![Add Badges](../../static/img/web/badges.png)

## RTL Support (Right-to-Left)

To enable RTL support for languages like Arabic or Hebrew:

1. Go to Admin Panel -> System Languages

![RTL Settings](../../static/img/web/rtl.webp)

## Setting Domain URL

To set the Domain URL:

1. Go to .env file

![Domain URL](../../static/img/web/domainUrl.png)

## Configuring Sitemap

To configure the sitemap for better SEO:

1. First set domain web url in .env file
2. Second open terminal and run command:

   <Tabs>
   <TabItem value="npm" label="npm" default>

   ```bash
   npm run dev
   ```

   </TabItem>
   <TabItem value="bun" label="bun">

   ```bash
   bun run dev
   ```

   </TabItem>
   </Tabs>

3. Go to public -> sitemap.xml

![Sitemap](../../static/img/web/sitemap.png)

## Changing Timer Settings

To adjust the timer and other features settings:

1. Go to Admin Panel -> Settings -> System Utilities

![System Utilities](../../static/img/web/system-utilites.png)

## Disabling Home Sections

To disable specific sections on the homepage:

1. Go to Admin Panel -> Web Settings -> Home Settings

![Home Sections](../../static/img/web/home-sections.webp)

## Score Configuration

To configure scoring:

1. Go to Admin Panel -> Settings -> System Utilities

![Score Configuration](../../static/img/web/score-add.png)

## Adding Google AdSense

To add Google AdSense to your application:

1. Go to [Google AdSense](https://adsense.google.com) and sign in to your account
2. Add your site as shown in the image

![AdSense](../../static/img/web/adsense.png)

3. Click on "Let's Go" button

![AdSense Site](../../static/img/web/adsensesite.png)

4. Copy the script code and paste it to your src -> pages -> \_document.js

![First Verify](../../static/img/web/first_verify.png)
![Script HTML](../../static/img/web/scripthtml.png)

5. After adding the script, run the command for build folder:

   <Tabs>
   <TabItem value="npm" label="npm" default>

   ```bash
   npm run export
   ```

   </TabItem>
   <TabItem value="bun" label="bun">

   ```bash
   bun run export
   ```

   </TabItem>
   </Tabs>

   ...and upload to your server

6. After uploading, click on verify button in Google AdSense

![Verify](../../static/img/web/verify.png)

7. If it says **"Getting ready…,"** your account is still under review and your site will not display ads until it has been approved

![Under Review](../../static/img/web/under_re.png)
