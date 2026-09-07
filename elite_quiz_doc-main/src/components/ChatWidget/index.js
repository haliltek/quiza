import { useEffect } from 'react';
import { createChat } from '@n8n/chat';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import '@n8n/chat/style.css';
import './custom-chat-styles.css';

export default function ChatWidget() {
  const {
    siteConfig: { title, customFields },
  } = useDocusaurusContext();

  useEffect(() => {
    // Initialize n8n chat widget
    createChat({
      webhookUrl: customFields.n8nChatWebhookUrl,
      webhookConfig: {
        method: 'POST',
        headers: {},
      },
      target: '#n8n-chat',
      mode: 'window',
      loadPreviousSession: true,
      showWelcomeScreen: false,
      initialMessages: [
        'Hi there! 👋',
        `Welcome to ${title}. How can I help you today?`,
      ],
      i18n: {
        en: {
          title: '',
          subtitle: '',
          footer: '',
          getStarted: 'New Conversation',
          inputPlaceholder: 'Type your question...',
        },
      },
      enableStreaming: false,
    });
  }, [customFields.n8nChatWebhookUrl, title]);

  return <div></div>;
}
