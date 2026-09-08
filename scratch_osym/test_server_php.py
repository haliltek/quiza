import subprocess

cmd = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_api php -r "
require_once \'/opt/elitequiz/backend/index.php\';
"']
