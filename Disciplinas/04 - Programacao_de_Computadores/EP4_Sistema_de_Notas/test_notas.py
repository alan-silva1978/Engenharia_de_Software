import unittest

# Importação das funções do módulo principal do sistema acadêmico
# Nota: Adapte 'seu_arquivo_principal' para o nome exato do seu arquivo Python (ex: media_notas_alunos)
from media_notas_alunos import calcular_media, verificar_aprovacao

class TestSistemaNotas(unittest.TestCase):

    def test_calcular_media_normal(self):
        """Testa e confere as médias normais limpas."""
        self.assertEqual(calcular_media([10.0, 8.0]), 9.0)

    def test_calcular_media_vazia(self):
        """Testa o caso extremo (edge case limitador) com a lista de notas vazia."""
        self.assertEqual(calcular_media([]), 0.0)

    def test_verificar_aprovacao_normal(self):
        """Verifica as condições normais de aprovação."""
        self.assertEqual(verificar_aprovacao(8.5), "Aprovado")
        
    def test_verificar_reprovacao_normal(self):
        """Verifica as condições normais de reprovação."""
        self.assertEqual(verificar_aprovacao(5.0), "Reprovado")

    def test_verificar_aprovacao_corte_zero(self):
        """Testa a estabilidade da aprovação informando zero na média de corte."""
        # Se a média é 0 e a nota de corte é 0, a relação (media >= media_minima) deve retornar 'Aprovado'
        self.assertEqual(verificar_aprovacao(0.0, media_minima=0), "Aprovado")

if __name__ == '__main__':
    unittest.main()