# main.py
import os
import sys

# Add 'src' directory to system path so we can import our modules cleanly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from parse_dicom import parse_dicom_directory
from anatomical_mapper import map_findings_to_anatomy
from hiv_module import analyze_hiv_reservoirs
from train_model import train_baseline_classifier

def run_omniscan_pipeline():
    print("=" * 75)
    print(" PROJECT OMNISCAN AI: UNIFIED MASTER EXECUTION PIPELINE")
    print("=" * 75)
    
    # Step 1: Parse DICOM Data
    print("\n[Step 1/4] Running DICOM Data Ingestion & Metadata Parsing...")
    df_summary = parse_dicom_directory("data/")
    if not df_summary.empty:
        df_summary.to_csv("data/dicom_summary.csv", index=False)
        print("-> DICOM summary successfully updated.")
    else:
        print("-> Using existing data structures.")

    # Step 2: Map Anatomy Findings
    print("\n[Step 2/4] Executing Unified Anatomical Body Mapping...")
    map_findings_to_anatomy("data/dicom_summary.csv")

    # Step 3: Run HIV Reservoir Research Module
    print("\n[Step 3/4] Executing Dedicated HIV Reservoir & Tissue Analysis...")
    analyze_hiv_reservoirs()

    # Step 4: Run AI/ML Classification Engine
    print("\n[Step 4/4] Training and Evaluating Baseline AI Classification Engine...")
    train_baseline_classifier()

    print("\n" + "=" * 75)
    print(" MASTER PIPELINE EXECUTION COMPLETE: All subsystems ran successfully.")
    print("=" * 75)

if __name__ == "__main__":
    run_omniscan_pipeline()