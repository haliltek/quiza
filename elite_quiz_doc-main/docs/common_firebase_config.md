---
pagination_prev: null
pagination_next: null
---

# Common Firebase Configuration

This guide will help you set up Firebase for Elite Quiz, step by step. No prior experience with Firebase is required. Just follow along, and you’ll be ready in no time.

---

## Why Do I Need Firebase?

Elite Quiz uses Firebase for two main things:

- **Authentication:** Let users sign in with Email, Google, Apple, or Phone.
- **Firestore Database:** Store battle quiz progress, battle messages.

---

## Step 1: Create Your Firebase Project

1. Go to the [Firebase Console](https://console.firebase.google.com/).
2. Click **Add project**.
3. Enter a project name (e.g., `EliteQuiz`) and accept the terms.
4. Choose whether to enable Google Analytics (recommended for most users).
5. Click **Create project** and wait for setup to finish.

You’ll see your new project dashboard when it’s ready.

![Screenshot: Creating a Firebase Project](/img/app/createFirebase1.webp)
![Screenshot: Firebase Project Setup Steps](/img/app/createFirebase2.webp)

---

## Step 2: Enable Sign-In Methods

Elite Quiz supports several ways for users to sign in. Enable them all now — you can turn off any you don’t want later from the admin panel.

:::note Important Note
To use Phone/OTP Login, your Firebase project must be on the **Blaze** (pay-as-you-go) plan. This feature will not work on the Spark (free tier) plan.
:::

**How to enable sign-in methods:**

1. In your Firebase project, click [**Authentication**](https://console.firebase.google.com/project/_/authentication/providers) in the left menu.
2. Go to the **Sign-in method** tab.
3. Enable these providers:
   - Email/Password
   - Phone
   - Google
   - Apple

![Screenshot: Enable Auth Methods in Firebase](/img/common/firebase_authentication.webp)

4. **Update Public Settings:** Go to [Project Settings](https://console.firebase.google.com/u/0/project/_/settings/general) and configure your Public Settings. The Public Facing Name appears in verification emails sent to users, so they'll see your Quiz App name instead of your Firebase project name.

![Screenshot: Update Public Settings](/img/common/firebase_update_public_settings.webp)

5. **For Elite Quiz Web users:** Add your website domain to the Authorized Domains list. Enter only the domain name without `https://` or `http://` (e.g., `elitequiz.wrteam.in`).

![Screenshot: Add Authorized Domains for Elite Web](/img/common/firebase_auth_add_authorised_domains.webp)

> **Tip:** To control which sign-in options are visible to your users, use the Elite Quiz admin panel:
>
> - Go to `Settings > Authentication Settings`.
> - Turn off any methods you don’t want users to see.

![Screenshot: Admin Panel Authentication Settings](/img/common/panel_auth_settings.png)

---

## Step 3: Set Up Firestore Database

Elite Quiz uses Firestore to store real-time data for battle quizzes, like quiz progress and chat messages.

### Option 1: Watch the Setup Video

import Video from '@site/src/components/Video';

<Video src="https://youtu.be/wILoHdogjOI" title="Firebase Firestore Setup" />

### Option 2: Follow These Steps

1. In Firebase, click **Build** in the left menu, then select [**Firestore Database**](https://console.firebase.google.com/project/_/firestore/).
2. Click **Create database**.
3. Choose the location closest to your users and confirm.

   ![Screenshot: Create Firestore Database](/img/common/firestore_create_db.png)
   ![Screenshot: Select Database Location](/img/common/firestore_create_step2.png)

4. **Set Firestore Security Rules:**

   - Go to the **Rules** tab.
   - Delete any existing rules and paste in the following:

   ```javascript
    rules_version = '2';
    service cloud.firestore {
        match /databases/{database}/documents {
            match /{document=**} {
                allow read, write: if request.auth.uid != null;
            }
        }
    }
   ```

   ![Screenshot: Add Rule in Firestore](/img/common/firestore_rules.webp)

5. **Create an Index for Messaging**

   - This is needed for the in-game chat feature.
   - In Firestore, go to the **Indexes** tab.
   - Click **Add Index** and fill in:
     - **Collection ID:** `messages`
     - **First Field:** `roomId` (Ascending) — note the capital "I"
     - **Second Field:** `timestamp` (Descending)
     - **Query Scope:** Collection

   ![Screenshot: Create Index for Messages](/img/common/firestore_index.webp)

---

## What’s Next?

- You’re done with the common Firebase setup! 🎉
- Now, follow the next guide for your platform (mobile or web) to finish integration.
