<?php
$url = 'https://www.scribd.com/document/822947672/HAK%C4%B0ML%C4%B0K-AKADEM%C4%B0S%C4%B0-HMGS-ANAYASA-HUKUKU-SORU-BANKASI';
preg_match('/(?:document|embeds)\/(\d+)/', $url, $m);
$docId = $m[1] ?? 'none';
echo "Doc ID: $docId\n";

$embedUrl = "https://www.scribd.com/embeds/$docId/content";
$ch = curl_init($embedUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
$html = curl_exec($ch);
curl_close($ch);

echo "HTML length: " . strlen($html) . "\n";
preg_match('/<title>(.*?)<\/title>/', $html, $tm);
echo "Title: " . ($tm[1] ?? 'None') . "\n";

preg_match_all('/pageNum:\s*(\d+).*?contentUrl:\s*"([^"]+)"/s', $html, $pageMatches);
echo "Pages found: " . count($pageMatches[1]) . "\n";
echo "HTML Body:\n" . substr($html, 0, 1500) . "\n";
