---
sidebar_position: 3
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Running the Project

## Step-by-Step Process

1. Open VS Code terminal by typing **CTRL+J** in Windows/Linux, and for MacOS **CMD+J** and execute the install command:

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

   This will take some time to download the necessary packages, so wait for a few minutes.

2. After the installation finishes, run the development command:
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

   This will launch the development server, and your application should be accessible at `http://localhost:3000`.

## Troubleshooting

If you encounter any issues during the installation:

1. Make sure you have the correct version of Node.js (or Bun) installed
2. Check that all environment variables are correctly set in the `.env` file
3. Try deleting the `node_modules` folder and running `npm i` (or `bun install`) again
4. Check your console for specific error messages

## Next Steps

After completing the installation, you'll need to:

1. [Integrate Firebase](./firebase-integration.md)
2. [Common Firebase Configuration](../common_firebase_config.md)
3. [Customize your application](./web-customization.md)
