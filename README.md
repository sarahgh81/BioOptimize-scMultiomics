# BioOptimize scMultiomics 🧬🔬

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/sarahgh81/BioOptimize-scMultiomics)](https://github.com/sarahgh81/BioOptimize-scMultiomics/stargazers)

**Proven experience analyzing single-cell multi-omics data: scRNA-seq, scATAC-seq, spatial transcriptomics, and integrated workflows.**

Part of the BioOptimize AI ecosystem — turning complex genomic data into clear, reproducible insights.

## Why This Repository?

This project demonstrates practical, production-oriented analysis of modern single-cell and spatial genomic data. It showcases:

- End-to-end pipelines for multiple modalities
- Multi-sample and multi-omics integration
- Transparent, educational code structure
- AI-assisted parameter guidance
- Reproducible environments and documentation
- **Real disease example**: Rheumatoid arthritis synovial scRNA-seq analysis

Ideal for research portfolios, collaborations, and teaching advanced single-cell methods.

## Supported Modalities

| Modality | Key Tools | Capabilities |
|----------|-----------|--------------|
| **scRNA-seq** | Scanpy, STARsolo, Harmony | QC, clustering, integration, markers |
| **scATAC-seq** | ArchR, Signac, SnapATAC | Peak calling, motif analysis, gene activity |
| **Spatial RNA-seq** | Squidpy, Scanpy | Spatial domains, neighborhood analysis |
| **Multi-omics** | Muon, Seurat WNN, Harmony | Joint embedding, cross-modality integration |

## Key Features

- Modular analysis pipelines (Python + R bridges where useful)
- Batch correction & multi-sample integration (Harmony, scVI, BBKNN)
- Spatial domain detection and ligand-receptor analysis
- AI Parameter Advisor for assay-specific recommendations
- Conda environment with full dependency stack
- Example notebooks and configuration-driven workflows
- CI-ready structure and comprehensive documentation

## Quick Start

```bash
git clone https://github.com/sarahgh81/BioOptimize-scMultiomics.git
cd BioOptimize-scMultiomics
conda env create -f environment.yml
conda activate biooptimize-sc
pip install -e .
```

### Example: scRNA-seq with Harmony integration
```python
from pipeline.scrna import analyze_scrna

result = analyze_scrna(
    adata_path="data/combined.h5ad",
    batch_key="sample",
    integration="harmony",
    resolution=0.6,
)
```

## Real Experiment Example

**Rheumatoid Arthritis (RA) Synovial Tissue Analysis**  
See [examples/RA_synovium_scRNAseq.ipynb](examples/RA_synovium_scRNAseq.ipynb) for a complete, realistic project using public data (E-MTAB-14192):

- Paired blood and synovial tissue from treatment-naive RA patients
- Multi-sample loading, QC, Harmony integration
- Clustering, marker genes, and tissue comparison
- Focus on immune cell heterogeneity relevant to RA pathogenesis

## Project Structure

```
BioOptimize-scMultiomics/
├── pipeline/
│   ├── scrna.py          # scRNA-seq analysis
│   ├── scatac.py         # scATAC-seq workflows
│   ├── spatial.py        # Spatial transcriptomics
│   ├── multiomics.py     # Integration layer
│   └── advisor.py        # AI recommendations
├── config/
├── examples/             # Includes RA analysis notebook
├── docs/
├── tests/
├── environment.yml
└── README.md
```

## Documentation

- [scRNA-seq Guide](docs/SCRNA.md)
- [scATAC-seq Guide](docs/SCATAC.md)
- [Spatial Analysis](docs/SPATIAL.md)
- [Multi-omics Integration](docs/MULTIOMICS.md)
- [Examples](examples/README.md)

## Citation

```bibtex
@software{BioOptimize_scMultiomics,
  author = {Ghasemi, Sarah},
  title = {BioOptimize scMultiomics: Analysis Framework for Single-Cell and Spatial Genomics},
  year = {2026},
  url = {https://github.com/sarahgh81/BioOptimize-scMultiomics}
}
```

## Related Projects

- [BioOptimize-mRNAseq](https://github.com/sarahgh81/BioOptimize-mRNAseq) — Bulk + single-cell RNA-seq pipeline
- BioOptimize AI — Full molecular biology workspace

## Contributing

PRs and issues welcome. Please open an issue for major changes. Research use only.

---

**Built for researchers who want clarity and reproducibility in single-cell genomics.**

> For Research Use Only. Not for diagnostic or clinical decision-making.
