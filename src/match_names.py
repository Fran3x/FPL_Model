def neutralize_name(name):
    return name.replace(" ", "-").replace("ï", "i").replace("é", "e").replace("á", "a").replace("ó", "o").replace("Á", "A").replace("ø", "o").replace("ć", "c").replace("í", "i").replace("ú", "u").replace("Ć", "C").replace("ã", "a").replace("ğ", "g").replace("ş", "s").replace("É", "E").replace("ñ", "n").replace("Ł", "L").replace("ń", "n").replace("ß", "ss").replace("ç", "c").replace("İ", "I").replace("č", "c").replace("ö", "o").replace("ë", "e").replace("š", "s").replace("ä", "a").replace("Ç", "C").replace("ü", "u").replace("Ø", "O").replace("ú", "u").replace("ú", "u").replace("è", "e").replace("ê", "e").replace("î", "i").replace("ð", "d").replace("Š", "S")


names = {
    # understat: fpl
    'Cristiano Ronaldo': 'Cristiano Ronaldo dos Santos Aveiro',
    'Son Heung-Min': 'Heung-Min Son',
    'Raphinha': 'Raphael Dias Belloli',
    'Bruno Fernandes': 'Bruno Miguel Borges Fernandes',
    'Richarlison': 'Richarlison de Andrade',
    'Emile Smith-Rowe': 'Emile Smith Rowe',
    'Said Benrahma': 'Saïd Benrahma',
    'Bernardo Silva': 'Bernardo Mota Veiga de Carvalho e Silva',
    'Gabriel Jesus': 'Gabriel Fernando de Jesus',
    'Rodri': 'Rodrigo Hernandez',
    'Martin Odegaard': 'Martin Ødegaard',
    'Jorginho': 'Jorge Luiz Frello Filho',
    'Rodrigo': 'Rodrigo Moreno',
    'Gabriel Martinelli': 'Gabriel Teodoro Martinelli Silva',
    'Philippe Coutinho': 'Philippe Coutinho Correia',
    'Fabinho': 'Fabio Henrique Tavares',
    'Gabriel': 'Gabriel Magalhães',
    'Eddie Nketiah': 'Edward Nketiah',
    'Juan Camilo Hernández': 'Juan Camilo Hernández Suárez',
    'Bruno Guimarães': 'Bruno Guimarães Rodriguez Moura',
    'Joelinton': 'Joelinton Cássio Apolinário de Lira',
    'Ben Chilwell': 'Benjamin Chilwell',
    'Fred': 'Frederico Rodrigues de Paula Santos',
    'Sergi Canos': 'Sergi Canós',
    'Thiago Silva': 'Thiago Thiago',
    'Emiliano Buendía': 'Emiliano Buendía Stati',
    'Rúben Neves': 'Rúben Diogo da Silva Neves',
    'João Pedro': 'João Pedro Junqueira de Jesus',
    'Fernandinho': 'Fernando Luiz Rosa',
    'N&#039;Golo Kanté': "N'Golo Kanté",
    'Oriol Romeu': 'Oriol Romeu Vidal',
    'Jonny': 'Jonathan Castro Otto',
    'Lucas Moura': 'Lucas Rodrigues Moura da Silva',
    'João Moutinho': 'João Filipe Iria Santos Moutinho',
    'Romain Saiss': 'Romain Saïss',
    'Douglas Luiz': 'Douglas Luiz Soares de Paulo',
    'Joe Willock': 'Joseph Willock',
    'Marc Guehi': 'Marc Guéhi',
    'Daniel Podence': 'Daniel Castelo Podence',
    'Trincão': 'Francisco Machado Mota de Castro Trincão',
    'Ferrán Torres': 'Ferran Torres',
    'Rúben Dias': 'Rúben Santos Gato Alves Dias',
    'Dele Alli': 'Bamidele Alli',
    'Raphael Varane': 'Raphaël Varane',
    'Thiago Alcántara': 'Thiago Alcántara do Nascimento',
    'João Cancelo': 'João Pedro Cavaco Cancelo',
    'Ricardo Pereira': 'Ricardo Domingos Barbosa Pereira',
    'Tanguy NDombele Alvaro': 'Tanguy Ndombele',
    'Nicolas Pepe': 'Nicolas Pépé',
    'Pedro Neto': 'Pedro Lomba Neto',
    'Valentino Livramento': 'Tino Livramento',
    'Mads Roerslev': 'Mads Roerslev Rasmussen',
    'Nuno Tavares': 'Nuno Varela Tavares',
    'Mohamed Elneny': 'Mohamed Naser El Sayed Elneny',
    'Kenedy': 'Robert Kenedy Nunes do Nascimento',
    'Alisson': 'Alisson Ramses Becker',
    'Asmir Begovic': 'Asmir Begović',
    'Samir': 'Samir Caetano de Souza Santos',
    'Alex Telles': 'Alex Nicolao Telles',
    'Allan': 'Allan Marques Loureiro',
    'Nicolas N&#039;Koulou': 'Nicolas Nkoulou',
    'Emiliano Martinez': 'Emiliano Martínez',
    'Kepa': 'Kepa Arrizabalaga',
    'Solly March': 'Solomon March',
    'Ederson': 'Ederson Santana de Moraes',
    'Lyanco': 'Lyanco Evangelista Silveira Neves Vojnovic',
    'Boubakary Soumare': 'Boubakary Soumaré',
    'Nathan Ferguson': 'Nathan Ferguson',
    'Oghenekaro Etebo': 'Oghenekaro Peter Etebo',
    'Samuel Kalu': 'Samuel Kalu ',
    'Imran Louza': 'Imrân Louza',
    'Diogo Dalot': 'José Diogo Dalot Teixeira',
    'Wesley': 'Wesley Moraes',
    'Jaden Philogene-Bidace': 'Jaden Philogene-Bidace',
    'David Raya': 'David Raya Martin',
    'Kristoffer Klaesson': 'Kristoffer Klaesson',
    'Bali Mumba': 'Bali Mumba',
    'Alejandro Garnacho': 'Alejandro Garnacho Ferreyra',
    'Chiquinho': 'Sonny Chiquinho',
    'Toti': 'Toti António Gomes',
    'Kayky': 'Kayky da Silva Chagas',
    'Zanka': 'Mathias Jorgensen',
    'Júnior Firpo': 'Héctor Junior Firpo Adames',
    'Josh Dasilva': 'Pelenda Joshua Dasilva',
    'Caglar Söyüncü': 'Çaglar Söyüncü',
    'Emerson': 'Emerson Aparecido Leite de Souza Junior',
    'André Gomes': 'André Filipe Tavares Gomes',
    'Hélder Costa': 'Hélder Wander Sousa de Azevedo e Costa',
    'Kiko Femenía': 'Francisco Femenía Far',
    'Trézéguet': 'Mahmoud Ahmed Ibrahim Hassan',
    'Nélson Semedo': 'Nélson Cabral Semedo',
    'José Sá': 'José Malheiro de Sá',
    'Aleksandar Mitrovic': 'Aleksandar Mitrović',
    'Erling Haaland': 'Erling Håland',
    'Jefferson Lerma': 'Jefferson Lerma Solís',
    'Taiwo Awoniyi': '',
    'Darwin Núñez': 'Darwin Núñez',
    'Ivan Perisic': 'Ivan Perišić'
}


