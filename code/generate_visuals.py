#!/usr/bin/env python3
"""
Livadance ENS Grant Proposal - Visual Generator
Generates charts, diagrams, and visual aids for the grant proposal
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np
from datetime import datetime, timedelta
import seaborn as sns

# Set style for better-looking charts
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class ProposalVisuals:
    def __init__(self):
        self.colors = {
            'primary': '#FF6B6B',      # Latin dance red
            'secondary': '#4ECDC4',    # Teal
            'accent': '#45B7D1',       # Blue
            'success': '#96CEB4',      # Green
            'warning': '#FFEAA7',      # Yellow
            'dark': '#2D3436'          # Dark gray
        }
        
    def create_budget_chart(self, save_path='visuals/budget_breakdown.png'):
        """Create a pie chart showing budget allocation"""
        categories = ['Event Logistics', 'Instructor Fees', 'ENS Onboarding', 
                     'Marketing & Outreach', 'Administrative', 'Contingency']
        amounts = [6000, 3000, 2250, 2250, 1500, 1500]
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Create pie chart
        wedges, texts, autotexts = ax.pie(amounts, labels=categories, 
                                         autopct='%1.1f%%', startangle=90,
                                         colors=[self.colors['primary'], self.colors['secondary'],
                                                self.colors['accent'], self.colors['success'],
                                                self.colors['warning'], self.colors['dark']])
        
        # Customize text
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.set_title('Budget Allocation - 15,000 USDC', fontsize=16, fontweight='bold', pad=20)
        
        # Add total amount
        plt.figtext(0.5, 0.02, f'Total Budget: 15,000 USDC', 
                   ha='center', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Budget chart saved to {save_path}")
        
    def create_timeline_chart(self, save_path='visuals/project_timeline.png'):
        """Create a Gantt chart showing project timeline"""
        fig, ax = plt.subplots(figsize=(16, 10))
        
        # Define phases and their durations
        phases = [
            ('Month 1: Planning & Foundation', 4, 0),
            ('Month 2: First Events & Learning', 4, 4),
            ('Month 3: Scaling & Optimization', 4, 8),
            ('Month 4: Expansion & Growth', 4, 12),
            ('Month 5: Evaluation & Reporting', 4, 16)
        ]
        
        # Define key milestones
        milestones = [
            ('Team Assembly', 1, 0),
            ('Partnerships Secured', 2, 0),
            ('First Event', 6, 0),
            ('4 Events Complete', 12, 0),
            ('Novi Sad Expansion', 15, 0),
            ('Project Closure', 20, 0)
        ]
        
        # Create Gantt bars
        y_positions = list(range(len(phases)))
        for i, (phase, duration, start) in enumerate(phases):
            ax.barh(i, duration, left=start, height=0.6, 
                   color=self.colors['primary'], alpha=0.8, edgecolor='white')
            
            # Add phase labels
            ax.text(start + duration/2, i, phase, ha='center', va='center',
                   fontweight='bold', color='white', fontsize=10)
        
        # Add milestone markers
        for milestone, week, y_offset in milestones:
            ax.scatter(week, y_offset, s=200, color=self.colors['warning'], 
                      marker='*', edgecolor='white', linewidth=2, zorder=5)
            ax.annotate(milestone, (week, y_offset + 0.3), ha='center', 
                       fontsize=9, fontweight='bold', color=self.colors['dark'])
        
        # Customize chart
        ax.set_xlim(0, 20)
        ax.set_ylim(-0.5, len(phases) - 0.5)
        ax.set_xlabel('Weeks', fontsize=12, fontweight='bold')
        ax.set_title('Project Timeline - 5 Months (20 Weeks)', 
                    fontsize=16, fontweight='bold', pad=20)
        
        # Set x-axis ticks
        ax.set_xticks(range(0, 21, 2))
        ax.set_xticklabels([f'Week {i}' for i in range(0, 21, 2)])
        
        # Remove y-axis labels
        ax.set_yticks([])
        
        # Add grid
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Timeline chart saved to {save_path}")
        
    def create_participant_flow(self, save_path='visuals/participant_flow.png'):
        """Create a flow diagram showing participant journey"""
        fig, ax = plt.subplots(figsize=(14, 10))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        
        # Define flow stages
        stages = [
            ('Registration', 1, 8, 2, 1),
            ('Pre-Event\nEmail', 3, 8, 2, 1),
            ('Event Day\n(Dance)', 5, 8, 2, 1),
            ('ENS\nIntroduction', 7, 8, 2, 1),
            ('Hands-on\nOnboarding', 9, 8, 2, 1),
            ('Post-Event\nSupport', 5, 6, 2, 1),
            ('Community\nIntegration', 5, 4, 2, 1),
            ('Ongoing\nUsage', 5, 2, 2, 1)
        ]
        
        # Draw stage boxes
        for stage, x, y, w, h in stages:
            box = FancyBboxPatch((x-w/2, y-h/2), w, h, 
                                boxstyle="round,pad=0.1", 
                                facecolor=self.colors['primary'], 
                                edgecolor='white', linewidth=2)
            ax.add_patch(box)
            
            # Add stage text
            ax.text(x, y, stage, ha='center', va='center', 
                   fontweight='bold', color='white', fontsize=9)
        
        # Draw flow arrows
        arrows = [
            ((2, 8), (2, 8)),      # Registration to Pre-Event
            ((4, 8), (4, 8)),      # Pre-Event to Event Day
            ((6, 8), (6, 8)),      # Event Day to ENS Intro
            ((8, 8), (8, 8)),      # ENS Intro to Onboarding
            ((9, 7), (6, 7)),      # Onboarding to Post-Event
            ((6, 5), (6, 5)),      # Post-Event to Community
            ((6, 3), (6, 3))       # Community to Ongoing
        ]
        
        for start, end in arrows:
            ax.annotate('', xy=end, xytext=start,
                       arrowprops=dict(arrowstyle='->', lw=2, color=self.colors['dark']))
        
        # Add success metrics
        metrics = [
            ('200-300\nParticipants', 8, 6),
            ('150+ ENS\nSubdomains', 8, 4),
            ('80% Retention\nRate', 8, 2)
        ]
        
        for metric, x, y in metrics:
            ax.text(x, y, metric, ha='center', va='center', 
                   fontweight='bold', color=self.colors['dark'], fontsize=10,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor=self.colors['warning'], alpha=0.7))
        
        ax.set_title('Participant Journey & Success Metrics', 
                    fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Participant flow diagram saved to {save_path}")
        
    def create_risk_matrix(self, save_path='visuals/risk_matrix.png'):
        """Create a risk assessment matrix"""
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Define risks with probability and impact scores (1-5)
        risks = [
            ('Low Participant\nTurnout', 3, 4, 'Targeted marketing,\npartnerships'),
            ('Technical\nDifficulties', 2, 3, 'Backup materials,\nsupport staff'),
            ('Regulatory\nChanges', 2, 3, 'Legal consultation,\ncompliance'),
            ('Budget\nOverruns', 2, 3, 'Regular reviews,\ncontingency fund'),
            ('Instructor\nAvailability', 3, 3, 'Multiple contracts,\nbackup plans')
        ]
        
        # Create risk matrix
        for risk, prob, impact, mitigation in risks:
            # Calculate risk score
            risk_score = prob * impact
            
            # Determine color based on risk level
            if risk_score >= 12:
                color = self.colors['primary']  # High risk
            elif risk_score >= 8:
                color = self.colors['warning']  # Medium risk
            else:
                color = self.colors['success']  # Low risk
            
            # Plot risk point
            ax.scatter(prob, impact, s=risk_score*100, color=color, alpha=0.7, edgecolor='white')
            
            # Add risk label
            ax.annotate(risk, (prob, impact), xytext=(5, 5), textcoords='offset points',
                       fontsize=9, fontweight='bold', ha='left')
            
            # Add mitigation strategy
            ax.annotate(f'Mitigation:\n{mitigation}', (prob, impact), 
                       xytext=(0, -20), textcoords='offset points',
                       fontsize=8, ha='center', va='top',
                       bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
        
        # Customize chart
        ax.set_xlim(0.5, 5.5)
        ax.set_ylim(0.5, 5.5)
        ax.set_xlabel('Probability (1=Low, 5=High)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Impact (1=Low, 5=High)', fontsize=12, fontweight='bold')
        ax.set_title('Risk Assessment Matrix', fontsize=16, fontweight='bold', pad=20)
        
        # Add grid
        ax.grid(True, alpha=0.3)
        ax.set_xticks(range(1, 6))
        ax.set_yticks(range(1, 6))
        
        # Add legend
        legend_elements = [
            plt.scatter([], [], s=100, color=self.colors['success'], label='Low Risk (1-7)'),
            plt.scatter([], [], s=100, color=self.colors['warning'], label='Medium Risk (8-11)'),
            plt.scatter([], [], s=100, color=self.colors['primary'], label='High Risk (12+)')
        ]
        ax.legend(handles=legend_elements, loc='upper right')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"Risk matrix saved to {save_path}")
        
    def create_ens_onboarding_flow(self, save_path='visuals/ens_onboarding_flow.png'):
        """Create a detailed ENS onboarding flow diagram"""
        fig, ax = plt.subplots(figsize=(16, 12))
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 12)
        
        # Define onboarding steps
        steps = [
            ('Pre-Event\nRegistration', 2, 10, 3, 1.5),
            ('Welcome\nPackage', 6, 10, 3, 1.5),
            ('Dance\nInstruction', 10, 10, 3, 1.5),
            ('ENS\nIntroduction', 14, 10, 3, 1.5),
            ('Wallet\nSetup', 2, 7, 3, 1.5),
            ('Subdomain\nClaiming', 6, 7, 3, 1.5),
            ('Integration\n& Testing', 10, 7, 3, 1.5),
            ('Post-Event\nSupport', 14, 7, 3, 1.5),
            ('Community\nAccess', 8, 4, 3, 1.5),
            ('Ongoing\nUsage', 8, 1, 3, 1.5)
        ]
        
        # Draw step boxes
        for step, x, y, w, h in steps:
            box = FancyBboxPatch((x-w/2, y-h/2), w, h, 
                                boxstyle="round,pad=0.1", 
                                facecolor=self.colors['secondary'], 
                                edgecolor='white', linewidth=2)
            ax.add_patch(box)
            
            # Add step text
            ax.text(x, y, step, ha='center', va='center', 
                   fontweight='bold', color='white', fontsize=9)
        
        # Draw flow arrows
        arrows = [
            ((3.5, 10), (4.5, 10)),      # Registration to Welcome
            ((7.5, 10), (8.5, 10)),      # Welcome to Dance
            ((11.5, 10), (12.5, 10)),    # Dance to ENS Intro
            ((2, 9.25), (2, 8.5)),       # Registration to Wallet
            ((6, 9.25), (6, 8.5)),       # Welcome to Subdomain
            ((10, 9.25), (10, 8.5)),     # Dance to Integration
            ((14, 9.25), (14, 8.5)),     # ENS Intro to Support
            ((3.5, 7), (4.5, 7)),        # Wallet to Subdomain
            ((7.5, 7), (8.5, 7)),        # Subdomain to Integration
            ((11.5, 7), (12.5, 7)),      # Integration to Support
            ((8, 5.5), (8, 5)),          # Integration to Community
            ((8, 2.5), (8, 2))           # Community to Ongoing
        ]
        
        for start, end in arrows:
            ax.annotate('', xy=end, xytext=start,
                       arrowprops=dict(arrowstyle='->', lw=2, color=self.colors['dark']))
        
        # Add time indicators
        time_labels = [
            ('Hour 1', 10, 11.5),
            ('Hour 2', 14, 11.5),
            ('Hour 3', 6, 5.5),
            ('Post-Event', 14, 5.5)
        ]
        
        for label, x, y in time_labels:
            ax.text(x, y, label, ha='center', va='center', 
                   fontweight='bold', color=self.colors['primary'], fontsize=10,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
        
        # Add success indicators
        success_metrics = [
            ('100% Wallet\nCreation', 2, 5.5),
            ('80%+ Subdomain\nClaims', 6, 5.5),
            ('ENS Integration\nSuccess', 10, 5.5),
            ('Community\nEngagement', 8, 2.5)
        ]
        
        for metric, x, y in success_metrics:
            ax.text(x, y, metric, ha='center', va='center', 
                   fontweight='bold', color=self.colors['success'], fontsize=8,
                   bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.7))
        
        ax.set_title('ENS Onboarding Flow - 3-Hour Workshop Structure', 
                    fontsize=16, fontweight='bold', pad=20)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
        print(f"ENS onboarding flow saved to {save_path}")
        
    def generate_all_visuals(self):
        """Generate all visual materials for the proposal"""
        print("Generating all visual materials for Livadance ENS Grant Proposal...")
        
        # Create visuals directory if it doesn't exist
        import os
        os.makedirs('visuals', exist_ok=True)
        
        # Generate all charts
        self.create_budget_chart()
        self.create_timeline_chart()
        self.create_participant_flow()
        self.create_risk_matrix()
        self.create_ens_onboarding_flow()
        
        print("\nAll visual materials generated successfully!")
        print("Files saved in the 'visuals' directory:")
        print("- budget_breakdown.png")
        print("- project_timeline.png")
        print("- participant_flow.png")
        print("- risk_matrix.png")
        print("- ens_onboarding_flow.png")

def main():
    """Main function to generate all visuals"""
    visual_generator = ProposalVisuals()
    visual_generator.generate_all_visuals()

if __name__ == "__main__":
    main()
