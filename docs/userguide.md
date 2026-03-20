# User Guide

## 1. Introduction

This guide explains how to use the Monitoring as Code Linter to validate Nagios configuration files.

---

## 2. Prerequisites

- Python installed
- Git installed
- Basic knowledge of Nagios configurations

---

## 3. Setup

### Clone Repository

```
git clone https://github.com/your-username/monitoring-linter.git
cd monitoring-linter
```

### Create Virtual Environment

```
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```
pip install -r requirements.txt
```

---

## 4. Running the Linter

```
python -m src.main.linter.main monitoring/nagios/services.cfg
```

---

## 5. Understanding Output

### Errors

Critical issues that must be fixed.

### Warnings

Non-critical issues or best practice violations.

### Info

Additional insights about configuration.

---

## 6. CI/CD Usage

- Push code to GitHub
- GitHub Actions automatically runs the linter
- Pipeline fails if errors are detected

---

## 7. Test Cases

Located in:

```
monitoring/nagios/testcases/
```

Use these files to test:

- Valid configurations
- Invalid configurations
- Duplicate services

---

## 8. Troubleshooting

| Issue            | Solution                     |
| ---------------- | ---------------------------- |
| Module not found | Activate virtual environment |
| File not found   | Check file path              |
| CI/CD failure    | Fix configuration errors     |

---

## 9. Best Practices

- Always validate before deployment
- Use meaningful service names
- Follow Nagios conventions
