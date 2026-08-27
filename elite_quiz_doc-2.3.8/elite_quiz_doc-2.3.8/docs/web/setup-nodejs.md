---
sidebar_position: 1
---

import useBaseUrl from '@docusaurus/useBaseUrl';

# Installation Guide

This guide provides a detailed walkthrough of the installation process for the Elite Quiz web application.

## Prerequisites

Before you begin setting up the Elite Quiz web version, ensure you have the following prerequisites installed:

:::info Note
You must install Node.js version 18 or later for the web application to function properly.
:::

1. **Node.js**: Version 18 or later

   - [Download Node.js](https://nodejs.org/en/download)
   - [Step-by-step guide to install Node.js](https://www.wrteam.in/blog/step-by-step-guide-to-install-nodejs-on-windows-mac/)

2. **Code editor**: [Visual Studio Code](https://code.visualstudio.com/) (recommended)

## How to setup Node Js on Windows?

1. If your system already has npm package installed, you can skip this step.

2. To check whether your system already has npm package installed or not, open Command Prompt and type the following commands:

```bash
node -v
npm -v
```

3. If npm is already installed, these commands will display the versions:

   <img
   src={useBaseUrl('/img/web/react-npm-check.webp')}
   alt="NPM Version Check"
   style={{width: '100%', objectFit: 'cover'}}
   />

4. If npm is not installed, download it from the official website: [npm](https://nodejs.org/en)

5. Download the "Recommended For Most Users" option for Windows (x64):

   <img
   src={useBaseUrl('/img/web/react-npm-node.webp')}
   alt="Download NPM"
   style={{width: '100%', objectFit: 'cover'}}
   />

6. After downloading the installer, follow these steps:

   - Launch the installer
   - Click next
   - Review and accept the End-user License Agreement; click next
   - Select your destination path; click next
   - In custom setup panel, select `npm package manager` option and click next

   **Step 1:**
   <img
   src={useBaseUrl('/img/web/react-npm-step1.webp')}
   alt="NPM Installation Step 1"
   style={{width: '100%', objectFit: 'cover'}}
   />

   **Step 2:**
   <img
   src={useBaseUrl('/img/web/react-npm-step2.webp')}
   alt="NPM Installation Step 2"
   style={{width: '100%', objectFit: 'cover'}}
   />

   **Step 3:**
   <img
   src={useBaseUrl('/img/web/react-npm-step3.webp')}
   alt="NPM Installation Step 3"
   style={{width: '100%', objectFit: 'cover'}}
   />

   **Step 4:**
   <img
   src={useBaseUrl('/img/web/react-npm-step4.webp')}
   alt="NPM Installation Step 4"
   style={{width: '100%', objectFit: 'cover'}}
   />

   **Step 5:**
   <img
   src={useBaseUrl('/img/web/react-npm-step5.webp')}
   alt="NPM Installation Step 5"
   style={{width: '100%', objectFit: 'cover'}}
   />

   **Step 6:**
   <img
   src={useBaseUrl('/img/web/react-npm-step6.webp')}
   alt="NPM Installation Step 6"
   style={{width: '100%', objectFit: 'cover'}}
   />

7. Verify npm installation by running the commands mentioned in steps 2 and 3.

## Installing Bun (Alternative Package Manager)

[Bun](https://bun.sh/) is a fast, all-in-one JavaScript runtime & toolkit designed for speed, including a package manager, bundler, and test runner. If you prefer to use Bun instead of npm, follow the steps below.

:::note
Always refer to the [official Bun installation guide](https://bun.sh/docs/installation) for the most up-to-date commands.
:::

### macOS / Linux

Open your terminal and run the following command:

```bash
curl -fsSL https://bun.sh/install | bash
```

This script installs `bun` to `~/.bun/bin`. You might need to add this directory to your `PATH` environment variable. The script will usually provide instructions on how to do this if needed.

### Windows

Open PowerShell (it's recommended to run it as Administrator) and run the following command:

```powershell
powershell -c "irm https://bun.sh/install.ps1 | iex"
```

### Verification

After installation, close and reopen your terminal or PowerShell window. Then, verify the installation by running:

```bash
bun -v
```

This command should display the installed version of Bun.
