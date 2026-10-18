# src/generate_sample.py
import os
import pydicom
from pydicom.dataset import Dataset, FileDataset
import datetime

def create_dummy_dicom(output_path="data/test_scan.dcm"):
    # Ensure data directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Create file meta information data elements
    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = pydicom.uid.UID('1.2.840.10008.5.1.4.1.1.2') # CT Image Storage
    file_meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
    file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian

    # Create the main Dataset
    ds = FileDataset(output_path, {}, file_meta=file_meta, preamble=b"\0" * 128)
    ds.PatientID = "OMNISCAN_TEST_001"
    ds.Modality = "CT"
    ds.StudyDate = datetime.datetime.now().strftime("%Y%m%d")
    ds.Rows = 512
    ds.Columns = 512
    
    # Save the file
    ds.save_as(output_path)
    print(f"Sample DICOM file successfully generated at: {output_path}")

if __name__ == "__main__":
    create_dummy_dicom()