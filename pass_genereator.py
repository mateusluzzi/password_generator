import string
import random

class Password:    
    """Senha customizada conforme força e tamanho definido pelo usuário
    
    :param strength: força da senha, de baixa a alta. 'low', 'mid', 'high'
    :type strength: str
    
    :param length: tamanho da senha em caracteres.
    :type length: int
    """
    
    input_universe = [list(string.ascii_letters),list(string.digits),list(string.punctuation)]    
    default_length = {
        'low':8,
        'mid':12,
        'high':16
    }
    
    @classmethod
    def show_input(cls):
        """Universo de caracteres considerados para criação da senha
        :return: Lista de listas contendo os caracteres usados para cada tipo de senha.
        :rtype: List
        """
        return cls.input_universe
    
    
    def __init__(self,strength='mid',length=None):
        self.strength = strength
        self.length = length
        if self.length == None:
            self.length = self.default_length[self.strength]
            
        self._generate()
        
        
    def _generate(self):
        password = []
        if self.strength == 'high':
            for i in range(self.length):
                password.append(random.choices(input_universe[random.randint(0,2)],k=1)[0])
        if self.strength == 'mid':
            for i in range(self.length):
                password.append(random.choices(input_universe[random.randint(0,1)],k=1)[0])
        if self.strength == 'low':
            for i in range(self.length):
                password.append(random.choices(input_universe[0],k=1)[0])
        self.password = ''.join(password)
        
