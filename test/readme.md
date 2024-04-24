# Logic Design Assembly Test Code

This repository provides a series of sample instruction codes which can used for evaluate the actuall microprocessor implementation.

Upload one of the Verilog modules to a secondary board, and connect pins for testing.

Also, use `process.py` for testing the code. It's a python-based microprocessor implementation which also provides detailed step-by-step analysis.

Sample usage:
```bash
# Upload your microprocessor to the FPGA
# Upload imem1.v to the FPGA
python process.py imem1.v
# Check the differences
```
