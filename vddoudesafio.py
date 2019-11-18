jogo = input("Se você quiser jogar no modo de amigos, digite 'amigos' "
             "\nSe quiser no modo de casal, digite 'casal':")

from random import randint
import time

desafio_casal_pesado = {
    '1': "DESAFIO: Tire a blusa de seu/sua parceira usando somente os dentes",
    '2': "DESAFIO: Tire duas peças da sua roupa",
    '3': "DESAFIO: Chupe um dos dedos delx",
    '4': "DESAFIO: Acaricie o corpo delx enquanto faz uma cara senxual",
    '5': "DESAFIO: Não se mexa por 1 min. e permita que elx faça o que quiser com você,"
         "\nse estx disse não, pare imediatamente",
    '6': "DESAFIO: Faça uma mímica sexual e elx terá que adivinhar o ato",
    '7': "DESAFIO: Beije a parte inferior da barriga delx",
    '8': "DESAFIO: Imite poses de sessão de fotos sexy",
    '9': "DESAFIO: Beije elx da forma mais intensa possível",
    '10': "DESAFIO: Beije uma parte da bunda delx",
    '11': "DESAFIO: De olhos fechados, elx coloca a sua mão em alguma parte do corpo delx,"
              "\ne vocÊ terá que adivinhar que parte é aquela",
    '12': "DESAFIO: De um tapa na bunda delx sem nada por cima",
    '13': "DESAFIO: Troquem toques em suas partes íntimas",
    '14': "DESAFIO: Tire sua parte íntima e coloque na sua cabeça, ",
          "\nfique assim por 3 rodadas",
    '15': "DESAFIO: Troquem toque no mamilo",
    '16': "DESAFIO: Permita que elx grave você dançando funk ou rebolando",

def desafio_casal_pesado(pergunta):
    if pergunta == 0:
        print("DESAFIO: Tire a blusa de seu/sua parceira usando somente os dentes")
    elif pergunta == 1:
        print("DESAFIO: Tire duas peças da sua roupa")
    elif pergunta == 2:
        print("DESAFIO: Tirem uma peça de roupa um do outro")
    elif pergunta == 3:
        print("DESAFIO: Chupe um dos dedos delx")
    elif pergunta == 4:
        print("DESAFIO: Acaricie o corpo deldesafio_casal_pesado = {
    '1': "DESAFIO: Tire a blusa de seu/sua parceira usando somente os dentes",
    '2': "DESAFIO: Tire duas peças da sua roupa",
    '3': "DESAFIO: Chupe um dos dedos delx",
    '4': "DESAFIO: Acaricie o corpo delx enquanto faz uma cara senxual",
    '5': "DESAFIO: Não se mexa por 1 min. e permita que elx faça o que quiser com você,"
         "\nse estx disse não, pare imediatamente",
    '6': "DESAFIO: Faça uma mímica sexual e elx terá que adivinhar o ato",
    '7': "DESAFIO: Beije a parte inferior da barriga delx",
    '8': "DESAFIO: Imite poses de sessão de fotos sexy",
    '9': "DESAFIO: Beije elx da forma mais intensa possível",
    '10': "DESAFIO: Beije uma parte da bunda delx",
    '11': "DESAFIO: De olhos fechados, elx coloca a sua mão em alguma parte do corpo delx,"
              "\ne vocÊ terá que adivinhar que parte é aquela",
    '12': "DESAFIO: De um tapa na bunda delx sem nada por cima",
    '13': "DESAFIO: Troquem toques em suas partes íntimas",
    '14': "DESAFIO: Tire sua parte íntima e coloque na sua cabeça, ",
          "\nfique assim por 3 rodadas",
    '15': "DESAFIO: Troquem toque no mamilo",
    '16': "DESAFIO: Permita que elx grave você dançando funk ou rebolando",x enquanto faz uma cara senxual")
    elif pergunta == 5:
        print("DESAFIO: Não se mexa por 1 min. e permita que elx faça o que quiser com você,"
              "\nse estx disse não, pare imediatamente")
    elif pergunta == 6:
        print("DESAFIO: Faça uma mímica sexual e elx terá que adiinhar o ato")
    elif pergunta == 7:
        print("DESAFIO: Beije a parte inferior da barriga delx")
    elif pergunta == 8:
        print("DESAFIO: Imite poses de sessão de fotos sexy")
    elif pergunta == 9:
        print("DESAFIO: Beije elx da forma mais intensa possível")
    elif pergunta == 10:
        print("DESAFIO: Beije uma parte da bunda delx")
    elif pergunta == 11:
        print("DESAFIO: De olhos fechados, elx coloca a sua mão em alguma parte do corpo delx,"
              "\ne vocÊ terá que adivinhar que parte é aquela")
    elif pergunta == 12:
        print("DESAFIO: De um tapa na bunda delx sem nada por cima")
    elif pergunta == 13:
        print("DESAFIO: Troquem toques em suas partes íntimas")
    elif pergunta == 14:
        print("DESAFIO: Tire sua parte íntima e coloque na sua cabeça, "
              "\nfique assim por 3 rodadas")
    elif pergunta == 15:
        print("DESAFIO: Troquem toque no mamilo")
    elif pergunta == 16:
        print("DESAFIO: Permita que elx grave você dançando funk ou rebolando")
    elif pergunta == 17:
        print("DESAFIO: Troque de roupas com elx por 3 rodadas")
    elif pergunta == 18:
        print("DESAFIO: Imite uma posição sexual")
    elif pergunta == 19:
        print("DESAFIO: Explore devagar e intensamente o corpo da outra pessoa")
    elif pergunta == 20:
        print("DESAFIO: Fique de 4 e deixe o outro apreciar a visão")
    elif pergunta == 21:
        print("DESAFIO: Lamba a barriga do seu parceiro até chegar na sua boca e beije-x")
    elif pergunta == 22:
        print("DESAFIO: Deixe que alguém do grupo te faça um chupão no pescoço")
    elif pergunta == 23:
        print("DESAFIO: Deixe que elx faça uma massagem, com direito a beijos intensos")
    elif pergunta == 24:
        print("DESAFIO:")
    elif pergunta == 25:
        print("DESAFIO: Termine todas as frases com sexy até a sua próxima rodada")


def verdade_casal_pesado(pergunta):
    if pergunta == 0:
        print("Qual foi o lugar mais exótico que você se masturbou?")
    elif pergunta == 1:
        print("Que tipo de pornografia te excita?")
    elif pergunta == 2:
        print("Já fez strip-tease?")
    elif pergunta == 3:
        print("Já fez sexo virtual?")
    elif pergunta == 4:
        print("Em casa ou no motel?")
    elif pergunta == 5:
        print("Já foi num sex-shop?")
    elif pergunta == 6:
        print("O que você gostaria de comprar em um sex-shop?")
    elif pergunta == 7:
        print("Já ficou com alguém comprometido?")
    elif pergunta == 8:
        print("Já usou algo pra lubrificar que não era lubrificante?")
    elif pergunta == 9:
        print("Já foi pego no flagra transando ou e masturbando?")
    elif pergunta == 10:
        print("Já ficou com vontade de vomitar durante o sexo oral?")
    elif pergunta == 11:
        print("já beijou a três?")
    elif pergunta == 12:
        print("O que você tem mais medo que te aconteça durante o sexo?")
    elif pergunta == 13:
        print("Prefere devagarzinho ou rápido?")
    elif pergunta == 14:
        print("Você toparia usar uma cueca/calcinha comestível?")
    elif pergunta == 15:
        print("No que você pensa enquanto está se masturbando?")
    elif pergunta == 16:
        print("Qual o segredo pra te deixar louco de tesão?")
    elif pergunta == 17:
        print("Qual o seu segredo pra deixar alguém louco de tesão?")
    elif pergunta == 18:
        print("Prefere ficar por cima ou por baixo?")
    elif pergunta == 19:
        print("O que você pensa sobre ser tocado por trás?")
    elif pergunta == 20:
        print("Se fosse tirar uma peça de roupa delx, qual seria?")
    elif pergunta == 21:
        print("Descreva o ambiene perfeito para uma noite de sexo?")
    elif pergunta == 22:
        print("Amor ou sexo?")
    elif pergunta == 23:
        print("Você já teve um sonho erótico com elx? "
              "\nSe sim, conte ele")
    elif pergunta == 24:
        print("Que tipo de música é perfeito pra transar?")
    elif pergunta == 25:
        print("Com que idade você se masturbou pela primeira vez?")


def desafio_casal(pergunta):
    if pergunta == 0:
        print("DESAFIO: Beije as costas do outro participante formando um número"
              "\ne elx vai ter que adivinhar qual é")
    elif pergunta == 1:
        print("DESAFIO: Sopre delicadamente o pescoço do outro participante")
    elif pergunta == 2:
        print("DESAFIO: Escolha uma parte do corpo delx que esteja quente,"
              "\n e derreta um cubo de gelo")
    elif pergunta == 3:
        print("DESAFIO: Beije os tornozelos delx")
    elif pergunta == 4:
        print("DESAFIO: Beije delicadamente a orelha delx")
    elif pergunta == 5:
        print("DESAFIO: Faça uma declaração de amor verdadeira")
    elif pergunta == 6:
        print("DESAFIO: Beije a barriga delx em um forma geométrica e faça com qeu elx adivinhe")
    elif pergunta == 7:
        print("DESAFIO: Faça cafuné nelx")
    elif pergunta == 8:
        print("DESAFIO: Ensine elx a rebolar")
    elif pergunta == 9:
        print("DESAFIO: Cante um rap sobre sua situação amorosa")
    elif pergunta == 10:
        print("DESAFIO: Faça uma massagem nos ombros delx")
    elif pergunta == 11:
        print("DESAFIO: Faça uma mímica e elx terá que adivinhar o ato")
    elif pergunta == 12:
        print("DESAFIO: Troquem olhares fixamente, o primeiro a desviar o olhar perde,"
              "\ne se a pessoa quiser, este terá que realizar um pedido")
    elif pergunta == 13:
        print("DESAFIO: De um apelido para elx, e chame-x assim até o final do jogo")
    elif pergunta == 14:
        print("DESAFIO: Lamba seu cotovelo")
    elif pergunta == 15:
        print("DESAFIO: Cheire o suvaco delx")
    elif pergunta == 16:
        print("DESAFIO: Tirem 2 selfies cada um com com as piores caretas possíveis"
              "\nquem tiver a pior ganha, e se quiser pode pedir um desejo ao outro")
    elif pergunta == 17:
        print("DESAFIO: Desenha um bigode nelx com a língua")
    elif pergunta == 18:
        print("DESAFIO: Simule um pedido de casamento")
    elif pergunta == 19:
        print("DESAFIO: Beije elx da forma masi intensa e apaixonante possível")
    elif pergunta == 20:
        print("DESAFIO: Façam uma guerra de travesseiro")
    elif pergunta == 21:
        print("DESAFIO: Oferença uma massagem onde elx quiser")
    elif pergunta == 22:
        print("DESAFIO: De um tapa na bunda delx sem nada por cima")
    elif pergunta == 23:
        print("DESAFIO: Coloque uma bala na boca e beije-x")
    elif pergunta == 24:
        print("DESAFIO: Faça 5 flexões com elx embaixo, e a cada descida de um beijo nelx")
    elif pergunta == 25:
        print("DESAFIO: Descreva elx em uma palavra")


def verdade_casal(pergunta):
    if pergunta == 0:
        print("Você ja foi numa praia de nudismo?")
    elif pergunta == 1:
        print("Você ja gostou da mesma pessoa que o seu amigo?")
    elif pergunta == 2:
        print("Você terminaria com elx por 1 trilhão de dólares?")
    elif pergunta == 3:
        print("Quantas pessoas você já beijou?")
    elif pergunta == 4:
        print("Alguma vez você ja gostou de algum professor(a)?")
    elif pergunta == 5:
        print("Qual o seu talento secreto?")
    elif pergunta == 6:
        print("Conte a sua história masi embaraçadora?")
    elif pergunta == 7:
        print("Qual a pior coisa de ter o seu gênero?")
    elif pergunta == 8:
        print("Você lembra cm detalhes a primeira vez que a vocês se beijaram?")
    elif pergunta == 9:
        print("Qual foi o maior problema que você e elx já tiveram?")
    elif pergunta == 10:
        print("Em algum momento você mentiu pra elx?")
    elif pergunta == 11:
        print("Você já fez um strip-tease?")
    elif pergunta == 12:
        print("Qual o lugar mas estranho que você ficou com tesão?")
    elif pergunta == 13:
        print("Qual a coisa mais embaraçosa qeu vocÊ já fez por elx?")
    elif pergunta == 14:
        print("Qual a coisa qeu você masi gosta delx?")
    elif pergunta == 15:
        print("Se você pudesse escolher um nome pra elx, qual seria?(não pode ser o mesmo)")
    elif pergunta == 16:
        print("Qual foi a coisa masi irritante qeu elx fez pra você?")
    elif pergunta == 17:
        print("Qual é a sua maior insegurança?")
    elif pergunta == 18:
        print("Qual é o melhor lugar para se beijar?")
    elif pergunta == 19:
        print("Qual é a coisa que você mais se arrepende em fazer?")
    elif pergunta == 20:
        print("Você ronca a noite?")
    elif pergunta == 21:
        print("Se fosse para vocês morem em outro país, qual você escolheria?")
    elif pergunta == 22:
        print("Como foi o seu primeiro beijo?")
    elif pergunta == 23:
        print("Qual foi o seu pior encontro??")
    elif pergunta == 24:
        print("Você já mandou fotos despido(a)")
    elif pergunta == 25:
        print("Você já saiu com várias pessoas ao mesmo tempo?")


def desafio_amigos(pergunta):
    if pergunta == 0:
        print("DESAFIO: Molhe o rosto e passe farinha")
    elif pergunta == 1:
        print("DESAFIO: Tente cantar 'galinha pintadinha' com a boca cheia de água")
    elif pergunta == 2:
        print("DESAFIO: Imite um peixe fora da água")
    elif pergunta == 3:
        print("DESAFIO: Dance 'oi, oi, oi'")
    elif pergunta == 4:
        print("DESAFIO: Cante um funk como se fosse ópera")
    elif pergunta == 5:
        print("DESAFIO: Arraste sua bunda no chão com se fosse um cachorro com coceira")
    elif pergunta == 6:
        print("DESAFIO: Vá até o seu vizinho e pergunte se ele tem um preservativo pra te dar")
    elif pergunta == 7:
        print("DESAFIO: Vá para o banheiro com a pessoa a sua direita e fique lá 5 min")
    elif pergunta == 8:
        print("DESAFIO: Faça 30 flexões e 50 abdominais")
    elif pergunta == 9:
        print("DESAFIO: Deixe todos te maquiarem da forma que quiserem")
    elif pergunta == 10:
        print("DESAFIO: Mastigue um chiclete mastigado por outra pessoa")
    elif pergunta == 11:
        print("DESAFIO: Permita que a pessoa a sua esquerda quebre um ovo cru na sua cabeça")
    elif pergunta == 12:
        print("DESAFIO: Engula uma colher de chá de ketchup, mostarda, ou algo semelhante")
    elif pergunta == 13:
        print("DESAFIO: Arrote o alfabeto")
    elif pergunta == 14:
        print("DESAFIO: Finge que está balada e mostre como você iria conquistar o crush")
    elif pergunta == 15:
        print("DESAFIO: Faça um quadradinho de 8")
    elif pergunta == 16:
        print("DESAFIO: Rateje-se como uma cobra")
    elif pergunta == 17:
        print("DESAFIO: Chupar um limão como se fosse uma laranja docinha")
    elif pergunta == 18:
        print("DESAFIO: Coce a orelha com o seu pé")
    elif pergunta == 19:
        print("DESAFIO: Faça uma pose de yoga e fique parado por 15 seg.")
    elif pergunta == 20:
        print("DESAFIO: Tente vender a blusa da pessoa a direita como se fosse uma blogueira")
    elif pergunta == 21:
        print("DESAFIO: Conte uma história desagradável e use tantas palavras sujas quanto possíve")
    elif pergunta == 22:
        print("DESAFIO: Desfile como se fosse a Gisele Bündchen")
    elif pergunta == 23:
        print("DESAFIO: Queime uma parte dos pêlos da sua perna")
    elif pergunta == 24:
        print("DESAFIO: Beba uma mistura que o grupo dize")
    elif pergunta == 25:
        print("DESAFIO: Beba um copo de água usando os pés")


def verdade_amigos(pergunta):
    if pergunta == 0:
        print("Qua a sua mania mais nojenta?")
    elif pergunta == 1:
        print("O que você faria se tivesse com dor de barriga e tivesse que"
              "\ncagar em um banheiro público, mas acabasse o papel higiênico?")
    elif pergunta == 2:
        print("Qual a pessoa mais aleatória que você ja stalkeou nas redes sociais?")
    elif pergunta == 3:
        print("Quantos dias vocÊ ja ficou sem tomar banho?")
    elif pergunta == 4:
        print("Conte aqui uma coisa que você espera que os seus pais nunca descubrem?")
    elif pergunta == 5:
        print("VocÊ já cagou no mato?")
    elif pergunta == 6:
        print("O que você faria se fosse do sexo oposto por um dia?")
    elif pergunta == 7:
        print("Você já roubou algo?")
    elif pergunta == 8:
        print("Qual foi a sua maior conquista?")
    elif pergunta == 9:
        print("Você já quis vomitar mas estava em um lugar público e engoliu o vômito??")
    elif pergunta == 10:
        print("Qual o momento masi inapropriado em que você peidou?")
    elif pergunta == 11:
        print("Você mentiu nesse jogo?")
    elif pergunta == 12:
        print("Quando foi a última vez qeu você chorou, poe quê?")
    elif pergunta == 13:
        print("Quando foi a última vez que você mijou na cama?")
    elif pergunta == 14:
        print("Você já fez cocô nas calça em público?")
    elif pergunta == 15:
        print("Se você pudesse mudar algo na sua vida o que seria?")
    elif pergunta == 16:
        print("Qual super poder você gostaria de ter?")
    elif pergunta == 17:
        print("Quem é a pessoa mais bonita das que estão jogando(você mesmo não pode)?")
    elif pergunta == 18:
        print("Com que pessoa você se arrepende de ter se envolvido?")
    elif pergunta == 19:
        print("Qual a razão mais boba que você brigou com alguém?")
    elif pergunta == 20:
        print("Qual foi o pior presente que vocÊ ja deu pra alguém?")
    elif pergunta == 21:
        print("De que pessoa não famosa você tem inveja?")
    elif pergunta == 22:
        print("Se você pudesse mudar de vida com uma celebridade por um dia, quem seria?")
    elif pergunta == 23:
        print("Qual foi a coisa mais ilegal que você ja fez?")
    elif pergunta == 24:
        print("Quantas pessoas você beijou esse ano?")
    elif pergunta == 25:
        print("Quem foi a sua primeira paixão, que ano?")


def desafio_amigos_pesado(pergunta):
    if pergunta == 0:
        print("DESAFIO: Simule o seu olhar mais sexy para alguém que esteja jogando")
    elif pergunta == 1:
        print("DESAFIO: Morda de leve o pescoço de alguém da roda")
    elif pergunta == 2:
        print("DESAFIO: Com os olhos fechados, encoste a mão em alguém da roda "
              "\ne adivinhe qual é a parte do corpo (com consentimento)")
    elif pergunta == 3:
        print("DESAFIO: Simule um sexo oral com uma fruta")
    elif pergunta == 4:
        print("DESAFIO: Beije alguém da roda (com consentimento)")
    elif pergunta == 5:
        print("DESAFIO: Coloque um cubo de gelo na boca e beije "
              "\no pescoço da pessoa a sua direita")
    elif pergunta == 6:
        print("DESAFIO: Mande uma mensagem de voz sexy para o seu crush")
    elif pergunta == 7:
        print("DESAFIO: Feche os olhos, alguém da roda de te dá um "
              "\nbeijo e você precisa adivinhar quem é")
    elif pergunta == 8:
        print("DESAFIO: De um beijo (do jeito que quiser) em todos os participantes")
    elif pergunta == 9:
        print("DESAFIO: Sente-se no colo de alguém por 10 min")
    elif pergunta == 10:
        print("DESAFIO: Diga algo muito sujo a pessoa a sua esquerda")
    elif pergunta == 11:
        print("DESAFIO: De uma aula de educação sexual")
    elif pergunta == 12:
        print("DESAFIO: De uma mordida em alguém da roda")
    elif pergunta == 13:
        print("DESAFIO: Ensine os outros integrantes a fazer o quadradinho")
    elif pergunta == 14:
        print("DESAFIO: Ensine a fazer o sexo oral perfeito utilizando uma banana")
    elif pergunta == 15:
        print("DESAFIO: Deixe que alguém do grupo faça um chupão nas suas costas")
    elif pergunta == 16:
        print("DESAFIO: Simule um orgasmo")
    elif pergunta == 17:
        print("DESAFIO: Troque de blusa com algum integrante do grupo")
    elif pergunta == 18:
        print("DESAFIO: Ensine o grupo a fazer um strip-tease")
    elif pergunta == 19:
        print("DESAFIO: Escolha duas pessoas e deem um beijo triplo")
    elif pergunta == 20:
        print("DESAFIO: Bata na bunda de uma mulher e um homem da roda")
    elif pergunta == 21:
        print("DESAFIO: Faça uma posição sexy e deixe todos os outros apreciarem")
    elif pergunta == 22:
        print("DESAFIO: Imite um coelho transando intensamente com um travesseiro")
    elif pergunta == 23:
        print("DESAFIO: Mostre a cor da sua cueca ou calcinha para todos")
    elif pergunta == 24:
        print("DESAFIO: Permite que tirem uma foto sua com outra pessoa na posição bunda-bunda")
    elif pergunta == 25:
        print("DESAFIO: Imite como uma gata mia ao transar")


def verdade_amigos_pesado(pergunta):
    if pergunta == 0:
        print("Qual parte do corpo você beijaria da pessoa a sua esquerda?")
    elif pergunta == 1:
        print("Que tipo de pornografia te excita?")
    elif pergunta == 2:
        print("Já fez strip-tease?")
    elif pergunta == 3:
        print("Já fez sexo virtual?")
    elif pergunta == 4:
        print("Em casa ou no motel?")
    elif pergunta == 5:
        print("Já foi num sex-shop?")
    elif pergunta == 6:
        print("O que você gostaria de comprar em um sex-shop?")
    elif pergunta == 7:
        print("Já ficou com alguém comprometido?")
    elif pergunta == 8:
        print("Já usou algo pra lubrificar que não era lubrificante?")
    elif pergunta == 9:
        print("Já foi pego no flagra transando ou e masturbando?")
    elif pergunta == 10:
        print("Já ficou com vontade de vomitar durante o sexo oral?")
    elif pergunta == 11:
        print("já beijou a três?")
    elif pergunta == 12:
        print("O que você tem mais medo que te aconteça durante o sexo?")
    elif pergunta == 13:
        print("Prefere devagarzinho ou rápido?")
    elif pergunta == 14:
        print("Você toparia usar uma cueca/calcinha comestível?")
    elif pergunta == 15:
        print("No que vocÊ pensa enquanto está se masturbando?")
    elif pergunta == 16:
        print("Qual o segredo pra te deixar louco de tesão?")
    elif pergunta == 17:
        print("Qual o seu segredo pra deixar alguém louco de tesão?")
    elif pergunta == 18:
        print("Prefere ficar por cima ou por baixo?")
    elif pergunta == 19:
        print("O que você pensa sobre ser tocado por trás?")
    elif pergunta == 20:
        print("Se fosse tirar uma peça de roupa da pessoa à sua direita, qual seria?")
    elif pergunta == 21:
        print("Descreva o ambiene perfeito para uma noite de sexo?")
    elif pergunta == 22:
        print("Amor ou sexo?")
    elif pergunta == 23:
        print("Qual é a pessoa mais sexy participando do jogo?")
    elif pergunta == 24:
        print("Que tipo de música é perfeito pra transar?")
    elif pergunta == 25:
        print("Com que idade você se masturbou pela primeira vez?")


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
                    pergunta = randint(0, 25)
                    verdade_casal(pergunta)
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
                    pergunta = randint(0, 25)
                    desafio_casal(pergunta)
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
                    pergunta = randint(0, 25)
                    verdade_casal_pesado(pergunta)
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
                    pergunta = randint(0, 25)
                    desafio_casal_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos(pergunta)
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
                        pergunta = randint(0, 25)
                        verdade_amigos_pesado(pergunta)
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
                        pergunta = randint(0, 25)
                        desafio_amigos_pesado(pergunta)
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
                    else:
                        input(" ""\nPara o próximo verdade ou desafio, aperte a tecla de replay...")
