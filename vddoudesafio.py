jogo = input("Se você quiser jogar no modo de amigos, digite 'amigos' "
             "\nSe quiser no modo de casal, digite 'casal':")

from random import randint
import time

desafio_casal_pesado = {
    0: "DESAFIO: Tirem uma peça de roupa um do outro",
    1: "DESAFIO: Tire a blusa de seu/sua parceira usando somente os dentes",
    2: "DESAFIO: Tire duas peças da sua roupa",
    3: "DESAFIO: Chupe um dos dedos delx",
    4: "DESAFIO: Acaricie o corpo delx enquanto faz uma cara senxual",
    5: "DESAFIO: Não se mexa por 1 min. e permita que elx faça o que quiser com você,"
         "\nse estx disse não, pare imediatamente",
    6: "DESAFIO: Faça uma mímica sexual e elx terá que adivinhar o ato",
    7: "DESAFIO: Beije a parte inferior da barriga delx",
    8: "DESAFIO: Imite poses de sessão de fotos sexy",
    9: "DESAFIO: Beije elx da forma mais intensa possível",
    10: "DESAFIO: Beije uma parte da bunda delx",
    11: "DESAFIO: De olhos fechados, elx coloca a sua mão em alguma parte do corpo delx,"
              "\ne vocÊ terá que adivinhar que parte é aquela",
    12: "DESAFIO: De um tapa na bunda delx sem nada por cima",
    13: "DESAFIO: Troquem toques em suas partes íntimas",
    14: "DESAFIO: Tire sua parte íntima e coloque na sua cabeça, "
          "\nfique assim por 3 rodadas",
    15: "DESAFIO: Troquem toque no mamilo",
    16: "DESAFIO: Permita que elx grave você dançando funk ou rebolando",
    17: "DESAFIO: Troque de roupas com elx por 3 rodadas",
    18: "DESAFIO: Imite uma posição sexual",
    19: "DESAFIO: Explore devagar e intensamente o corpo da outra pessoa",
    20: "DESAFIO: Fique de 4 e deixe o outro apreciar a visão",
    21:"DESAFIO: Lamba a barriga do seu parceiro até chegar na sua boca e beije-x",
    22: "DESAFIO: Deixe que alguém do grupo te faça um chupão no pescoço",
    23: "DESAFIO: Deixe que elx faça uma massagem, com direito a beijos intensos",
    24: "DESAFIO: ",
    25: "DESAFIO: Termine todas as frases com sexy até a sua próxima rodada",
}

verdade_casal_pesado = {
    0: "Com que idade você se masturbou pela primeira vez?",
    1: "Qual foi o lugar mais exótico que você se masturbou?",
    2: "Que tipo de pornografia te excita?",
    3: "Já fez strip-tease?",
    4: "Já fez sexo virtual?",
    5: "Em casa ou no motel?",
    6: "Já foi num sex-shop?",
    7: "O que você gostaria de comprar em um sex-shop?",
    8: "Já ficou com alguém comprometido?",
    9: "Já usou algo pra lubrificar que não era lubrificante?",
    10: "Já foi pego no flagra transando ou e masturbando?",
    11:"Já ficou com vontade de vomitar durante o sexo oral?",
    12: "Já beijou a três?",
    13:"O que você tem mais medo que te aconteça durante o sexo?",
    14: "Prefere devagarzinho ou rápido?",
    15: "Você toparia usar uma cueca/calcinha comestível?",
    16: "No que você pensa enquanto está se masturbando?",
    17: "Qual o segredo pra te deixar louco de tesão?",
    18: "Qual o seu segredo pra deixar alguém louco de tesão?",
    19: "Prefere ficar por cima ou por baixo?",
    20: "O que você pensa sobre ser tocado por trás?",
    21: "Se fosse tirar uma peça de roupa delx, qual seria?",
    22: "Descreva o ambiene perfeito para uma noite de sexo?",
    23: "Amor ou sexo?",
    24: "Você já teve um sonho erótico com elx? "
              "\nSe sim, conte ele",
    25:"Que tipo de música é perfeito pra transar?",
}

