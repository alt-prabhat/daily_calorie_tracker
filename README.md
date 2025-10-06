# <p align="center">My First Portfolio Project</p>

Simple command‑line tool to log meals, calculate total and average calories, compare against a user daily limit, and optionally save a session report. Built as an individual mini project for the course: Programming for Problem Solving using Python.

---

## 1. Project Overview
A lightweight Python script (tracker.py) that:
- Prompts the user for a daily calorie limit
- Collects meal names and calorie values
- Computes total and average calories
- Warns if limit exceeded
- Displays a formatted summary table
- Optionally saves a timestamped log to calorie_log.txt

---

## 2. Learning Objectives Covered
| Objective | How Addressed |
|-----------|---------------|
| input(), type conversion | Used for numeric (float/int) and text inputs |
| Lists & data storage | Parallel lists: meal_names, calorie_val |
| Arithmetic & comparison | Total, average, limit comparison, warning |
| String formatting | f-strings, \n, \t, decorative lines |
| File I/O | Writes structured log with timestamp |
| Logical thinking | Structured task flow (Tasks 1–6) |

---

## 3. Files
```
daily_calorie_tracker/
│ tracker.py
│ calorie_log.txt        (generated only if user saves)
│ README.md
```

---

## 4. How to Run (Windows)
1. Open terminal in project folder  
2. Run:  
   ```
   python tracker.py
   ```
3. Follow on‑screen prompts  
4. Choose Y to save a session log (creates/overwrites calorie_log.txt)

Python Version: Works with Python 3.10+

---

## 5. Program Flow (Task Mapping)
| Task | Implementation in tracker.py |
|------|-------------------------------|
| Task 1 | Header comments + welcome prints |
| Task 2 | Loop over user-specified meal count; append to lists |
| Task 3 | sum() for total, average = total / count |
| Task 4 | if total_cal > daily_lim → warning string |
| Task 5 | Formatted table using tabs & lines |
| Task 6 (Bonus) | Optional save with timestamp using datetime |

---

## 6. Sample Run (Example 1)
```
--- Daily Calorie Tracker CLI by Prabhat Bhatia ---

=> Enter your meals and their calorie values.

Enter your daily calorie limit: 2000
How many meals do you want to enter:3

Meal 1:
Meal name: Vada Pav
Calories for Vada Pav: 700

Meal 2:
Meal name: Sandwich
Calories for Sandwich: 600

Meal 3:
Meal name: Rasmalai
Calories for Rasmalai: 800

Meal Name 			           Calories:
--------------------------------------------------
Vada Pav 			             700.0 cal
Sandwich 			             600.0 cal
Rasmalai 			             800.0 cal

Total calories: 2100.0
Average calories: 700.0
WARNING: Daily calorie limit exceeded!

Do you want to save this report? (Y/N): y

Saved to calorie_log.txt.
```

---

## 7. Generated Log Format (calorie_log.txt)
```
CALORIE TRACKER LOG - 2025-10-06 19:36:54.744298
Daily Calorie Limit: 2000.0

Meal Name 			 Calories 
Vada Pav: 			 700.0 cal 

Sandwich: 			 600.0 cal 

Rasmalai: 			 800.0 cal 

Total calories: 2100.0
Average calories: 700.0
WARNING: Daily calorie limit exceeded!
```

---

## 8. References
- Python Docs: https://docs.python.org/3/
- datetime module (standard library)

---

## 9. Details
- Prabhat Bhatia
- 2501410006
- B.Tech CSE Cyber Security(First Semester)
- 6th October 2025
- Web Development - Lab Assignment(1+2)
