import subprocess

php_test = """<?php
define('BASEPATH', '/var/www/html/system/');
define('APPPATH', '/var/www/html/application/');

class CI_Controller {}

require_once '/var/www/html/application/controllers/Book_Importer.php';

$refClass = new ReflectionClass('Book_Importer');
$importer = $refClass->newInstanceWithoutConstructor();

$ref = new ReflectionMethod('Book_Importer', 'parse_generic_pdf');
$ref->setAccessible(true);
$res = $ref->invoke($importer, '/tmp/2009.pdf', '2009 KPSS');

echo "SUCCESS: " . ($res['error'] ? 'NO' : 'YES') . "\n";
echo "TOTAL: " . count($res['questions']) . "\n";

foreach ($res['questions'] as $q) {
    if ($q['test'] === 'GY' && $q['qnum'] === 28) {
        echo "=== GY 28 ===\n";
        echo "Q: " . $q['question'] . "\n";
        echo "A: " . $q['optiona'] . "\n";
        echo "B: " . $q['optionb'] . "\n";
        echo "C: " . $q['optionc'] . "\n";
        echo "D: " . $q['optiond'] . "\n";
        echo "E: " . $q['optione'] . "\n";
        echo "Ans: " . $q['answer'] . "\n";
    }
    if ($q['test'] === 'GK' && $q['qnum'] === 1) {
        echo "=== GK 1 ===\n";
        echo "Subject: " . $q['subject'] . "\n";
        echo "Q: " . $q['question'] . "\n";
        echo "A: " . $q['optiona'] . "\n";
        echo "B: " . $q['optionb'] . "\n";
        echo "C: " . $q['optionc'] . "\n";
        echo "D: " . $q['optiond'] . "\n";
        echo "E: " . $q['optione'] . "\n";
        echo "Ans: " . $q['answer'] . "\n";
    }
}
"""

with open('d:/quiza/scratch_osym/test_invoker.php', 'w', encoding='utf-8') as f:
    f.write(php_test)

subprocess.run(['scp', 'd:/quiza/scratch_osym/test_invoker.php', 'root@142.93.104.78:/tmp/test_invoker.php'])
cmd = ['ssh', 'root@142.93.104.78', 'docker cp /tmp/test_invoker.php elitequiz_api:/tmp/test_invoker.php; docker exec elitequiz_api php /tmp/test_invoker.php']
res = subprocess.run(cmd, capture_output=True, text=True)
print("STDOUT:", res.stdout)
print("STDERR:", res.stderr)
