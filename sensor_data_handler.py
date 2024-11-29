# sensor_data_handler.py
import logging

# Import generated FlatBuffers modules
import schema.SensorLog.SensorType as SensorType
import schema.SensorLog.BME688Data as BME688Data
import schema.SensorLog.ENS160Data as ENS160Data
import schema.SensorLog.LSM6D032Data as LSM6D032Data
import schema.SensorLog.MPLAltimeterData as MPLAltimeterData
import schema.SensorLog.BNO055Data as BNO055Data

class SensorDataHandler:
    def __init__(self):
        self.logger = logging.getLogger("AuxiliaryLogger")
        self.logger.debug("SensorDataHandler initialized.")

    def handle_sensor_batch(self, sensor_batch):
        timestamp = sensor_batch.Timestamp()
        self.logger.info(f"Sensor Batch Timestamp: {timestamp}")
        for i in range(sensor_batch.MessagesLength()):
            sensor_message = sensor_batch.Messages(i)
            self.handle_sensor_message(sensor_message)

    def handle_sensor_message(self, sensor_message):
        sensor_type = sensor_message.SensorType()
        data_union = sensor_message.Data()
        if sensor_type == SensorType.SensorType.BME688:
            self.handle_bme688_data(data_union.BME688Data())
        elif sensor_type == SensorType.SensorType.ENS160:
            self.handle_ens160_data(data_union.ENS160Data())
        elif sensor_type == SensorType.SensorType.LSM6D032:
            self.handle_lsm6d032_data(data_union.LSM6D032Data())
        elif sensor_type == SensorType.SensorType.MPLAltimeter:
            self.handle_mpl_altimeter_data(data_union.MPLAltimeterData())
        elif sensor_type == SensorType.SensorType.BNO055:
            self.handle_bno055_data(data_union.BNO055Data())
        else:
            self.logger.warning(f"Unknown sensor type: {sensor_type}")

    def handle_bme688_data(self, data):
        temperature = data.Temperature()
        pressure = data.Pressure()
        humidity = data.Humidity()
        gas_resistance = data.GasResistance()
        altitude = data.Altitude()
        self.logger.info(f"BME688 Data - Temp: {temperature}, Pressure: {pressure}, Humidity: {humidity}")

    def handle_ens160_data(self, data):
        aqi = data.Aqi()
        tvoc = data.Tvoc()
        eco2 = data.Eco2()
        self.logger.info(f"ENS160 Data - AQI: {aqi}, TVOC: {tvoc}, eCO2: {eco2}")

    def handle_lsm6d032_data(self, data):
        accel_x = data.AccelX()
        accel_y = data.AccelY()
        accel_z = data.AccelZ()
        self.logger.info(f"LSM6D032 Data - Accel X: {accel_x}, Y: {accel_y}, Z: {accel_z}")

    def handle_mpl_altimeter_data(self, data):
        pressure = data.Pressure()
        altitude = data.Altitude()
        self.logger.info(f"MPL Altimeter Data - Pressure: {pressure}, Altitude: {altitude}")

    def handle_bno055_data(self, data):
        accel_x = data.AccelX()
        accel_y = data.AccelY()
        accel_z = data.AccelZ()
        self.logger.info(f"BNO055 Data - Accel X: {accel_x}, Y: {accel_y}, Z: {accel_z}")
        # Handle other fields as needed

    # Add additional methods for other sensor types if necessary
