import re

class RuleEngine:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        self.alert_names = set()

    def run(self, data):
        groups = data.get("groups", [])

        for group in groups:
            for rule in group.get("rules", []):
                self.check_rule(rule)

        return self.errors, self.warnings, self.info

    def check_rule(self, rule):
        name = rule.get("alert")

        if not name:
            self.errors.append("Missing alert name")
            return

        # Duplicate check
        if name in self.alert_names:
            self.warnings.append(f"Duplicate alert: {name}")
        self.alert_names.add(name)

        # Labels & annotations
        labels = rule.get("labels", {})
        annotations = rule.get("annotations", {})

        if "severity" not in labels:
            self.errors.append(f"{name}: Missing severity")

        if "description" not in annotations:
            self.info.append(f"{name}: Missing description")

        if "runbook" not in annotations:
            self.info.append(f"{name}: Missing runbook")

        # Naming convention
        if not re.match(r'^[A-Z][a-zA-Z0-9]+$', name):
            self.warnings.append(f"{name}: Not CamelCase")

        # Threshold check
        expr = rule.get("expr", "")
        match = re.search(r'>\s*(\d+)', expr)
        if match and int(match.group(1)) > 90:
            self.warnings.append(f"{name}: Threshold too high")