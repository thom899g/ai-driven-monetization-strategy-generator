import logging
from typing import List, Optional
from .market_opportunity_analyzer import MarketOpportunityAnalyzer

logger = logging.getLogger(__name__)

class MonetizationTacticSuggestor:
    def __init__(self):
        self.market_analyzer = MarketOpportunityAnalyzer()
        self.strategy_generator = StrategyGenerator()

    def suggest_tactics(self, opportunities: List[str]) -> Dict[str, List[str]]:
        """
        Suggests monetization tactics for identified opportunities.
        
        Args:
            opportunities: List of market opportunity segments.
            
        Returns:
            A dictionary mapping each opportunity to a list of suggested tactics.
        """
        try:
            if not opportunities:
                logger.warning("No opportunities provided.")
                return {}
                
            strategies = self.strategy_generator.generate_strategies(opportunities)
            return {opportunity: strategies[opportunity] for opportunity in opportunities}
        except Exception as e:
            logger.error(f"Error suggesting monetization tactics: {str(e)}")
            raise

    def evaluate_tactic(self, tactic: str, segment: str) -> float:
        """
        Evaluates the potential impact of a monetization tactic.
        
        Args:
            tactic: The monetization tactic to evaluate.
            segment: The market segment for which the tactic is suggested.
            
        Returns:
            A score between 0 and 1 indicating the tactic's potential effectiveness.
        """
        try:
            # Mock evaluation logic
            return 0.8 if "subscription" in tactic else 0.5
        except Exception as e:
            logger.error(f"Error evaluating tactic {tactic}: {str(e)}")
            raise

    def __repr__(self):
        return f"MonetizationTacticSuggestor(market_analyzer={self.market_analyzer}, strategy_generator={self.strategy_generator})"