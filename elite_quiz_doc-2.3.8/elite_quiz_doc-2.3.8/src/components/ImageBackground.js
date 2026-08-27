import React from 'react';
import styles from './ImageBackground.module.css';

export default function ImageBackground({ children }) {
  return (
    <div className={styles.imageBackgroundContainer}>
      <div className={styles.imageBackgroundPattern}></div>
      {children}
    </div>
  );
}
