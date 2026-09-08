<?php
$h = '$2y$10$BMrcIYxcLaikC2E7JvQ7XepMHZv76w/ZfvRNLxzhWJxNtNORjYVi.';
$candidates = [
    'admin', 'admin123', 'admin@123', 'admin1234', '123456', '12345678', 
    'quiza', 'quiza123', 'quiza2026', 'halil', 'halil123', 'halil2026', 
    'elitequiz', 'password', 'root', 'Halil123', 'Halil1234', 'halil@quiza.com'
];
foreach ($candidates as $p) {
    if (password_verify($p, $h)) {
        echo "MATCH: $p\n";
        exit;
    }
}
echo "No match found in candidates\n";
