const fs = require('fs');

const content = fs.readFileSync('d:/quiza/turkce_lang.php', 'utf8');
const lines = content.split('\n');
const langMap = {};

lines.forEach(line => {
    const match = line.match(/\$lang\['([^']+)'\]\s*=\s*"([^"]*)";/);
    if (match) {
        langMap[match[1]] = match[2];
    }
});

console.log('Total System Language Keys:', Object.keys(langMap).length);
console.log('Sample entries (0-20):');
Object.entries(langMap).slice(0, 20).forEach(([k, v]) => console.log(`${k} => ${v}`));