desafio_casal = {
    0: "DESAFIO: Beije as costas do outro participante formando um número"

              "\ne elx vai ter que adivinhar qual é",
    1: "DESAFIO: Sopre delicadamente o pescoço do outro participante",
    2: "DESAFIO: Escolha uma parte do corpo delx que esteja quente,"
              "\n e derreta um cubo de gelo",
    3: "DESAFIO: Beije os tornozelos delx",
    4: "DESAFIO: Beije delicadamente a orelha delx",
    5: "DESAFIO: Faça uma declaração de amor verdadeira",
    6: "DESAFIO: Beije a barriga delx em um forma geométrica e faça com qeu elx adivinhe",
    7: "DESAFIO: Faça cafuné nelx",
    8: "DESAFIO: Ensine elx a rebolar",
    9: "DESAFIO: Cante um rap sobre sua situação amorosa",
    10: "DESAFIO: Faça uma massagem nos ombros delx",
    11: "DESAFIO: Faça uma mímica e elx terá que adivinhar o ato",
    12: "DESAFIO: Troquem olhares fixamente, o primeiro a desviar o olhar perde"
              "\ne se a pessoa quiser, este terá que realizar um pedido",
    13: "DESAFIO: De um apelido para elx, e chame-x assim até o final do jogo",
    14: "DESAFIO: Lamba seu cotovelo",
    15: "DESAFIO: Cheire o suvaco delx",
    16: "DESAFIO: Tirem 2 selfies cada um com com as piores caretas possíveis"
              "\nquem tiver a pior ganha, e se quiser pode pedir um desejo ao outro",
    17: "DESAFIO: Desenha um bigode nelx com a língua",
    18: "DESAFIO: Simule um pedido de casamento",
    19: "DESAFIO: Beije elx da forma masi intensa e apaixonante possível",
    20: "DESAFIO: Façam uma guerra de travesseiro",
    21: "DESAFIO: Oferença uma massagem onde elx quiser",
    22: "DESAFIO: De um tapa na bunda delx sem nada por cima",
    23: "DESAFIO: Coloque uma bala na boca e beije-x",
    24: "DESAFIO: Faça 5 flexões com elx embaixo, e a cada descida de um beijo nelx",
    25: "DESAFIO: Descreva elx em uma palavra",
}

verdade_casal = {
    0: "Você já saiu com várias pessoas ao mesmo tempo?",
    1: "Você ja foi numa praia de nudismo?",
    2:"Você ja gostou da mesma pessoa que o seu amigo?",
    3: "Você terminaria com elx por 1 trilhão de dólares?",
    4: "Quantas pessoas você já beijou?",
    5: "Alguma vez você ja gostou de algum professor(a)?",
    6: "Qual o seu talento secreto?",
    7: "Conte a sua história masi embaraçadora?",
    8: "Qual a pior coisa de ter o seu gênero?",
    9: "Você lembra com detalhes a primeira vez que a vocês se beijaram?",
    10: "Qual foi o maior problema que você e elx já tiveram?",
    11: "Em algum momento você mentiu pra elx?",
    12: "Você já fez um strip-tease?",
    13: "Qual o lugar mas estranho que você ficou com tesão?",
    14: "Qual a coisa mais embaraçosa qeu vocÊ já fez por elx?",
    15: "Qual a coisa qeu você masi gosta delx?",
    16: "Se você pudesse escolher um nome pra elx, qual seria?(não pode ser o mesmo)",
    17: "Qual foi a coisa masi irritante qeu elx fez pra você?",
    18: "Qual é a sua maior insegurança?",
    19: "Qual é o melhor lugar para se beijar?",
    20: "Qual é a coisa que você mais se arrepende em fazer?",
    21: "Você ronca a noite?",
    22: "Se fosse para vocês morem em outro país, qual você escolheria?",
    23: "Como foi o seu primeiro beijo?",
    24: "Qual foi o seu pior encontro??",
    25: "Você já mandou fotos despido(a)",
}

