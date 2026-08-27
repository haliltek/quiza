import React from 'react';
import CodeBlock from '@theme-original/CodeBlock';

export default function CodeBlockWrapper(props) {
  const { className, metastring, children } = props;

  // Extract file name from the metastring if available
  let fileName = null;
  if (metastring) {
    const fileMatch = metastring.match(/title="([^"]*)"/);
    if (fileMatch && fileMatch[1]) {
      fileName = fileMatch[1];
    }
  }

  return (
    <>
      {fileName && (
        <div className="code-block-file-name" data-file-name={fileName}>
          {fileName}
        </div>
      )}
      <CodeBlock {...props} />
    </>
  );
}
