import copy
import platform
import sys
import time

import serial.tools.list_ports
from PySide6.QtCore import QTimer, QDateTime, QEventLoop, Slot
from PySide6.QtWidgets import QMainWindow, QApplication

import const_var as const
import utils
from RSDControl import RSDControl
from configForm import ConfigWindow
from config_settings import ConfigSettings
from log import Log
from serialReadThread import SerialReadThread
from ui_main import Ui_MainWindow


# @dataclass
# class Colors:
# 	WHITE: str = '#fff'
# 	YELLOW: str = '#f0d264'
# 	GREEN: str = '#00AE68'
# 	GRAY: str = 'gray'
# 	LIGHT_GRAY: str = '#ededed'
# 	RED: str = '#aa0000'
# 	PINK: str = '#fa5a5a'
# 	BROWN: str = '#cc3300'
# 	ORANGE: str = '#e65c00'
# 	SKY: str = '#00b0f0'
# 	M_GRAY: str = '#d6d6d6'


class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self):
		"""
		Initialize the main window.
		"""
		super(MainWindow, self).__init__()
		# UI 설정
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# frameless window
		# self.setWindowFlag(Qt.FramelessWindowHint)

		# read config from config file (config.ini)
		self.config = ConfigSettings()
		console_en = self.config.log.getint("console")
		log_level = self.config.log.get("level")

		self.log = Log('rsd', console_en=console_en, log_level=log_level)
		self.log_title = "rsd"

		self.log.info("Load app...")
		self.log.debug(f"platform= {platform.system()} ")

		self.rsd_control = RSDControl(self.config, self.log, slave_id=1)

		self.config_form = ConfigWindow(self, config=self.config, log=self.log)

		# serial communication
		self.ser = serial.Serial()
		self.port_readable = False
		# self.serial_init()
		self.rs485_stat = None

		# set event handler
		self.assign_widgets()

		self.serial_thread = None

		# if self.ser is None:
		# 	# self.update_statusbar("RS485 connection 오류")
		# 	# self.show_alert("RS485 connection 오류, 연결정보 확인 후 재시작하세요.")
		# 	# self.btn_start.hide()
		# 	self.log.error(f"RS485 connection error")
		# else:
		# 	self.serial_thread = SerialReadThread(self.ser, self.log)
		# 	# SerialReadThread 에서 emit() 후 즉시 수신 안됨 => Qt.DirectConnection 추가
		# 	# self.serial_thread.start()
		# 	self.serial_thread.data_recv_signal.connect(self.read_serial, Qt.DirectConnection)

		# send command via rs485
		self.send_buf = []
		self.recv_buf = []
		# save received data to temporary buffer
		self.tmp_buf = []
		self.set_recv_read_size = 0
		self.set_recv_write_size = 0
		self.recv_buf_size = 0
		self.is_start_parse = False

		# show now datetime
		self.now_timer = QTimer(self)
		# self.timer.setInterval(1000)  # ms
		self.now_timer.timeout.connect(self.update_nowtime)
		self.now_timer.start(1000)  # ms

		# configuration for automatic control
		self.is_start = False
		# default: 2 minutes (120000 ms)
		read_interval = self.config.rs485.getint('interval_ms')

		self.sensor_timer = QTimer(self)
		# self.sensor_timer.setInterval(read_interval)  # ms, 5 minutes
		self.sensor_timer.timeout.connect(self.on_timer_sensing)

	def assign_widgets(self):
		"""
		Assign widgets to UI.
        """
		# tool button event
		self.ui.tool_close.clicked.connect(self.on_exit)
		self.ui.tool_setting.clicked.connect(self.open_config_form)

		# load comport list
		self.ui.comport_list.addItems(self.get_comports())
		self.ui.connect_btn.clicked.connect(self.on_comport_connect_clicked)
		# self.ui.on_off_toggle.clicked.connect(self.on_manual_control)
		self.ui.btn_off.clicked.connect(self.on_manual_off)
		self.ui.btn_on.clicked.connect(self.on_manual_on)
		self.ui.btn_port_refresh.clicked.connect(self.on_port_refresh)

		self.init_widgets()

	def update_nowtime(self):
		"""
		1초에 한번씩 시간을 표시
		:return:
		"""
		now = QDateTime.currentDateTime()
		self.ui.current_time.setText(now.toString('yyyy.MM.dd hh:mm:ss'))

	def open_config_form(self):
		"""
		Open configuration form.
		"""
		self.config_form.show()

	def on_manual_control(self):
		"""
		manual control
		:return:
		:rtype:
		"""
		if self.ui.on_off_toggle.isChecked():
			# send rsd on
			self.send_rsd_control_on()
		else:
			# send rsd off
			self.send_rsd_control_off()

	def on_manual_on(self):
		"""
		manual control
		:return:
		:rtype:
		"""
		if not self.serial_thread:
			self.show_statusbar("COM Port 연결 안됨")
		else:
			# send rsd on
			self.send_rsd_control_on()

	def on_manual_off(self):
		"""
		manual control
		:return:
		:rtype:
		"""
		if not self.serial_thread:
			self.show_statusbar("COM Port 연결 안됨")
		else:
			# send rsd off
			self.send_rsd_control_off()

	def on_port_refresh(self):
		# load comport list
		self.ui.comport_list.clear()
		self.ui.comport_list.addItems(self.get_comports())

	def on_comport_connect_clicked(self):
		"""
		Connect to the selected serial port.
		"""
		# self.log.debug("EVENT: RS485 connect button")
		# 버튼이 눌린 상태인지 확인
		if self.ui.connect_btn.isChecked():
			# connect status
			self.ui.connect_btn.setText("Disconnect")
			# 연결 작업 수행
			port_name = self.ui.comport_list.currentText()
			# save com port value to config file
			self.config.rs485 = ('port', port_name)
			self.log.info(f'selected comport: {port_name}')

			self.config.save_config()
			# self.serial_init(port_name)

			if not self.serial_thread:
				self.serial_thread = SerialReadThread(port_name, 9600, self.log)
				# 	# SerialReadThread 에서 emit() 후 즉시 수신 안됨 => Qt.DirectConnection 추가
				# 	# self.serial_thread.start()
				# 	self.serial_thread.data_recv_signal.connect(self.read_serial, Qt.DirectConnection)
				self.serial_thread.data_recv_signal.connect(self.read_serial)
				self.serial_thread.serial_activated_signal.connect(
					self.signal_serial_activated)
				self.serial_thread.start()

			# start serial thread and timer
			# 인증용, 보류, 241028
			self.sensor_timer.setInterval(self.config.rs485.getint('interval_ms'))  # ms, 5 minutes
			# self.sensor_timer.start()
			self.log.info(f'serial thread start')
		else:
			# disconnect status
			# 연결 해제 작업 수행
			# stop serial, thread and timer
			self.sensor_timer.stop()
			if self.serial_thread:
				self.serial_thread.stop()
				self.serial_thread = None  # thread object 해제

			self.ui.connect_btn.setText("Connect")
		# if self.ser.is_open:
		# 	self.ser.close()
		# update rs485 widget
		# self.update_widget_rs485_connect(False)

	def on_timer_sensing(self):
		"""
		Send request-sensor-cmd to RTU when refresh button is clicked
		:return:
		:rtype:
		"""
		self.get_rsd_status()

	def on_exit(self):
		"""
		Exit the application.
        """
		self.log.info('exit: App')
		self.show_statusbar('종료중...')

		if self.config_form.isVisible():
			self.config_form.close()

		try:
			if self.now_timer.isActive():
				self.now_timer.stop()

			if self.sensor_timer.isActive():
				self.sensor_timer.stop()

			# self.log.debug("close serial_thread")

			if self.serial_thread:
				self.serial_thread.stop()
		# self.serial_thread.join()  # 스레드가 완전히 종료될 때까지 기다림

		# self.log.debug("close serial")

		# if self.port_readable and self.ser.is_open:
		# 	self.ser.close()
		# if self.rs485_stat and self.ser.is_open:
		# 	self.ser.close()
		except AttributeError as e:
			self.log.error(e)
		# finally:
		# 	pass

		self.close()

	def closeEvent(self, event):
		if self.config_form.isVisible():
			self.config_form.close()

		try:
			if self.now_timer.isActive():
				self.now_timer.stop()

			if self.sensor_timer.isActive():
				self.sensor_timer.stop()

			# self.log.debug("close serial_thread")

			if self.serial_thread:
				self.serial_thread.stop()

		# self.log.debug("close serial")

		# if self.port_readable and self.ser.is_open:
		# 	self.ser.close()
		# if self.rs485_stat and self.ser.is_open:
		# 	self.ser.close()
		except AttributeError as e:
			self.log.error(e)
		# finally:
		# 	pass

		self.close()

	def show_statusbar(self, msg):
		"""Show message on status bar """
		self.ui.statusbar.showMessage(msg)

	def get_rsd_status(self):
		"""
		Read RSD datas such as temperature, current, arc status
		using timer thread
		:return:
		"""
		# self.log.debug(f"start rsd data reading....")
		# if self.config.sensor.getint("relay8") == 1:
		self.send_rsd_status()

	def send_rsd_status(self):
		# cmd = [self.slave_id, const.FC_01, 0, RelayChannelRegister.RELAY1.value, 0, 16]
		# crc = crc16_modbus(cmd)  # low high
		# cmd.extend(crc)
		# return cmd
		cmd = self.rsd_control.packet_rsd_status

		# self.serial_write(cmd)
		self.serial_thread.send_data(cmd)
		self.rsd_control.send_buffer = cmd
		self.delay(1000)

	def send_rsd_control_off(self):
		"""
		send packet of rsd off
		:return:
		:rtype:
		"""
		# 마지막 제어 패킷 전송 시간이 1초 이후이면 진행
		if (time.time() - self.rsd_control.datas.control_res_date) > 1.0:
			cmd = self.rsd_control.packet_rsd_off
			# self.delay(200)
			self.serial_thread.send_data(cmd)
			self.rsd_control.send_buffer = cmd
			self.delay(1000)

	def send_rsd_control_on(self):
		"""
		send packet of rsd on
		:return:
		:rtype:
		"""
		cmd = self.rsd_control.packet_rsd_on
		# self.delay(200)
		self.serial_thread.send_data(cmd)
		self.rsd_control.send_buffer = cmd
		self.delay(1000)

	def get_comports(self):
		"""
        Get available serial ports.
        """
		ports = serial.tools.list_ports.comports()
		return [port.device for port in ports]

	def serial_write(self, cmd):
		"""
		send command
		:param cmd: byte type value
		:return:
		"""
		result = False
		try:
			if self.ser.is_open:
				# self.set_rs485_tx_mode()  # for RPi
				self.ser.write(bytes(bytearray(cmd)))
				self.ser.flush()
				result = True

				# recv buffer size
				if cmd[1] == const.FC_03:
					self.set_recv_read_size = (cmd[5] * 2) + 5
				else:
					self.set_recv_write_size = 8

				self.log.info(
					f"write...{utils.get_hex_format_debug(cmd)}", "serial"
				)
		# self.log.debug(f"set recv size {self.set_recv_read_size}")
		# self.set_rs485_rx_mode()  # for RPi
		except serial.SerialException as e:
			self.log.error(e, "serial")

		return result

	def serial_init(self, port, timeout=0.5):
		"""
		serial initialization according to OS such as Raspberry Pi, Windows
		:param timeout:
		:type timeout:
		:return:
		:rtype:
		"""
		# self.log.info(f"os= {platform.system()}")

		# if platform.system() == "Linux":
		# 	# RE_DE = 16
		# 	self.rede = self.config.com485.getint('rede_rpi')
		# 	port = self.config.com485.get("port_rpi")
		#
		# 	GPIO.setwarnings(False)
		# 	GPIO.setmode(GPIO.BCM)
		# 	GPIO.setup(self.rede, GPIO.OUT)
		# else:
		if port is None:
			port = self.config.rs485.get('port')

		self.ser.port = port
		self.ser.baudrate = self.config.rs485.getint('baudrate')

		self.serial_open()

	def serial_open(self):
		self.serial_close()

		result = False

		try:
			self.ser.open()
		except IOError as e:
			self.add_alert_msg(f"RS485 연결 실패")
			self.log.error(
				f'Open failed on port {self.ser.port}, baud= {self.ser.baudrate}',
				'serial')
			return False
		else:
			# self.add_alert_msg(f"RS485 연결 성공")
			self.log.info(f"Connected {self.ser.port}, baud= {self.ser.baudrate}",
			              'serial')
			# update widget and status bar
			self.show_statusbar(f'{self.ser.port} 연결됨')
			self.update_widget_rs485_connect()

		# connect to the serial port and test that it is readable
		self.port_readable = self.check_serial()

		if not self.ser.writable():
			raise Exception("port not writable")

		# GPIO.output(rst, GPIO.LOW)
		# set_rs485_rx_mode()
		# time.sleep(0.1)
		self.delay(100)
		# return self.serial
		return True

	def serial_close(self):
		if self.ser.is_open:
			self.ser.close()

	def check_serial(self):
		self.log.info(f"Testing read on port: {self.ser.port}")
		port_readable = self.ser.readable()

		if port_readable:
			self.log.info("Test read on port was successful")
		else:
			self.log.error("Test read on port failed")

		return port_readable

	@Slot(object)
	def signal_serial_activated(self, data):
		if data is True:
			self.update_widget_rs485_connect(True)
			self.show_statusbar(f"{self.config.rs485.get('port')} 연결됨")
		else:
			self.update_widget_rs485_connect(False)
			self.show_statusbar(f"COM port 연결 해제")

	@Slot(object)
	def read_serial(self, data):
		"""수신 데이터 처리"""
		# self.log.debug(f"recv : {data=}", "slot")
		buf = copy.deepcopy(data)
		data.clear()
		self.rs485_stat = True

		# self.log.debug(f"init val: {buf=} tmp_buf {self.tmp_buf}", "slot")

		if type(buf) is bytes:
			tmp_data = list(bytes(buf))
			self.tmp_buf.extend(tmp_data)
			self.log.debug(f"type: bytes {tmp_data}", "serial")
		elif type(buf) is list:
			self.tmp_buf.extend(buf)
		# self.log.debug(f"type: list {buf}", "serial")
		else:
			self.tmp_buf.append(buf)

		if self.is_start_parse is False:
			if len(self.tmp_buf) > 5:
				i = 0
				# fc_code = None
				while True:
					ch = self.tmp_buf[i]
					# self.log.debug(f"ch= {ch}")
					if (i == 0) and (ch != const.HEADER_BYTE):
						# log.debug(f"del {ch}")
						del self.tmp_buf[i]
						continue
					elif (i == 1) and (ch not in const.SLAVE_SET):
						# log.debug(f"del {ch}")
						del self.tmp_buf[i]
						continue
					elif i == 2:
						# check FC code
						if ch in const.FC_SET:
							# fc_code = ch
							self.is_start_parse = True
							# log.debug("parse start...")
							break
						else:
							del self.tmp_buf[:3]
							i = 0
							continue

					i += 1

		if self.is_start_parse:
			# function code에 따라 data length 다름
			if self.tmp_buf[2] in const.FC06_SET:
				total_len = 8
			# elif self.tmp_buf[1] == const.FC_01:
			# 	total_len = 6
			else:
				total_len = self.tmp_buf[3] + 5

			tmp_buf_len = len(self.tmp_buf)
			# self.log.debug(f"tmp buf: total len= {total_len}, {self.tmp_buf}")

			if tmp_buf_len < total_len:
				return
			elif tmp_buf_len == total_len:
				# TODO: 얕은 복사로 인해 참조 error
				recv_buf = copy.deepcopy(self.tmp_buf)
				self.tmp_buf.clear()
				self.parse_data(recv_buf)
			else:
				recv_buf = copy.deepcopy(self.tmp_buf[:total_len])
				del self.tmp_buf[:total_len]
				self.parse_data(recv_buf)

				self.log.debug(f"len = {len(self.tmp_buf)}")

			# if len(self.tmp_buf) > 5:
			# 	self.parse_data(self.tmp_buf)

			self.is_start_parse = False

	def parse_data(self, data):
		"""
		parsing data received using rs485
		:param data:
		:type data:
		:return:
		:rtype:
		"""
		buf = copy.deepcopy(data)

		self.log.info(f"parse data: {utils.get_hex_format_debug(buf)}")
		# self.log.debug("RS485: TX: {}".format(self.send_buf))

		buf_len = len(buf)
		if buf_len < 6:
			return

		# if (self.send_buf[0] != self.buf[0]) or (self.send_buf[1] != self.buf[1]):
		#    self.recv_buf.clear()
		#    return

		# get checksum
		crc = utils.calculate_checksum(buf[:-1])

		if buf[-1] != crc:
			self.log.error(
				f"rs485: valid Checksum: 0x{buf[-1]:02x} -> 0x{crc:02x}")

		# check slave id
		slave_addr = buf[1]

		if slave_addr not in const.SLAVE_SET:
			# self.update_statusbar('RS485 수신 오류')
			self.log.error(f"RS485: slave_id= 0x{slave_addr:02x}")
			return

		self.rsd_control.parse_data(buf)
		self.update_widget_rsd_data()

		# 아크 발생하면 긴급정지, 인증용 보류
		# if self.rsd_control.datas.is_arc == 1:
		# 	self.delay(200)
		# 	self.send_rsd_control_off()

		# if self.weather_form.isVisible():
		#     self.weather_sig.emit()

		# now = QDateTime.currentDateTime()
		# self.last_recv_time.setText(now.toString('yyyy.MM.dd hh:mm:ss'))

		# clear send and recv buffer
		# self.recv_buf.clear()
		self.tmp_buf.clear()
		self.recv_buf_size = 0
		# self.send_buf.clear()

	def delay(self, milliseconds):
		"""
		Use instead of time.sleep()
		:param milliseconds:
		:type milliseconds:
		:return:
		:rtype:
		"""
		# TODO: time.sleep() 사용시 UI 멈춤 증상 발생
		loop = QEventLoop()
		QTimer.singleShot(milliseconds, loop.quit)  # msec
		loop.exec()

	def update_widget_rs485_connect(self, is_connected=True):
		"""
		update widget with rs485 data
        :return:
        :rtype:
        """
		# disconnected values, default
		background_color = '#aa0000'
		text = '연결 안됨'

		if is_connected:
			# connected
			background_color = f"#00b050"
			text = '연결됨'
		# else:
		# 	# disconnected
		# 	background_color = f"background-color: red; color: #fff;"

		style = f"border-radius: 5px; background-color: {background_color}; color: #fff;"

		self.ui.val_rs485_status.setStyleSheet(style)
		self.ui.val_rs485_status.setText(text)

	def update_widget_rsd_data(self):
		"""
		update rsd data on widget
		:return:
		:rtype:
		"""
		# system status
		status_color = 'green'
		if self.rsd_control.datas.rsd_status == 0:
			self.ui.val_status.setText('정지')
			status_color = 'red'
			# self.ui.on_off_toggle.setChecked(False)
		else:
			self.ui.val_status.setText('동작중')
			# self.ui.on_off_toggle.setChecked(True)
		style_status = f"color: {status_color};"
		self.ui.val_status.setStyleSheet(style_status)

		self.ui.val_rsd_id.setText(f'{self.rsd_control.datas.rsd_id}')
		self.ui.val_current.setText(f'{self.rsd_control.datas.current}')
		self.ui.val_temperature.setText(f'{self.rsd_control.datas.temperature}')
		self.ui.val_count.setText(f'{self.rsd_control.datas.arc_count} 회')
		self.ui.val_frequency.setText(f'{self.rsd_control.datas.arc_frequency} kHz')
		# arc status
		arc_stat_text = '정상'
		# bg_color = '#00b050'
		bg_color = '#ffffff'
		if self.rsd_control.datas.is_arc == 1:
			arc_stat_text = '감지'
			bg_color = '#da833d'

		style = f'background-color: {bg_color}; color: #fff; border-radius: 5px'
		self.ui.val_arc_status.setText(arc_stat_text)
		self.ui.val_arc_status.setStyleSheet(style)

	def init_widgets(self):
		"""
		clear data on widgets
		:return:
		:rtype:
		"""
		self.ui.val_count.clear()
		self.ui.val_current.clear()
		self.ui.val_frequency.clear()
		self.ui.val_temperature.clear()
		self.ui.val_arc_status.clear()


if __name__ == "__main__":
	# 프로그램 실행 클래스
	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()

	# 프로그램을 이벤트 루프로 진입
	ret = app.exec()
	sys.exit(ret)
