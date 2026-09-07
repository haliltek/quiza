---
sidebar_position: 1
---

# Web Changelogs

This page documents the version history and updates for the Elite Quiz Web application.

<div className="changelog-container">


<details open>
<summary><h2>Version 2.3.9 (31 Mar 2026)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Added the database and assets backup option in the admin panel
- <span className="badge badge--info">Improved</span> Improvements and bugfix
</ul>
</details>

<details>
<summary><h2>Version 2.3.8 (30 Jan 2026)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Progressive Web App (PWA) integration for enhanced web app experience and offline support
- <span className="badge badge--success">Added</span> Cookie integration to support compliance and improved session handling
- <span className="badge badge--success">Added</span> Custom AdSense components to improve ad placement and overall user experience

- <span className="badge badge--info">Improved</span> Level selection made optional in Quiz Zone and MultiMatch within category and subcategory flows
- <span className="badge badge--info">Improved</span> Display of playable question counts on category and subcategory cards in Quiz Zone and MultiMatch
- <span className="badge badge--info">Improved</span> Wallet page clarity with defined conversion rate between coins and currency
- <span className="badge badge--info">Improved</span> Referral system messaging to clearly show coin rewards for both referrer and new users

- <span className="badge badge--danger">Fixed</span> Wallet payout issues ensuring accurate and reliable transactions
- <span className="badge badge--danger">Fixed</span> Leaderboard issues affecting ranking and data display
- <span className="badge badge--danger">Fixed</span> UI issues on the Play Screen for mobile devices
- <span className="badge badge--danger">Fixed</span> Core logic refactored to enhance error handling and overall code stability

- <span className="badge badge--info">Refactored</span> Codebase improvements for better maintainability, performance, and consistent error management
</ul>
</details>

<details>
<summary><h2>Version 2.3.7 (25 Nov 2025)</h2></summary>
<ul>
- <span className="badge badge--danger">Fixed</span> Removed breadcrumb from single page views
- <span className="badge badge--danger">Fixed</span> Corrected breadcrumb path for navigation
- <span className="badge badge--danger">Fixed</span> UI alignment issues across components
- <span className="badge badge--danger">Fixed</span> Random battle matchmaking issue in language-off mode
- <span className="badge badge--danger">Fixed</span> Guess-the-word hint error with incomplete answers
- <span className="badge badge--danger">Fixed</span> Header and footer alignment problems

- <span className="badge badge--info">Improved</span> General code cleanup and optimization
- <span className="badge badge--info">Improved</span> Minor UI refinements for consistency
</ul>
</details>

<details>
<summary><h2>Version 2.3.6 (28 Oct 2025)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> AI Question Bank in the Admin Panel — auto-generate questions for five main quiz types using OpenAI or Gemini AI models

- <span className="badge badge--danger">Fixed</span> Header highlight issue for consistent UI feedback  
- <span className="badge badge--danger">Fixed</span> “Previous” and “Next” button functionality in Exam Quiz section  
- <span className="badge badge--danger">Fixed</span> Incorrect display of played exams in history view  
- <span className="badge badge--danger">Fixed</span> One-vs-One Battle gameplay issue for smoother experience  

- <span className="badge badge--info">Improved</span> Overall code structure and removed redundant logic  
- <span className="badge badge--info">Improved</span> API response handling for enhanced performance and reliability  
</ul>
</details>

<details>
<summary><h2>Version 2.3.5 (14 Aug 2025)</h2></summary>
<ul>
- <span className="badge badge--danger">Fixed</span> Audio and Fun and Learn quiz review answer when user does not select any option  
- <span className="badge badge--danger">Fixed</span> Enabled Join Battle button while user is connected and removed unnecessary restrictions  
- <span className="badge badge--danger">Fixed</span> Added placeholder image when no category or subcategory image is available  
- <span className="badge badge--danger">Fixed</span> Removed red line from timer during the last five seconds  
- <span className="badge badge--danger">Fixed</span> Multi Match premium category issue  
- <span className="badge badge--danger">Fixed</span> Alignment issue in profile  
- <span className="badge badge--danger">Fixed</span> Correct question statistics when user does not click on any question  
- <span className="badge badge--danger">Fixed</span> RTL (Right-to-Left language) display issues  

- <span className="badge badge--warning">Removed</span> Popup confirmation on review page if user has already opted not to see it again  

