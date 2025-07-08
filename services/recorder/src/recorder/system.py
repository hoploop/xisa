from datetime import time
import logging
import platform
import threading
from AppKit import NSWorkspace
from Foundation import NSObject, NSRunLoop, NSDate
import psutil
from enum import Enum, auto

log = logging.getLogger(__name__)

class System:
    def __init__(self,on_started,on_stopped):
        self.shouldstop = False
        self.on_started = on_started
        self.on_stopped = on_stopped
        
    def stop(self):
        self.shouldstop = True


class AppLaunchObserver(NSObject):
    def applicationLaunched_(self, notification):
        app_info = notification.userInfo()
        app_name = app_info["NSApplicationName"]
        print(f"🚀 Launched: {app_name}")
        
    def applicationTerminated_(self, notification):
        app_info = notification.userInfo()
        app_name = app_info["NSApplicationName"]
        print(f"❌ Closed: {app_name}")
        
class MicrosoftSystem(System):
    
    
    def get_running_apps(self):
        apps = set()
        for proc in psutil.process_iter(['name']):
            try:
                apps.add(proc.info['name'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return apps

    def start(self):
        self.seen = set()
        logging.info("App Monitor started...")
        while not self.shouldstop:
            current = self.get_running_apps()
            new_apps = current - self.seen
            for app in new_apps:
                self.on_started(app)
                logging.info(f"🚀 Launched: {app}")
            self.seen = current
            time.sleep(2)  # check every 2 seconds

class LinuxSystem(System):
    
    def get_running_apps(self):
        apps = set()
        for proc in psutil.process_iter(['name']):
            try:
                apps.add(proc.info['name'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        return apps

    def start(self):
        self.seen = set()
        logging.info("🚀 App Monitor started...")
        while self.shouldstop:
            current = self.get_running_apps()
            new_apps = current - self.seen
            for app in new_apps:
                self.on_started(app)
                logging.info(f"New app launched: {app}")
            self.seen = current
            time.sleep(2)

class DarwinSystem(System):
    
    def start(self):
        workspace = NSWorkspace.sharedWorkspace()
        center = workspace.notificationCenter()

        observer = AppLaunchObserver.alloc().init()
        center.addObserver_selector_name_object_(
            observer,
            b'applicationLaunched:',
            'NSWorkspaceDidLaunchApplicationNotification',
            None
        )
        center.addObserver_selector_name_object_(
            observer,
            b'applicationTerminated:',
            'NSWorkspaceDidTerminateApplicationNotification',
            None
        )
        
        log.info("🔍 Listening for app launches... (Press Ctrl+C to stop)")
        while not self.shouldstop:
            NSRunLoop.currentRunLoop().runUntilDate_(NSDate.dateWithTimeIntervalSinceNow_(0.1))
            time.sleep(0.1)
    
    
class OperatingSystem(Enum):
    MACOS = auto()
    LINUX = auto()
    WINDOWS = auto()
    UNKNOWN = auto()

class SystemListener:
    def __init__(self):
        self._listener_thread = None
        self._frame = 0
        
    
        
    def set_frame(self,value:int):
        self._frame = value
        
    def start(self):
        if self._recording: return
        self._recording = True
        log.info('Start recording mouse events')
        self._events = []
        
        os = self.detect_os()
        if os == OperatingSystem.MACOS:
            self._listener = DarwinSystem()
        elif os == OperatingSystem.WINDOWS:
            self._listener = MicrosoftSystem()
        else:
            self._listener = LinuxSystem()
        self._listener_thread = threading.Thread(target=self._listener.start)
        self._listener_thread.daemon = True
        self._listener_thread.start()
        
            
        
    def detect_os(self) -> OperatingSystem:
        system = platform.system()
        if system == "Darwin":
            return OperatingSystem.MACOS
        elif system == "Linux":
            return OperatingSystem.LINUX
        elif system == "Windows":
            return OperatingSystem.WINDOWS
        else:
            return OperatingSystem.UNKNOWN
        
    def stop(self):
        self._listener.stop()
        self._listener_thread.join()
