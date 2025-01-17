import flet as ft

def main(pagina):
    titulo = ft.Text("ZapChat")

    # Pop-up para entrar no chat
    titulo_popup = ft.Text("Bem-vindo ao ChatZap")
    caixa_nome = ft.TextField(label="Digite o seu nome")

    # Área de chat
    chat = ft.Column()
    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem")
    
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # Função para enviar mensagem
    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = "" 
        pagina.update()
    
    # Botão de enviar mensagem
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    # Função para entrar no chat
    def entrar_no_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        
        # Adicionar o chat e o campo de envio
        pagina.add(ft.Text(f"Bem-vindo, {caixa_nome.value}!"))
        pagina.add(chat)
        pagina.add(linha_enviar)
        pagina.update()

        # Enviar mensagem de boas-vindas no túnel
        mensagem = f"{caixa_nome.value} entrou no chat!"
        pagina.pubsub.send_all(mensagem)

    # Configuração do pop-up
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_no_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    # Função para abrir o pop-up
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    # Botão de iniciar chat
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)
    pagina.add(titulo)
    pagina.add(botao)

ft.app(main, view=ft.WEB_BROWSER)
