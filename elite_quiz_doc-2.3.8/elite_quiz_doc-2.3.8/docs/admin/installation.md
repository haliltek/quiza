---
sidebar_position: 2
---

# Installing Admin Panel

This guide will walk you through the process of installing the Elite Quiz Admin Panel on your server.

## Installation Steps

1. **Create your domain or subdomain** on your server (shared hosting or VPS).

   :::tip Recommendation for Web Users
   If you have purchased the web version of Elite Quiz alongside the Admin Panel, it is recommended to install the **Admin Panel on a subdomain** (e.g., `admin.yourdomain.com`) and the **Web application on your main domain** (e.g., `yourdomain.com`). This separation helps in managing both applications effectively.
   :::

2. **Set up an empty database** on your server and keep track of these credentials:

   - Database name
   - Database username
   - Database password

   :::caution Note
   Avoid using hyphens(-) in the **Database Name**, as it doesn't work in some configurations.
   :::

3. **Upload the source code to your server**:

   - Begin by extracting the Source Code you acquired from CodeCanyon.
   - Unpack the Admin Panel zip file and proceed to upload the PHP Code Folder's contents onto your Server.

   :::caution Note
   .htaccess file is essential; kindly verify its existence. If it is not visible, enable the option to display hidden files.
   :::

   :::caution Note
   Supported PHP version should be greater than or equal to 8.1
   :::

4. **Run the installation wizard**:
   - Now head to your project's URL (e.g., mydomain.com or subdomain.mydomain.com).
   - The Installation screen will then walk you through the process seamlessly.

Great news! You're all set. To get started, open your admin panel URL in your browser (e.g., yourdomain.com or subdomain.yourdomain.com).

For reference, you can check out our demo panel at:
[https://elitequiz.wrteam.me](https://elitequiz.wrteam.me)

**Default Login Details**  
User: admin  
Pass: admin123

## Common Errors

### Admin Panel's Server Issues

#### Issue: ob_start() Error

You might see errors related to ob_start() function in PHP.

#### Solution:

Go to Admin panel's code root files -> index.php and write: `ob_start();` in new line after `<?php`

![ob_start solution](/img/panel/ob_start.webp)

You can also check the answer here:

![ob_start solution (answer)](/img/panel/ob_start-ans.png)
