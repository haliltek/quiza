<?php
define('BASEPATH', '/var/www/html/system/');
define('APPPATH', '/var/www/html/application/');

class CI_Controller {}

require_once '/var/www/html/application/controllers/Book_Importer.php';

$refClass = new ReflectionClass('Book_Importer');
$importer = $refClass->newInstanceWithoutConstructor();

$ref = new ReflectionMethod('Book_Importer', 'parse_generic_pdf');
$ref->setAccessible(true);
$res = $ref->invoke($importer, '/tmp/2009.pdf', '2009 KPSS');

echo "SUCCESS: " . ($res['error'] ? 'NO' : 'YES') . "
";
echo "TOTAL: " . count($res['questions']) . "
";

foreach ($res['questions'] as $q) {
    if ($q['test'] === 'GY' && $q['qnum'] === 28) {
        echo "=== GY 28 ===
";
        echo "Q: " . $q['question'] . "
";
        echo "A: " . $q['optiona'] . "
";
        echo "B: " . $q['optionb'] . "
";
        echo "C: " . $q['optionc'] . "
";
        echo "D: " . $q['optiond'] . "
";
        echo "E: " . $q['optione'] . "
";
        echo "Ans: " . $q['answer'] . "
";
    }
    if ($q['test'] === 'GK' && $q['qnum'] === 1) {
        echo "=== GK 1 ===
";
        echo "Subject: " . $q['subject'] . "
";
        echo "Q: " . $q['question'] . "
";
        echo "A: " . $q['optiona'] . "
";
        echo "B: " . $q['optionb'] . "
";
        echo "C: " . $q['optionc'] . "
";
        echo "D: " . $q['optiond'] . "
";
        echo "E: " . $q['optione'] . "
";
        echo "Ans: " . $q['answer'] . "
";
    }
}
