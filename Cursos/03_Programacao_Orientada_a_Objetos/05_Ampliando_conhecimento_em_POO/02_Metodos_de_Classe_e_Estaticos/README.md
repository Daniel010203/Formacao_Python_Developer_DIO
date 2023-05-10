# Métodos de classe e Métodos estático

Métodos de classe e métodos estáticos são ambos tipos de métodos em programação orientada a objetos.

Os métodos de classe são aqueles que são associados à classe em si e não a instâncias da classe. Eles podem acessar e modificar atributos de classe, mas não podem acessar atributos de instância. O primeiro parâmetro de um método de classe é geralmente chamado de "cls" e é usado para se referir à classe.

Já os métodos estáticos são métodos que pertencem à classe, mas não dependem de nenhum atributo de classe ou instância. Eles são geralmente usados para funções de utilidade que não estão diretamente relacionadas a instâncias ou atributos da classe.

Em Python, para definir um método de classe, basta usar o decorador @classmethod antes da definição do método e incluir o parâmetro "cls" como primeiro parâmetro. Para definir um método estático, basta usar o decorador @staticmethod antes da definição do método. Ambos os tipos de métodos podem ser chamados diretamente da classe, sem precisar criar uma instância da classe.

---