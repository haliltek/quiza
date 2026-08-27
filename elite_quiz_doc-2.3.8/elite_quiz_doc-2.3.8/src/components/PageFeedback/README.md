# PageFeedback Component - Testing & Analytics Guide

## Testing the Feedback Widget

### 1. Local Development Testing

**Browser Console Method:**

1. Open your browser DevTools (F12 or Right-click → Inspect)
2. Go to the **Console** tab
3. Paste this code to monitor GA4 events:

```javascript
// Monitor all gtag events
const originalGtag = window.gtag;
window.gtag = function(...args) {
  console.log('📊 GA4 Event Captured:', {
    command: args[0],
    eventName: args[1],
    parameters: args[2]
  });
  return originalGtag.apply(this, args);
};
```

4. Now submit feedback on any doc page
5. You should see console logs like:

```javascript
📊 GA4 Event Captured: {
  command: "event",
  eventName: "page_feedback_rating_selected",
  parameters: {
    rating: 5,
    page_path: "/admin/setup",
    page_title: "Admin Panel Setup | Elite Quiz Documentation"
  }
}

📊 GA4 Event Captured: {
  command: "event",
  eventName: "page_feedback",
  parameters: {
    rating: 5,
    page_path: "/admin/setup",
    page_title: "Admin Panel Setup | Elite Quiz Documentation",
    feedback_comment: "Great guide!",
    timestamp: "2025-10-13T08:20:55.512Z"
  }
}
```

### 2. Network Tab Verification

1. Open DevTools → **Network** tab
2. Filter by "collect" or "google-analytics"
3. Submit feedback
4. Look for POST requests to `https://www.google-analytics.com/g/collect?...`
5. Check the request payload for your event data

### 3. GA4 DebugView (Recommended)

**Enable Debug Mode:**

Add this to your browser console:
```javascript
localStorage.setItem('gtag-debug', 'true');
```

Then:
1. Go to Google Analytics → **Admin** → **DebugView**
2. Submit feedback on your site
3. Events will appear in real-time with full details

---

## Finding Feedback in Google Analytics 4

### ⚠️ Important: Localhost Events Won't Show

**Events submitted on `localhost:3000` will NOT appear in GA4** because:
- GA4 filters out localhost traffic by default
- You need to deploy to production first

### Step 1: Deploy to Production

```bash
# Build the site
bun run build

# Deploy to GitHub Pages
USE_SSH=true bun run deploy
# OR
GIT_USER=<username> bun run deploy
```

Your site will be live at: `https://wrteam-in.github.io/elite_quiz_doc/`

### Step 2: View Real-Time Events

1. Go to: https://analytics.google.com
2. Select your property (Tracking ID: `G-CS432E2TJ6`)
3. Navigate to: **Reports** → **Realtime**
4. Submit feedback on your LIVE site
5. Watch events appear in real-time under "Event count by Event name":
   - `page_feedback`
   - `page_feedback_rating_selected`

### Step 3: View Historical Events (After 24-48 hours)

#### Basic Events Report
1. **Reports** → **Engagement** → **Events**
2. Find `page_feedback` in the list
3. Click on it to see:
   - Total event count
   - Users who triggered the event
   - Event count per user

#### Detailed Event Parameters
1. **Reports** → **Engagement** → **Events** → `page_feedback`
2. Click **View event details**
3. You'll see all parameters:
   - `rating` (1-5)
   - `page_path` (which page)
   - `page_title` (page title)
   - `feedback_comment` (if provided)
   - `timestamp`

### Step 4: Create Custom Dimensions (For Advanced Filtering)

To filter and segment feedback by rating or page:

1. Go to: **Admin** → **Data display** → **Custom definitions**
2. Click **Create custom dimension**
3. Create these dimensions:

| Dimension Name | Event Parameter | Scope |
|---------------|-----------------|-------|
| Feedback Rating | `rating` | Event |
| Feedback Page | `page_path` | Event |
| Feedback Comment | `feedback_comment` | Event |

