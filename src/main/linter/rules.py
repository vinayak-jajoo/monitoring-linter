import re
import json
import os


class RuleEngine:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        self.service_names = set()
        self.rules = self.load_rules()

    def load_rules(self):
        path = os.path.join(os.path.dirname(__file__), "rules_config.json")
        with open(path, "r") as f:
            return json.load(f)

    def run_nagios_config(self, content):
        services = re.findall(r'define service\s*{([^}]*)}', content, re.DOTALL)

        if not services:
            self.errors.append("No service definitions found")

        for service in services:
            self.check_service(service)

        return self.errors, self.warnings, self.info

    def check_service(self, block):
        fields = {
            "host_name": self.extract(block, "host_name"),
            "service_description": self.extract(block, "service_description"),
            "check_command": self.extract(block, "check_command"),
        }

        # Required fields
        for field in self.rules["required_fields"]:
            if not fields.get(field):
                self.errors.append(f"Missing {field}")

        desc = fields["service_description"]
        cmd = fields["check_command"]

        # Duplicate check
        if self.rules["enable_duplicate_check"] and desc:
            if desc in self.service_names:
                self.warnings.append(f"Duplicate service: {desc}")
            self.service_names.add(desc)

        # Naming rule
        if desc and not re.match(self.rules["naming_regex"], desc):
            self.warnings.append(f"{desc}: Invalid naming")

        # Command rule
        if cmd and not cmd.startswith(self.rules["command_prefix"]):
            self.warnings.append(f"{desc}: Invalid command format")

        # Info detection
        if cmd:
            if "cpu" in cmd.lower():
                self.info.append(f"{desc}: CPU monitoring configured")
            if "memory" in cmd.lower():
                self.info.append(f"{desc}: Memory monitoring configured")

    def extract(self, block, field):
        match = re.search(rf'{field}\s+(.+)', block)
        return match.group(1).strip() if match else None