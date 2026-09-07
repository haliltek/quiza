---
sidebar_position: 8
---

# Bulk Import Questions

:::tip
The Import Questions feature lets you upload multiple questions at once using CSV or Excel files. This saves time when creating large question banks for your quizzes.
:::

## Before You Start

### File Format Requirements

- **File types**: CSV (.csv) or Excel (.xlsx)
- **Encoding**: CSV files must be UTF-8 encoded
- **Header row**: First row must contain column names
- **Column order**: Can be in any order, but names must match exactly

### Unicode CSV Conversion (For Non-English Content)

If you're using non-English text, follow these steps to ensure proper encoding:

1. Fill your data in Excel using the provided format
2. Save as **Unicode Text (\*.txt)**
3. Open the .txt file in Notepad
4. Replace Tab spaces with commas (,)
5. Save with .txt extension and change encoding to **UTF-8**
6. Change file extension from .txt to .csv
7. Upload the converted .csv file

---

## Quiz Zone Questions

Standard multiple-choice questions with single correct answers, supporting both regular and true/false formats.

### Required Columns

| Column          | Description             | Example Values                              |
| --------------- | ----------------------- | ------------------------------------------- |
| `category`      | Category ID (number)    | `63`                                        |
| `subcategory`   | Subcategory ID (number) | `97`                                        |
| `language_id`   | Language ID (number)    | `1` for English, `2` for other              |
| `question_type` | Question format         | `1` for multiple choice, `2` for true/false |
| `question`      | Question text           | `"What is the capital of France?"`          |
| `option 1`      | First option            | `"Paris"` or `"True"`                       |
| `option 2`      | Second option           | `"London"` or `"False"`                     |
| `option 3`      | Third option            | `"Berlin"` (blank for true/false)           |
| `option 4`      | Fourth option           | `"Madrid"` (blank for true/false)           |
| `option 5`      | Fifth option (optional) | `"Rome"` or blank                           |
| `answer`        | Correct answer          | `"a"`, `"b"`, `"c"`, `"d"`, or `"e"`        |
| `level`         | Difficulty level        | `1`, `2`, `3`, etc.                         |
| `note`          | Additional notes        | `"Geography basics"` or blank               |

### Sample Data Format

```csv
category,subcategory,language_id,question_type,question,option 1,option 2,option 3,option 4,option 5,answer,level,note
63,97,2,1,What is the capital of France?,Paris,London,Berlin,Madrid,,a,1,Geography basics
63,97,1,2,Is water H2O?,True,False,,,,a,2,Chemistry fact
```

### Multiple Choice Example

```csv
category,subcategory,language_id,question_type,question,option 1,option 2,option 3,option 4,option 5,answer,level,note
63,97,1,1,Which planet is closest to the Sun?,Mercury,Venus,Earth,Mars,,a,1,Solar system
63,97,1,1,What is 5 × 7?,30,35,40,45,,b,2,Basic math
```

### True/False Example

```csv
category,subcategory,language_id,question_type,question,option 1,option 2,option 3,option 4,option 5,answer,level,note
63,97,1,2,The Earth is flat,True,False,,,,b,1,Basic science
63,97,1,2,Water boils at 100°C,True,False,,,,a,1,Physics
```

---

## Multi Match Questions

Matching questions where users connect left items to right items. Supports multiple selection and sequence ordering.

### Required Columns

| Column                   | Description      | Values                                      |
| ------------------------ | ---------------- | ------------------------------------------- |
| `category`               | Category ID      | `63`                                        |
| `subcategory`            | Subcategory ID   | `97`                                        |
| `language_id`            | Language ID      | `1`, `2`, etc.                              |
| `question_type`          | Question format  | `1` for multiple choice, `2` for true/false |
| `question`               | Question text    | `"Match countries to capitals"`             |
| `option 1` to `option 5` | Answer options   | Various options                             |
| `answer_type`            | Answer format    | `1` for multi-select, `2` for sequence      |
| `answer1` to `answer5`   | Correct answers  | `"a"`, `"b"`, `"c"`, etc.                   |
| `level`                  | Difficulty level | `1`, `2`, `3`                               |
| `note`                   | Additional notes | Optional                                    |

