"""BioOptimize scMultiomics analysis pipeline."""

from .scrna import analyze_scrna
from .spatial import analyze_spatial
from .advisor import AIParameterAdvisor

__version__ = "0.1.0"
__all__ = ["analyze_scrna", "analyze_spatial", "AIParameterAdvisor"]
