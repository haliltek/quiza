import React, { useState, useEffect, useRef } from 'react';
import styles from './styles.module.css';

const EMOJI_RATINGS = [
  { emoji: '😞', label: 'Very Unhelpful', value: 1 },
  { emoji: '😕', label: 'Not Helpful', value: 2 },
  { emoji: '😐', label: 'Okay', value: 3 },
  { emoji: '😊', label: 'Helpful', value: 4 },
  { emoji: '🤩', label: 'Very Helpful', value: 5 },
];

const STORAGE_KEY = 'elite-quiz-docs-feedback';

export default function PageFeedback() {
  const [selectedRating, setSelectedRating] = useState(null);
  const [hoveredRating, setHoveredRating] = useState(null);
  const [comment, setComment] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [showComment, setShowComment] = useState(false);
  const [previousFeedback, setPreviousFeedback] = useState(null);
  const commentSectionRef = useRef(null);

  // Get current page info
  const pagePath = typeof window !== 'undefined' ? window.location.pathname : '';
  const pageTitle = typeof document !== 'undefined' ? document.title : '';

  useEffect(() => {
    // Check if feedback already submitted for this page
    if (typeof window !== 'undefined') {
      try {
        const stored = localStorage.getItem(STORAGE_KEY);
        if (stored) {
          const feedback = JSON.parse(stored);
          if (feedback[pagePath]) {
            setPreviousFeedback(feedback[pagePath]);
            setIsSubmitted(true);
          }
        }
      } catch (error) {
        console.error('Error loading feedback from storage:', error);
      }
    }
  }, [pagePath]);

  const handleRatingClick = (rating) => {
    setSelectedRating(rating);
    setShowComment(true);

    // Auto-submit rating to GA4 immediately
    const timestamp = new Date().toISOString();
    if (typeof window !== 'undefined' && window.gtag) {
      window.gtag('event', 'page_feedback', {
        rating: rating,
        page_path: pagePath,
        page_title: pageTitle,
        timestamp: timestamp,
      });
    }

    // Store in localStorage (without comment)
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      const allFeedback = stored ? JSON.parse(stored) : {};
      allFeedback[pagePath] = {
        rating: rating,
        hasComment: false,
        timestamp: Date.now(),
        submitted: true,
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(allFeedback));
    } catch (error) {
      console.error('Error saving feedback to storage:', error);
    }

    // Smooth scroll to comment section after a brief delay
    setTimeout(() => {
      if (commentSectionRef.current) {
        commentSectionRef.current.scrollIntoView({
          behavior: 'smooth',
          block: 'nearest',
        });
      }
    }, 300);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!selectedRating || !comment.trim()) {
      // If no comment, just show thank you (rating already submitted)
      setIsSubmitted(true);
      return;
    }

    setIsSubmitting(true);

    // Send comment update to Google Analytics
    const timestamp = new Date().toISOString();
    if (typeof window !== 'undefined' && window.gtag) {
      window.gtag('event', 'page_feedback_comment', {
        rating: selectedRating,
        page_path: pagePath,
        page_title: pageTitle,
        feedback_comment: comment.trim(),
        timestamp: timestamp,
      });
    }

    // Update localStorage with comment
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      const allFeedback = stored ? JSON.parse(stored) : {};
      allFeedback[pagePath] = {
        rating: selectedRating,
        hasComment: true,
        timestamp: Date.now(),
        submitted: true,
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(allFeedback));
      setPreviousFeedback(allFeedback[pagePath]);
    } catch (error) {
      console.error('Error saving feedback to storage:', error);
    }

    // Simulate submission delay for better UX
    setTimeout(() => {
      setIsSubmitting(false);
      setIsSubmitted(true);
    }, 500);
  };

  const handleEdit = () => {
    setIsSubmitted(false);
    setPreviousFeedback(null);
    setShowComment(false);
    setSelectedRating(null);
    setComment('');

    // Remove from localStorage
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        const allFeedback = JSON.parse(stored);
        delete allFeedback[pagePath];
        localStorage.setItem(STORAGE_KEY, JSON.stringify(allFeedback));
      }
    } catch (error) {
      console.error('Error removing feedback from storage:', error);
    }
  };

  // Don't render on homepage or non-doc pages
  if (typeof window !== 'undefined' && (pagePath === '/' || pagePath === '/elite_quiz_doc/' || pagePath === '/elite_quiz_doc')) {
    return null;
  }

  if (isSubmitted && previousFeedback) {
    return (
      <div className={styles.feedbackContainer}>
        <div className={styles.thankYouState}>
          <div className={styles.checkmark}>✓</div>
          <h3>Thank you for your feedback!</h3>
          <p>Your input helps us improve our documentation.</p>
          <button
            onClick={handleEdit}
            className={styles.editButton}
            aria-label="Edit your feedback"
          >
            Edit Feedback
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className={styles.feedbackContainer}>
      <form onSubmit={handleSubmit} className={styles.feedbackForm}>
        <h3 className={styles.feedbackTitle}>Was this page helpful?</h3>

        <div className={styles.ratingsContainer}>
          {EMOJI_RATINGS.map((item) => (
            <button
              key={item.value}
              type="button"
              onClick={() => handleRatingClick(item.value)}
              onMouseEnter={() => setHoveredRating(item.value)}
              onMouseLeave={() => setHoveredRating(null)}
              className={`${styles.emojiButton} ${
                selectedRating === item.value ? styles.selected : ''
              } ${hoveredRating === item.value ? styles.hovered : ''}`}
              aria-label={`Rate ${item.label}`}
              aria-pressed={selectedRating === item.value}
            >
              <span className={styles.emoji} role="img" aria-label={item.label}>
                {item.emoji}
              </span>
              <span className={styles.ratingLabel}>{item.label}</span>
            </button>
          ))}
        </div>

        {showComment && (
          <div ref={commentSectionRef} className={styles.commentSection}>
            <p className={styles.thanksMessage}>
              Thanks for your feedback! Want to share more details?
            </p>

            <textarea
              id="feedback-comment"
              value={comment}
              onChange={(e) => setComment(e.target.value)}
              placeholder="Tell us what we could improve... (optional)"
              className={styles.commentTextarea}
              rows={3}
              maxLength={1000}
            />
            <div className={styles.characterCount}>
              {comment.length}/1000 characters
            </div>

            <div className={styles.buttonGroup}>
              <button
                type="submit"
                disabled={isSubmitting || !comment.trim()}
                className={styles.submitButton}
              >
                {isSubmitting ? (
                  <>
                    <span className={styles.spinner}></span>
                    Sending...
                  </>
                ) : (
                  'Add Comment'
                )}
              </button>
              <button
                type="button"
                onClick={() => {
                  setPreviousFeedback({ submitted: true });
                  setIsSubmitted(true);
                }}
                className={styles.skipButton}
              >
                Skip
              </button>
            </div>
          </div>
        )}
      </form>
    </div>
  );
}
