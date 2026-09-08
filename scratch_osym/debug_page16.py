import subprocess

php_test = """<?php
$text = shell_exec('pdftotext -enc UTF-8 -layout /tmp/2009.pdf -');
$pages = array_values(array_filter(explode("\x0c", $text), function($p) { return !empty(trim($p)); }));
$pContent = $pages[15]; // Page 16 (0-indexed 15)
echo "=== RAW PAGE 16 ===\n";
echo $pContent;
"""

# Copy 2009.pdf to remote /tmp/2009.pdf
subprocess.run(['scp', 'd:/quiza/scratch_osym/2009.pdf', 'root@142.93.104.78:/tmp/2009.pdf'])

# Run php test
cmd = ['ssh', 'root@142.93.104.78', 'docker exec -i elitequiz_api php -r "
$text = shell_exec(\'pdftotext -enc UTF-8 -layout /tmp/2009.pdf -\');
$pages = array_values(array_filter(explode(\\"\\x0c\\", $text), function(\\$p) { return !empty(trim(\\$p)); }));
echo substr(\\$pages[15], 0, 2000);
"']
res = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
