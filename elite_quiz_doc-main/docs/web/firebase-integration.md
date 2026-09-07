---
sidebar_position: 4
---

# Firebase Integration

:::note
If you already have purchased the App version of Elite Quiz and already created a firebase project, then you can skip the first step.
:::

## Installation Video Tutorial

To help you get started quickly, we have created a video tutorial that guides you through the installation and setup process:

   <iframe 
   width="100%" 
   height="500" 
   style={{ borderRadius: '10px' }}
   src="https://www.youtube.com/embed/adrnST-IrgU" 
   title="Firebase Configuration Video Tutorial" 
   frameborder="0" 
   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
   allowfullscreen>
   </iframe>

## How to Configure Firebase

1. Create a firebase project in your account:

   ![Create Firebase Project 1](../../static/img/web/createFirebase1.jpg)
   ![Create Firebase Project 2](../../static/img/web/createFirebase2.jpg)
   ![Create Firebase Project 3](../../static/img/web/createFirebase3.jpg)
   ![Create Firebase Project 4](../../static/img/web/createFirebase4.jpg)

2. Add web application to your firebase project:

   ![Add Web App](../../static/img/web/addWeb.png)

3. Enter the App Name and Click on Register App:

   ![Register App](../../static/img/web/addWeb2.png)

4. Configure firebase integration and domain in firebase console:

   ![Firebase Integration](../../static/img/web/firebase-integration.png)

5. Copy the highlighted code and paste one by one as per labels given in admin panel -> web settings -> settings:

   ![Firebase Config Code](../../static/img/web/addWeb3.png)

6. This credentials should match with the credentials that you have set in admin panel. Otherwise it will not work properly:

   ![Admin Panel Config](../../static/img/web/addWeb4.png)

7. Configure domain in firebase console:

   ![Domain Configuration](../../static/img/web/firebase-configuration.png)

8. To connect you website with Google analytics, Copy this measurementId and paste it in .env file in the website code

![admin panel measurementId](../../static/img/web/firebaseMeasuremetid.png)
![measurementId paste in .env file in code ](../../static/img/web/envFirebase.png)

9. Log in to [Google Analytics](https://marketingplatform.google.com/about/analytics/) using the same account you used to create the Firebase project.
   ![measurementId paste in .env file in code ](../../static/img/web/analycs_web.png)

10. You have successfully connected your Web application to your firebase project.

## Why Firebase Is Important

Firebase provides authentication, real-time database, and cloud functions that are essential for the Elite Quiz app to function properly. The setup ensures users can log in, data is synced, and the application runs smoothly.
