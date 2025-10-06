import pyautogui
import time

pyautogui.PAUSE=0.8
#pegar procs
protocolo = [
7313562022,7312742022,7316882023,73123322022,73129122022,73133482022,73126582022,73154982021,73173212020,73154972021,73161222020,73148452021,73122652022,73134482021,73140672021,73123732021,73146832021,73154932021,73119142022,73126742022,7316902023,73175782020,7317092021,7316592023,7316532023,73129252021,73176292020,73185432020,7316202022,73122122022,73133422022,73115612022,7314562021,7317412023,7314792023,73120482022,7316782022,73184102020,731832023,7314422023,731852022,73163372020,7317762023,7314192020,73173842020,73121902022,73126722022,73119022022,73128932021,722312022,7315512023,73129892022,73127292022,73130822022,73130832022,73111692022,7315262023,731721222020,73160232021,73117972022,73127302022,7222232022,73175882020,7311892022,73177562020,73124772022,731822022,73130572022,7317832023,73118942022,73113302021,73175612020,7316552022,73119512022,73123862022
]
time.sleep(3)

for item in protocolo:
    #entrar na pogina do sigapce, deve estar na esquerda, primeira das paginas
    pyautogui.click(x=199, y=13)

    #clicar no campo   
    pyautogui.click(x=504, y=417)
    #escrever proc
    pyautogui.write(str(item))
    #pesquisar
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=166, y=600)
    print("pesquisou protocolo")
    #clicar 3 vezes no email 
    pyautogui.scroll(-200)
    pyautogui.tripleClick(x=348, y=589)
    print("clicou no email")

    #copiar email
    pyautogui.hotkey("ctrl", "c")
    pyautogui.press("f5")
    pyautogui.click(x=388, y=16)
    pyautogui.click(x=94, y=260)
    pyautogui.click(x=144, y=339)
    print("copiou o email")
   
    #ir no correio eletronico e colar email
    pyautogui.hotkey("ctrl","v")
    pyautogui.click(x=113, y=419)
    print("colou o endereço de email")
    #colocar assunto
    pyautogui.click(x=197, y=375)
    assunto = f'{item} esta pronto para retirada'
    pyautogui.write(assunto)
    print("colocou assunto")
    #deletar assinatura eletronica
    pyautogui.tripleClick(x=643, y=519)
    pyautogui.press("backspace")
    print("deletar assinatura eletronica automatica")
    time.sleep(1)
    #colar mensagem
    mensagem = f"""Boa tarde, 
                O protocolo {item} abaixo esta pronto para retirada neste SFPC/3

                Informamos que os responsaveis e/ou procuradores mediante apresentacao de documento/procuracao, terao dia 30 dias a contar deste email  para retirada do seu processo. Apos essa data nao sera possivel a retirada.


                HORARIOS DE ATENDIMENTO PARA PESSOA FISICA E JURIDICA
                Rua dos Andradas, nº 551  - Centro Histórico - Porto Alegre
                Terça e Quinta-feira: das 13h15min às 16h30min
                E-mail: faleconoscosfpc3@3rm.eb.mil.br"""
    pyautogui.typewrite(mensagem)
    print("colou a mensagem ")
    time.sleep(3)
    # modificar protocolo 
    # enviar 
    pyautogui.click(x=45, y=703)#enviar email
    print("enviou o email")
    time.sleep(1)
    pyautogui.click(x=204, y=216)#deletar o rascunho de email
    print("deletou o rascunho caso tenha um")
    print(f"enviou o email do processo{item}")
    #voltar para pagina no sigapce
    pyautogui.click(x=199, y=13)

    ######################    bloco de automação finalizada   ################
print(f"processo finalizado, foram enviados \n ---------{len(protocolo)}   emails----------")