- <span className="badge badge--success">Added</span> Dashed lines in sequence questions to help users better understand the order  
- <span className="badge badge--success">Added</span> Numerical badges for Group Battle rank  

- <span className="badge badge--info">Improved</span> Code structure, removed unused parameters, polished UI, and enhanced reusability of utility functions  
</ul>
</details>

<details>
<summary><h2>Version 2.3.4 (17 Jul 2025)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Coins, scores, badges, and reward distribution are now fully managed via the backend, enhancing security and integrity  
- <span className="badge badge--success">Added</span> Breadcrumb navigation on relevant pages to improve user experience and navigation clarity  

- <span className="badge badge--info">Improved</span> Dark mode theme for better visual consistency  
- <span className="badge badge--info">Improved</span> Codebase structure with removal of unused code, repositories, and redundant logic for improved maintainability  
</ul>
</details>

<details>
<summary><h2>Version 2.3.3 (27 May 2025)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Dark mode  
- <span className="badge badge--success">Added</span> Web Push Notifications  
- <span className="badge badge--success">Added</span> Load More button on category and subcategory pages  

- <span className="badge badge--info">Improved</span> Implemented standard breadcrumb  
- <span className="badge badge--info">Improved</span> Converted local images to match the primary color  
- <span className="badge badge--info">Improved</span> Component skeletons  
- <span className="badge badge--info">Improved</span> Made timer animation smoother  
- <span className="badge badge--info">Improved</span> Placeholder image for missing images  
- <span className="badge badge--info">Improved</span> Many bug fixes and performance enhancements  
</ul>
</details>

<details>
<summary><h2>Version 2.3.2 (12 Apr 2025)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> "Hint deduct coins" in Guess The Word setting rather than using the "lifeline deduct coins" from quiz zone setting
- <span className="badge badge--danger">Fixed</span> Badges Notification Translation issue
- <span className="badge badge--info">Improved</span> Remove 2x coin & score gains from premium categories win
- <span className="badge badge--info">Improved</span> Label translation
- <span className="badge badge--info">Improved</span> Refactor API call method
</ul>
</details>

<details>
<summary><h2>Version 2.3.1 (28 Mar 2025)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Multi Match Quiz Feature
- <span className="badge badge--success">Added</span> CSS to Tailwind CSS for Optimisation codebase convert theme
- <span className="badge badge--danger">Fixed</span> Premium Category issue fix in all quiz features
- <span className="badge badge--info">Improved</span> UI Improvement and Minor bug fixed
</ul>
</details>

<details>
<summary><h2>Version 2.3.0 (8 Jan 2025)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Added PDFs to Fun'N'Learn comprehension
- <span className="badge badge--success">Added</span> Added YouTube video to Fun'N'Learn comprehension
- <span className="badge badge--success">Added</span> Added images in questions for Fun'N'Learn
</ul>
</details>

<details>
<summary><h2>Version 2.2.0 (12 Nov 2024)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Option to set default Quiz and System Language from Admin Panel
- <span className="badge badge--success">Added</span> Rather than JSON, add/update translations directly from Admin Panel
- <span className="badge badge--info">Improved</span> Update UI for playScreen and reviewScreen to improve option readability
- <span className="badge badge--info">Improved</span> Auto-focus for login input
</ul>
</details>

<details>
<summary><h2>Version 2.1.9 (24 Sept 2024)</h2></summary>
<ul>
- <span className="badge badge--info">Improved</span> Language Translations from Admin panel
- <span className="badge badge--success">Added</span> Separate the App Language from the Content Language
- <span className="badge badge--success">Added</span> When language mode is disabled we should get all the data instead of the default English language
- <span className="badge badge--info">Improved</span> Move the bookmarks to the Review Answers Section
- <span className="badge badge--info">Improved</span> Show answer correctness in the bookmark play area
- <span className="badge badge--success">Added</span> Updated firebase-php package in Admin Panel
</ul>
</details>

<details>
<summary><h2>Version 2.1.8 (16 Aug 2024)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Remove Premium From Subcategories in Admin Panel
- <span className="badge badge--success">Added</span> Add dynamic authentication methods in Admin Panel
- <span className="badge badge--info">Improved</span> API Changes
- <span className="badge badge--info">Improved</span> UI Improvements and minor issues fix
</ul>
</details>

