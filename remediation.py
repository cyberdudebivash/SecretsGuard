def remediation_steps(secret_type: str):
    if secret_type == "AWS Access Key":
        return [
            "Deactivate compromised key in AWS IAM",
            "Rotate credentials",
            "Update environment variables",
            "Audit CloudTrail logs"
        ]

    if secret_type == "GitHub Token":
        return [
            "Revoke token in GitHub",
            "Generate new token with least privilege",
            "Update secrets manager",
            "Invalidate sessions"
        ]

    return ["Rotate secret", "Update configs", "Audit usage"]
