# Image Cleanup Tool for Docusaurus

This tool helps you safely identify and remove unused images from your Docusaurus `static/img/` directory.

## ✨ Features

- **Safe Detection**: Scans all documentation files, source code, and config files for image references
- **Multiple Reference Patterns**: Detects images referenced via:
  - Markdown syntax: `![alt](path)`
  - HTML img tags: `<img src="path" />`
  - Import statements: `import image from 'path'`
  - require() calls: `require('path')`
  - Docusaurus useBaseUrl: `useBaseUrl('path')`
  - Direct string references
- **Comprehensive Reporting**: Shows unused images organized by directory with potential space savings
- **Confirmation Required**: Prevents accidental deletion with explicit confirmation flags
- **Path Normalization**: Handles various path formats and variations

## 🚀 Quick Start

### 1. Scan for Unused Images (Safe - No Deletion)

```bash
# Using npm/bun scripts (recommended)
bun run cleanup:images

# Or run directly
node cleanup-unused-images.js
```

### 2. Delete Unused Images (Permanent Action)

```bash
# Using npm/bun scripts (recommended)
bun run cleanup:images:delete

# Or run directly
node cleanup-unused-images.js --delete --confirm
```

## 📊 Example Output

```
🧹 Docusaurus Image Cleanup Tool
========================================
🔍 Finding all images in static/img...
📊 Found 191 total images
🔍 Scanning files for image references...
📊 Found 230 image references
🔍 Identifying unused images...
📊 Found 83 unused images

📋 CLEANUP REPORT
==================================================
Total images: 191
Referenced images: 108
Unused images: 83

🗑️  UNUSED IMAGES:
------------------------------

📁 app/
   • add-unity-ad-ids.webp
   • addFirebaseAuth.webp
   • changeFont.webp
   ...

📁 panel/
   • authentication_settings copy.webp
   • sections.png
   ...

💾 Potential space savings: 10.61 MB
```

## 🔍 How It Works

The tool performs these steps:

1. **Find All Images**: Recursively scans `static/img/` for image files (png, jpg, jpeg, gif, svg, webp, ico)

2. **Scan References**: Searches these locations for image references:

   - `docs/**/*.{md,mdx}` - All documentation files
   - `src/**/*.{js,jsx,ts,tsx}` - All source code files
   - `docusaurus.config.js` - Main configuration
   - `sidebars.js` - Sidebar configuration

3. **Pattern Matching**: Uses multiple regex patterns to catch various reference formats

4. **Path Normalization**: Handles different path variations:

   - `/img/example.png`
   - `img/example.png`
   - `static/img/example.png`
   - Just filenames: `example.png`

5. **Safety Checks**: Only marks images as unused if no references are found

## ⚙️ Command Line Options

```bash
node cleanup-unused-images.js [options]

Options:
  --delete     Delete unused images (requires --confirm)
  --confirm    Skip confirmation prompt for deletion
  --help, -h   Show help message

Examples:
  node cleanup-unused-images.js                    # Scan and report only
  node cleanup-unused-images.js --delete --confirm # Delete unused images
```

## 🛡️ Safety Features

- **Report First**: Always run without `--delete` first to review the list
- **Confirmation Required**: Must explicitly use `--confirm` flag for deletion
- **No Undo**: Deleted files cannot be recovered (use git if you need to revert)
- **Conservative Matching**: Uses multiple pattern matching to avoid false positives

## 🔧 Customization

You can modify the script to:

- **Add More File Types**: Edit `imageExtensions` array
- **Change Search Paths**: Modify `searchPaths` array
- **Add New Patterns**: Extend the regex patterns in `extractImageReferences()`

## 📝 Package.json Scripts

The tool is integrated into your package.json:

```json
{
  "scripts": {
    "cleanup:images": "node cleanup-unused-images.js",
    "cleanup:images:delete": "node cleanup-unused-images.js --delete --confirm"
  }
}
```

## ⚠️ Important Notes

1. **Always Review First**: Run the scan-only mode before deleting anything
2. **Check Git Status**: Ensure your git repo is clean before running deletion
3. **Backup Recommended**: Consider creating a backup of `static/img/` before deletion
4. **Test After Cleanup**: Build your documentation after cleanup to ensure nothing is broken

## 🐛 Troubleshooting

### "Module not found" errors

```bash
bun install glob  # or npm install glob
```

### False positives (images marked as unused but actually used)

- Check if the image is referenced in a non-standard way
- Add custom patterns to the `extractImageReferences()` function
- Images in subdirectories might need path adjustments

### Images not being detected as unused

- Ensure the image reference uses a supported pattern
- Check if there are typos in the image path
- Verify the image is actually in the `static/img/` directory

## 📈 Performance

- Processes ~200 images and ~40 files in under 1 second
- Memory efficient for large documentation sites
- Uses Node.js built-in modules for maximum compatibility

---

**Remember**: This tool is designed to be conservative. If you find legitimate images being marked as unused, please review the patterns and consider updating the script rather than manually managing the exclusions.