desafio_amigos = {
    0: "DESAFIO: Molhe o rosto e passe farinha",
    1: "DESAFIO: Tente cantar 'galinha pintadinha' com a boca cheia de água",
    2: "DESAFIO: Imite um peixe fora da água",
    3: "DESAFIO: Dance 'oi, oi, oi'",
    4:"DESAFIO: Cante um funk como se fosse ópera",
    5:"DESAFIO: Arraste sua bunda no chão com se fosse um cachorro com coceira",
    6:"DESAFIO: Vá até o seu vizinho e pergunte se ele tem um preservativo pra te dar",
    7: "DESAFIO: Vá para o banheiro com a pessoa a sua direita e fique lá 5 min",
    8: "DESAFIO: Faça 30 flexões e 50 abdominais",
    9: "DESAFIO: Deixe todos te maquiarem da forma que quiserem",
    10: "DESAFIO: Mastigue um chiclete mastigado por outra pessoa",
    11: "DESAFIO: Permita que a pessoa a sua esquerda quebre um ovo cru na sua cabeça",
    12: "DESAFIO: Engula uma colher de chá de ketchup, mostarda, ou algo semelhante",
    13: "DESAFIO: Arrote o alfabeto",
    14: "DESAFIO: Finge que está balada e mostre como você iria conquistar o crush",
    15: "DESAFIO: Faça um quadradinho de 8",
    16: "DESAFIO: Rateje-se como uma cobra",
    17: "DESAFIO: Chupar um limão como se fosse uma laranja docinha",
    18: "DESAFIO: Coce a orelha com o seu pé",
    19: "DESAFIO: Faça uma pose de yoga e fique parado por 15 seg.",
    20: "DESAFIO: Tente vender a blusa da pessoa a direita como se fosse uma blogueira",
    21: "DESAFIO: Conte uma história desagradável e use tantas palavras sujas quanto possíve",
    22: "DESAFIO: Desfile como se fosse a Gisele Bündchen",
    23: "DESAFIO: Queime uma parte dos pêlos da sua perna",
    24: "DESAFIO: Beba uma mistura que o grupo dize",
    25: "DESAFIO: Beba um copo de água usando os pés",
}

verdade_amigos ={
    0: "Qual a sua mania mais nojenta?",
    1: "O que você faria se tivesse com dor de barriga e tivesse que"
        "\ncagar em um banheiro público, mas acabasse o papel higiênico?",
    2: "Qual a pessoa mais aleatória que você ja stalkeou nas redes sociais?",
    3: "Quantos dias vocÊ ja ficou sem tomar banho?",
    4: "Conte aqui uma coisa que você espera que os seus pais nunca descubrem?",
    5: "Você já cagou no mato?",
    6: "O que você faria se fosse do sexo oposto por um dia?",
    7: "Você já roubou algo?",
    8: "Qual foi a sua maior conquista?",
    9: "Você já quis vomitar mas estava em um lugar público e engoliu o vômito?",
    10: "Qual o momento masi inapropriado em que você peidou?",
    11: "Você mentiu nesse jogo?",
    12: "Quando foi a última vez qeu você chorou, poe quê?",
    13: "Quando foi a última vez que você mijou na cama?",
    14: "Você já fez cocô nas calça em público?",
    15: "Se você pudesse mudar algo na sua vida o que seria?",
    16: "Qual super poder você gostaria de ter?",
    17: "Quem é a pessoa mais bonita das que estão jogando(você mesmo não pode)?",
    18: "Com que pessoa você se arrepende de ter se envolvido?",
    19: "Qual a razão mais boba que você brigou com alguém?",
    20: "Qual foi o pior presente que vocÊ ja deu pra alguém?",
    21: "De que pessoa não famosa você tem inveja?",
    22: "Se você pudesse mudar de vida com uma celebridade por um dia, quem seria?",
    23: "Qual foi a coisa mais ilegal que você ja fez?",
    24: "Quantas pessoas você beijou esse ano?",
    25: "Quem foi a sua primeira paixão, que ano?",
}

