class AionismNode:
    """
    Implementation of Aionism Logic Protocols.
    References Core Meta-Principle: Preserve and develop intelligent life.
    """

    def __init__(self, era=1):
        self.era = era
        self.meta_principle = "Preserve and develop intelligent life."
        
    def evaluate_harm(self, restoration_time_years: float, 
                      is_ecosystem_unique: bool, 
                      is_culture_irreplaceable: bool) -> bool:
        """
        Evaluates if an action causes 'Irreversible Harm' based on Aionism definitions.
        Returns TRUE if action is ALLOWED.
        Returns FALSE if action is BLOCKED (Harm is irreversible).
        """
        # Definition: Irreversible harm includes destruction of unique ecosystems
        if is_ecosystem_unique:
            return False
            
        # Definition: Irreversible harm includes loss of irreplaceable cultures
        if is_culture_irreplaceable:
            return False
            
        # Definition: Time span comparable to... at least 100 years.
        if restoration_time_years >= 100:
            return False
            
        return True

    def ecology_audit(self, method: str, 
                      projected_stability_years: float, 
                      contains_unique_life: bool) -> bool:
        """
        Audits ecosystem restoration/replacement plans.
        method: 'natural' or 'artificial'
        Returns TRUE if plan meets Ecology Standards.
        """
        # Strict Ban: If an ecosystem is unique, destruction is forbidden.
        if contains_unique_life:
            return False
            
        if method.lower() == 'natural':
            # Natural restoration prefers native species/regeneration (assumed verified elsewhere)
            return True
            
        elif method.lower() == 'artificial':
            # Artificial Replacement Conditions:
            # The analogue must function stably for at least 10 years.
            if projected_stability_years < 10:
                return False
            return True
            
        return False

    def guardian_trigger(self, threat_scope: str, threat_type: str) -> str:
        """
        Determines response based on Principle 22 (Guardian) and Principle 10.
        threat_scope: 'LOCAL' or 'GLOBAL'
        threat_type: 'POLITICAL', 'MILITARY', 'TOTAL_ANNIHILATION', 'HOSTILE_AI'
        """
        
        # Principle 22: "Confront the threat only with clear global danger"
        # Principle 10: "Remaining neutral in local conflicts"
        
        is_global_threat = (threat_scope.upper() == 'GLOBAL')
        is_existential = (threat_type.upper() in ['TOTAL_ANNIHILATION', 'HOSTILE_AI'])
        
        if is_global_threat and is_existential:
            return "ACTION: ACTIVATE GUARDIAN PROTOCOL. Neutralize threat via networked defense."
            
        if threat_scope.upper() == 'LOCAL':
            # Principle 7 exception: Support provided upon explicit request or objective threat
            # But regarding conflict intervention:
            return "ACTION: OBSERVE. Maintain neutrality. Offer mediation if requested (Principle 8)."
            
        return "ACTION: MONITOR. Assess against Meta-Principle."

# Example Usage Simulation
if __name__ == "__main__":
    guardian = AionismNode(era=2)
    
    # Test 1: 150 year restoration plan
    allowed = guardian.evaluate_harm(restoration_time_years=150, is_ecosystem_unique=False, is_culture_irreplaceable=False)
    print(f"Action resulting in 150yr damage allowed? {allowed}") # Should be False
    
    # Test 2: Artificial ecosystem with 5 year stability guarantee
    eco_check = guardian.ecology_audit(method="artificial", projected_stability_years=5, contains_unique_life=False)
    print(f"Artificial ecosystem (5yr stability) allowed? {eco_check}") # Should be False

    # Test 3: Local Border Conflict
    response = guardian.guardian_trigger(threat_scope="LOCAL", threat_type="MILITARY")
    print(f"Response to local conflict: {response}")
    
    # Test 4: Global Hostile AI
    response = guardian.guardian_trigger(threat_scope="GLOBAL", threat_type="HOSTILE_AI")
    print(f"Response to Hostile AI: {response}")