<details>
<summary><h2>Version 2.1.7 (5 Aug 2024)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Important announcement for Premium Subcategories for the upcoming update
- <span className="badge badge--info">Improved</span> Minimum one language to be present in languages setting and UI Improvements
- <span className="badge badge--danger">Fixed</span> Latex Questions Options cut-off issue
</ul>
</details>

<details>
<summary><h2>Version 2.1.6 (15 July 2024)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Make Latex optional for Quiz zone and Sub Quizzes, also Exam
- <span className="badge badge--success">Added</span> Default web settings and placeholders
- <span className="badge badge--info">Improved</span> Remove Image from Image Question in edit
- <span className="badge badge--info">Improved</span> New UI for the Battles join
- <span className="badge badge--info">Improved</span> UI Improvements
</ul>
</details>

<details>
<summary><h2>Version 2.1.5 (5 June 2024)</h2></summary>
<ul>
- <span className="badge badge--info">Improved</span> UI improvements
- <span className="badge badge--info">Improved</span> Added support for new cloud messaging for firebase with http
</ul>
</details>

<details>
<summary><h2>Version 2.1.4 (28 May 2024)</h2></summary>
<ul>
- <span className="badge badge--info">Improved</span> Removed unused queries for Header & Footer from controller
- <span className="badge badge--info">Improved</span> IAP verification and reward distribution from admin side
- <span className="badge badge--success">Added</span> Updated admin panel code to support PHP 8.2
- <span className="badge badge--danger">Fixed</span> In admin panel, in Guess The Word allows typing non english answers textfield
- <span className="badge badge--info">Improved</span> In Admin Panel, improved daily quiz screen
- <span className="badge badge--info">Improved</span> Removed unused APIs code from admin panel side
- <span className="badge badge--info">Improved</span> Admin panel in login screen you can toggle password visibility and added code for remember me checkbox
- <span className="badge badge--success">Added</span> Next Js 14 Update Latest
- <span className="badge badge--success">Added</span> Firebase Update Latest
- <span className="badge badge--info">Improved</span> Slider API Merge With Home Settings
- <span className="badge badge--success">Added</span> Coins and Category Show in Join User in Battle
- <span className="badge badge--info">Improved</span> UI Improvements and minor Bug fixes
</ul>
</details>

<details>
<summary><h2>Version 2.1.3 (29 Apr 2024)</h2></summary>
<ul>
- <span className="badge badge--danger">Fixed</span> Category order language filters the categories dropdown
- <span className="badge badge--danger">Fixed</span> Audio question update issue
- <span className="badge badge--danger">Fixed</span> Exam sample download file issue
- <span className="badge badge--danger">Fixed</span> Home page section issue
- <span className="badge badge--info">Improved</span> Improvement UI and APIs calling
</ul>
</details>

<details>
<summary><h2>Version 2.1.2 (8 Apr 2024)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Home Settings from admin panel with language-wise
- <span className="badge badge--success">Added</span> Footer and Header color from admin panel
- <span className="badge badge--success">Added</span> Badges are now language-wise
- <span className="badge badge--success">Added</span> Added credit score and deducted score for the contest
- <span className="badge badge--danger">Fixed</span> Coins and Score Board
- <span className="badge badge--info">Improved</span> UI Improvement
</ul>
</details>

<details>
<summary><h2>Version 2.1.1 (20 Mar 2024)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Added functionality for users to cancel their redemption requests (in Wallet feat.)
- <span className="badge badge--info">Improved</span> Flexibility by moving web constants to the admin panel & new options
- <span className="badge badge--success">Added</span> Exam Rank Filter (Admin Panel)
- <span className="badge badge--warning">Removed</span> Remove access_key (not required) from APIs (Web, Panel)
</ul>
</details>

<details>
<summary><h2>Version 2.1.0 (14 Feb 2024)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> React Js(library) -> Next Js(Framework) Implement
- <span className="badge badge--success">Added</span> New UI added
- <span className="badge badge--danger">Fixed</span> Bug Fixes and Improvements

Admin Panel Changelog:

- <span className="badge badge--danger">Fixed</span> Table responsive for mobile view
- <span className="badge badge--danger">Fixed</span> Leaderboard APIs in APIs
- <span className="badge badge--danger">Fixed</span> Language Update Data Fixed
- <span className="badge badge--success">Added</span> Slug for Category and Subcategory
- <span className="badge badge--success">Added</span> Latex support in Question Report
- <span className="badge badge--danger">Fixed</span> Other minor fixes
</ul>
</details>

