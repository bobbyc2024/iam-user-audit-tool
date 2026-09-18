# IAM User Audit Tool

A Python-based IAM auditing tool that analyses user account data from a CSV file and identifies potential identity and access management security issues.

## 🔐 Features

- Counts total user accounts
- Identifies accounts without MFA
- Detects inactive accounts
- Identifies administrator accounts
- Flags administrator accounts without MFA
- Generates a list of accounts requiring review

## 🛠️ Built With

- Python
- CSV

## ▶️ Usage

Run the tool against a CSV file:

```bash
python3 iam_audit.py sample_users.csv
```

You can also audit your own CSV file:

```bash
python3 iam_audit.py users.csv
```

## 📄 CSV Format

The CSV file should contain the following columns:

```text
username,name,status,mfa_enabled,role,last_login_days
```

Example:

```text
goku,Son Goku,Active,Yes,User,2
vegeta,Vegeta,Active,No,User,5
gojo,Satoru Gojo,Active,Yes,Admin,1
```

## 📊 Example Output

```text
================================
        IAM USER AUDIT
================================

Total Accounts:             5
Accounts Without MFA:       3
Inactive Accounts:          1
Admin Accounts:             2
Admins Without MFA:         1

⚠️ ACCOUNTS REQUIRING REVIEW

vegeta   - MFA not enabled
itachi   - Inactive account / MFA not enabled
levi     - Admin without MFA
```

## 🎯 Purpose

This project demonstrates practical Python automation for Identity and Access Management (IAM), including account auditing, MFA compliance and privileged access review.
