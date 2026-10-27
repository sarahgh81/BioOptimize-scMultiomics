# BioOptimize scMultiomics Overview

This repository demonstrates **proven experience** analyzing modern single-cell and spatial genomic data.

## Modalities Covered

### scRNA-seq
- STARsolo / Alevin quantification interfaces
- Scanpy end-to-end workflow
- Multi-sample integration (Harmony, scVI, BBKNN)
- Clustering, marker genes, trajectory-ready outputs

### scATAC-seq
- Peak calling and tile matrix construction
- Motif analysis and gene activity scoring
- Integration with RNA-seq (gene activity ↔ expression)
- Tools: ArchR, Signac, SnapATAC patterns

### Spatial RNA-seq
- Visium / Slide-seq / other spatial formats
- Spatial graph construction (Squidpy)
- Neighborhood enrichment and spatial domains
- Ligand-receptor and cell-cell communication patterns

### Multi-omics Integration
- RNA + ATAC joint analysis
- Weighted nearest neighbor (WNN) style approaches
- Muon / multi-modal AnnData handling
- Cross-modality batch correction

## Design Principles

1. **Transparency** — clear parameter choices and method comparisons
2. **Modularity** — each modality is self-contained yet integrable
3. **Reproducibility** — conda environments, config-driven, versioned
4. **Education** — well-documented code suitable for teaching and portfolios
5. **AI Assistance** — parameter advisor that explains recommendations

## Typical Workflow

```
Raw data → Quantification → QC → Normalization → Integration → Embedding → Clustering → Interpretation
```

For multi-omics:
```
RNA + ATAC → Individual processing → Joint embedding → Shared clusters → Cross-modal validation
```

See modality-specific guides in the `docs/` folder for detailed examples.