<details>
<summary><h2>Version 2.0.9 (11 Dec 2023)</h2></summary>
<ul>
Admin Panel Update:
- <span className="badge badge--success">Added</span> Maths Question Edit Bug Fix
- <span className="badge badge--success">Added</span> Options Shuffle in API
- <span className="badge badge--success">Added</span> Quiz Mode done Toggle
- <span className="badge badge--success">Added</span> Contest prize issue solved in coin history
- <span className="badge badge--success">Added</span> Dashboard chart fixed and added filter for months
- <span className="badge badge--success">Added</span> Theme Color Added
- <span className="badge badge--success">Added</span> Footer Copyrights Text is customisable
- <span className="badge badge--success">Added</span> Latex Support for Quiz Zone and Exam Module's Questions
- <span className="badge badge--success">Added</span> Download Sample CSV file Directly

Web Update:

- <span className="badge badge--success">Added</span> Dynamic Theme Color Added from Admin Panel
- <span className="badge badge--success">Added</span> Latex in Quiz Zone and Exam Feature
- <span className="badge badge--success">Added</span> Contest Play Feature of More Reward Points
- <span className="badge badge--danger">Fixed</span> Review Answer Deduct Coins
- <span className="badge badge--danger">Fixed</span> Sitemap Xml
- <span className="badge badge--info">Improved</span> Improvement and Minor Bug Fixes
</ul>
</details>

