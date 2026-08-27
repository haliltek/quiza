import React from 'react';

export default function Video({ src, title, ...props }) {
  // Check if the src is a YouTube link (supports both youtu.be and youtube.com/embed)
  const isYouTube =
    typeof src === 'string' && (src.includes('youtube.com') || src.includes('youtu.be'));

  const videoStyle = {
    display: 'block',
    margin: '0 auto',
    borderRadius: '16px', // Rounded corners
    overflow: 'hidden',
  };

  if (isYouTube) {
    // Convert youtu.be short links to embed links if needed
    let embedSrc = src;
    if (src.includes('youtu.be/')) {
      const videoId = src.split('youtu.be/')[1].split(/[?&]/)[0];
      embedSrc = `https://www.youtube.com/embed/${videoId}`;
    }
    return (
      <iframe
        width="90%"
        height="400"
        src={embedSrc}
        title={title || 'YouTube Video'}
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowFullScreen
        style={videoStyle}
        {...props}
      />
    );
  }

  return (
    <video controls width="100%" title={title} style={videoStyle} {...props}>
      <source src={src} type="video/mp4" />
      Your browser does not support the video tag.
    </video>
  );
}
