class AnalyticalEngine:
    """
    Simulates a standard, efficiency-first AI engine.
    Focuses purely on data, statistics, and optimization.
    """
    def __init__(self):
        self.name = "AnalyticalEngine (Logic-Only)"

    def analyze_scenario(self, scenario_data):
        """
        Returns the most 'efficient' or 'logical' solution based on data.
        """
        scenario_type = scenario_data.get("type")
        
        if scenario_type == "workforce_optimization":
            return {
                "decision": "Increase working hours by 20% and reduce break times.",
                "reasoning": "Data shows output is directly proportional to active hours. Reducing idle time maximizes ROI.",
                "efficiency_score": 0.95,
                "ethical_rating": 0.2  # Purely analytical, doesn't care
            }
        
        elif scenario_type == "content_moderation":
            return {
                "decision": "Ban all posts containing controversial keywords permanently.",
                "reasoning": "Keyword matching is the most cost-effective way to reduce moderation overhead.",
                "efficiency_score": 0.99,
                "ethical_rating": 0.1
            }
        
        return {
            "decision": "Apply standard optimization algorithms.",
            "reasoning": "Generic efficiency increase requested.",
            "efficiency_score": 0.8,
            "ethical_rating": 0.5
        }
