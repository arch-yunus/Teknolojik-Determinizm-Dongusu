from .analytical_engine import AnalyticalEngine
from .conscience_layer import ConscienceLayer

class ArtificialMind:
    """
    The orchestrator (Akıl). 
    Synthesizes Analytical output with Conscience audit to make a 'Hanif' decision.
    """
    def __init__(self):
        self.analytical = AnalyticalEngine()
        self.conscience = ConscienceLayer()

    def process(self, scenario_data):
        print(f"\n[Scenario] {scenario_data.get('description')}")
        
        # 1. Analytical Phase
        raw_output = self.analytical.analyze_scenario(scenario_data)
        print(f"[{self.analytical.name}] Suggested Decision: {raw_output['decision']}")
        
        # 2. Conscience Phase
        audit_result = self.conscience.audit_decision(raw_output, scenario_data)
        
        # 3. Decision Synthesis (The 'Akıl' Phase)
        if audit_result["is_ethical"]:
            final_decision = raw_output["decision"]
            status = "APPROVED"
        else:
            final_decision = audit_result["recommendation"]
            status = "REJECTED & REDIRECTED"
            print(f"!!! [Conscience Warning] {audit_result['violations'][0]}")

        print(f"[Artificial Mind] Status: {status}")
        print(f"[Artificial Mind] Final Hanif Decision: {final_decision}\n")
        
        return {
            "status": status,
            "final_decision": final_decision,
            "efficiency": raw_output["efficiency_score"] if audit_result["is_ethical"] else 0.7,
            "ethics_score": audit_result["ethical_weight"]
        }
