---
sidebar_position: 6
---

# Settings

The Settings section in the Elite Quiz Admin Panel provides comprehensive control over the appearance, behavior, and functionality of your quiz application.

## Content Management

This section explains how to manage various content sections in the Elite Quiz admin panel.

## Privacy Policy

You can set Privacy Policy for your website and app:

![Privacy Policy](/img/panel/pp.png)

## Terms & Conditions

You can set Terms and Conditions for your website and app:

![Terms & Conditions](/img/panel/tc.png)

## About Us Content

You can set and manage your About Us content for the app:

![About Us](/img/panel/about-us.png)

## How to Play Content

You can set and manage your How to Play (instructions) content for the app:

![Instructions](/img/panel/instructions.png)

## AI Settings for AI Question Bank

Use the **AI Settings** screen to connect your AI Question Bank to either Gemini or OpenAI. Entering the wrong model code or API key will break question generation, so double-check every field before you click **Submit**.

![AI Settings](/img/panel/ai_setting.webp)

### Step 1: Choose an AI Provider

- Select **Gemini** to use Google’s Gemini API.
- Select **OpenAI** to use GPT models from the OpenAI platform.
- Stick with one provider per environment so your model limits and billing are easy to manage.

### Step 2: Enter a Valid Text Model Name

The **AI Model** field must contain a text-generation model code from the provider you selected. Copy the value exactly as documented—uppercase/lowercase and hyphens matter.

#### Gemini models

1. Open the [Gemini model catalog](https://ai.google.dev/gemini-api/docs/models).
2. Browse the **text** models (Gemini Pro, Gemini Flash, etc.). Avoid image-only or audio-only variants.
3. Click **Learn more** on the model you want, then copy the **Model code** (for example, `gemini-2.0-flash-exp`). Paste that code into the **AI Model** field.

![Gemini model copy code](/img/panel/gemini-models.gif)

#### OpenAI models

1. Go to the [OpenAI models list](https://platform.openai.com/docs/models).
2. Select a text model such as GPT-4.1 or GPT-4o variants. Do not copy image, audio, or embeddings models.
3. Copy the model ID (for example, `gpt-4.1-mini`) and paste it into the **AI Model** field.

![OpenAI model copy code](/img/panel/openai-models.gif)

:::caution Use text models only
Image-generation or embeddings model IDs will not work with the AI Question Bank. Always choose a model whose description clearly says “text generation” or “chat.”
:::

### Step 3: Generate API Keys

Each provider needs its own API key. Keys are secret—store them in a secure password manager and rotate them if they are ever exposed.

#### Gemini API key (Google AI Studio)

1. Sign in to [Google AI Studio](https://aistudio.google.com/api-keys).
2. Click **Create API key** (or **Get API key** if it’s your first time) and follow the prompts.
3. Copy the generated key and paste it into the **AI API Key** box in the admin panel.

#### OpenAI API key

1. Sign in to your [OpenAI API Keys](https://platform.openai.com/api-keys) page.
2. Click **Create new secret key**, give it a friendly name, and confirm.
3. Copy the key once it appears (you will not see it again) and paste it into the **AI API Key** box.

After adding the provider, model code, and API key, click **Submit**. Run a quick test generation to confirm the connection before moving on.
