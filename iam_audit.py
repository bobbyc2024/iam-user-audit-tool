import csv
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 iam_audit.py <users.csv>")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.exists(filename):
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)

with open(filename, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    users = list(reader)

# Audit counters
mfa_missing = 0
inactive_users = 0
admin_users = 0
admin_without_mfa = 0

# Accounts that require review
review_accounts = []

for user in users:

    if user["mfa_enabled"] == "No":
        mfa_missing += 1

    if user["status"] == "Inactive":
        inactive_users += 1

    if user["role"] == "Admin":
        admin_users += 1

    if user["role"] == "Admin" and user["mfa_enabled"] == "No":
        admin_without_mfa += 1

    # Build review reasons
    reasons = []

    if user["status"] == "Inactive":
        reasons.append("Inactive account")

    if user["role"] == "Admin" and user["mfa_enabled"] == "No":
        reasons.append("Admin without MFA")
    elif user["mfa_enabled"] == "No":
        reasons.append("MFA not enabled")

    if reasons:
        review_accounts.append(
            (user["username"], " / ".join(reasons))
        )

# Display report
print("\n================================")
print("        IAM USER AUDIT")
print("================================\n")

print(f"{'Total Accounts:':<28}{len(users)}")
print(f"{'Accounts Without MFA:':<28}{mfa_missing}")
print(f"{'Inactive Accounts:':<28}{inactive_users}")
print(f"{'Admin Accounts:':<28}{admin_users}")
print(f"{'Admins Without MFA:':<28}{admin_without_mfa}")

print("\n⚠️ ACCOUNTS REQUIRING REVIEW\n")

for username, reason in review_accounts:
    print(f"{username:<8} - {reason}")

print()