def name_fbref_to_fpl(name):
    # input name should be after neutralizing
    output = name
    if name == "Thiago-Alcantara":
        output = "Thiago-Alcantara-do-Nascimento"
    if name == "Alisson":
        output = "Alisson-Ramses-Becker"
    if name == "Miguel-Almiron":
        output = "Miguel Almirón Rejala"
    if name == "Antony":
        output = "Antony-Matheus-dos-Santos"
    if name == "Joe-Aribo":
        output = "Joe-Ayodele-Aribo"
    if name == "Bryan":
        output = "Bryan-Gil-Salvatierra"
    if name == "Thiago-Alcantara":
        output = "Thiago-Alcantara-do-Nascimento"
    if name == "Ederson":
        output = "Ederson-Santana-de-Moraes"
    if name == "Emi-Buendia":
        output = "Emiliano-Buendia-Stati"
    if name == "Moises-Caicedo":
        output = "Moises-Caicedo-Corozo"
    if name == "Fabio-Carvalho":
        output = "Fabio-Freitas-Gouveia-Carvalho"
    if name == "Casemiro":
        output = "Carlos-Henrique-Casimiro"
    if name == "Marc-Cucurella":
        output = "Marc-Cucurella-Saseta"
    if name == "Diogo-Dalot":
        output = "Diogo-Dalot-Teixeira"
    if name == "Ruben-Dias":
        output = "Ruben-Gato-Alves-Dias"
    if name == "Bruno-Fernandes":
        output = "Bruno-Borges-Fernandes"
    if name == "Gabriel-Jesus":
        output = "Gabriel Fernando de Jesus"
    if name == "Hugo-Bueno":
        output = "Hugo Bueno Lopez"
    if name == "Jonny-Castro":
        output = "Jonathan Castro Otto"
    if name == "Bruno-Guimaraes":
        output = "Bruno Guimarães Rodriguez Moura"
    if name == "Pierre-Hojbjerg":
        output = "Pierre-Emile Højbjerg"
    if name == "Joelinton":
        output = "Joelinton Cássio Apolinário de Lira"
    if name == "Darwin-Nunez":
        output = "Thiago-Alcantara-do-Nascimento"
    if name == "Andreas-Pereira":
        output = "Andreas-Hoelgebaum-Pereira"
    if name == "Richarlison":
        output = "Richarlison de Andrade"
    if name == "Martinelli":
        output = "Gabriel Martinelli Silva"    
    if name == "Bernardo-Silva":
        output = "Bernardo Veiga de Carvalho e Silva"
    if name == "Kostas-Tsimikas":
        output = "Konstantinos Tsimikas"
    if name == "Ben-White":
        output = "Benjamin White"
    if name == "Sergi-Canos":
        output = "Sergi Canós Tenés"
    if name == "Julio-Cesar-Enciso":
        output = "Julio Enciso"
    if name == "Diego-Costa":
        output = "Diego Da Silva Costa"
    if name == "Philippe-Coutinho":
        output = "Philippe Coutinho Correia"
    if name == "Gabriel-Dos-Santos":
        output = "Gabriel dos Santos Magalhães"
    if name == "Emerson":
        output = "Emerson Leite de Souza Junior"
    if name == "Fabinho":
        output = "Fabio Henrique Tavares"
    if name == "Junior-Firpo":
        output = "Junior Firpo Adames"
    if name == "Pablo-Fornals":
        output = "Pablo Fornals Malla"
    if name == "Fred":
        output = "Frederico Rodrigues de Paula Santos"
    if name == "Idrissa-Gana-Gueye":
        output = "Idrissa Gueye"
    if name == "David-de-Gea":
        output = "David De Gea Quintana"
    if name == "Degnand-Gnonto":
        output = "Wilfried Gnonto"
    if name == "Toti-Gomes":
        output = "Toti António Gomes"
    if name == "Joe-Gomez":
        output = "Joseph Gomez"
    if name == "Jorginho":
        output = "Jorge Luiz Frello Filho"
    if name == "Diogo-Jota":
        output = "Diogo Teixeira da Silva"
    if name == "Ezri-Konsa":
        output = "Ezri Konsa Ngoyo"
    if name == "Juan-Larios":
        output = "Juan Larios López"
    if name == "Jefferson-Lerma":
        output = "Jefferson Lerma Solís"
    if name == "Renan-Lodi":
        output = "Renan Augusto Lodi dos Santos"
    if name == "Douglas-Luiz":
        output = "Douglas Luiz Soares de Paulo"
    if name == "Lyanco":
        output = "Lyanco Silveira Neves Vojnovic"
    if name == "Javier-Manquillo":
        output = "Javier Manquillo Gaitán"
    if name == "Marquinhos":
        output = "Marcus Oliveira Alencar"
    if name == "Emiliano-Martinez":
        output = "Emiliano Martínez Romero"
    if name == "Lucas-Moura":
        output = "Lucas Rodrigues Moura da Silva"
    if name == "Joao-Moutinho":
        output = "João Filipe Iria Santos Moutinho"
    if name == "Vitaliy-Mykolenko":
        output = "Vitalii Mykolenko"
    if name == "Neto":
        output = "Norberto Murara Neto"
    if name == "Pedro-Neto":
        output = "Pedro Lomba Neto"
    if name == "Ruben-Neves":
        output = "Rúben da Silva Neves"
    if name == "Matheus-Nunes":
        output = "Matheus Luiz Nunes"
    if name == "Joao-Palhinha":
        output = "João Palhinha Gonçalves"
    if name == "Emerson-Palmieri":
        output = "Emerson Palmieri dos Santos"
    if name == "Lucas-Paqueta":
        output = "Lucas Tolentino Coelho de Lima"
    if name == "Daniel-Podence":
        output = "Daniel Castelo Podence"
    if name == "David-Raya":
        output = "David Raya Martin"
    if name == "Marc-Roca":
        output = "Marc Roca Junqué"
    if name == "Rodri":
        output = "Rodrigo Hernandez"
    if name == "Mads-Roerslev":
        output = "Mads Roerslev Rasmussen"
    if name == "Jose-Sa":
        output = "José Malheiro de Sá"
    if name == "Jeremy-Sarmiento":
        output = "Jeremy Sarmiento Morante"
    if name == "Luis-Sinisterra":
        output = "Luis Sinisterra Lucumí"
    if name == "Fabio-Vieira":
        output = "Fábio Ferreira Vieira"
    if name == "Ruben-Vinagre":
        output = "Rúben Nascimento Vinagre"
    if name == "Carlos-Vinicius":
        output = "Carlos Vinícius Alves Morais"
    if name == "Willian":
        output = "Willian Borges da Silva"
    if name == "Rodrigo":
        output = "Rodrigo Moreno"
    if name == "Nelson-Semedo":
        output = "Nélson Cabral Semedo"
    if name == "Thiago-Silva":
        output = "Thiago Emiliano da Silva"
    if name == "Cedric-Soares":
        output = "Cédric Alves Soares"
    if name == "Thiago-Alcantara":
        output = "Thiago-Alcantara-do-Nascimento"
    
    
    return neutralize_name(output)



def team_understat_to_fpl(team_name):
    if team_name == "Wolverhampton Wanderers":
        return "Wolves"
    if team_name == "Newcastle United":
        return "Newcastle Utd"
    if team_name == "Manchester United":
        return "Manchester Utd"
    if team_name == "Nottingham Forest":
        return "Nott'ham Forest"
    return team_name