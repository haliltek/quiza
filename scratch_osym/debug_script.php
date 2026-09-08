<?php
$text = shell_exec('pdftotext -enc UTF-8 -layout /tmp/2009.pdf -');
$pages = array_values(array_filter(explode("\x0c", $text), function($p) { return !empty(trim($p)); }));
echo "TOTAL PAGES: " . count($pages) . "\n";
echo "=== PAGE 16 (first 2500 chars) ===\n";
echo substr($pages[15], 0, 2500);
