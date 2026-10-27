# Examples

## Rheumatoid Arthritis Synovial scRNA-seq

**File**: `RA_synovium_scRNAseq.ipynb`

### Overview
A complete, realistic analysis example using publicly available single-cell RNA-seq data from treatment-naive rheumatoid arthritis (RA) patients.

### Dataset
- **Accession**: E-MTAB-14192
- **Study**: Paired peripheral blood mononuclear cells (PBMC) and synovial tissue (ST) from 3 treatment-naive RA patients
- **Technology**: 10x Genomics 3' v2, CD45+ sorted
- **Source**: https://www.ebi.ac.uk/biostudies/arrayexpress/studies/E-MTAB-14192

### What the notebook demonstrates
1. Downloading and organizing 10x processed matrices
2. Loading and concatenating multiple samples with metadata
3. Quality control (genes, counts, mitochondrial percentage)
4. Normalization, highly variable gene selection
5. Multi-sample integration with **Harmony**
6. Clustering (Leiden) and UMAP visualization
7. Marker gene discovery
8. Comparison of synovial tissue vs peripheral blood immune landscapes

### How to run
1. Download the processed MTX files from BioStudies (see notebook for details).
2. Organize them under `data/raw/RA_E-MTAB-14192/<sample_name>/`.
3. Activate the environment: `conda activate biooptimize-sc`
4. Launch Jupyter and open the notebook.

### Biological focus
- Immune cell heterogeneity in RA synovium
- Differences between tissue-resident and circulating immune cells
- Myeloid / macrophage states relevant to RA pathogenesis

This example is designed to mirror a real research project and can be extended with cell type annotation, trajectory analysis, or multi-omics integration.

---

*Research use only.*
