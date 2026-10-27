"""AI-assisted parameter recommendations for single-cell multi-omics."""

from typing import Dict, Any

class AIParameterAdvisor:
    """Suggests analysis parameters based on assay type and basic metadata."""

    def suggest(
        self,
        assay: str = "scrna",
        n_cells: int = 5000,
        n_samples: int = 1,
        species: str = "human",
    ) -> Dict[str, Any]:
        recommendations = {
            "scrna": {
                "integration": "harmony" if n_samples > 1 else "none",
                "resolution": 0.5 if n_cells < 10000 else 0.6,
                "n_pcs": 30,
                "notes": "Harmony recommended for multi-sample. Consider scVI for complex batch effects.",
            },
            "scatac": {
                "peak_calling": True,
                "tile_size": 500,
                "notes": "ArchR or Signac recommended. Gene activity scores useful for integration with RNA.",
            },
            "spatial": {
                "n_neighs": 6,
                "resolution": 0.4,
                "notes": "Squidpy spatial neighbors + neighborhood enrichment. Adjust n_neighs based on tissue density.",
            },
            "multiomics": {
                "method": "muon" if n_samples > 1 else "seurat_wnn",
                "notes": "Joint embedding preferred when both modalities available on same cells.",
            },
        }
        return recommendations.get(assay, {"notes": "Specify assay: scrna, scatac, spatial, or multiomics"})

    def pretty(self, recs: Dict[str, Any]) -> str:
        lines = ["AI Parameter Recommendations:"]
        for k, v in recs.items():
            lines.append(f"  {k}: {v}")
        return "\n".join(lines)
