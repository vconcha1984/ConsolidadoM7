from django.test import TestCase

# Create your tests here.
from .models import Laboratorio
from django.urls import reverse

# Create your tests here.
class LaboratorioModelTest(TestCase):
    def setUp(self):
        self.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio de Prueba',
            ciudad='Concepción',
            pais='Chile'
        )
    
    def test_str_method(self):
        lab = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(lab.nombre,"Laboratorio de Prueba")
        self.assertEqual(lab.ciudad,"Concepción")
        self.assertEqual(lab.pais,"Chile")
    
    def test_laboratorio_url_status_code(self):
        response = self.client.get('/laboratorio/')
        self.assertEqual(response.status_code, 200)
    
    def test_index_template_and_content(self):
        response = self.client.get(reverse('laboratorio:index'))
        self.assertEqual(response.status_code, 200)
        
        self.assertTemplateUsed(response, 'laboratorio/index.html')
        self.assertContains(response, 'Laboratorio de Prueba')