4. After 24 hours, go to **Reports** → **Explore**
5. Create a custom report:
   - **Dimensions**: Feedback Page, Feedback Rating
   - **Metrics**: Event count
   - **Filters**: Event name = `page_feedback`

### Step 5: Create Exploration Reports

**Example: Pages Needing Improvement**

1. Go to: **Explore** (left sidebar)
2. Click **Blank** to create new exploration
3. Configure:
   - **Dimensions**: Add "Page path" and "Event name"
   - **Metrics**: Add "Event count"
   - **Filters**:
     - Event name = `page_feedback`
     - rating parameter < 3 (once custom dimension is set up)
4. **Visualization**: Table or Bar chart

**Example: Feedback Distribution**

1. **Explore** → **Blank**
2. **Dimensions**: Feedback Rating (custom dimension)
3. **Metrics**: Event count
4. **Visualization**: Pie chart or Bar chart
5. Shows: How many 1-star, 2-star, 3-star, etc. ratings

---

## Event Structure Reference

### Event 1: `page_feedback_rating_selected`
Fired when user clicks an emoji (before submitting)

```javascript
{
  event: "page_feedback_rating_selected",
  rating: 5,                    // 1-5
  page_path: "/admin/setup",
  page_title: "Admin Panel Setup | Elite Quiz Documentation"
}
```

### Event 2: `page_feedback`
Fired when user submits feedback (with or without comment)

```javascript
{
  event: "page_feedback",
  rating: 5,                    // 1-5
  page_path: "/admin/setup",
  page_title: "Admin Panel Setup | Elite Quiz Documentation",
  feedback_comment: "Great guide!", // Optional, undefined if empty
  timestamp: "2025-10-13T08:20:55.512Z"
}
```

---

## Troubleshooting

### Events Not Showing in GA4?

**1. Check if gtag is loaded:**
```javascript
console.log(typeof window.gtag); // Should be "function"
```

**2. Check tracking ID:**
```javascript
// Should see G-CS432E2TJ6 in page source
document.documentElement.innerHTML.includes('G-CS432E2TJ6')
```

**3. Verify you're on production:**
- Localhost events are filtered by GA4
- Use your live site: `https://wrteam-in.github.io/elite_quiz_doc/`

**4. Wait for data processing:**
- Real-time: Appears within seconds
- Reports: Takes 24-48 hours to fully process

**5. Check browser extensions:**
- Ad blockers may block Google Analytics
- Try in incognito mode

### LocalStorage Data

Feedback is stored locally to prevent duplicates:

```javascript
// View stored feedback
console.log(localStorage.getItem('elite-quiz-docs-feedback'));

// Clear all feedback (for testing)
localStorage.removeItem('elite-quiz-docs-feedback');
```

---

## Quick Start Checklist

- [ ] Deploy site to production (`bun run deploy`)
- [ ] Visit live site (not localhost)
- [ ] Submit test feedback
- [ ] Check **Realtime** report in GA4 (appears within seconds)
- [ ] Wait 24 hours for data in main reports
- [ ] Create custom dimensions for advanced filtering
- [ ] Build custom exploration reports for insights

---

## Analytics Dashboard Examples

### Sample BigQuery SQL (If you export to BigQuery)

```sql
-- Get all feedback with ratings
SELECT
  event_date,
  event_timestamp,
  user_pseudo_id,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_path') AS page_path,
  (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'rating') AS rating,
  (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'feedback_comment') AS comment
FROM
  `your-project.analytics_YOUR_PROPERTY_ID.events_*`
WHERE
  event_name = 'page_feedback'
ORDER BY
  event_timestamp DESC
```

### Sample Google Sheets Integration

You can also export GA4 data to Google Sheets for easier analysis:

1. Install **Google Analytics Add-on** for Sheets
2. Create a query to pull `page_feedback` events
3. Build charts and pivot tables in Sheets

---

## Need Help?

If events still aren't showing:
1. Check browser console for JavaScript errors
2. Verify GA4 tracking ID in `docusaurus.config.js`
3. Test on production site (not localhost)
4. Wait 24-48 hours for data processing
5. Try GA4 DebugView for real-time debugging
