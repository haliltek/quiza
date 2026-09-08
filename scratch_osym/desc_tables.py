import subprocess

cmd_desc_cat = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "DESCRIBE tbl_category;"']
res_desc_cat = subprocess.run(cmd_desc_cat, capture_output=True, text=True)
print("DESCRIBE tbl_category:")
print(res_desc_cat.stdout)

cmd_desc_subcat = ['ssh', 'root@142.93.104.78', 'docker exec elitequiz_db mysql -uelite_user -pelite_user_pass_2026 elite_quiz_db -e "DESCRIBE tbl_subcategory;"']
res_desc_subcat = subprocess.run(cmd_desc_subcat, capture_output=True, text=True)
print("DESCRIBE tbl_subcategory:")
print(res_desc_subcat.stdout)
