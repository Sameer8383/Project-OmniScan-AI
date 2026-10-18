# src/parse_dicom.py
import os
import pandas as pd
import pydicom

def parse_dicom_directory(data_dir="data/"):
    """
    Scans a directory for DICOM files, extracts core metadata headers,
    and returns a structured Pandas DataFrame.
    """
    metadata_list = []
    
    print(f"Scanning directory: {data_dir} for DICOM files...")
    
    # Walk through the data directory
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            # Check for DICOM extension (often .dcm or uppercase .DCM)
            if file.lower().endswith('.dcm') or '.' not in file:
                file_path = os.path.join(root, file)
                try:
                    # Read DICOM file headers without loading full pixel array to save memory
                    ds = pydicom.dcmread(file_path, stop_before_pixels=True)
                    
                    record = {
                        "File_Name": file,
                        "Patient_ID": getattr(ds, 'PatientID', 'Unknown'),
                        "Modality": getattr(ds, 'Modality', 'Unknown'),
                        "Study_Date": getattr(ds, 'StudyDate', 'Unknown'),
                        "Rows": getattr(ds, 'Rows', None),
                        "Columns": getattr(ds, 'Columns', None),
                        "File_Path": file_path
                    }
                    metadata_list.append(record)
                except Exception as e:
                    print(f"Could not parse {file}: {e}")
                    
    # Convert list of records into a Pandas DataFrame
    df = pd.DataFrame(metadata_list)
    return df

if __name__ == "__main__":
    df_summary = parse_dicom_directory()
    print("\n--- DICOM Metadata Summary ---")
    print(df_summary)
    
    # Save summary to CSV if data was found
    if not df_summary.empty:
        output_path = "data/dicom_summary.csv"
        df_summary.to_csv(output_path, index=False)
        print(f"\nMetadata successfully saved to {output_path}")
    else:
        print("\nNo DICOM files found in 'data/' yet. (This is normal—place sample .dcm files in the 'data/' folder to test parsing!)")