import time

print("Bem-vindo ao MormonPedia!")
print("Esta enciclopédia é dedicada a fornecer informações para os membros da Igreja de Jesus Cristo dos Santos dos Últimos Dias (Mórmon).")
print("Muito obrigado por aceitar o nosso presente! :-)")
print("Por favor, escolha um artigo para ler:")

time.sleep(1)

print("1. O que é a Igreja de Jesus Cristo dos Santos dos Últimos Dias?")
print("2. Quem é Joseph Smith?")
print("3. O que é o Livro de Mórmon?")
print("4. Quem é Jesus Cristo?")
print("5. Quem é Deus, o nosso Pai Celestial?")
print("6. Quem é o Espírito Santo?")
print("7. Créditos e agradecimentos")

artigo = input("Digite o número do artigo que quer ler: ")

if artigo == "1":
    print("\nA Igreja de Jesus Cristo dos Santos dos Últimos Dias, ou igreja Mórmon, é uma religião cristã que acredita que Jesus Cristo é o Salvador do mundo e que Deus, o Pai Celestial, é o nosso Pai. Foi fundada por Joseph Smith em 1830. A igreja tem mais de 16 milhões de membros em todo o mundo.")
elif artigo == "2":
    print("\nJoseph Smith foi o fundador da Igreja de Jesus Cristo dos Santos dos Últimos Dias. Nascido em 1805 em Vermont, ele teve uma série de visões e revelações que levaram ao restabelecimento da igreja em 1830. Ele traduziu o Livro de Mórmon e liderou a igreja até sua morte em 1844.")
elif artigo == "3":
    print("\nO Livro de Mórmon é um livro sagrado que os membros da Igreja acreditam ser outro testamento de Jesus Cristo. Ele foi traduzido por Joseph Smith a partir de placas de ouro que ele disse ter recebido de um anjo chamado Morôni. O livro narra a história de antigos habitantes das Américas e seus ensinamentos de Jesus Cristo.")
elif artigo == "4":
    print("\nJesus Cristo é o Filho de Deus e o Salvador do mundo. Nasceu em Belém, viveu uma vida perfeita, ensinou o evangelho e morreu na cruz para expiar os pecados da humanidade. Ele ressuscitou dos mortos e oferece a todos a oportunidade de voltar a viver com Deus.")
elif artigo == "5":
    print("\nDeus, o nosso Pai Celestial, é o Criador do universo e de todos nós. Ele nos ama, conhece cada um de seus filhos e deseja que retornemos a Sua presença. Ele nos deu um plano de felicidade e enviou Jesus Cristo para ser nosso Salvador.")
elif artigo == "6":
    print("\nO Espírito Santo é o terceiro membro da Trindade. Ele é um ser espiritual que testifica de Jesus Cristo, consola, guia e inspira as pessoas. Os membros da Igreja acreditam que podem sentir a influência do Espírito Santo ao viverem de acordo com os ensinamentos de Deus.")
elif artigo == "7":
    print("\nCréditos e agradecimentos:\nCriador: MiloMilow\nLicença: MIT\nAgradecemos a todos que contribuíram para este projeto e aos membros da Igreja de Jesus Cristo dos Santos dos Últimos Dias por sua fé e dedicação.")
else:
    print("\nArtigo não encontrado. Por favor, escolha um número de 1 a 7.")