"""Spatial RNA-seq analysis using Squidpy and Scanpy."""

import scanpy as sc
import squidpy as sq
from pathlib import Path
from typing import Optional

def analyze_spatial(
    adata_path: str,
    library_id: Optional[str] = None,
    n_neighs: int = 6,
    resolution: float = 0.4,
    output_dir: str = "results/spatial",
) -> str:
    """
    Spatial transcriptomics workflow: QC, clustering, spatial domains, neighborhood enrichment.

    Parameters
    ----------
    adata_path : str
        Path to spatial AnnData (.h5ad) with spatial coordinates
    library_id : str, optional
        Library ID for multi-sample spatial data
    n_neighs : int
        Number of spatial neighbors
    resolution : float
        Clustering resolution
    output_dir : str
        Output directory

    Returns
    -------
    str
        Path to processed AnnData
    """
    adata = sc.read_h5ad(adata_path)

    # Basic processing
    sc.pp.filter_cells(adata, min_genes=200)
    sc.pp.normalize_total(adata)
    sc.pp.log1p(adata)
    sc.pp.highly_variable_genes(adata, n_top_genes=2000)
    sc.pp.pca(adata)
    sc.pp.neighbors(adata)
    sc.tl.umap(adata)
    sc.tl.leiden(adata, resolution=resolution, key_added="spatial_clusters")

    # Spatial graph and analysis
    sq.gr.spatial_neighbors(adata, n_neighs=n_neighs, library_key=library_id)
    sq.gr.nhood_enrichment(adata, cluster_key="spatial_clusters")
    sq.pl.nhood_enrichment(adata, cluster_key="spatial_clusters")

    # Save
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    out_path = Path(output_dir) / "spatial_processed.h5ad"
    adata.write(out_path)

    return str(out_path)