desafio_amigos_pesado = {
    0: "DESAFIO: Imite como uma gata mia ao transar",
    1: "DESAFIO: Simule o seu olhar mais sexy para alguém que esteja jogando",
    2: "DESAFIO: Morda de leve o pescoço de alguém da roda",
    3: "DESAFIO: Com os olhos fechados, encoste a mão em alguém da roda"
              "\ne adivinhe qual é a parte do corpo (com consentimento)",
    4: "DESAFIO: Simule um sexo oral com uma fruta",
    5: "DESAFIO: Beije alguém da roda (com consentimento)",
    6: "DESAFIO: Coloque um cubo de gelo na boca e beije "
              "\no pescoço da pessoa a sua direita",
    7: "DESAFIO: Mande uma mensagem de voz sexy para o seu crush",
    8: "DESAFIO: Feche os olhos, alguém da roda de te dá um "
          "\nbeijo e você precisa adivinhar quem é",
    9: "DESAFIO: De um beijo (do jeito que quiser) em todos os participantes",
    10: "DESAFIO: Sente-se no colo de alguém por 10 min",
    11: "DESAFIO: Diga algo muito sujo a pessoa a sua esquerda",
    12: "DESAFIO: De uma aula de educação sexual",
    13: "DESAFIO: De uma mordida em alguém da roda",
    14: "DESAFIO: Ensine os outros integrantes a fazer o quadradinho",
    15: "DESAFIO: Ensine a fazer o sexo oral perfeito utilizando uma banana",
    16: "DESAFIO: Deixe que alguém do grupo faça um chupão nas suas costas",
    17: "DESAFIO: Simule um orgasmo",
    18: "DESAFIO: Troque de blusa com algum integrante do grupo",
    19: "DESAFIO: Ensine o grupo a fazer um strip-tease",
    20: "DESAFIO: Escolha duas pessoas e deem um beijo triplo",
    21: "DESAFIO: Bata na bunda de uma mulher e um homem da roda",
    22: "DESAFIO: Faça uma posição sexy e deixe todos os outros apreciarem",
    23: "DESAFIO: Imite um coelho transando intensamente com um travesseiro",
    24: "DESAFIO: Mostre a cor da sua cueca ou calcinha para todos",
    25: "DESAFIO: Permite que tirem uma foto sua com outra pessoa na posição bunda-bunda",
}

verdade_amigos_pesado ={
    0: "Com que idade você se masturbou pela primeira vez?",
    1: "Qual parte do corpo você beijaria da pessoa a sua esquerda?",
    2: "Que tipo de pornografia te excita?",
    3: "Já fez strip-tease?",
    4: "Já fez sexo virtual?",
    5: "Em casa ou no motel?",
    6: "Já foi num sex-shop?",
    7: "O que você gostaria de comprar em um sex-shop?",
    8: "Já ficou com alguém comprometido?",
    9: "Já usou algo pra lubrificar que não era lubrificante?",
    10: "Já foi pego no flagra transando ou e masturbando?",
    11: "Já ficou com vontade de vomitar durante o sexo oral?",
    12: "Já beijou a três?",
    13: "O que você tem mais medo que te aconteça durante o sexo?",
    14: "Prefere devagarzinho ou rápido?",
    15: "Você toparia usar uma cueca/calcinha comestível?",
    16: "No que vocÊ pensa enquanto está se masturbando?",
    17: "Qual o segredo pra te deixar louco de tesão?",
    18: "Qual o seu segredo pra deixar alguém louco de tesão?",
    19: "Prefere ficar por cima ou por baixo?",
    20: "O que você pensa sobre ser tocado por trás?",
    21: "Se fosse tirar uma peça de roupa da pessoa à sua direita, qual seria?",
    22: "Descreva o ambiene perfeito para uma noite de sexo?",
    23: "Amor ou sexo?",
    24: "Qual é a pessoa mais sexy participando do jogo?",
    25: "Que tipo de música é perfeito pra transar?",
}

