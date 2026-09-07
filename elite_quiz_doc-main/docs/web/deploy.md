---
sidebar_position: 9
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Deploying the Web Application

This guide will walk you through the process of deploying your Elite Quiz web application to a production server.

## Building for Production

1. After all the changes, you are ready to deploy your Web application on a Live Server.

2. Open VS Code terminal by typing **CTRL+J** in Windows/Linux, or **CMD+J** for MacOS and execute the command:

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

   This will take a few seconds to build the live and optimized version of the web application.

3. After the process completes, go to web's code root files -> out folder and upload these files to your live server.

   :::caution Important
   Only upload the **out** folder's files on the server. Do not upload any other files to the server.
   :::

4. If you're facing any deployment-related problems, you can follow the official documentation: [Next.js Web Deployment](https://nextjs.org/docs/pages/building-your-application/deploying)

## How to Update to a New Version

If you need to update your web application to a new version:

1. Extract the zip file of web code which you get from CodeCanyon.
2. Open the web code in VS Code editor.
3. Download Node.js (version 20) or Bun from their respective official websites if not already installed.
4. Open the .env file in your project.
5. Add your admin URL and web URL as per the documentation.
6. Add your title, description, keywords, and other details in the .env file.
7. Run the install command in your terminal:
   <Tabs>
   <TabItem value="npm" label="npm" default>

   ```bash
   npm i
   ```

   </TabItem>
   <TabItem value="bun" label="bun">

   ```bash
   bun install
   ```

   </TabItem>
   </Tabs>

8. Run the command to build your project:
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

9. After the `out` folder is created, make a zip of the `out` folder and upload the contents inside the `out` folder to your web domain or subdomain server.

## Deployment Options

### Traditional Web Hosting

1. Upload the contents of the `out` folder to your web server using FTP or SSH
2. Configure your web server to serve the files correctly

### Deployment Platforms

Elite Quiz can be deployed on various platforms:

- **[Hostinger](https://www.hostinger.com/)**: Affordable and reliable hosting solution
- **[Vercel](https://vercel.com/)**: Optimal for Next.js applications
- **[Netlify](https://www.netlify.com/)**: Easy deployment with continuous integration

## Post-Deployment Verification

After deploying, verify the following:

1. The site loads correctly at your domain
2. User authentication works properly
3. API calls are successful
4. All features function as expected
5. No console errors appear
6. The site is responsive on different devices

## Setting Up a Custom Domain

If you're using a custom domain:

1. Purchase a domain from a domain registrar
2. Configure your DNS settings to point to your hosting provider
3. Add SSL certificate for HTTPS (many hosting providers offer this automatically)
