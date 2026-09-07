#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const glob = require('glob');

/**
 * Docusaurus Image Cleanup Tool
 * Safely identifies and removes unused images from static/img directory
 */

class ImageCleanup {
  constructor() {
    this.staticImgPath = './static/img';
    this.imageExtensions = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico'];
    this.searchPaths = [
      './docs/**/*.{md,mdx}',
      './src/**/*.{js,jsx,ts,tsx}',
      './docusaurus.config.js',
      './sidebars.js'
    ];
    this.imageReferences = new Set();
    this.allImages = new Set();
    this.unusedImages = new Set();
  }

  /**
   * Find all image files in static/img directory
   */
  findAllImages() {
    console.log('🔍 Finding all images in static/img...');

    const findImagesRecursively = (dir) => {
      const items = fs.readdirSync(dir);

      for (const item of items) {
        const fullPath = path.join(dir, item);
        const stat = fs.statSync(fullPath);

        if (stat.isDirectory()) {
          findImagesRecursively(fullPath);
        } else if (this.imageExtensions.includes(path.extname(item).toLowerCase())) {
          // Store relative path from static/img
          const relativePath = path.relative(this.staticImgPath, fullPath);
          this.allImages.add(relativePath);
        }
      }
    };

    if (fs.existsSync(this.staticImgPath)) {
      findImagesRecursively(this.staticImgPath);
    }

    console.log(`📊 Found ${this.allImages.size} total images`);
    return this.allImages;
  }

  /**
   * Find all image references in documentation and source files
   */
  async findImageReferences() {
    console.log('🔍 Scanning files for image references...');

    for (const pattern of this.searchPaths) {
      const files = glob.sync(pattern);

      for (const file of files) {
        try {
          const content = fs.readFileSync(file, 'utf8');
          this.extractImageReferences(content, file);
        } catch (error) {
          console.warn(`⚠️  Could not read file: ${file}`);
        }
      }
    }

    console.log(`📊 Found ${this.imageReferences.size} image references`);
    return this.imageReferences;
  }

  /**
   * Extract image references from file content
   */
  extractImageReferences(content, filePath) {
    // Patterns to match image references
    const patterns = [
      // Markdown images: ![alt](path) or ![alt](path "title")
      /!\[.*?\]\(([^)]+)\)/g,
      // HTML img tags: <img src="path" />
      /<img[^>]+src=["']([^"']+)["'][^>]*>/g,
      // Import statements: import image from 'path'
      /import\s+.*?\s+from\s+["']([^"']+)["']/g,
      // require() calls: require('path')
      /require\s*\(\s*["']([^"']+)["']\s*\)/g,
      // Direct string references to /img/ paths
      /["']([^"']*\/img\/[^"']+)["']/g,
      // Docusaurus useBaseUrl references
      /useBaseUrl\s*\(\s*["']([^"']+)["']\s*\)/g,
    ];

