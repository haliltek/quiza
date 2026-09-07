import { themes as prismThemes } from 'prism-react-renderer';
import dotenv from 'dotenv';

dotenv.config();

// With JSDoc @type annotations, IDEs can provide config autocompletion
/** @type {import('@docusaurus/types').Config} */
export default {
  title: 'Elite Quiz Documentation',
  tagline: 'Web & App',
  url: 'https://wrteam-in.github.io',
  baseUrl: '/elite_quiz_doc',
  onBrokenLinks: 'warn',
  favicon: 'img/favicon.svg',
  organizationName: 'WRTeam-in', // Usually your GitHub org/user name.
  projectName: 'elite_quiz_doc', // Usually your repo name.

  // Custom fields for environment variables
  customFields: {
    n8nChatWebhookUrl: process.env.N8N_CHAT_WEBHOOK_URL || '',
  },

  // Markdown configuration
  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  themes: ['@docusaurus/theme-mermaid'],

  // Add local search plugin with a unique ID to avoid conflicts
  plugins: [
    require.resolve('@easyops-cn/docusaurus-search-local'),

    [
      '@docusaurus/plugin-google-gtag',
      {
        trackingID: 'G-CS432E2TJ6',
        anonymizeIP: true,
      },
    ],
  ],

  presets: [
    [
      '@docusaurus/preset-classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Remove any Algolia reference if it exists
      navbar: {
        title: 'Elite Quiz Docs',
        logo: {
          alt: 'Elite Quiz Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            href: 'https://wrteam.in/',
            label: 'WRTeam',
            position: 'right',
          },
          {
            type: 'search',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [],
        copyright: `Copyright © ${new Date().getFullYear()} WRTeam.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
        additionalLanguages: ['dart'],
      },
      docs: {
        sidebar: {
          hideable: true,
        },
      },
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      mermaid: {
        theme: { light: 'default', dark: 'dark' },
      },
    }),
};
