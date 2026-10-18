# src/hiv_module.py
import pandas as pd
import datetime

def analyze_hiv_reservoirs():
    """
    Simulates the tracking and analysis of HIV tissue reservoirs,
    differentiating between viral states, sample requirements, and assay methods.
    """
    print("=" * 60)
    print("PROJECT OMNISCAN AI: HIV RESERVOIR & TISSUE ANALYSIS MODULE")
    print("=" * 60)
    
    reservoir_data = [
        {
            "Anatomical_Region": "Peripheral Blood",
            "Reservoir_Type": "Central/Effector Memory T-Cells",
            "Analyte_Investigated": "Cell-associated DNA / Plasma RNA",
            "Detection_Feasibility": "Routine (Blood Sample)",
            "Active_vs_Latent": "Latent provirus + Low baseline transcription",
            "Clinical_Status": "Suppressed (<20 copies/mL on ART)"
        },
        {
            "Anatomical_Region": "Lymph Nodes",
            "Reservoir_Type": "Germinal Center Follicular T-helper Cells",
            "Analyte_Investigated": "Proviral DNA / p24 Protein",
            "Detection_Feasibility": "Invasive Biopsy / FNA Required",
            "Active_vs_Latent": "High density of transcriptionally silent provirus",
            "Clinical_Status": "Refractory Sanctuary Site"
        },
        {
            "Anatomical_Region": "Gut-Associated Lymphoid Tissue (GALT)",
            "Reservoir_Type": "Lamina Propria Memory T-Cells",
            "Analyte_Investigated": "Cell-Associated RNA / DNA",
            "Detection_Feasibility": "Endoscopic Mucosal Biopsy Required",
            "Active_vs_Latent": "Major early depletion site with persistent latency",
            "Clinical_Status": "High Persistence Density"
        },
        {
            "Anatomical_Region": "Brain & Central Nervous System",
            "Reservoir_Type": "Microglia & Perivascular Macrophages",
            "Analyte_Investigated": "CSF Viral Load / Cell-associated DNA",
            "Detection_Feasibility": "Lumbar Puncture (CSF Sample)",
            "Active_vs_Latent": "Compartmentalized viral replication/latency",
            "Clinical_Status": "Blood-Brain Barrier Protected"
        },
        {
            "Anatomical_Region": "Bone Marrow",
            "Reservoir_Type": "Hematopoietic Stem Cells (HSCs)",
            "Analyte_Investigated": "CD34+ Sorted Proviral DNA",
            "Detection_Feasibility": "Bone Marrow Aspiration Required",
            "Active_vs_Latent": "Long-lived progenitor cellular latency",
            "Clinical_Status": "Deep Sanctuarial Reserve"
        }
    ]
    
    df_hiv = pd.DataFrame(reservoir_data)
    
    # Display the structured reservoir analysis
    for idx, row in df_hiv.iterrows():
        print(f"\n[Reservoir Target: {row['Anatomical_Region']}]")
        print(f"  Cellular Target  : {row['Reservoir_Type']}")
        print(f"  Analyte          : {row['Analyte_Investigated']}")
        print(f"  Assay Requirement: {row['Detection_Feasibility']}")
        print(f"  State Profile    : {row['Active_vs_Latent']}")
        print(f"  Clinical Status  : {row['Clinical_Status']}")
        
    print("\n" + "=" * 60)
    
    # Export report
    output_path = "data/hiv_reservoir_report.csv"
    df_hiv.to_csv(output_path, index=False)
    print(f"HIV reservoir research analysis saved to {output_path}")

if __name__ == "__main__":
    analyze_hiv_reservoirs()