# Siemens S7 PLC Communication with Snap7

This directory contains a collection of Python scripts designed to interact with Siemens S7 PLCs (Programmable Logic Controllers) using the `python-snap7` library. These scripts provide examples for various operations such as reading from and writing to PLC memory, testing connections, and more.

## Scripts Overview

Below is a description of each script found in this directory:

### `memory.py`

This script defines a Python class `S71200` which simplifies interaction with an S7-1200 PLC.

*   **Purpose**: To provide a higher-level abstraction for reading and writing various data types to different memory areas of an S7-1200 PLC.
*   **Class**: `S71200(ip, debug=False)`
    *   `ip` (str): The IP address of the PLC.
    *   `debug` (bool, optional): Enables debug printing if set to `True`.
*   **Methods**:
    *   `getMem(mem, returnByte=False)`: Reads data from a specified memory location.
        *   `mem` (str): The memory address (e.g., 'MX0.0', 'MB0', 'MW0', 'MD0', 'FREAL0', 'QX0.0', 'IB0').
        *   `returnByte` (bool, optional): If `True`, returns the raw byte array; otherwise, returns the parsed data type.
    *   `writeMem(mem, value)`: Writes data to a specified memory location.
        *   `mem` (str): The memory address.
        *   `value`: The value to write (appropriate for the specified memory type).
*   **Supported Memory Areas**:
    *   `M` (Merkers / Memory Bits)
    *   `Q` (Outputs)
    *   `I` (Inputs)
*   **Supported Data Types**: Boolean (bit), Byte (int), Word (int), DWord (int/dword), Real (float).
*   **Example**: The script includes a commented-out example section (`if __name__=="__main__":`) demonstrating how to use the `S71200` class to read and write to PLC memory.

### `snap7-PLC-test.py`

This script provides functions to read and write to the Merker (MK) memory area of a PLC and includes a test case.

*   **Purpose**: To test basic read and write operations on a PLC's MK memory area.
*   **Functions**:
    *   `ReadMemory(plc, byte, bit, datatype)`: Reads data from a specific address in the MK memory area.
    *   `WriteMemory(plc, byte, bit, datatype, value)`: Writes data to a specific address in the MK memory area.
*   **Example**: The `if __name__=="__main__":` block connects to a PLC, reads a bit from memory address MK100.2, attempts to write to it, and prints the status.

### `snap7-client.py`

A simple client script to read real values from different memory areas of a PLC.

*   **Purpose**: To demonstrate connecting to a PLC and reading floating-point numbers from the MK (Merker), PA (Process Image Output), and PE (Process Image Input) memory areas.
*   **Operation**: Connects, reads a 4-byte real value starting from address 0 in areas 0x83 (MK), 0x82 (PA), and 0x81 (PE), prints these values, and disconnects.

### `snap7-read-write.py`

This script demonstrates reading and writing a real (floating-point) value to the MK memory area of a PLC.

*   **Purpose**: To provide a clear example of reading and modifying a real value in the PLC's memory.
*   **Functions**:
    *   `ReadMemory(plc, byte, bit, datatype)`: Reads data (focused on MK area due to `areas['MK']`).
    *   `WriteMemory(plc, byte, bit, datatype, value)`: Writes data (focused on MK area).
*   **Example**: The script connects to a PLC, reads a real value from address 0 of the MK area, writes the value of Pi (3.141592) to the same location, and then reads it back to verify the write.

### `snap7-test-connection.py`

A very basic script to test the network connection to a PLC.

*   **Purpose**: To quickly verify if a connection can be established with the PLC at the specified IP address.
*   **Operation**: Attempts to connect to the PLC, prints whether the connection was successful, and then disconnects.

### `snap7-write-input.py`

This script demonstrates reading from and writing to the Process Image Input (PE) area of a PLC. Writing to inputs is typically used for simulation or forcing values.

*   **Purpose**: To show how to interact with the PLC's input image table.
*   **Functions**:
    *   `ReadMemory(plc, byte, bit, datatype)`: Reads data from the PE memory area (`areas['PE']`).
    *   `WriteMemory(plc, byte, bit, datatype, value)`: Writes data to the PE memory area.
*   **Example**: The script connects to a PLC, reads a bit from input address 0.0 (e.g., I0.0), writes a '1' to it, and then reads it back to show the change in the process image.

## Prerequisites

*   **Python 3.x**
*   **`python-snap7` library**: This library is essential for communication with the S7 PLCs. It can be installed via pip:
    ```bash
    pip install python-snap7
    ```
*   **Siemens S7 PLC**: You need access to a compatible Siemens S7 PLC (e.g., S7-1200, S7-1500, S7-300, S7-400) configured with an IP address on the same network as the machine running these scripts. The PLC should also be configured to allow PUT/GET communication from external partners (often a setting in the PLC's hardware configuration or protection settings).

## Usage

1.  **Configure IP Addresses**: Before running any script, you will likely need to modify the PLC's IP address within the script. Most scripts have a line like `plc.connect('192.168.1.X', 0, 1)` where `'192.168.1.X'` should be replaced with your PLC's actual IP address.
2.  **Run from Command Line**: Open a terminal or command prompt, navigate to this `snap7` directory, and execute the desired script using Python:
    ```bash
    python <script_name>.py
    ```
    For example:
    ```bash
    python snap7-test-connection.py
    ```
3.  **Observe Output**: The scripts will print information to the console regarding their operations, such as connection status, data read, or confirmation of data written.

**Note**: Ensure your network configuration allows communication between your computer and the PLC on the necessary ports (typically TCP port 102 for S7 communication).