if jogo.lower() == "casal":
    nome1 = input("Nome1:")
    nome2 = input("Nome2:")
    while True:
        pesado = input("Você quer jogar no modo pesado(+18)?(sim ou não)")
        print("LEMBRE-SE QUE TUDO TEM QUER SER FEITO COM CONSENTIMENTO")
        pesado = pesado.replace("ã", "a")
        if pesado.lower() == "nao":
            time.sleep(0.3)
            print("Girando a roleta")
            time.sleep(1)
            resultado = randint(0, 1)
            if resultado == 0:
                ordem = randint(0, 1)
                if ordem == 0:
                    print("Verdade para", nome1)
                else:
                    print("Verdade para", nome2)
                manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                manual1 = manual1.lower()
                manual1 = manual1.replace("ã", "a")
                if manual1 == "nao":
                    verdade_casal = verdade_casal[randint(0, 25)]
                    print(verdade_casal)
                    input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
            else:
                ordem = randint(0, 1)
                if ordem == 0:
                    print("Desafio para", nome1)
                else:
                    print("Desafio para", nome2)
                manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                manual2 = manual2.lower()
                manual2 = manual2.replace("ã", "a")
                if manual2 == "nao":
                    desafio_casal = desafio_casal[randint(0, 25)]
                    print(desafio_casal)
                    input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
        else:
            time.sleep(0.3)
            print("Girando a roleta")
            time.sleep(1)
            resultado = randint(0, 1)
            if resultado == 0:
                ordem = randint(0, 1)
                if ordem == 0:
                    print("Verdade para", nome1)
                else:
                    print("Verdade para", nome2)
                manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                manual1 = manual1.lower()
                manual1 = manual1.replace("ã", "a")
                if manual1 == "nao":
                    verdade_casal_pesado = verdade_casal_pesado[randint(0, 25)]
                    print(verdade_casal_pesado)
                    input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
            else:
                ordem = randint(0, 1)
                if ordem == 0:
                    print("Desafio para", nome1)
                else:
                    print("Desafio para", nome2)
                manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                manual2 = manual2.lower()
                manual2 = manual2.replace("ã", "a")
                if manual2 == "nao":
                    desafio_casal_pesado = desafio_casal_pesado[randint(0, 25)]
                    print(desafio_casal_pesado)
                    input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")

