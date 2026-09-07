# Elite Quiz Documentation

This is the documentation site for Elite Quiz, built with [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

## Getting Started

### Prerequisites

- [Bun](https://bun.sh/) version 1.0 or higher
- Node.js version 18 or higher (for compatibility)

### Installation

```bash
# Clone the repository
git clone <repository-url>

# Navigate to the project directory
cd elite-quiz-docs

# Install dependencies using Bun
bun install
```

### Local Development

```bash
# Start the development server
bun start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```bash
# Build the website
bun run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```bash
# Build and deploy to server
USE_SSH=true bun run deploy
```

Not using SSH:

```bash
# Build and deploy to GitHub pages
GIT_USER=<Your GitHub username> bun run deploy
```

## Documentation Structure

The documentation is organized into the following sections:

- `/`: Root documentation pages

  - `/introduction.md`: General introduction
  - `/overview.md`: Platform overview
  - `/features.md`: Feature documentation
  - `/faq.md`: Frequently asked questions
  - `/support.md`: Support information
  - `/rating.md`: Feedback and rating
  - `/contactus.md`: Contact information

- `/web/`: Web application documentation

  - `/web/setup-nodejs.md`: Web setup guide
  - `/web/deploy.md`: Deployment instructions
  - `/web/changelog.md`: Web version changelog

- `/mobile/`: Mobile app documentation

  - `/mobile/overview.md`: Mobile app overview
  - `/mobile/setup.md`: Mobile setup guide
  - `/mobile/changelog.md`: Mobile version changelog

- `/admin/`: Admin panel documentation

  - `/admin/overview.md`: Admin panel overview
  - `/admin/setup.md`: Admin setup guide

- `/static`: Contains static assets like images
  - `/static/img/`: Images used in the documentation

## Customization

- Edit `docusaurus.config.js` to customize site configuration
- Edit `sidebars.js` to customize documentation sidebar
- Edit `/src/pages/index.js` to customize the landing page
- Edit `/src/css/custom.css` to customize styling

## Development Tools

- **Package Manager**: [Bun](https://bun.sh/)
- **Documentation**: [Docusaurus 2](https://docusaurus.io/)
- **Code Formatting**: [Prettier](https://prettier.io/)
- **Spell Checking**: [CSpell](https://cspell.org/)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the terms of the license included with your purchase.
