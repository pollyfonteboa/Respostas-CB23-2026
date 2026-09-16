\#1



As classe podem ser organizadas em 3 classes bases: Pessoas, Restaurante e Iguarias. 



A ordem hierárquica será definida de cima para baixo a seguir:







1° Classe base: Pessoa



Subclasse 1: Funcionário (herda os atributos de pessoa)



Subclasses 2: Chef de cozinha/ Gerente/ Garçom (os três herdam os atributos de funcionário e consequentemente de pessoa)







2° Classe base: Restaurante



Subclasse 1: Pizzaria(herda os atributos de restaurante)







3° Classe base: Iguaria 



Subclasse 1: Pizza/ Bolo  (os dois herdam os atributos de Iguaria)







\#2



Para fazer a associação entre Restaurante e Iguarias pode-se criar uma Classe de associação "Cardápio", que irá ter como atributos as classes Restaurante e Iguaria. Essa classe de associação receberia os dados de restaurante e os dados de iguaria associados a esse restaurante, montando-se assim um cardápio que associa o restaurantes às iguarias presentes nele.







\#3



Argumento 1: \*\*Lista de\*\* \*\*Instâncias de Iguaria\*\*



Como Iguaria recebe como argumento as instâncias de pizza e bolo, o garçom pode anotar o pedido de uma mesa como uma lista de Iguarias, podendo realizar o pedido e acompanhar os preços para fechar a conta no final.







Argumento 2: \*\*Instâncias de bolo e pizza\*\*



Como o chefe de cozinha precisa dos dados completos dos pratos e não precisa anotar os valores, deve receber as instâncias de bolo e pizza.





Argumento 3: \*\*Instâncias de Funcionário\*\*



Ele irá receber todos os atributos do funcionário e de pessoa, necessários para que ele realize a demissão e rescisão de contrato de qualquer cargo.



