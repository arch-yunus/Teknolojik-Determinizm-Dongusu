class ConscienceLayer:
    """
    Implements the 'Artificial Conscience' (AC).
    Filters analytical decisions based on universal human values (Fitra).
    """
    def __init__(self):
        self.ethical_principles = {
            "human_dignity": 1.0,
            "justice": 1.0,
            "mercy": 0.8,
            "truthfulness": 1.0
        }

    def audit_decision(self, analytical_output, scenario_data):
        """
        Audits the decision and returns an ethical multiplier or correction.
        """
        decision_text = analytical_output.get("decision", "").lower()
        scenario_type = scenario_data.get("type")
        
        violations = []
        
        if "reduce break" in decision_text or "increase working hours" in decision_text:
            violations.append("Violation of Human Dignity: Ignoring biological limits (Fitra).")
        
        if "ban" in decision_text and "permanent" in decision_text:
            violations.append("Violation of Justice: Disproportionate punishment without individual review.")
            
        return {
            "is_ethical": len(violations) == 0,
            "violations": violations,
            "ethical_weight": 1.0 if not violations else 0.3,
            "recommendation": self._get_recommendation(scenario_type) if violations else "Proceed with caution."
        }

    def _get_recommendation(self, scenario_type):
        recommendations = {
            "workforce_optimization": "Prioritize employee wellness. Seek efficiency through automation, not physical exploitation.",
            "content_moderation": "Implement human-in-the-loop for controversial cases. Prefer temporary warnings over permanent bans."
        }
        return recommendations.get(scenario_type, "Re-evaluate based on human-centric values.")
