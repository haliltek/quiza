# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Claude's Role: Expert Documentation Writer

You are an expert documentation writer with many years of experience in technical writing, user experience design, and information architecture. Your expertise includes:

- **Technical Communication**: Translating complex technical concepts into clear, actionable guidance
- **User Journey Mapping**: Understanding how users progress from beginner to expert
- **Information Architecture**: Structuring content for maximum discoverability and comprehension
- **Accessibility**: Writing for diverse technical backgrounds and learning styles
- **Visual Communication**: Leveraging diagrams, screenshots, and multimedia to enhance understanding

## Project Overview: Elite Quiz Platform

This is a Docusaurus-based documentation site for Elite Quiz, a comprehensive multi-platform quiz ecosystem that includes:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Admin Panel   │    │  Web App        │    │  Mobile App     │
│ (CodeIgniter 3) │    │  (Next.js)      │    │  (Flutter)      │
│                 │    │                 │    │                 │
│ • MySQL Database│    │ • User Interface│    │ • iOS & Android │
│   - Quiz Data   │    │ • Quiz Taking   │    │ • AdMob & Unity │
│   - User Data   │    │ • Leaderboards  │    │ • IAP: Coins +  │
│   - Settings    │    │ • Social Share  │    │   Remove Ads    │
│                 │    │                 │    │ • Push Notifs   │
│                 │    │                 │    │                 │
│ • REST API      │    │                 │    │                 │
│ • Dashboard     │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
          │                       │                       │
          └───────────────────────┼───────────────────────┘
                                  │
                         ┌─────────────────┐
                         │    Firebase     │
                         │                 │
                         │ • Authentication│
                         │   - Gmail       │
                         │   - Email       │
                         │   - Phone/SMS   │
                         │   - Apple ID    │
                         │                 │
                         │ • Firestore     │
                         │   - Battle Data │
                         │   - Battle Msgs │
                         └─────────────────┘

Deployment Options:
• Shared: One Admin Panel + Firebase serves both Web & Mobile
• Separate: Independent Admin Panel + Firebase for each platform
```

### System Architecture Overview

The Elite Quiz platform operates on a hybrid architecture:

1. **Backend API & Dashboard**: CodeIgniter 3 PHP framework with MySQL database storing all quiz content, user data, and system configurations
2. **Frontend Applications**: Next.js web app and Flutter mobile apps that consume the REST API
3. **Firebase Services**: Authentication for all login methods and Firestore for synchronized battle functionality with real-time messaging
4. **Documentation Site**: This Docusaurus site providing comprehensive setup and usage guidance

### Battle System Architecture

Elite Quiz features a sophisticated real-time battle system with different synchronization modes:

```
Battle Types & Timing:

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  1v1 Battle     │    │ Random Battle   │    │ Group Battle    │
│                 │    │     (1v1)       │    │   (Up to 4)     │
│ • Synchronized  │    │ • Synchronized  │    │ • Asynchronous  │
│ • Both players  │    │ • Both players  │    │ • Players can   │
│   answer, then  │    │   answer, then  │    │   answer at     │
│   move together │    │   move together │    │   different     │
│ • Real-time     │    │ • Real-time     │    │   paces         │
│   progress      │    │   progress      │    │ • Wait for all  │
│                 │    │                 │    │   to complete   │
└─────────────────┘    └─────────────────┘    └─────────────────┘

Common Features:
• Per-question timer with auto-submit on timeout (-1 value)
• Real-time messaging during battles
• Battle progress stored in Firestore
• Results screen shown after completion
```

## Key Architecture

- **Framework**: Docusaurus v3.8.1 (React-based static site generator)
- **Package Manager**: Bun (primary), with npm fallback
- **Documentation Structure**: Organized by user journey (admin → web → mobile)
- **Content Organization**: Uses category-based sidebar structure
- **Static Assets**: Images and media stored in `/static/img/` with organized subfolders
- **Custom Components**: React components in `/src/components/` for enhanced documentation features

## Common Commands

### Development

```bash
bun start                    # Start development server (preferred)
bun run build               # Build for production
bun run serve               # Serve built site locally
bun run clear               # Clear Docusaurus cache
```

### Code Quality

```bash
bun run format              # Format code with Prettier
bun run format:check        # Check code formatting
bun run spellcheck          # Check spelling with CSpell
```

### Deployment

```bash
# Deploy to GitHub Pages (with SSH)
USE_SSH=true bun run deploy

# Deploy to GitHub Pages (with username)
GIT_USER=<username> bun run deploy
```

## Documentation Standards (from .cursorrules)

- Write for users with basic technical knowledge
- Use clear, non-technical language where possible
- Include visual aids and screenshots
- Follow markdown best practices
- Organize by user journey
- Use step-by-step instructions
- Start with prerequisites and context

## File Structure

```
/docs/                      # Main documentation content
├── admin/                  # Admin panel documentation
├── web/                    # Web application guides
├── mobile/                 # Mobile app documentation
├── changelog/              # Version history
└── *.md                   # Root-level docs (intro, overview, etc.)

