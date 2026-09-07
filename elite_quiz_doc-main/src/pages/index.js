import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import styles from './index.module.css';
import DocBanner from '../components/DocBanner';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container hero-content">
        <h1 className={styles.hero__title}>{siteConfig.title}</h1>
        <p className={styles.hero__subtitle}>{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link className="button button--secondary button--lg" to="/introduction">
            Get Started
          </Link>
        </div>
      </div>
    </header>
  );
}

function QuickLinks() {
  return (
    <div className={styles.quickLinksSection}>
      <div className="container">
        <h2 className={styles.quickLinksHeading}>Quick Access</h2>
        <div className={styles.quickLinksGrid}>
          <Link className={styles.quickLinkCard} to="/admin/overview">
            <h3>Admin Panel</h3>
            <p>Manage your quiz platform with our comprehensive admin panel</p>
          </Link>
          <Link className={styles.quickLinkCard} to="/web/web-setup-overview">
            <h3>Web Application</h3>
            <p>Explore the web version of Elite Quiz and its features</p>
          </Link>
          <Link className={styles.quickLinkCard} to="/mobile/overview">
            <h3>Mobile App</h3>
            <p>Discover the features of our mobile application</p>
          </Link>
          <Link className={styles.quickLinkCard} to="/changelog/web">
            <h3>Change Logs</h3>
            <p>View updates and version history for our products</p>
          </Link>
        </div>
      </div>
      <DocBanner />
    </div>
  );
}

export default function Home() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="Documentation for Elite Quiz Web Application"
    >
      <div
        className="homepage-wrapper"
        style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}
      >
        <HomepageHeader />
        <main
          style={{
            flex: 1,
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'center',
          }}
        >
          <QuickLinks />
          {/* Use regular class names for the animation elements */}
          <ul className="circlesRound">
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
            <li></li>
          </ul>
        </main>
      </div>
    </Layout>
  );
}
