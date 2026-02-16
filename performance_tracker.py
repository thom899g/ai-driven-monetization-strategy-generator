import logging
from typing import Dict, Optional
from datetime import datetime
import threading

logger = logging.getLogger(__name__)

class PerformanceTracker:
    def __init__(self):
        self.performance_data = {}
        self.is_tracking = False

    def start_tracking(self) -> None:
        """
        Starts the performance tracking process.
        
        Runs in a background thread to continuously log metrics.
        """
        try:
            if self.is_tracking:
                logger.info("Performance tracking is already running.")
                return
                
            self.is_tracking = True
            track_thread = threading.Thread(target=self._track_performance)
            track_thread.daemon = True
            track_thread.start()
            logger.info("Started performance tracking.")
        except Exception as e