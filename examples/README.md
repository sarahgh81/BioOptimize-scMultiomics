# Examples

## 1. Rheumatoid Arthritis Synovial Tissue scRNA-seq

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

### Biological focus
- Immune cell heterogeneity in RA synovium
- Differences between tissue-resident and circulating immune cells
- Myeloid / macrophage states relevant to RA pathogenesis

---

## 2. Rheumatoid Arthritis Synovial Fluid: Pre- vs Post-Treatment

**File**: `RA_synovial_fluid_treatment.ipynb`

### Overview
Analysis of treatment response in RA synovial fluid using paired pre- and post-treatment samples from patients receiving TNF-α or JAK inhibitors.

### Dataset
- **Accession**: GSE296117 (GEO)
- **Paper**: He et al., *Scientific Data* (2025)
- **Design**: Paired synovial fluid samples before and after 1 month of adalimumab or tofacitinib (+ MTX)
- **Cells**: ~100,000 high-quality cells
- **Source**: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE296117
- **Processed data**: Seurat RDS available as GEO supplementary file (~2.3 GB)

### What the notebook demonstrates
1. Loading processed data (RDS → AnnData)
2. QC and preprocessing
3. Patient-level Harmony integration
4. Clustering and marker visualization
5. Pre- vs post-treatment comparison
6. Focus on pathogenic cell states (SPP1+ macrophages, CXCL13+ T cells)

### Biological focus
- Dynamic effects of TNF-α and JAK inhibitors on synovial fluid immune cells
- Reduction of pathogenic macrophage and T cell states after treatment
- Drug-specific transcriptional and communication changes

### How to run
1. Download `GSE296117_RA_geo.rds` from GEO supplementary files.
2. Convert to AnnData (or use pre-converted h5ad) and place in `data/raw/GSE296117/`.
3. Activate environment and open the notebook.

---

Both examples are designed to mirror real research projects and can be extended with cell type annotation, trajectory analysis, ligand-receptor inference, or multi-omics integration.

*Research use only.*
