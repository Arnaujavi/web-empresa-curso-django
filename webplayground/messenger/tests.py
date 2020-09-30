from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')#None es donde iria el email que en este caso no le asignamos ninguno
        self.user2 = User.objects.create_user('user2', None, 'test1234')
        self.user3 = User.objects.create_user('user3', None, 'test1234')

        self.thread = Thread.objects.create()
    
    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)#Añadimos los dos usuarios al hilo(Thread)
        self.assertEqual(len(self.thread.users.all()), 2)#Mediremos la longitud los hilos con el length que en teoria deberian de ser los dos user creados
    
    def test_filter_thread_by_users(self):
        self.thread.users.add(self.user1, self.user2)#Añadimos los dos usuarios al hilo(Thread)
        threads = Thread.objects.filter(users = self.user1).filter(users = self.user2)#Como es un query set podemos añadir tantos filtros como queramos
        self.assertEqual(self.thread, threads[0])
    
    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(users = self.user1).filter(users = self.user2)#Como es un query set podemos añadir tantos filtros como queramos
        self.assertEqual(len(threads), 0)#Mediremos la longitud los hilos con el length que en teoria deberian de ser los threads creados anteriormente que deberian de ser 0

    def test_add_message_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        message1 = Message.objects.create(user = self.user1, content = "Muy buenas")
        message2 = Message.objects.create(user = self.user2, content = "Hola")
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for message in self.thread.messages.all():
            print("({}): {}".format(message.user, message.content))

    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)#Añadimos al hilo los usuarios 1 y 2 
        message1 = Message.objects.create(user = self.user1, content = "Muy buenas")
        message2 = Message.objects.create(user = self.user2, content = "Hola")
        message3 = Message.objects.create(user = self.user3, content = "Soy un espia")
        self.thread.messages.add(message1, message2, message3)
        self.assertEqual(len(self.thread.messages.all()), 2)    
    
    def test_find_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)#Añadimos al hilo los usuarios 1 y 2 
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, thread)

    def test_find_or_create_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)#Añadimos al hilo los usuarios 1 y 2 
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.thread, thread)
        thread = Thread.objects.find_or_create(self.user1, self.user3)
        self.assertIsNotNone(thread)