import subprocess

cmd_cats = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT id, category_name, language_id FROM tbl_category WHERE language_id = 52 OR category_name LIKE \'%KPSS%\';"']
res_cats = subprocess.run(cmd_cats, capture_output=True, text=True)
print("=== CATEGORIES ===")
print(res_cats.stdout)

cmd_subcats = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "SELECT id, maincat_id, subcategory_name, language_id FROM tbl_subcategory WHERE language_id = 52;"']
res_subcats = subprocess.run(cmd_subcats, capture_output=True, text=True)
print("=== SUBCATEGORIES (language_id=52) ===")
print(res_subcats.stdout)