    for (const pattern of patterns) {
      let match;
      while ((match = pattern.exec(content)) !== null) {
        let imagePath = match[1];

        // Skip external URLs
        if (imagePath.startsWith('http://') || imagePath.startsWith('https://')) {
          continue;
        }

        // Normalize path
        imagePath = this.normalizePath(imagePath);

        if (imagePath) {
          this.imageReferences.add(imagePath);

          // Also add variants (with and without leading slash)
          if (imagePath.startsWith('/')) {
            this.imageReferences.add(imagePath.substring(1));
          } else {
            this.imageReferences.add('/' + imagePath);
          }
        }
      }
    }
  }

  /**
   * Normalize image path to match our storage format
   */
  normalizePath(imagePath) {
    // Remove query parameters and fragments
    imagePath = imagePath.split('?')[0].split('#')[0];

    // Handle different path formats
    if (imagePath.startsWith('/img/')) {
      return imagePath.substring(5); // Remove '/img/'
    } else if (imagePath.startsWith('img/')) {
      return imagePath.substring(4); // Remove 'img/'
    } else if (imagePath.includes('/img/')) {
      const imgIndex = imagePath.indexOf('/img/');
      return imagePath.substring(imgIndex + 5);
    }

    // Check if it's an image file extension
    const ext = path.extname(imagePath).toLowerCase();
    if (this.imageExtensions.includes(ext)) {
      return imagePath;
    }

    return null;
  }

  /**
   * Find unused images by comparing all images with references
   */
  findUnusedImages() {
    console.log('🔍 Identifying unused images...');

    for (const image of this.allImages) {
      let isUsed = false;

      // Check exact match
      if (this.imageReferences.has(image)) {
        isUsed = true;
      }

      // Check variations
      const imageName = path.basename(image);
      const imageDir = path.dirname(image);

      for (const ref of this.imageReferences) {
        // Check if reference matches the image path or just filename
        if (ref.includes(imageName) || ref.endsWith(image) || image.endsWith(ref)) {
          isUsed = true;
          break;
        }
      }

      if (!isUsed) {
        this.unusedImages.add(image);
      }
    }

    console.log(`📊 Found ${this.unusedImages.size} unused images`);
    return this.unusedImages;
  }

  /**
   * Generate report of unused images
   */
  generateReport() {
    console.log('\n📋 CLEANUP REPORT');
    console.log('='.repeat(50));
    console.log(`Total images: ${this.allImages.size}`);
    console.log(`Referenced images: ${this.allImages.size - this.unusedImages.size}`);
    console.log(`Unused images: ${this.unusedImages.size}`);

    if (this.unusedImages.size > 0) {
      console.log('\n🗑️  UNUSED IMAGES:');
      console.log('-'.repeat(30));

      const sortedUnused = Array.from(this.unusedImages).sort();
      const groupedByDir = {};

      for (const image of sortedUnused) {
        const dir = path.dirname(image);
        if (!groupedByDir[dir]) {
          groupedByDir[dir] = [];
        }
        groupedByDir[dir].push(path.basename(image));
      }

      for (const [dir, files] of Object.entries(groupedByDir)) {
        console.log(`\n📁 ${dir}/`);
        files.forEach(file => console.log(`   • ${file}`));
      }

      // Calculate space savings
      let totalSize = 0;
      for (const image of this.unusedImages) {
        try {
          const fullPath = path.join(this.staticImgPath, image);
          const stat = fs.statSync(fullPath);
          totalSize += stat.size;
        } catch (error) {
          // File might not exist
        }
      }

      console.log(`\n💾 Potential space savings: ${this.formatBytes(totalSize)}`);
    }

    return this.unusedImages.size > 0;
  }

  /**
   * Safely delete unused images with confirmation
   */
  async deleteUnusedImages(autoConfirm = false) {
    if (this.unusedImages.size === 0) {
      console.log('✅ No unused images found. Nothing to delete.');
      return;
    }

    if (!autoConfirm) {
      console.log(`\n⚠️  About to delete ${this.unusedImages.size} unused images.`);
      console.log('Are you sure? This action cannot be undone.');
      console.log('Run with --confirm flag to skip this prompt.');
      return;
    }

    console.log(`\n🗑️  Deleting ${this.unusedImages.size} unused images...`);

    let deletedCount = 0;
    const errors = [];

    for (const image of this.unusedImages) {
      try {
        const fullPath = path.join(this.staticImgPath, image);
        fs.unlinkSync(fullPath);
        deletedCount++;
        console.log(`   ✓ Deleted: ${image}`);
      } catch (error) {
        errors.push({ image, error: error.message });
        console.log(`   ✗ Failed to delete: ${image} (${error.message})`);
      }
    }

    console.log(`\n✅ Deleted ${deletedCount} images`);
    if (errors.length > 0) {
      console.log(`❌ Failed to delete ${errors.length} images`);
    }
  }

  /**
   * Format bytes to human readable string
   */
  formatBytes(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  }

  /**
   * Run the cleanup process
   */
  async run(deleteMode = false, autoConfirm = false) {
    try {
      console.log('🧹 Docusaurus Image Cleanup Tool');
      console.log('='.repeat(40));

      await this.findAllImages();
      await this.findImageReferences();
      this.findUnusedImages();

      const hasUnusedImages = this.generateReport();

      if (deleteMode && hasUnusedImages) {
        await this.deleteUnusedImages(autoConfirm);
      } else if (hasUnusedImages) {
        console.log('\n💡 To delete unused images, run:');
        console.log('   node cleanup-unused-images.js --delete --confirm');
      }

    } catch (error) {
      console.error('❌ Error during cleanup:', error.message);
      process.exit(1);
    }
  }
}

// CLI handling
const args = process.argv.slice(2);
const deleteMode = args.includes('--delete');
const autoConfirm = args.includes('--confirm');
const showHelp = args.includes('--help') || args.includes('-h');

if (showHelp) {
  console.log(`
Docusaurus Image Cleanup Tool

Usage:
  node cleanup-unused-images.js [options]

Options:
  --delete     Delete unused images (requires --confirm)
  --confirm    Skip confirmation prompt for deletion
  --help, -h   Show this help message

Examples:
  node cleanup-unused-images.js                    # Scan and report only
  node cleanup-unused-images.js --delete --confirm # Delete unused images
`);
  process.exit(0);
}

// Run the cleanup
const cleanup = new ImageCleanup();
cleanup.run(deleteMode, autoConfirm);