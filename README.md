🚀 Features

accepts any number of subjects

Validates:

Credits (only 1, 2, 3, or 4)

Grades (S, A, B, C, D, E, F)

Uses a standard grade-to-grade-point mapping

Calculates weighted CGPA

Displays CGPA up to two decimal places

📊 Grade-to-Point Mapping
Grade	Grade Point
S	10
A	9
B	8
C	7
D	6
E	5
F	0
🧮 How the Calculation Works

For each subject:

Weighted Score = Grade Point × Credit


Your CGPA is computed as:

CGPA = Total Weighted Score / Total Credits

📌 Usage

Run the script:

python cgpa_calculator.py


Enter the number of subjects.

For each subject:

Enter valid credits (1, 2, 3, or 4).

Enter a valid grade (S/A/B/C/D/E/F).

Your CGPA will be displayed at the end.

📝 Example Output
=== CGPA Calculator ===
Enter number of subjects: 3

Subject 1:
Enter credits (1, 2, 3, or 4): 3
Enter grade (S/A/B/C/D/E/F): A

Subject 2:
Enter credits (1, 2, 3, or 4): 4
Enter grade (S/A/B/C/D/E/F): B

Subject 3:
Enter credits (1, 2, 3, or 4): 3
Enter grade (S/A/B/C/D/E/F): S

------------------------
Your CGPA is: 8.78
------------------------

✔ Requirements

Python 3.x

📄 License

This project is free to use and modify.
