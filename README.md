# 🔐 Password Generator CLI App – Screenshots Walkthrough

This document provides a complete walkthrough of the Password Generator CLI application, built in Python. It includes UI interactions, password strength validation, and proof of development history dating back to 2021.

---

## 🗂️ Project Directory Snapshot

<img width="681" height="571" alt="image" src="https://github.com/user-attachments/assets/bc451c93-f323-40ab-9019-629ff728d5fa" />


📁 This screenshot verifies that several files (e.g., `PasswordGenerator.py`, `html1.py`, `printfile.py`, etc.) date back to **May-June 2021**, confirming the original development period of this project.

---

## 🏁 Main Menu

<img width="1106" height="625" alt="Screenshot 2025-07-20 205637" src="https://github.com/user-attachments/assets/2b065ce7-c02c-4063-9a2f-564430198e3c" />


Options:
1. Generate only a random Password  
2. Generate – Manage and save a Password  
3. Show Saved Accounts and Passwords  
4. Check how strong your Password is!  
0. STOP  

---

## 🔑 Weak Password Generation – Lowercase Only

<img width="1363" height="720" alt="Screenshot 2025-07-20 205659" src="https://github.com/user-attachments/assets/b05b8686-7a0f-484a-933a-245b0b7c7890" />
<img width="610" height="299" alt="Screenshot 2025-07-20 205816" src="https://github.com/user-attachments/assets/726a9cda-c4c4-4763-94e1-4acce1edc3f9" />


- User selected: **Weak Password**
- Type: **Lowercase only**
- Generated password: `rfirjsen`
- Choice: Not saved.

---

## 🔐 Weak, Medium, and Strong Password Types

### Weak Password Types

<img width="582" height="254" alt="Screenshot 2025-07-20 205914" src="https://github.com/user-attachments/assets/2e97b057-8603-4fef-9cc7-5fc8a8fd753a" />


- Choices: Lowercase, Uppercase, Numbers only

### Medium Password Example

<img width="582" height="254" alt="Screenshot 2025-07-20 205914" src="https://github.com/user-attachments/assets/a3d796eb-13a7-4368-8bab-e43c6e325d54" />

- Contains mixed-case letters and numbers  
- Sample: `u4GhQ0xT`

### Strong Password Example

<img width="546" height="320" alt="Screenshot 2025-07-20 205942" src="https://github.com/user-attachments/assets/a7dda5ea-a1d9-47e6-b70d-a266e209d676" />

- User defined length: 14  
- Example: `$T3TyU4fyT33$y`  


---

## ✅ Password Strength Checker

<img width="1093" height="420" alt="Screenshot 2025-07-20 210112" src="https://github.com/user-attachments/assets/d8e54ccf-41ba-4bda-b8e7-15c8098f91a3" />

- Input password: `Lulumall@123`  
- Found repeated digits: `['1', '1']`  
- Suggestion: Consider modifying for better strength

---

## ✅ Password Management

<img width="1288" height="413" alt="Screenshot 2025-07-20 210034" src="https://github.com/user-attachments/assets/e3315ffe-2d7a-477e-b2bc-bde84bee1160" />


- Input website to search: `instagram.com`  
- Found result cannot be shown as they contained my real data!  
- Suggestion: Consider modifying for better structure and looks.

---

## 🗃️ Project Structure (Partial List)
Includes:
- 'passgenfun' - Complete functions defined for operation
- `PasswordGenerator.py` – Core logic  
- `PasswordGenerator_UI.py` – Interface handler  
- `records.db` – Local storage of saved credentials  (Though removed for safety reasons)
- `Manage Passwords.bat` – Batch shortcut to launch the app  
- `securedfamilydb.py`, `SearchLike.py`, `SecureLock.py` – Additional tools/scripts

---

📌 **Note:** This project was built purely using Python and local file/database management — no external GUI frameworks or cloud databases were used.