### Sample Format

```csv
category,subcategory,language_id,question_type,question,option 1,option 2,option 3,option 4,option 5,answer_type,answer1,answer2,answer3,answer4,answer5,level,note
63,97,2,1,Match elements to symbols,Hydrogen,Carbon,Oxygen,Nitrogen,,1,a,c,b,d,,1,Chemistry matching
```

---

## Exam Questions

Questions designed for formal examinations with specific marking schemes.

### Required Columns

| Column                   | Description               | Values                                      |
| ------------------------ | ------------------------- | ------------------------------------------- |
| `exam_module_id`         | Exam module identifier    | `1`, `2`, etc.                              |
| `mark`                   | Points for correct answer | `1`, `2`, `5`, etc.                         |
| `question_type`          | Question format           | `1` for multiple choice, `2` for true/false |
| `question`               | Question text             | Full question                               |
| `option 1` to `option 5` | Answer choices            | Various options                             |
| `answer`                 | Correct answer            | `"a"`, `"b"`, `"c"`, `"d"`, `"e"`           |

### Sample Format

```csv
exam_module_id,mark,question_type,question,option 1,option 2,option 3,option 4,option 5,answer
2,1,1,What is the speed of light?,3×10⁸ m/s,3×10⁶ m/s,3×10⁹ m/s,3×10⁷ m/s,,a
1,2,2,Energy cannot be created or destroyed,True,False,,,,a
```

---

## Contest Questions

Questions for timed contests and competitions.

### Required Columns

| Column                   | Description            | Values                                      |
| ------------------------ | ---------------------- | ------------------------------------------- |
| `contest_id`             | Contest identifier     | `1`, `2`, etc.                              |
| `question_type`          | Question format        | `1` for multiple choice, `2` for true/false |
| `question`               | Question text          | Full question                               |
| `option 1` to `option 5` | Answer choices         | Various options                             |
| `answer`                 | Correct answer         | `"a"`, `"b"`, `"c"`, `"d"`, `"e"`           |
| `note`                   | Additional information | Optional notes                              |

### Sample Format

```csv
contest_id,question_type,question,option 1,option 2,option 3,option 4,option 5,answer,note
2,1,Which is the largest ocean?,Atlantic,Pacific,Indian,Arctic,,b,Geography contest
1,2,Mount Everest is the tallest mountain,True,False,,,,a,Physical geography
```

---

## Common Issues & Solutions

### Upload Errors

| Error                     | Solution                                                        |
| ------------------------- | --------------------------------------------------------------- |
| "Invalid file format"     | Ensure file is .csv or .xlsx with proper encoding               |
| "Missing required column" | Check that all required columns are present and named correctly |
| "Invalid answer value"    | Answer must be "a", "b", "c", "d", or "e" (lowercase)           |
| "Category not found"      | Create the category first or use correct category ID            |

### Data Validation Tips

- **Answer values**: Use lowercase letters (a, b, c, d, e)
- **Question types**: Use `1` for multiple choice, `2` for true/false
- **Empty cells**: Leave cells blank rather than using "N/A" or spaces
- **Special characters**: Ensure proper UTF-8 encoding for non-English text
- **File size**: Large files may timeout; split into smaller batches if needed

### Best Practices

- Test with a small sample file first
- Keep backup copies of your data
- Use consistent formatting throughout your file
- Validate category and subcategory IDs exist before import
- Review imported questions after upload to ensure accuracy

:::warning Important Notes

- Categories and subcategories must exist in your system before importing questions
- Option 5 is only available if enabled in System Settings
- Question types determine which options are required (true/false uses only options 1-2)
- Language IDs correspond to your system's configured languages
  :::

---

## Need Help?

If you encounter issues during import:

1. Download the sample file for your quiz type
2. Compare your format with the sample
3. Check error messages for specific row/column issues
4. Ensure all required fields are filled
5. Verify file encoding is UTF-8 for CSV files

For large imports, consider breaking your data into smaller batches to avoid timeouts.