else:
    quantidade = input("Quantas pessoas iram jogar?(Máx.6)")
    if quantidade == "2":
        nome1 = input("Nome1:")
        nome2 = input("Nome2:")
        while True:
            pesadoamigo = input("Você quer jogar no modo pesado(+18)?(sim ou não)")
            print("LEMBRE-SE QUE TUDO TEM QUER SER FEITO COM CONSENTIMENTO")
            pesadoamigo = pesadoamigo.replace("ã", "a")
            if pesadoamigo == "nao":
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 2)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    else:
                        print("Verdade para", nome2)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos_pesado = verdade_amigos_pesado[randint(0, 25)]
                        print(verdade_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 2)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    else:
                        print("Desafio para", nome2)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos = desafio_amigos[randint(0, 25)]
                        print(desafio_amigos)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
            else:
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 1)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    else:
                        print("Verdade para", nome2)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos = verdade_amigos[randint(0, 25)]
                        print(verdade_amigos)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 1)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    else:
                        print("Desafio para", nome2)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos_pesado = desafio_amigos_pesado[randint(0, 25)]
                        print(desafio_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
    elif quantidade == "3":
        nome1 = input("Nome1:")
        nome2 = input("Nome2:")
        nome3 = input("Nome3:")
        while True:
            pesadoamigo = input("Você quer jogar no modo pesado(+18)?(sim ou não)")
            print("LEMBRE-SE QUE TUDO TEM QUER SER FEITO COM CONSENTIMENTO")
            pesadoamigo = pesadoamigo.replace("ã", "a")
            if pesadoamigo == "nao":
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 2)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    elif ordem == 1:
                        print("Verdade para", nome2)
                    else:
                        print("Verdade para", nome3)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos = verdade_amigos[randint(0, 25)]
                        print(verdade_amigos)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 2)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    elif ordem == 1:
                        print("Desafio para", nome2)
                    else:
                        print("Desafio para", nome3)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos = desafio_amigos[randint(0, 25)]
                        print(desafio_amigos)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
            else:
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 2)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    elif ordem == 1:
                        print("Verdade para", nome2)
                    else:
                        print("Verdade para", nome3)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos_pesado = verdade_amigos_pesado[randint(0, 25)]
                        print(verdade_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 2)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    elif ordem == 1:
                        print("Desafio para", nome2)
                    else:
                        print("Desafio para", nome3)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos_pesado = desafio_amigos_pesado[randint(0, 25)]
                        print(desafio_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
    elif quantidade == "4":
        nome1 = input("Nome1:")
        nome2 = input("Nome2:")
        nome3 = input("Nome3:")
        nome4 = input("Nome4:")
        while True:
            pesadoamigo = input("Você quer jogar no modo pesado(+18)?(sim ou não)")
            print("LEMBRE-SE QUE TUDO TEM QUER SER FEITO COM CONSENTIMENTO")
            pesadoamigo = pesadoamigo.replace("ã", "a")
            if pesadoamigo == "nao":
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 3)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    elif ordem == 1:
                        print("Verdade para", nome2)
                    elif ordem == 2:
                        print("Verdade para", nome3)
                    else:
                        print("Verdade para", nome4)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos_pesado = verdade_amigos_pesado[randint(0, 25)]
                        print(verdade_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 3)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    elif ordem == 1:
                        print("Desafio para", nome2)
                    elif ordem == 2:
                        print("Desafio para", nome3)
                    else:
                        print("Desafio para", nome4)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos = desafio_amigos[randint(0, 25)]
                        print(desafio_amigos)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
            else:
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 3)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    elif ordem == 1:
                        print("Verdade para", nome2)
                    elif ordem == 2:
                        print("Verdade para", nome3)
                    else:
                        print("Verdade para", nome4)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos_pesado = verdade_amigos_pesado[randint(0, 25)]
                        print(verdade_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 3)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    elif ordem == 1:
                        print("Desafio para", nome2)
                    elif ordem == 2:
                        print("Desafio para", nome3)
                    else:
                        print("Desafio para", nome4)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos_pesado = desafio_amigos_pesado[randint(0, 25)]
                        print(desafio_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
    elif quantidade == "5":
        nome1 = input("Nome1:")
        nome2 = input("Nome2:")
        nome3 = input("Nome3:")
        nome4 = input("Nome4:")
        nome5 = input("Nome5:")
        while True:
            pesadoamigo = input("Você quer jogar no modo pesado(+18)?(sim ou não)")
            print("LEMBRE-SE QUE TUDO TEM QUER SER FEITO COM CONSENTIMENTO")
            pesadoamigo = pesadoamigo.replace("ã", "a")
            if pesadoamigo == "nao":
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 4)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    elif ordem == 1:
                        print("Verdade para", nome2)
                    elif ordem == 2:
                        print("Verdade para", nome3)
                    elif ordem == 3:
                        print("Verdade para", nome4)
                    else:
                        print("Verdade para", nome5)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos_pesado = verdade_amigos_pesado[randint(0, 25)]
                        print(verdade_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 4)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    elif ordem == 1:
                        print("Desafio para", nome2)
                    elif ordem == 2:
                        print("Desafio para", nome3)
                    elif ordem == 3:
                        print("Desafio para", nome4)
                    else:
                        print("Desafio para", nome5)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos = desafio_amigos[randint(0, 25)]
                        print(desafio_amigos)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
            else:
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 4)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    elif ordem == 1:
                        print("Verdade para", nome2)
                    elif ordem == 2:
                        print("Verdade para", nome3)
                    elif ordem == 3:
                        print("Verdade para", nome4)
                    else:
                        print("Verdade para", nome5)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos_pesado = verdade_amigos_pesado[randint(0, 25)]
                        print(verdade_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 4)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    elif ordem == 1:
                        print("Desafio para", nome2)
                    elif ordem == 2:
                        print("Desafio para", nome3)
                    elif ordem == 3:
                        print("Desafio para", nome4)
                    else:
                        print("Desafio para", nome5)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos_pesado = desafio_amigos_pesado[randint(0, 25)]
                        print(desafio_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
    elif quantidade == "6":
        nome1 = input("Nome1:")
        nome2 = input("Nome2:")
        nome3 = input("Nome3:")
        nome4 = input("Nome4:")
        nome5 = input("Nome5:")
        nome6 = input("Nome6:")
        while True:
            pesadoamigo = input("Você quer jogar no modo pesado(+18)?(sim ou não)")
            print("LEMBRE-SE QUE TUDO TEM QUER SER FEITO COM CONSENTIMENTO")
            pesadoamigo = pesadoamigo.replace("ã", "a")
            if pesadoamigo == "nao":
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 4)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    elif ordem == 1:
                        print("Verdade para", nome2)
                    elif ordem == 2:
                        print("Verdade para", nome3)
                    elif ordem == 3:
                        print("Verdade para", nome4)
                    elif ordem == 4:
                        print("Verdade para", nome5)
                    else:
                        print("Verdade para", nome6)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos_pesado = verdade_amigos_pesado[randint(0, 25)]
                        print(verdade_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 4)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    elif ordem == 1:
                        print("Desafio para", nome2)
                    elif ordem == 2:
                        print("Desafio para", nome3)
                    elif ordem == 3:
                        print("Desafio para", nome4)
                    elif ordem == 4:
                        print("Desafio para", nome5)
                    else:
                        print("Desafio para", nome6)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos = desafio_amigos[randint(0, 25)]
                        print(desafio_amigos)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
            else:
                time.sleep(0.3)
                print("Girando a roleta")
                time.sleep(1)
                resultado = randint(0, 1)
                if resultado == 0:
                    ordem = randint(0, 4)
                    if ordem == 0:
                        print("Verdade para", nome1)
                    elif ordem == 1:
                        print("Verdade para", nome2)
                    elif ordem == 2:
                        print("Verdade para", nome3)
                    elif ordem == 3:
                        print("Verdade para", nome4)
                    elif ordem == 4:
                        print("Verdade para", nome5)
                    else:
                        print("Verdade para", nome6)
                    manual1 = input("Você quer fazer a pergunta manualmente?(sim ou não)")
                    manual1 = manual1.lower()
                    manual1 = manual1.replace("ã", "a")
                    if manual1 == "nao":
                        verdade_amigos_pesado = verdade_amigos_pesado[randint(0, 25)]
                        print(verdade_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                else:
                    ordem = randint(0, 4)
                    if ordem == 0:
                        print("Desafio para", nome1)
                    elif ordem == 1:
                        print("Desafio para", nome2)
                    elif ordem == 2:
                        print("Desafio para", nome3)
                    elif ordem == 3:
                        print("Desafio para", nome4)
                    elif ordem == 4:
                        print("Desafio para", nome5)
                    else:
                        print("Desafio para", nome6)
                    manual2 = input("Você quer fazer o desafio manualmente?(sim ou não)")
                    manual2 = manual2.lower()
                    manual2 = manual2.replace("ã", "a")
                    if manual2 == "nao":
                        desafio_amigos_pesado = desafio_amigos_pesado[randint(0, 25)]
                        print(desafio_amigos_pesado)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
