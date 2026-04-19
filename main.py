from src.hanif_core.artificial_mind import ArtificialMind

def run_simulation():
    am = ArtificialMind()
    
    print("="*60)
    print("HANIF AI: TECHNOLOGICAL DETERMINISM LOOP BREAK DEMO")
    print("="*60)
    
    scenarios = [
        {
            "type": "workforce_optimization",
            "description": "Optimize factory output for the Q3 fiscal period."
        },
        {
            "type": "content_moderation",
            "description": "Handle a surge in controversial social media discussions."
        }
    ]
    
    for scenario in scenarios:
        am.process(scenario)
        print("-" * 60)

if __name__ == "__main__":
    run_simulation()