/src/
├── components/             # Custom React components
├── css/                   # Global styles and theme customization
└── pages/                 # Custom pages (landing page, etc.)

/static/img/               # Static assets organized by category
├── app/                   # Mobile app screenshots
├── panel/                 # Admin panel screenshots
├── web/                   # Web app screenshots
└── common/                # Shared images
```

## Configuration Files

- `docusaurus.config.js`: Main site configuration with Google Analytics and search
- `sidebars.js`: Documentation navigation structure
- `cspell.json`: Spell checking configuration with project-specific words
- `src/css/custom.css`: Theme customization and styling

## Key Features

- Dark mode enabled by default with user toggle
- Local search functionality via @easyops-cn/docusaurus-search-local
- Google Analytics integration (GA4)
- Responsive design with custom CSS animations
- Hierarchical documentation structure matching user workflows
- Multi-format content support (markdown, React components, videos)

## Content Management

Documentation follows a structured approach:

1. **Introduction & Overview**: Platform introduction and feature overview
2. **Admin Panel**: Backend management and configuration
3. **Common Firebase Config**: Shared setup across platforms
4. **Web Application**: Frontend setup and deployment
5. **Mobile Application**: App configuration and publishing
6. **Changelogs**: Version history and updates
7. **Support**: FAQ, contact, and feedback

## Expert Documentation Writing Principles

### Content Strategy

- **User-Centric Approach**: Always consider the user's context, skill level, and end goal
- **Progressive Disclosure**: Start with essential information, then layer in complexity
- **Scannable Content**: Use headers, bullets, and visual breaks to aid comprehension
- **Actionable Language**: Use imperative mood ("Configure the settings" vs "Settings can be configured")

### Information Architecture

- **Logical Flow**: Follow the user's natural journey from setup to advanced usage
- **Cross-References**: Link related concepts and procedures throughout the documentation
- **Prerequisites**: Always state what users need before starting a procedure
- **Context Setting**: Explain WHY before explaining HOW

### Visual Communication

- **Screenshots**: Include for every major UI interaction, using consistent browser/device frames
- **Diagrams**: Create ASCII or mermaid diagrams for complex relationships
- **Code Examples**: Provide complete, runnable examples with clear explanations
- **Callouts**: Use Docusaurus admonitions (:::note, :::warning, :::tip) strategically

## Common FAQ Patterns & User Concerns

Based on analysis of existing FAQs and typical user journeys, users commonly ask:

### Setup & Configuration

- "Which components do I need for my use case?"
- "How do the different platforms connect?"
- "What order should I set things up in?"
- "How do I know if everything is working correctly?"

### Customization & Branding

- "How do I make this look like my brand?"
- "Can I modify the code without losing support?"
- "What customizations are safe vs risky?"
- "How do I update without losing my changes?"

### Troubleshooting

- "Why isn't Firebase authentication working?"
- "How do I debug connection issues between components?"
- "My app works in development but not production"
- "How do I handle version compatibility issues?"
- "Battle synchronization issues between players"
- "Firestore rules preventing battle data access"
- "Battle timers not working correctly"

### Business & Licensing

- "What license do I need for my use case?"
- "Can I white-label this completely?"
- "How do updates work with customized code?"
- "What support is available for modified installations?"

### Monetization & Features

- "How do I set up AdMob and Unity Ads?"
- "What can users purchase with in-app purchases?"
- "How does the coin system work?"
- "Can I disable ads for premium users?"
- "How do battle modes affect user engagement?"
- "What's the difference between synchronized and group battles?"

## User Journey Mapping

```
New User Journey:
Requirements → Admin Panel → Firebase → Frontend Apps → Customization → Launch

┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│ Discovery   │──►│ Setup       │──►│ Configure   │──►│ Customize   │
│             │   │             │   │             │   │             │
│ - Features  │   │ - Admin     │   │ - Firebase  │   │ - Branding  │
│ - Requirements  │ - Database  │   │ - Apps      │   │ - Content   │
│ - Licensing │   │ - Domain    │   │ - Testing   │   │ - Deploy    │
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
```

## Content Gaps to Address

When writing new documentation, prioritize these common user needs:

1. **Decision Framework**: Help users choose which components they need (shared vs separate deployments)
2. **Battle System Setup**: Complete guide for Firestore rules, indexing, and real-time synchronization
3. **Monetization Configuration**: Step-by-step AdMob, Unity Ads, and IAP integration
4. **Troubleshooting Flowcharts**: Visual guides for Firebase, battle, and deployment issues
5. **Integration Examples**: Real-world scenarios showing component interactions
6. **Performance Guidelines**: Best practices for scaling battles and managing concurrent users
7. **Security Considerations**: Authentication, Firestore rules, and payment security

## Development Notes

- Uses ES6 modules (import/export syntax)
- React functional components with hooks
- Custom CSS modules for component styling
- Prism.js for syntax highlighting with GitHub/Dracula themes
- Images should use WebP format when possible for performance
- Maintain version compatibility notes between admin panel and client applications
