"""scRNA-seq analysis pipeline with multi-sample integration."""

import scanpy as sc
from pathlib import Path
from typing import Optional

def analyze_scrna(
    adata_path: str,
    batch_key: str = "sample",
    integration: str = "harmony",
    resolution: float = 0.5,
    n_neighbors: int = 15,
    n_pcs: int = 30,
    output_dir: str = "results/scrna",
) -> str:
    """
    End-to-end scRNA-seq analysis: QC, normalization, integration, clustering, markers.

    Parameters
    ----------
    adata_path : str
        Path to AnnData .h5ad file
    batch_key : str
        Column in adata.obs for batch/sample
    integration : str
        "harmony", "scvi", or "none"
    resolution : float
        Leiden resolution
    output_dir : str
        Directory to save results

    Returns
    -------
    str
        Path to processed AnnData
    """
    adata = sc.read_h5ad(adata_path)

    # Basic QC
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.filter_genes(adata, min_cells=3)
    adata.var["mt"] = adata.var_names.str.startswith("MT-")
    sc.pp.calculate_qc_metrics(adata, qc_vars=["mt"], percent_top=None, log1p=False, inplace=True)
    adata = adata[adata.obs.pct_counts_mt < 20, :].copy()

    # Normalization & HVG
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, n_top_genes=2000, batch_key=batch_key)
    adata = adata[:, adata.var.highly_variable].copy()

    # PCA
    sc.pp.scale(adata, max_value=10)
    sc.tl.pca(adata, n_comps=n_pcs)

    # Integration
    if integration == "harmony":
        sc.external.pp.harmony_integrate(adata, key=batch_key, basis="X_pca")
        use_rep = "X_pca_harmony"
    elif integration == "scvi":
        import scvi
        scvi.model.SCVI.setup_anndata(adata, batch_key=batch_key)
        model = scvi.model.SCVI(adata)
        model.train()
        adata.obsm["X_scVI"] = model.get_latent_representation()
        use_rep = "X_scVI"
    else:
        use_rep = "X_pca"

    # Neighbors, UMAP, clustering
    sc.pp.neighbors(adata, n_neighbors=n_neighbors, use_rep=use_rep)
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution=resolution)

    # Marker genes
    sc.tl.rank_genes_groups(adata, "leiden", method="wilcoxon")

    # Save
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    out_path = Path(output_dir) / "processed.h5ad"
    adata.write(out_path)

    return str(out_path)
