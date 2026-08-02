"""
Automated Hardware Functional Test & Protocol Diagnostics Tool
Simulates I2C and SPI protocol verification and automates fault isolation using PyTest.
"""

import pytest
import logging
import datetime

# Configure Diagnostic Logger
logging.basicConfig(
    filename='diagnostic_failures.log', 
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - COMPONENT FAULT - %(message)s'
)

# --- 1. Hardware Mock Classes (Simulating Physical Interfaces) ---
class MockI2CBus:
    def read_byte_data(self, address, register):
        # Simulating a faulty temperature sensor at address 0x40
        if address == 0x40 and register == 0x01:
            return 0xFF  # Hex 0xFF indicates a bus read failure or unresponsive IC
        return 0x5A      # Hex 0x5A is our simulated "Pass" state

class MockSPIBus:
    def transfer(self, data_packet):
        # Simulating a successful SPI flash memory read
        if data_packet == [0x03, 0x00, 0x00, 0x00]: # Standard SPI Read Command
            return [0x00, 0x00, 0x00, 0xAA] # 0xAA indicates successful read
        return [0x00, 0x00, 0x00, 0x00]

# --- 2. PyTest Fixtures (Setup / Teardown) ---
@pytest.fixture
def i2c_bus():
    print("\n[SETUP] Initializing I2C Bus...")
    bus = MockI2CBus()
    yield bus
    print("\n[TEARDOWN] Closing I2C Bus...")

@pytest.fixture
def spi_bus():
    print("\n[SETUP] Initializing SPI Bus...")
    bus = MockSPIBus()
    yield bus
    print("\n[TEARDOWN] Closing SPI Bus...")

# --- 3. Automated Functional Tests ---
def test_i2c_temp_sensor_read(i2c_bus):
    """Isolates faults on the I2C Temperature Sensor (U12)"""
    sensor_address = 0x40
    data_register = 0x01
    expected_value = 0x5A
    
    actual_value = i2c_bus.read_byte_data(sensor_address, data_register)
    
    # Fault Isolation Logic
    if actual_value != expected_value:
        logging.error(f"U12 (Temp Sensor) I2C Read Failed. Addr: {hex(sensor_address)}, Expected: {hex(expected_value)}, Got: {hex(actual_value)}")
        
    assert actual_value == expected_value, f"Hardware Failure: I2C Temp Sensor returned {hex(actual_value)}"

def test_spi_flash_memory_integrity(spi_bus):
    """Verifies SPI communication with Flash Memory (U4)"""
    read_command = [0x03, 0x00, 0x00, 0x00]
    expected_response = 0xAA
    
    response = spi_bus.transfer(read_command)
    actual_data = response[-1]
    
    if actual_data != expected_response:
        logging.error(f"U4 (SPI Flash) Read Failed. Expected: {hex(expected_response)}, Got: {hex(actual_data)}")
        
    assert actual_data == expected_response, "Hardware Failure: SPI Flash memory unresponsive."
