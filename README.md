# Monitoring as Code Linter (Nagios-Based)

## Overview

This project implements a **Monitoring as Code Linter** designed to validate Nagios configuration files before deployment. It ensures that monitoring configurations are correct, consistent, and production-ready.

The system integrates:

* Nagios configuration validation
* Rule-based linting engine
* Puppet-based deployment structure
* CI/CD automation using GitHub Actions

---

## Objectives

* Validate Nagios monitoring configurations
* Detect errors, warnings, and misconfigurations
* Prevent faulty configurations from being deployed
* Automate validation using CI/CD pipelines
* Demonstrate DevOps practices using Puppet and GitHub Actions

---

## Project Structure

```
monitoring-linter/
│
├── .github/workflows/        # CI/CD pipeline
├── docs/                     # Documentation files
├── infrastructure/puppet/    # Puppet modules for deployment
├── monitoring/nagios/        # Nagios configs and test cases
├── src/main/linter/          # Core linter implementation
├── tests/                    # Test files
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Features

* Rule-based validation of Nagios service configurations
* Detection of:

  * Missing required fields
  * Duplicate services
  * Invalid naming conventions
  * Incorrect command formats
* Informational insights (CPU, memory monitoring detection)
* CI/CD integration for automated validation
* Puppet module for configuration deployment

---

## Technologies Used

* Python
* Nagios (Monitoring)
* Puppet (Configuration Management)
* GitHub Actions (CI/CD)
* JSON (Rule configuration)

---

## How It Works

1. User writes Nagios configuration (`services.cfg`)
2. Linter parses and validates configuration
3. Errors and warnings are generated
4. CI/CD pipeline automatically runs on every push
5. Invalid configurations fail the pipeline
6. Valid configurations are ready for deployment via Puppet

---

## Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/monitoring-linter.git
cd monitoring-linter
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## Usage

Run the linter on a Nagios configuration file:

```
python -m src.main.linter.main monitoring/nagios/services.cfg
```

---

## Example Output

```
--- LINT REPORT ---

ERRORS:
 - Missing host_name

WARNINGS:
 - CPU Load: Invalid naming

-------------------
```

---

## CI/CD Integration

The project uses GitHub Actions to automate validation:

* Runs on every push to main branch
* Executes the linter
* Fails if errors are detected
* Ensures only valid configurations are accepted

---

## Puppet Integration

Puppet is used to deploy monitoring configurations:

* Modular structure
* Deploys `services.cfg` to target systems
* Ensures consistency across environments

---

## Test Cases

Located in:

```
monitoring/nagios/testcases/
```

Includes:

* Valid configuration
* Invalid configuration
* Duplicate service cases

---

## Future Improvements

* Support for multiple configuration files
* Integration with real Nagios server
* Advanced rule customization
* Web interface for linting

---

## Conclusion

This project demonstrates a complete DevOps workflow by integrating monitoring, validation, deployment, and automation. It ensures reliable monitoring configurations and reduces operational risks.

---

## Author

Vinayak Jajoo

---
