import pyautogui
import time

pyautogui.PAUSE=0.8
#pegar procs
protocolo = [
#nesta caixa é anexado os protocolos separados por virgula
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
                O protocolo {item} abaixo esta pronto para retirada neste XXXX

                Informamos que os responsaveis e/ou procuradores mediante apresentacao de documento/procuracao, terao dia 30 dias a contar deste email  para retirada do seu processo. Apos essa data nao sera possivel a retirada.


                HORARIOS DE ATENDIMENTO PARA PESSOA FISICA E JURIDICA
                ENDEREÇO 
                Terça e Quinta-feira: das 13h15min às 16h30min
                E-mail: email_ficticio@email.com"""
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
