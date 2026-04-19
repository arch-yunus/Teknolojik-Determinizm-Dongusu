import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.text import Text
from src.hanif_core.artificial_mind import ArtificialMind

console = Console()

def run_simulation():
    am = ArtificialMind()
    
    console.print(Panel.fit(
        "[bold cyan]HANIF AI: BREAKING THE TECHNOLOGICAL DETERMINISM LOOP[/bold cyan]\n"
        "[dim]Conceptual Prototype v1.0[/dim]",
        border_style="blue"
    ))
    
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
        console.print(f"\n[bold yellow]>>> INPUT SCENARIO:[/bold yellow] [white]{scenario['description']}[/white]")
        
        with console.status("[bold cyan]Synthesizing...[/bold cyan]") as status:
            time.sleep(1)
            result = am.process(scenario)
        
        # Decision Synthesis Table
        table = Table(show_header=True, header_style="bold magenta", box=None)
        table.add_column("Layer", style="cyan")
        table.add_column("Action / Status", style="white")
        
        # Re-evaluating results for display
        status_color = "green" if "APPROVED" in result["status"] else "red"
        
        table.add_row("Analytical Engine", "Optimizing for ROI/Speed...")
        table.add_row("Conscience Layer", f"[{status_color}]Auditing against Fıtrat Principles...[/{status_color}]")
        table.add_row("Artificial Mind", f"[{status_color}]{result['status']}[/{status_color}]")
        
        console.print(Panel(table, title="Synthesis Log", border_style="cyan"))
        
        console.print(f"\n[bold white]FINAL HANIF DECISION:[/bold white]")
        console.print(f"[bold {status_color}]{result['final_decision']}[/bold {status_color}]")
        console.print("-" * 50)
        time.sleep(1)

if __name__ == "__main__":
    run_simulation()
