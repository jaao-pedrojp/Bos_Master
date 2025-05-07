import sqlite3

def init_db():
    conn = sqlite3.connect('rpg_rules.db')
    c = conn.cursor()

    # Create table for RPG rules
    c.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            keywords TEXT NOT NULL
        )
    ''')

    # Clear existing data
    c.execute('DELETE FROM rules')

    # Insert detailed RPG rules with more explanatory descriptions
    rules = [
        ("Objetivo do Jogo", 
         "O objetivo principal do jogo é eliminar todos os adversários até que reste apenas um jogador vencedor. "
         "Cada jogador deve usar suas habilidades, estratégias e recursos para superar os demais participantes e alcançar a vitória final.", 
         "objetivo,eliminar,adversários,jogador"),
        
        ("Criação da Partida", 
         "Na criação da partida, todos os personagens começam com o mesmo nível básico de invulnerabilidade, força e velocidade. "
         "Esses atributos podem variar dependendo dos poderes ou bênçãos que cada personagem recebe, influenciando seu desempenho durante o jogo.", 
         "personagens,nível,invulnerabilidade,força,velocidade,poder"),
        
        ("Poderes", 
         "Cada jogador sorteia um poder especial de uma lista específica disponível no jogo. "
         "Esses poderes conferem habilidades únicas que podem ser usadas estrategicamente para obter vantagem durante a partida.", 
         "poder,jogador,sorteia,lista"),
        
        ("Mimetismo", 
         "O mimetismo permite que cada jogador sorteie uma transformação especial de uma lista específica, "
         "que pode alterar suas habilidades ou aparência, proporcionando vantagens táticas no jogo.", 
         "mimetismo,jogador,sorteia,transformação,lista"),
        
        ("Armas", 
         "Antes do início da partida, cada jogador sorteia uma arma que pode ser corpo a corpo (melee) ou de fogo. "
         "A escolha da arma influencia o estilo de combate e as estratégias que o jogador poderá utilizar.", 
         "arma,jogador,sorteia,melee,fogo"),
        
        ("Local de Luta", 
         "O local onde a batalha acontece é escolhido aleatoriamente a partir de uma lista de locais variados. "
         "Cada local pode apresentar características únicas que influenciam o ambiente e as estratégias dos jogadores.", 
         "local,luta,escolhido,aleatoriamente,batalha,lista"),
        
        ("Vestimenta", 
         "Os personagens usam um macacão cinza padrão equipado com diversos gadgets tecnológicos que variam conforme a bênção recebida. "
         "Essas vestimentas proporcionam habilidades e vantagens específicas durante o jogo, influenciando a performance do jogador.", 
         "vestimenta,macacão,cinza,gadgets,bênção"),
        
        ("Turnos", 
         "O jogo é estruturado em turnos, onde cada jogador tem direito a realizar suas ações uma vez por turno. "
         "A ordem dos turnos é respeitada para garantir a organização e o equilíbrio da partida.", 
         "turno,jogador,direito"),
        
        ("Ações Livres", 
         "Ações livres são ilimitadas e incluem atividades como falar, se locomover a pequenas distâncias e descrever sua aparência e vestimenta livremente. "
         "Não há restrições de regras para essas ações, permitindo que cada jogador expresse sua criatividade e personalidade durante o jogo.", 
         "ações livres,ilimitadas,falar,locomover,pequenas distâncias,descrição,aparência,vestimenta"),
        
        ("Ações Padrão", 
         "Ações padrão são aquelas limitadas por turno e incluem andar, correr, realizar acrobacias e atacar. "
         "Essas ações são fundamentais para o progresso do jogo e exigem planejamento estratégico por parte dos jogadores.", 
         "ações padrão,andar,correr,acrobacia,ataque,limite"),
        
        ("Sistema de Ações", 
         "O sistema de ações utiliza um dado D20 para determinar o sucesso ou falha em ataques e outras ações padrão. "
         "O resultado do dado influencia diretamente o desenrolar das situações de combate e desafios.", 
         "sistema,ações,dado,D20,sucesso,falha,ataques"),
        
        ("Sucesso", 
         "Quando um ataque ou ação é bem-sucedida, o dano é aplicado com base em um dado D6. "
         "Há possibilidade de sucesso crítico, que causa efeitos adicionais, e sequelas que podem afetar o desempenho futuro do jogador.", 
         "sucesso,dano,D6,sucesso crítico,sequelas"),
        
        ("Falha", 
         "Falhas críticas podem causar sequelas negativas e dependem da interpretação do mestre ou dos jogadores. "
         "Essas falhas adicionam elementos de imprevisibilidade e desafio ao jogo.", 
         "falha,crítica,sequelas,interpretação,mestre,jogador"),
        
        ("Defesa", 
         "Jogadores atacados podem rolar um dado D6 para tentar evitar parte do dano recebido. "
         "O sucesso parcial na defesa reduz o impacto do ataque, aumentando as chances de sobrevivência.", 
         "defesa,dado,D6,evitar,dano,parcial"),
        
        ("Barra de Vida", 
         "Cada jogador começa com 100 pontos de vida, que podem variar dependendo das bênçãos recebidas. "
         "A barra de vida indica a saúde atual do personagem e influencia sua capacidade de continuar na partida.", 
         "barra de vida,pontos de vida,jogador,bênção"),
        
        ("Eliminação", 
         "Um jogador é eliminado quando seus pontos de vida chegam a zero. "
         "Em algumas situações específicas, pode haver a possibilidade de retorno ao jogo, conforme regras especiais.", 
         "eliminação,pontos de vida,voltar,situações"),
        
        ("Recuperação", 
         "Não existe recuperação de vida padrão, exceto por habilidades específicas como o mimetismo da salamandra, "
         "que deve ser interpretado pelo mestre para equilibrar o jogo.", 
         "recuperação,vida,mimetismo,salamandra,interpretação,mestre"),
        
        ("Alianças", 
         "Jogadores podem formar alianças temporárias para obter vantagens estratégicas, "
         "mas devem desfazê-las para alcançar a vitória, pois não há possibilidade de vitória dupla.", 
         "alianças,jogadores,formar,desfazer,vitória"),
        
        ("Final da Partida", 
         "A partida termina quando apenas um jogador permanece vivo, que é declarado o vencedor oficial do jogo.", 
         "final,partida,jogo,jogador,vencedor"),
        
        ("Novidades", 
         "O transmorfismo animal permite que jogadores se transformem em animais com habilidades extras, "
         "mas essa transformação custa um turno para ser realizada, exigindo planejamento.", 
         "novidades,transmorfismo animal,transformação,animal,habilidades,turno"),
        
        ("Bênção Antiga", 
         "Bênçãos antigas são itens escondidos no mapa que concedem passivas vantajosas aos jogadores, "
         "limitadas a três por jogador para manter o equilíbrio do jogo.", 
         "bênção antiga,bênçãos,itens,mapa,passivas,limite"),
    ]

    c.executemany('INSERT INTO rules (category, description, keywords) VALUES (?, ?, ?)', rules)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    print("Banco de dados atualizado com as regras detalhadas do RPG.")