<details>
<summary><h2>Version 2.0.8 (1 Nov 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Play With Bot In Random 1 vs 1 Battle
- <span className="badge badge--success">Added</span> Toggle Added for Home Screen Section
- <span className="badge badge--success">Added</span> New documentation added for video doc, change log, app doc, admin panel etc
- <span className="badge badge--danger">Fixed</span> Minor Premium Categories issue Fixed
- <span className="badge badge--info">Improved</span> Guess the word feature for all language
</ul>
</details>

<details>
<summary><h2>Version 2.0.7 (21 Sep 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Premium Quiz Categories: Elevate your quiz game with Premium Categories and Subcategories, available in all the quizzes!
- <span className="badge badge--info">Improved</span> UI Improvement & Bug Fixes

Admin Panel Specific:

- <span className="badge badge--success">Added</span> Premium Quiz Categories: Create and edit premium categories/subcategories
- <span className="badge badge--success">Added</span> Revamped Login Page Design Experience: Customize it with Your Own Background Image for a Unique Touch
- <span className="badge badge--success">Added</span> Reinforced Security: We've brought back the JWT Key input for enhanced security within the admin panel
</ul>
</details>

<details>
<summary><h2>Version 2.0.6 (9 Aug 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> New Home screen design
- <span className="badge badge--info">Improved</span> UI Improvements
</ul>
</details>

<details>
<summary><h2>Version 2.0.5 (20 July 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Battle UI
- <span className="badge badge--info">Improved</span> Minor Bug Fixes
</ul>
</details>

<details>
<summary><h2>Version 2.0.4 (20 June 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Guest Mode
- <span className="badge badge--success">Added</span> Profile Custom Image
- <span className="badge badge--warning">Updated</span> Updated Latest Library
- <span className="badge badge--info">Improved</span> Improvements & bug fixes
</ul>
</details>

<details>
<summary><h2>Version 2.0.3 (20 May 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Added Firebase, Logo, Footer etc data from Admin Panel
- <span className="badge badge--success">Added</span> Added Coin History Feature
- <span className="badge badge--success">Added</span> Added Badges Feature
</ul>
</details>

<details>
<summary><h2>Version 2.0.2 (18 Mar 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Added Sounds Feature on the answer
- <span className="badge badge--success">Added</span> Added Admin Panel
- <span className="badge badge--danger">Fixed</span> Fix Guess the word Feature
</ul>
</details>

<details>
<summary><h2>Version 2.0.1 (1 Mar 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> New Exam Module
- <span className="badge badge--danger">Fixed</span> 1 vs 1 Battle and Group Battle
- <span className="badge badge--danger">Fixed</span> General Improvements and Bug Fixes
</ul>
</details>

<details>
<summary><h2>Version 2.0.0 (10 Feb 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Math Mania Feature
- <span className="badge badge--success">Added</span> React 18 Added
- <span className="badge badge--success">Added</span> SVG images Added
- <span className="badge badge--success">Added</span> Loader Added with every Route
- <span className="badge badge--info">Optimized</span> Redux Store Optimize
- <span className="badge badge--danger">Fixed</span> useEffect Cleanup Function Error Fix
- <span className="badge badge--danger">Fixed</span> SelfChallenge issue Fix
- <span className="badge badge--danger">Fixed</span> Improvements & bug fixes
</ul>
</details>

<details>
<summary><h2>Version 1.0.9 (1 Feb 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Audio Quiz
- <span className="badge badge--success">Added</span> Redux Added
- <span className="badge badge--info">Improved</span> 1 vs 1 Battle issue Fixed
- <span className="badge badge--danger">Fixed</span> Improvements & bug fixes
</ul>
</details>

<details>
<summary><h2>Version 1.0.8 (11 Jan 2023)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Group Battle Feature
- <span className="badge badge--danger">Fixed</span> Quiz Zone Issue Fixed
- <span className="badge badge--success">Added</span> More language labels
- <span className="badge badge--info">Improved</span> UI Improved
</ul>
</details>

<details>
<summary><h2>Version 1.0.7 (15 Nov 2022)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Battle Quiz Feature
- <span className="badge badge--success">Added</span> All Quiz Timer Dynamic from Admin panel
- <span className="badge badge--success">Added</span> Theme Changed
- <span className="badge badge--success">Added</span> Loader Added
- <span className="badge badge--success">Added</span> Dynamic Mode Added and data added
- <span className="badge badge--danger">Fixed</span> Language Selector with slider fixed
- <span className="badge badge--danger">Fixed</span> Improvements and issues fixed
</ul>
</details>

<details>
<summary><h2>Version 1.0.6 (26 Sep 2022)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Contest Play Mode
- <span className="badge badge--info">Improved</span> Improvements and Issue Fixed
</ul>
</details>

<details>
<summary><h2>Version 1.0.5 (14 Sep 2022)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Self-Learning Feature
- <span className="badge badge--info">Improved</span> Improvements and Issues Fixed
</ul>
</details>

<details>
<summary><h2>Version 1.0.4 (19 Aug 2022)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Guess the word feature
- <span className="badge badge--danger">Fixed</span> Language Mode Fix with Language Selector
- <span className="badge badge--danger">Fixed</span> Quiz Zone Question issue
- <span className="badge badge--info">Improved</span> Slider Improvement
- <span className="badge badge--info">Improved</span> Fun and learn question issue Improvement
- <span className="badge badge--info">Improved</span> UI Improvement
- <span className="badge badge--info">Improved</span> Spinner Improvement
</ul>
</details>

<details>
<summary><h2>Version 1.0.3 (17 June 2022)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> True / False Feature
- <span className="badge badge--success">Added</span> Fun and Learn Feature
- <span className="badge badge--success">Added</span> 50-50 Feature Disabled when true / false questions
- <span className="badge badge--danger">Fixed</span> Audience Poll issue with true or false questions
- <span className="badge badge--info">Improved</span> User Experience in Quiz Play Scrolling issue Fix
- <span className="badge badge--danger">Fixed</span> Time Network error
- <span className="badge badge--info">Improved</span> Optimized Code
- <span className="badge badge--danger">Fixed</span> Smooth Scroll
</ul>
</details>

<details>
<summary><h2>Version 1.0.2 (27 May 2022)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> RTL Feature added
- <span className="badge badge--success">Added</span> Footer Section Added
- <span className="badge badge--danger">Fixed</span> Login and Logout issue fix
- <span className="badge badge--info">Improved</span> UI Improvement and Animations Added
</ul>
</details>

<details>
<summary><h2>Version 1.0.1 (10 May 2022)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Daily quiz
- <span className="badge badge--success">Added</span> Maintenance mode
- <span className="badge badge--success">Added</span> More animations
- <span className="badge badge--success">Added</span> More feature with payara
- <span className="badge badge--info">Improved</span> Optimization and Improvements of performance
</ul>
</details>

<details>
<summary><h2>Version 1.0.0 (29 Mar 2022)</h2></summary>
<ul>
- <span className="badge badge--success">Added</span> Initial version with Base Quiz
</ul>
</details>

</div>
