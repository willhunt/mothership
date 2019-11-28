from django.test import TestCase, Client
from unittest import skipIf
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Device, Channel, Data


# HELPER FUNCTIONS -------------------------------------------------------------
def create_user(password=None):
    user = User.objects.create_user('testuser', 'testuser@testuser.com', password)
    user.first_name = 'Test'
    user.last_name = 'User'
    user.save()
    return user


def create_superuser(password=None):
    user = User.objects.create_superuser('admin', 'admin@website.com', password)
    return user


def temp_device(name='Test Device', description='Test device description'):
    ''' Returns device that is not added to the database '''
    return Device(name=name, description=description)


def temp_channel(name='Test Channel', device=None, sensor_type='Test Type'):
    ''' Returns channel that is not added to the database '''
    return Channel(name=name, device=device, sensor_type=sensor_type)


def create_device(user=None, name='Test Device'):
    ''' Creates a device for testing '''
    image='http://www.hotel-r.net/im/hotel/asia/lk/happy-banana-0.png'
    device = Device.objects.create(name=name, description='This is a test device',
                                    latitude=0, longitude=0,
                                    public=True, image=image, user=user)
    return device


def create_channel(device=None, name='Test Channel', sensor_type='Test Type'):
    ''' Creates a channel for testing '''
    channel = Channel.objects.create(name=name, device=device)
    return channel



# SUPERCLASS TESTS -------------------------------------------------------------
class DeviceTestsWithUser(TestCase):
    ''' Inherit for testing with a user logged in '''
    def setUp(self):
        # Create user
        password = 'qwerty'
        self.user = create_user(password=password)
        self.client = Client()
        self.loggedin = self.client.login(username=self.user.username, password=password)


class DeviceTestsWithDevices(DeviceTestsWithUser):
    ''' Inherit for testing with devices already in database
        user is required to add device (foreign key) '''
    def setUp(self):
        super().setUp()
        # Create device
        self.devices = []
        self.devices.append(create_device(user=self.user))
        self.devices.append(create_device(user=self.user, name='Another Test Device'))


class DeviceTestsWithChannel(DeviceTestsWithDevices):
    ''' Inherit for testing with channel already in database
        user is required to add device (foreign key)
        device required for channel (foreign key) '''
    def setUp(self):
        super().setUp()
        # Create channels
        self.channel = []
        for device in self.devices:
            self.channel.append(create_channel(device=device, name='Test Channel 1'))
            self.channel.append(create_channel(device=device, name='Test Channel 2'))



# TESTS ------------------------------------------------------------------------
class DeviceViewTestsNoData(TestCase):
    def test_device_index_with_no_devices(self):
        ''' If no device exists, an appropriate message should be displayed '''
        response = self.client.get(reverse('logIOT:devices'))
        # Check http response code is good
        self.assertEqual(response.status_code, 200)
        # Check correct message shows when user has no devices
        self.assertContains(response, "No devices")
        # Check there are actually no devices
        self.assertQuerysetEqual(response.context['object_list'], [])


class DeviceViewTests(DeviceTestsWithDevices):
    def test_device_index_with_some_devices(self):
        ''' If devices exist then they should be listed '''
        response = self.client.get(reverse('logIOT:devices'))
        # Check http response code is good
        self.assertEqual(response.status_code, 200)
        # Check devices are listed
        self.assertContains(response, "Test Device")
        self.assertContains(response, "Another Test Device")


class DeviceGeneralTests(TestCase):
    ''' General model tests without saving to database (faster) '''
    def test_create_new_device(self):
        # Device model
        device = temp_device()
        self.assertTrue(isinstance(device, Device))
        # Channel model
        channel = temp_channel(device=device)
        self.assertTrue(isinstance(channel, Channel))

    def test_device_str_method(self):
        # Device model
        device = temp_device()
        self.assertEqual(device.__str__(), device.name)
        # Channel model
        channel = temp_channel(device=device)
        channel_string = channel.name + ': ' + channel.sensor_type
        self.assertEqual(channel.__str__(), channel_string)

    @skipIf(True, "Device must be added to database and have a 'pk' i think for this to work")
    def test_device_absolute_url(self):
        device = temp_device()
        response = self.client.get(device.get_absolute_url())
        self.assertEqual(response.status_code, 200)

class DeviceGeneralTestsWithDb(DeviceTestsWithChannel):
    ''' General model tests using database entries '''
    def test_device_absolute_url(self):
        response = self.client.get(self.devices[0].get_absolute_url())
        self.assertEqual(response.status_code, 200)


class DeviceFormTests(TestCase):
    def test_cannot_leave_field_empty(self):
        # User adds device but leaves name field blank
        pass









